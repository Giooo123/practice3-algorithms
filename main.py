def w_interval(ints):
    ints.sort(key=lambda x: x[1])
    n = len(ints)
    best_w = [0]*n
    prev_int = [-1]*n
    for cur in range(n):
        s, f, w = ints[cur]
        prev = cur-1
        while prev >= 0 and ints[prev][1] > s:
            prev -= 1
        take = w + (best_w[prev] if prev >= 0 else 0)
        skip = best_w[cur-1] if cur else 0
        if take > skip:
            best_w[cur] = take
            prev_int[cur] = prev
        else:
            best_w[cur] = skip
            prev_int[cur] = cur-1

    chosen = []
    i = n-1

    while i >= 0:
        if prev_int[i] == i-1:
            i -= 1
        else:
            chosen.append(ints[i])
            i = prev_int[i]
    return f'Общий вес - {best_w[-1]}. Интервлы: {chosen[::-1]}'

intervals = [
    (1, 4, 5),
    (3, 5, 1),
    (0, 6, 8),
    (4, 7, 4),
    (3, 9, 6),
    (5, 9, 3),
    (6, 10, 2),
    (8, 11, 4),
    (8, 12, 7),
    (2, 13, 9),
    (12, 14, 6),
    (1, 15, 8),
    (13, 16, 5),
    (14, 17, 4),
    (16, 18, 3),
    (17, 19, 7),
    (18, 20, 2),
    (19, 22, 6),
    (21, 24, 5),
    (23, 26, 9)
]

print(w_interval(intervals))