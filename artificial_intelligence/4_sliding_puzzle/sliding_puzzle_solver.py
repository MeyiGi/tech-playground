"""
Sliding Puzzle Solver using A* Search Algorithm.

This module provides an optimal solution for solving sliding puzzles (8-puzzle, 15-puzzle, etc.)
using the A* search algorithm with Manhattan distance heuristic.

Time Complexity: O(b^d) where b is branching factor, d is solution depth
Space Complexity: O(b^d) for storing explored states
Optimality: Guaranteed to find shortest solution path
"""

from __future__ import annotations

import heapq
import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Tuple, List, Set, FrozenSet
import time


class Direction(Enum):
    """Represents possible moves in the puzzle."""
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __repr__(self) -> str:
        return self.name


@dataclass(frozen=True)
class PuzzleState:
    """
    Immutable representation of a puzzle state.
    
    Uses tuple for efficient hashing and comparison.
    Stores configuration in row-major order.
    """
    grid: Tuple[int, ...]
    rows: int
    cols: int
    blank_pos: Tuple[int, int]
    
    @classmethod
    def from_2d_list(cls, grid_2d: List[List[int]]) -> PuzzleState:
        """Create state from 2D list representation."""
        rows = len(grid_2d)
        cols = len(grid_2d[0]) if rows > 0 else 0
        
        # Flatten to tuple and find blank position
        flat_grid = []
        blank_pos = None
        for i, row in enumerate(grid_2d):
            for j, val in enumerate(row):
                flat_grid.append(val)
                if val == 0:
                    blank_pos = (i, j)
        
        if blank_pos is None:
            raise ValueError("Puzzle must contain exactly one blank tile (0)")
            
        return cls(
            grid=tuple(flat_grid),
            rows=rows,
            cols=cols,
            blank_pos=blank_pos
        )
    
    def to_2d_list(self) -> List[List[int]]:
        """Convert state back to 2D list for display."""
        return [
            list(self.grid[i * self.cols:(i + 1) * self.cols])
            for i in range(self.rows)
        ]
    
    def get_value(self, row: int, col: int) -> int:
        """Get tile value at position."""
        return self.grid[row * self.cols + col]
    
    def move(self, direction: Direction) -> Optional[PuzzleState]:
        """
        Generate new state by moving blank tile in given direction.
        
        Returns None if move is invalid (out of bounds).
        """
        row, col = self.blank_pos
        d_row, d_col = direction.value
        new_row, new_col = row + d_row, col + d_col
        
        # Check bounds
        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return None
        
        # Swap blank with target position
        grid_list = list(self.grid)
        blank_idx = row * self.cols + col
        target_idx = new_row * self.cols + new_col
        
        grid_list[blank_idx], grid_list[target_idx] = grid_list[target_idx], grid_list[blank_idx]
        
        return PuzzleState(
            grid=tuple(grid_list),
            rows=self.rows,
            cols=self.cols,
            blank_pos=(new_row, new_col)
        )
    
    def __hash__(self) -> int:
        return hash(self.grid)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PuzzleState):
            return NotImplemented
        return self.grid == other.grid


@dataclass(order=True)
class SearchNode:
    """
    Node in the A* search tree.
    
    Ordered by f_score (g + h) for priority queue operations.
    """
    f_score: int
    g_score: int = field(compare=False)
    state: PuzzleState = field(compare=False)
    parent: Optional[SearchNode] = field(default=None, compare=False)
    move: Optional[Direction] = field(default=None, compare=False)


