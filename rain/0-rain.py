#!/usr/bin/python3
"""Calculate how much water will be retained after it rains."""


def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max
    right_max[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate trapped water
    trapped = 0
    for i in range(n):
        water = min(left_max[i], right_max[i]) - walls[i]
        if water > 0:
            trapped += water

    return trapped
