def euclid(m,k):
    L = list()
    y = 0
    slope = k / m
    L.append(1);
    for x in range(1,m):
        if (slope * x - y >= 1):
            L.append(1)
            y = y + 1
        else:
            L.append(0)
    return L
