def number_to_binary(number: int, bit_number: int) -> str:
    """
    Convert a non-negative integer to its binary representation,
    padded with leading zeros to exactly `bit_number` bits.
    Raises ValueError if the number is negative or too large.
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    # Format as binary without the '0b' prefix, then pad
    b = format(number, 'b')
    if len(b) > bit_number:
        raise ValueError(f"number requires more than {bit_number} bits")
    return b.zfill(bit_number)


def binary_to_number(binary_str: str) -> int:
    """
    Convert a binary string (e.g. '0101') to its integer value.
    Raises ValueError if the string contains non-binary characters.
    """
    # Validate
    if not all(c in '01' for c in binary_str):
        raise ValueError("binary_str must contain only '0' or '1'")
    return int(binary_str, 2)


def number_to_hex(number: int, hex_digits: int) -> str:
    """
    Convert a non-negative integer to its hexadecimal representation (uppercase),
    padded with leading zeros to exactly `hex_digits` digits.
    Raises ValueError if the number is negative or too large.
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    h = format(number, 'X')  # uppercase hex without '0x'
    if len(h) > hex_digits:
        raise ValueError(f"number requires more than {hex_digits} hex digits")
    return h.zfill(hex_digits)


def hex_to_number(hex_str: str) -> int:
    """
    Convert a hexadecimal string (e.g. '0A3F' or 'a3f') to its integer value.
    Raises ValueError if the string contains non-hex characters.
    """
    # Strip optional "0x"/"0X"
    s = hex_str.strip()
    if s.lower().startswith('0x'):
        s = s[2:]
    # Validate
    if not all(c in '0123456789abcdefABCDEF' for c in s):
        raise ValueError("hex_str must be a valid hexadecimal string")
    return int(s, 16)

