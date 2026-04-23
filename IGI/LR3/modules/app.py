"""Application entry logic."""

from modules.input_utils import request_eps_value, request_repeat_choice, request_x_value
from modules.series_math import calculate_arccos_series
from modules.ui import print_header, print_result


def run_application() -> None:
    """Run the interactive laboratory work application."""
    print_header()

    while True:
        x_value = request_x_value()
        eps_value = request_eps_value()

        try:
            result, elapsed_time = calculate_arccos_series(x_value, eps_value)
            print_result(result, elapsed_time)
        except ArithmeticError as error:
            print(f"Calculation error: {error}")

        if not request_repeat_choice():
            print("The program has been finished.")
            break
