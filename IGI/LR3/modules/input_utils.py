"""Helpers for interactive input."""

from modules.validators import parse_float, validate_eps_value, validate_x_value


def request_float(prompt_text: str, field_name: str) -> float:
    """Request a floating-point number until it is entered correctly."""
    while True:
        raw_value = input(prompt_text)
        try:
            return parse_float(raw_value, field_name)
        except ValueError as error:
            print(f"Input error: {error}")


def request_x_value() -> float:
    """Request a valid x value from the user."""
    while True:
        x_value = request_float("Enter x in [-1, 1]: ", "x")
        try:
            return validate_x_value(x_value)
        except ValueError as error:
            print(f"Input error: {error}")


def request_eps_value() -> float:
    """Request a valid positive epsilon from the user."""
    while True:
        eps_value = request_float("Enter eps (> 0): ", "eps")
        try:
            return validate_eps_value(eps_value)
        except ValueError as error:
            print(f"Input error: {error}")


def request_repeat_choice() -> bool:
    """Ask whether the user wants to repeat the calculation."""
    while True:
        answer = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if answer in {"y", "yes", "д", "да"}:
            return True
        if answer in {"n", "no", "н", "нет"}:
            return False
        print("Input error: enter 'y' or 'n'.")