class SlidingPuzzleSolver:
    """
    Optimal sliding puzzle solver using A* search with Manhattan distance heuristic.
    
    Features:
    - Guaranteed optimal solution (shortest path)
    - Efficient state representation and hashing
    - State deduplication to avoid revisiting states
    - Memory efficient - only stores necessary information
    """
    
    def __init__(self, initial_state: PuzzleState, goal_state: PuzzleState):
        """
        Initialize solver with start and goal states.
        
        Args:
            initial_state: Starting puzzle configuration
            goal_state: Target puzzle configuration
            
        Raises:
            ValueError: If states have incompatible dimensions
        """
        if (initial_state.rows != goal_state.rows or 
            initial_state.cols != goal_state.cols):
            raise ValueError("Initial and goal states must have same dimensions")
        
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.rows = initial_state.rows
        self.cols = initial_state.cols
        
        # Build goal position lookup for O(1) heuristic calculation
        self._goal_positions = {}
        for i in range(self.rows):
            for j in range(self.cols):
                value = goal_state.get_value(i, j)
                if value != 0:  # Don't track blank tile
                    self._goal_positions[value] = (i, j)
        
        # Statistics
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.search_time = 0.0
        
        self._logger = logging.getLogger(__name__)
    
    def manhattan_distance(self, state: PuzzleState) -> int:
        """
        Calculate Manhattan distance heuristic.
        
        Sum of distances each tile needs to move to reach goal position.
        This is an admissible and consistent heuristic for A*.
        
        Time Complexity: O(n) where n is number of tiles
        """
        distance = 0
        for i in range(self.rows):
            for j in range(self.cols):
                value = state.get_value(i, j)
                if value != 0 and value in self._goal_positions:
                    goal_i, goal_j = self._goal_positions[value]
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance
    
    def is_solvable(self) -> bool:
        """
        Check if puzzle can be solved by moving from initial to goal state.
        
        Two states are in the same solvability class if they have the same parity.
        For the standard solved state, we need to check if initial state has
        the correct parity.
        
        A state's parity depends on:
        - For odd width: inversion count parity
        - For even width: (inversion count + blank row from bottom) parity
        
        Time Complexity: O(n²) where n is number of tiles
        """
        def get_parity(state: PuzzleState) -> int:
            """Get parity (0 or 1) for a puzzle state."""
            # Get non-zero tiles in order
            tiles = [x for x in state.grid if x != 0]
            
            # Count inversions
            inversions = 0
            for i in range(len(tiles)):
                for j in range(i + 1, len(tiles)):
                    if tiles[i] > tiles[j]:
                        inversions += 1
            
            if self.cols % 2 == 1:
                # Odd width: return inversion parity
                return inversions % 2
            else:
                # Even width: (inversions + blank row from bottom) parity
                blank_row_from_bottom = self.rows - state.blank_pos[0]
                return (inversions + blank_row_from_bottom) % 2
        
        # Two states are solvable from each other if they have the same parity
        initial_parity = get_parity(self.initial_state)
        goal_parity = get_parity(self.goal_state)
        
        return initial_parity == goal_parity
    
    def solve(self, max_iterations: Optional[int] = None) -> Optional[List[Direction]]:
        """
        Solve puzzle using A* search algorithm.
        
        Args:
            max_iterations: Optional limit on nodes to expand (for safety)
            
        Returns:
            List of moves to reach goal, or None if unsolvable
            
        Time Complexity: O(b^d) where b is branching factor, d is solution depth
        Space Complexity: O(b^d)
        """
        start_time = time.time()
        
        # Check solvability first
        if not self.is_solvable():
            self._logger.warning("Puzzle configuration is not solvable")
            return None
        
        # Priority queue: (f_score, node)
        frontier = []
        initial_h = self.manhattan_distance(self.initial_state)
        initial_node = SearchNode(
            f_score=initial_h,
            g_score=0,
            state=self.initial_state
        )
        heapq.heappush(frontier, initial_node)
        
        # Track visited states to avoid cycles
        explored: Set[Tuple[int, ...]] = set()
        
        # Track best g_score for each state
        g_scores = {self.initial_state.grid: 0}
        
        self.nodes_expanded = 0
        self.max_frontier_size = 1
        
        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))
            
            # Check iteration limit
            if max_iterations and self.nodes_expanded >= max_iterations:
                self._logger.warning(f"Reached max iterations: {max_iterations}")
                return None
            
            current = heapq.heappop(frontier)
            
            # Goal test
            if current.state == self.goal_state:
                self.search_time = time.time() - start_time
                return self._reconstruct_path(current)
            
            # Skip if already explored with better path
            if current.state.grid in explored:
                continue
            
            explored.add(current.state.grid)
            self.nodes_expanded += 1
            
            # Expand neighbors
            for direction in Direction:
                new_state = current.state.move(direction)
                
                if new_state is None:
                    continue
                
                # Calculate scores
                tentative_g = current.g_score + 1
                
                # Skip if we've found a better path to this state
                if (new_state.grid in g_scores and 
                    g_scores[new_state.grid] <= tentative_g):
                    continue
                
                g_scores[new_state.grid] = tentative_g
                h_score = self.manhattan_distance(new_state)
                f_score = tentative_g + h_score
                
                new_node = SearchNode(
                    f_score=f_score,
                    g_score=tentative_g,
                    state=new_state,
                    parent=current,
                    move=direction
                )
                
                heapq.heappush(frontier, new_node)
        
        self.search_time = time.time() - start_time
        self._logger.warning("No solution found (search space exhausted)")
        return None
    
    def _reconstruct_path(self, node: SearchNode) -> List[Direction]:
        """Reconstruct solution path from goal node."""
        path = []
        current = node
        
        while current.parent is not None:
            if current.move is not None:
                path.append(current.move)
            current = current.parent
        
        return list(reversed(path))
    
    def get_statistics(self) -> dict:
        """Return search statistics."""
        return {
            'nodes_expanded': self.nodes_expanded,
            'max_frontier_size': self.max_frontier_size,
            'search_time_seconds': self.search_time,
        }


