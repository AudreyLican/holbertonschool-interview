#!/usr/bin/python3

def validUTF8(data):
    num_bytes = 0  # Number of bytes left in the current UTF-8 character

    for num in data:
        byte = num & 0xFF  # keep the 8 least significant bits
        
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # If it starts with '10', it's invalid as a starting byte
                return False
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1  # Reduce the count of expected continuation bytes

    return num_bytes == 0  # Must end with no leftover expected bytes
