from typing import Sequence


def array_to_integer(byte_array: Sequence) -> int:
    return int.from_bytes(byte_array, byteorder='little')


def map_from_to(value: int, from_min: int, from_max: int, to_min: int, to_max: int) -> int:
    result = (value - from_min) / (from_max - from_min) * (to_max - to_min) + to_min
    return int(result)
