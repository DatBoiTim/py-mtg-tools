import os

def flip(cause_uuid: bytes) -> bool|None:
    """
    Uses urandom for more realistic randomness
    Treats even numbers as heads, odd as tails
    Returns true if flip is won
    Returns false if flip is lost
    """
    flip_bstr: byte_string = os.getrandom(1)
    flip_int: int = int.from_bytes(flip_bstr)
    print(flip_int)
    if flip_int % 2 == 0:
        return True
    else:
        return False
    raise ValueError("flip_it() resulted in a non-heads, non-tails result")