def solve_puzzle(
    initial_grid: List[List[int]],
    goal_grid: Optional[List[List[int]]] = None,
    verbose: bool = False
) -> Optional[List[Direction]]:
    """
    Convenience function to solve a sliding puzzle.
    
    Args:
        initial_grid: Starting configuration (0 represents blank)
        goal_grid: Target configuration (defaults to sorted tiles)
        verbose: If True, print detailed statistics
        
    Returns:
        List of moves to solve, or None if unsolvable
        
    Example:
        >>> initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        >>> solution = solve_puzzle(initial)
        >>> print(f"Solution: {solution}")
    """
    # Setup logging
    if verbose:
        logging.basicConfig(level=logging.INFO)
    
    # Create states
    initial_state = PuzzleState.from_2d_list(initial_grid)
    
    if goal_grid is None:
        # Default goal: sorted tiles with blank at end
        rows = len(initial_grid)
        cols = len(initial_grid[0]) if rows > 0 else 0
        goal_grid = [
            list(range(i * cols, (i + 1) * cols))
            for i in range(rows)
        ]
    
    goal_state = PuzzleState.from_2d_list(goal_grid)
    
    # Solve
    solver = SlidingPuzzleSolver(initial_state, goal_state)
    solution = solver.solve()
    
    # Print statistics if verbose
    if verbose:
        stats = solver.get_statistics()
        print(f"\n{'='*60}")
        print(f"Puzzle Solved: {solution is not None}")
        if solution:
            print(f"Solution Length: {len(solution)} moves")
            print(f"Moves: {[m.name for m in solution]}")
        print(f"Nodes Expanded: {stats['nodes_expanded']:,}")
        print(f"Max Frontier Size: {stats['max_frontier_size']:,}")
        print(f"Search Time: {stats['search_time_seconds']:.4f} seconds")
        print(f"{'='*60}\n")
    
    return solution


def visualize_solution(
    initial_grid: List[List[int]],
    moves: List[Direction],
    goal_grid: Optional[List[List[int]]] = None
) -> None:
    """
    Print step-by-step visualization of solution.
    
    Args:
        initial_grid: Starting configuration
        moves: Sequence of moves to apply
        goal_grid: Optional target configuration to verify
    """
    state = PuzzleState.from_2d_list(initial_grid)
    
    print("\nInitial State:")
    _print_grid(state.to_2d_list())
    
    for i, move in enumerate(moves, 1):
        state = state.move(move)
        if state is None:
            print(f"ERROR: Invalid move {move} at step {i}")
            return
        
        print(f"\nStep {i}: Move {move.name}")
        _print_grid(state.to_2d_list())
    
    if goal_grid:
        goal_state = PuzzleState.from_2d_list(goal_grid)
        if state == goal_state:
            print("\n✓ Goal state reached!")
        else:
            print("\n✗ Goal state NOT reached")


def _print_grid(grid: List[List[int]]) -> None:
    """Pretty print grid with alignment."""
    if not grid:
        return
    
    # Find max width needed
    max_val = max(max(row) for row in grid)
    width = len(str(max_val))
    
    for row in grid:
        print("  ".join(f"{val:>{width}}" if val != 0 else "·".rjust(width) for val in row))


# Example usage and test cases
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("Sliding Puzzle Solver - A* Algorithm\n")
    
    # Test Case 1: Easy 3x3 puzzle (few moves)
    print("Test 1: Easy 3x3 Puzzle")
    easy_puzzle = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    solution = solve_puzzle(easy_puzzle, verbose=True)
    if solution:
        visualize_solution(easy_puzzle, solution)
    
    # Test Case 2: Medium 3x3 puzzle
    print("\n\nTest 2: Medium 3x3 Puzzle")
    medium_puzzle = [
        [1, 4, 2],
        [3, 7, 5],
        [6, 8, 0]
    ]
    solution = solve_puzzle(medium_puzzle, verbose=True)
    if solution and len(solution) <= 10:  # Only visualize short solutions
        visualize_solution(medium_puzzle, solution)
    
    # Test Case 3: Hard 3x3 puzzle (from original code)
    print("\n\nTest 3: Hard 3x3 Puzzle")
    hard_puzzle = [
        [4, 6, 0],
        [1, 8, 3],
        [7, 2, 5]
    ]
    solution = solve_puzzle(hard_puzzle, verbose=True)
    
    # Test Case 4: Classic hard case from AI textbook
    print("\n\nTest 4: Classic Hard Puzzle (Russell & Norvig)")
    classic_puzzle = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
    solution = solve_puzzle(classic_puzzle, verbose=True)
    
    # Test Case 5: Unsolvable puzzle
    print("\n\nTest 5: Unsolvable Puzzle")
    unsolvable = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]
    solution = solve_puzzle(unsolvable, verbose=True)