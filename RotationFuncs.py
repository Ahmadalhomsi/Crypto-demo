def rotate_left(value: int, shift: int, width: int) -> int:
    """
    Perform a circular left bit shift on `value`.

    Args:
        value: The non-negative integer to rotate.
        shift: Number of bit positions to rotate left.
        width: Bit width for the rotation (e.g., 8, 16, 32).

    Returns:
        The result of rotating `value` left by `shift` within `width` bits.

    Raises:
        ValueError: If value is negative or width is non-positive.
    """
    if value < 0:
        raise ValueError("Value must be non-negative")  # validation
    if width <= 0:
        raise ValueError("Width must be a positive integer")
    # Normalize shift to [0, width)
    shift %= width  # avoids full-width redundant rotations :contentReference[oaicite:7]{index=7}
    # Mask to retain only `width` bits
    mask = (1 << width) - 1
    # Left-shifted part & overflowed bits wrapped around
    left = (
        value << shift
    ) & mask  # shifted and masked :contentReference[oaicite:8]{index=8}
    wrap = (value & mask) >> (
        width - shift
    )  # bits that overflow :contentReference[oaicite:9]{index=9}
    return left | wrap


def rotate_right(value: int, shift: int, width: int) -> int:
    """
    Perform a circular right bit shift on `value`.

    Args:
        value: The non-negative integer to rotate.
        shift: Number of bit positions to rotate right.
        width: Bit width for the rotation (e.g., 8, 16, 32).

    Returns:
        The result of rotating `value` right by `shift` within `width` bits.

    Raises:
        ValueError: If value is negative or width is non-positive.
    """
    if value < 0:
        raise ValueError("Value must be non-negative")
    if width <= 0:
        raise ValueError("Width must be a positive integer")
    # Normalize shift to [0, width)
    shift %= width  # avoids redundant rotations :contentReference[oaicite:13]{index=13}
    mask = (1 << width) - 1
    right = (
        value & mask
    ) >> shift  # logical right shift within mask :contentReference[oaicite:14]{index=14}
    wrap = (
        value << (width - shift)
    ) & mask  # bits that overflow from the right :contentReference[oaicite:15]{index=15}
    return right | wrap
