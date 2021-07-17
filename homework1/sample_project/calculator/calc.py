def check_power_of_2(a: int) -> bool:
    """Checks if a number is a power of 2"""
    return False if a < 1 else not (bool(a & (a - 1)))
