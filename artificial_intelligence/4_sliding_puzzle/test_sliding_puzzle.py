"""
Unit tests for Sliding Puzzle Solver.

Tests cover:
- State representation and operations
- Heuristic calculations
- Solvability detection
- A* search correctness
- Edge cases and error handling
"""

import unittest
from sliding_puzzle_solver import (
    PuzzleState,
    Direction,
    SlidingPuzzleSolver,
    solve_puzzle
)


class TestPuzzleState(unittest.TestCase):
    """Test PuzzleState class."""
    
    def test_from_2d_list(self):
        """Test creation from 2D list."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        
        self.assertEqual(state.rows, 3)
        self.assertEqual(state.cols, 3)
        self.assertEqual(state.blank_pos, (1, 1))
        self.assertEqual(state.get_value(0, 0), 1)
        self.assertEqual(state.get_value(1, 1), 0)
    
    def test_from_2d_list_no_blank(self):
        """Test that missing blank raises error."""
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(ValueError):
            PuzzleState.from_2d_list(grid)
    
    def test_to_2d_list(self):
        """Test conversion back to 2D list."""
        original = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(original)
        reconstructed = state.to_2d_list()
        
        self.assertEqual(original, reconstructed)
    
    def test_move_up_valid(self):
        """Test valid upward move."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        new_state = state.move(Direction.UP)
        
        self.assertIsNotNone(new_state)
        self.assertEqual(new_state.blank_pos, (0, 1))
        self.assertEqual(new_state.get_value(0, 1), 0)
        self.assertEqual(new_state.get_value(1, 1), 2)
    
    def test_move_up_invalid(self):
        """Test invalid upward move (out of bounds)."""
        grid = [[0, 2, 3], [4, 1, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        new_state = state.move(Direction.UP)
        
        self.assertIsNone(new_state)
    
    def test_move_down_valid(self):
        """Test valid downward move."""
        grid = [[1, 0, 3], [4, 2, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        new_state = state.move(Direction.DOWN)
        
        self.assertIsNotNone(new_state)
        self.assertEqual(new_state.blank_pos, (1, 1))
        self.assertEqual(new_state.get_value(1, 1), 0)
    
    def test_move_left_valid(self):
        """Test valid leftward move."""
        grid = [[1, 2, 0], [4, 5, 6], [7, 8, 3]]
        state = PuzzleState.from_2d_list(grid)
        new_state = state.move(Direction.LEFT)
        
        self.assertIsNotNone(new_state)
        self.assertEqual(new_state.blank_pos, (0, 1))
    
    def test_move_right_valid(self):
        """Test valid rightward move."""
        grid = [[0, 2, 3], [4, 1, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        new_state = state.move(Direction.RIGHT)
        
        self.assertIsNotNone(new_state)
        self.assertEqual(new_state.blank_pos, (0, 1))
    
    def test_state_equality(self):
        """Test state equality comparison."""
        grid1 = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        grid2 = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        grid3 = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
        
        state1 = PuzzleState.from_2d_list(grid1)
        state2 = PuzzleState.from_2d_list(grid2)
        state3 = PuzzleState.from_2d_list(grid3)
        
        self.assertEqual(state1, state2)
        self.assertNotEqual(state1, state3)
    
    def test_state_hashable(self):
        """Test that states can be used in sets/dicts."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        
        state_set = {state}
        self.assertIn(state, state_set)


class TestSlidingPuzzleSolver(unittest.TestCase):
    """Test SlidingPuzzleSolver class."""
    
    def setUp(self):
        """Set up common test fixtures."""
        self.goal_3x3 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.goal_state_3x3 = PuzzleState.from_2d_list(self.goal_3x3)
    
    def test_manhattan_distance_goal(self):
        """Test Manhattan distance for goal state is 0."""
        state = PuzzleState.from_2d_list(self.goal_3x3)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        self.assertEqual(solver.manhattan_distance(state), 0)
    
    def test_manhattan_distance_one_move(self):
        """Test Manhattan distance for one move away."""
        # Swap 0 and 1: distance should be 1
        grid = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        self.assertEqual(solver.manhattan_distance(state), 1)
    
    def test_manhattan_distance_complex(self):
        """Test Manhattan distance calculation."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        # Calculate manually:
        # 1 at (0,0) -> goal (0,1): distance 1
        # 2 at (0,1) -> goal (0,2): distance 1
        # 3 at (0,2) -> goal (1,0): distance 1+2=3
        # 4 at (1,0) -> goal (1,1): distance 1
        # 5 at (1,2) -> goal (1,2): distance 0
        # 6 at (2,0) -> goal (2,0): distance 0
        # 7 at (2,1) -> goal (2,1): distance 0
        # 8 at (2,2) -> goal (2,2): distance 0
        # Total: 1+1+3+1 = 6
        self.assertEqual(solver.manhattan_distance(state), 6)
    
    def test_is_solvable_solvable(self):
        """Test solvability detection for solvable puzzle."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        self.assertTrue(solver.is_solvable())
    
    def test_is_solvable_unsolvable(self):
        """Test solvability detection for unsolvable puzzle."""
        # This configuration has odd number of inversions (unsolvable for 3x3)
        grid = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        self.assertFalse(solver.is_solvable())
    
    def test_solve_already_solved(self):
        """Test solving already solved puzzle."""
        state = PuzzleState.from_2d_list(self.goal_3x3)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solution = solver.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 0)
    
    def test_solve_one_move(self):
        """Test solving puzzle requiring one move."""
        grid = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solution = solver.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 1)
        self.assertEqual(solution[0], Direction.LEFT)
    
    def test_solve_simple_puzzle(self):
        """Test solving simple puzzle."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solution = solver.solve()
        self.assertIsNotNone(solution)
        
        # Verify solution by applying moves
        current = state
        for move in solution:
            current = current.move(move)
            self.assertIsNotNone(current)
        
        self.assertEqual(current, self.goal_state_3x3)
    
    def test_solve_medium_puzzle(self):
        """Test solving medium difficulty puzzle."""
        grid = [[1, 4, 2], [3, 7, 5], [6, 8, 0]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solution = solver.solve()
        self.assertIsNotNone(solution)
        
        # Verify solution
        current = state
        for move in solution:
            current = current.move(move)
        
        self.assertEqual(current, self.goal_state_3x3)
    
    def test_solve_unsolvable(self):
        """Test that unsolvable puzzle returns None."""
        grid = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solution = solver.solve()
        self.assertIsNone(solution)
    
    def test_solve_with_max_iterations(self):
        """Test max iterations limit."""
        grid = [[1, 4, 2], [3, 7, 5], [6, 8, 0]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        # Set very low limit
        solution = solver.solve(max_iterations=5)
        # May or may not find solution depending on search order
        # Just verify it doesn't crash
        self.assertIsInstance(solution, (list, type(None)))
    
    def test_statistics_tracking(self):
        """Test that solver tracks statistics."""
        grid = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, self.goal_state_3x3)
        
        solver.solve()
        stats = solver.get_statistics()
        
        self.assertIn('nodes_expanded', stats)
        self.assertIn('max_frontier_size', stats)
        self.assertIn('search_time_seconds', stats)
        self.assertGreater(stats['nodes_expanded'], 0)
        self.assertGreaterEqual(stats['search_time_seconds'], 0)


class TestConvenienceFunctions(unittest.TestCase):
    """Test convenience functions."""
    
    def test_solve_puzzle_default_goal(self):
        """Test solve_puzzle with default goal."""
        initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        solution = solve_puzzle(initial)
        
        self.assertIsNotNone(solution)
        self.assertIsInstance(solution, list)
    
    def test_solve_puzzle_custom_goal(self):
        """Test solve_puzzle with custom goal."""
        initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        solution = solve_puzzle(initial, goal)
        
        self.assertIsNotNone(solution)
    
    def test_solve_puzzle_2x2(self):
        """Test solving 2x2 puzzle."""
        initial = [[1, 0], [2, 3]]
        goal = [[0, 1], [2, 3]]
        solution = solve_puzzle(initial, goal)
        
        self.assertIsNotNone(solution)
        
        # Verify solution
        state = PuzzleState.from_2d_list(initial)
        for move in solution:
            state = state.move(move)
        
        expected_goal = PuzzleState.from_2d_list(goal)
        self.assertEqual(state, expected_goal)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""
    
    def test_incompatible_dimensions(self):
        """Test that incompatible dimensions raise error."""
        initial = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        goal = [[0, 1], [2, 3]]
        
        initial_state = PuzzleState.from_2d_list(initial)
        goal_state = PuzzleState.from_2d_list(goal)
        
        with self.assertRaises(ValueError):
            SlidingPuzzleSolver(initial_state, goal_state)
    
    def test_1x1_puzzle(self):
        """Test trivial 1x1 puzzle."""
        grid = [[0]]
        state = PuzzleState.from_2d_list(grid)
        solver = SlidingPuzzleSolver(state, state)
        
        solution = solver.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)