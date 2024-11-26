"""Asks user if they want to perform another calculation"""
from Data.Shared.classes.validators import Validators
from global_variables import MEMORY_OPERATIONS


def parse(result):
    """Also includes memory operations"""
    try_again = input("Would you like to try again? (Y / N) "
                      "// Store a value into memory? (MS / M+ / M-): ").lower()
    if try_again in MEMORY_OPERATIONS:
        Validators.validate_memory(try_again, result)
        return True
    if try_again == "y":
        return False
    return True
