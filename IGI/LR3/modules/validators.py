"""Validation helpers for user input."""


def parse_float(user_input: str, field_name: str) -> float:
    """Convert user input to float with a clear error message."""
    try:
        return float(user_input.replace(",", ".").strip())
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a real number.") from exc


def validate_x_value(x_value: float) -> float:
    """Validate the argument range for arccos(x)."""
    if not -1.0 <= x_value <= 1.0:
        raise ValueError("x must belong to the interval [-1, 1].")
    return x_value


def validate_eps_value(eps_value: float) -> float:
    """Validate the required positive accuracy."""
    if eps_value <= 0:
        raise ValueError("eps must be greater than 0.")
    return eps_value
