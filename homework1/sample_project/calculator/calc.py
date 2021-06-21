def check_power_of_2(num: int) -> bool:
    """Checks if a number is a power of 2"""
    return False if num < 1 else not bool(num & (num - 1))
