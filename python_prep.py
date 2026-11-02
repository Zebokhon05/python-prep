def exercise_1(S):
    total = 0
    for x in S:
        total += x
    return total


def exercise_2(S):
    return sum(S)


def exercise_3():
    points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    f = {}
    for (x, y) in points:
        f[(x, y)] = 8 * x + 3 * y
    return f
    
