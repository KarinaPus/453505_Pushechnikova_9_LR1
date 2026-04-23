"""Presentation helpers for the console interface."""


def print_main_header() -> None:
    """Show the main program heading."""
    print("=" * 72)
    print("Laboratory work 3. Variant 9")
    print("Interactive launcher for the laboratory tasks")
    print("=" * 72)


def print_task_menu() -> None:
    """Display the available tasks."""
    print("\nAvailable tasks")
    print("-" * 72)
    print("1 - Task 1: arccos(x) using a power series")
    print("2 - Task 2: sequence processing")
    print("0 - Exit")
    print("-" * 72)


def print_task_1_header() -> None:
    """Show the heading for task 1."""
    print("\nTask 1. Variant 9")
    print("Function: arccos(x) = pi/2 - arcsin(x)")
    print("Series domain: |x| <= 1")
    print("-" * 72)


def print_result(result: dict, elapsed_time: float) -> None:
    """Display the calculation result in a user-friendly form."""
    print("\nCalculation result")
    print("-" * 72)
    print(f"x              = {result['x']:.10f}")
    print(f"F(x)           = {result['series_value']:.10f}")
    print(f"n              = {result['terms_used']}")
    print(f"Math F(x)      = {result['math_value']:.10f}")
    print(f"Absolute error = {result['absolute_error']:.10e}")
    print(f"Elapsed time   = {elapsed_time:.6f} s")
    print("-" * 72)


def print_task_2_stub() -> None:
    """Show a stub message for task 2."""
    print("\nTask 2. Variant 9")
    print("-" * 72)
    print("This task has not been implemented yet.")
    print("The menu is already prepared, so task 2 can be added next.")
    print("-" * 72)
