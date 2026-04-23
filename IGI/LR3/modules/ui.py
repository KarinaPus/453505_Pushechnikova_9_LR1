"""Presentation helpers for the console interface."""


def print_header() -> None:
    """Show the program heading."""
    print("=" * 72)
    print("Laboratory work 3. Task 1. Variant 9")
    print("Function: arccos(x) = pi/2 - arcsin(x)")
    print("Series domain: |x| <= 1")
    print("=" * 72)


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
