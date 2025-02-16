#!/usr/bin/python3
"""
This module contains a function `canUnlockAll` that determines whether all
boxes in a list of lists can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each index contains a list of keys
        for other boxes.

    Returns:
        bool: True if all boxes can be unlocked,
        False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # The first box is initially unlocked
    keys = set(boxes[0])  # Keys available from the first box

    # Process until no new boxes can be unlocked
    while keys:
        new_key = keys.pop()  # Take a key from the set

        if new_key < n and not unlocked[new_key]:
            unlocked[new_key] = True  # Unlock the box
            keys.update(boxes[new_key])  # Add new keys from the unlocked box

    return all(unlocked)  # Check if all boxes are unlocked
