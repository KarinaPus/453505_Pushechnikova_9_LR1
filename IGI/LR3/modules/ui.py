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
    print("3 - Task 3: count spaces and punctuation marks")
    print("0 - Exit")
    print("-" * 72)


def print_task_1_header() -> None:
    """Show the heading for task 1."""
    print("\nTask 1. Variant 9")
    print("Function: arccos(x) = pi/2 - arcsin(x)")
    print("Series domain: |x| <= 1")
    print("-" * 72)


def print_task_2_header() -> None:
    """Show the heading for task 2."""
    print("\nTask 2. Variant 9")
    print("Goal: calculate the arithmetic mean of even integers")
    print("Input ends when you enter 0")
    print("-" * 72)


def print_task_3_header() -> None:
    """Show the heading for task 3."""
    print("\nTask 3. Variant 9")
    print("Goal: count spaces and punctuation marks in the entered text")
    print("Regular expressions are not used")
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


def print_task_2_result(result: dict, elapsed_time: float) -> None:
    """Display the result for task 2."""
    print("\nCalculation result")
    print("-" * 72)
    print(f"Entered numbers     = {result['numbers_count']}")
    print(f"Even numbers count  = {result['even_numbers_count']}")
    print(f"Even numbers        = {result['even_numbers']}")
    print(f"Average value       = {result['average_value']:.10f}")
    print(f"Elapsed time        = {elapsed_time:.6f} s")
    print("-" * 72)


def print_task_3_result(result: dict, elapsed_time: float) -> None:
    """Display the result for task 3."""
    print("\nCalculation result")
    print("-" * 72)
    print(f"Entered text length = {result['text_length']}")
    print(f"Spaces count        = {result['spaces_count']}")
    print(f"Punctuation count   = {result['punctuation_count']}")
    print(f"Elapsed time        = {elapsed_time:.6f} s")
    print("-" * 72)
