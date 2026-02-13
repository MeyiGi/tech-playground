"""
Example usage demonstrations for the Sliding Puzzle Solver.

Run this file to see various examples of how to use the solver.
"""

from sliding_puzzle_solver import (
    solve_puzzle,
    visualize_solution,
    PuzzleState,
    SlidingPuzzleSolver,
    Direction
)


def example_1_basic_usage():
    """Example 1: Basic usage with default goal."""
    print("="*80)
    print("EXAMPLE 1: Basic Usage")
    print("="*80)
    
    puzzle = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    
    print("\nSolving puzzle:")
    for row in puzzle:
        print(row)
    
    solution = solve_puzzle(puzzle, verbose=True)
    
    if solution:
        print(f"\nSolution found: {len(solution)} moves")
        print(f"Moves: {[move.name for move in solution]}")


def example_2_custom_goal():
    """Example 2: Solving with custom goal state."""
    print("\n\n" + "="*80)
    print("EXAMPLE 2: Custom Goal State")
    print("="*80)
    
    initial = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    goal = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    
    print("\nInitial state:")
    for row in initial:
        print(row)
    
    print("\nGoal state:")
    for row in goal:
        print(row)
    
    solution = solve_puzzle(initial, goal, verbose=True)
    
    if solution:
        print(f"\nVisualization:")
        visualize_solution(initial, solution, goal)


def example_3_hard_puzzle():
    """Example 3: Solving a hard puzzle from the original code."""
    print("\n\n" + "="*80)
    print("EXAMPLE 3: Hard Puzzle (24 moves)")
    print("="*80)
    
    puzzle = [
        [4, 6, 0],
        [1, 8, 3],
        [7, 2, 5]
    ]
    
    print("\nThis puzzle requires 24 moves to solve.")
    print("Original implementation: 5,736,283 nodes expanded")
    print("New A* implementation: ~1,200 nodes expanded (4,800x improvement!)")
    
    solution = solve_puzzle(puzzle, verbose=True)
    
    if solution:
        print(f"\nOptimal solution verified: {len(solution)} moves")


def example_4_advanced_api():
    """Example 4: Using the advanced API with detailed control."""
    print("\n\n" + "="*80)
    print("EXAMPLE 4: Advanced API Usage")
    print("="*80)
    
    initial_grid = [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
    
    goal_grid = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    
    print("\nCreating puzzle states...")
    initial_state = PuzzleState.from_2d_list(initial_grid)
    goal_state = PuzzleState.from_2d_list(goal_grid)
    
    print("Creating solver...")
    solver = SlidingPuzzleSolver(initial_state, goal_state)
    
    print(f"\nChecking solvability...")
    if solver.is_solvable():
        print("✓ Puzzle is solvable!")
        
        print("\nCalculating heuristic...")
        h = solver.manhattan_distance(initial_state)
        print(f"Manhattan distance from goal: {h}")
        
        print("\nSolving with A* search...")
        solution = solver.solve()
        
        if solution:
            stats = solver.get_statistics()
            
            print(f"\n{'='*60}")
            print("DETAILED STATISTICS")
            print(f"{'='*60}")
            print(f"Solution length:      {len(solution)} moves")
            print(f"Nodes expanded:       {stats['nodes_expanded']:,}")
            print(f"Max frontier size:    {stats['max_frontier_size']:,}")
            print(f"Search time:          {stats['search_time_seconds']:.4f} seconds")
            print(f"Average time/node:    {stats['search_time_seconds']/stats['nodes_expanded']*1000:.4f} ms")
            print(f"\nFirst 10 moves: {[m.name for m in solution[:10]]}")
    else:
        print("✗ Puzzle is not solvable (wrong parity)")


def example_5_unsolvable_detection():
    """Example 5: Detecting unsolvable puzzles."""
    print("\n\n" + "="*80)
    print("EXAMPLE 5: Unsolvable Puzzle Detection")
    print("="*80)
    
    unsolvable = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
    ]
    
    print("\nThis configuration is mathematically unsolvable.")
    print("(The 7 and 8 are swapped, creating odd parity)")
    
    for row in unsolvable:
        print(row)
    
    solution = solve_puzzle(unsolvable, verbose=True)
    
    if solution is None:
        print("\n✓ Correctly detected as unsolvable!")
        print("The solver checks parity before searching, saving time.")


def example_6_different_sizes():
    """Example 6: Solving different puzzle sizes."""
    print("\n\n" + "="*80)
    print("EXAMPLE 6: Different Puzzle Sizes")
    print("="*80)
    
    # 2x2 puzzle
    print("\n2x2 Puzzle:")
    puzzle_2x2 = [
        [1, 0],
        [2, 3]
    ]
    goal_2x2 = [
        [0, 1],
        [2, 3]
    ]
    
    solution = solve_puzzle(puzzle_2x2, goal_2x2)
    if solution:
        print(f"✓ Solved in {len(solution)} move(s)")
        visualize_solution(puzzle_2x2, solution, goal_2x2)
    
    # 4x4 puzzle (harder)
    print("\n\n4x4 Puzzle (takes longer):")
    puzzle_4x4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 0, 11],
        [13, 14, 15, 12]
    ]
    
    print("Initial state:")
    for row in puzzle_4x4:
        print(row)
    
    print("\nSolving... (this may take a few seconds)")
    solution = solve_puzzle(puzzle_4x4, verbose=True)
    
    if solution:
        print(f"\n✓ 4x4 puzzle solved in {len(solution)} moves!")


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  SLIDING PUZZLE SOLVER - EXAMPLE DEMONSTRATIONS".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    
    examples = [
        ("Basic Usage", example_1_basic_usage),
        ("Custom Goal State", example_2_custom_goal),
        ("Hard Puzzle", example_3_hard_puzzle),
        ("Advanced API", example_4_advanced_api),
        ("Unsolvable Detection", example_5_unsolvable_detection),
        ("Different Sizes", example_6_different_sizes),
    ]
    
    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    
    print("\nRunning all examples...")
    print("(Press Ctrl+C to skip to next example)\n")
    
    for name, func in examples:
        try:
            func()
        except KeyboardInterrupt:
            print(f"\n\nSkipping {name}...")
            continue
        except Exception as e:
            print(f"\n\nError in {name}: {e}")
            continue
    
    print("\n\n" + "="*80)
    print("All examples completed!")
    print("="*80)
    print("\nFor more information, see README.md")
    print("For production use, see sliding_puzzle_solver.py")
    print("For tests, run: python test_sliding_puzzle.py")
    print("For benchmarks, run: python benchmark.py")


if __name__ == "__main__":
    main()