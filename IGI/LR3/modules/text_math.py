"""Business logic for text analysis tasks."""

import string

from modules.decorators import log_execution_time


@log_execution_time
def count_spaces_and_punctuation(text_value: str) -> dict:
    """Count spaces and punctuation marks in a text without regex."""
    spaces_count = 0
    punctuation_count = 0

    for symbol in text_value:
        if symbol == " ":
            spaces_count += 1
        if symbol in string.punctuation:
            punctuation_count += 1

    return {
        "text_length": len(text_value),
        "spaces_count": spaces_count,
        "punctuation_count": punctuation_count,
    }
