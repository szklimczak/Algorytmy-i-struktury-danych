# Skończone

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def orientacja(p, q, r):
    k = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)
    if k == 0:
        return 0
    elif k > 0:
        return 1
    else:
        return 2

def start_point(punkty):
    start_point = 0
    for i in range(1, len(punkty)):
        if punkty[i].x < punkty[start_point].x:
            start_point = i
        elif punkty[i].x == punkty[start_point].x:
            if punkty[i].y < punkty[start_point].y:
                start_point = i
    return start_point

def jarvis1(punkty):
    start = start_point(punkty)
    p = start
    hull = []
    while True:
        hull.append(punkty[p])
        q = (p + 1) % len(punkty)
        for i in range(len(punkty)):
            if orientacja(punkty[p], punkty[i], punkty[q]) == 2:
                q = i
        p = q
        if p == start:
            break
    return hull

def jarvis2(punkty):
    start = start_point(punkty)
    p = start
    hull = []
    while True:
        hull.append(punkty[p])
        q = (p + 1) % len(punkty)
        for r in range(len(punkty)):
            orient = orientacja(punkty[p], punkty[r], punkty[q])
            if orient == 2:
                q = r
            elif orient == 0:
                if (punkty[r].x - punkty[p].x) ** 2 + (punkty[r].y - punkty[p].y) ** 2 > \
                        (punkty[q].x - punkty[p].x) ** 2 + (punkty[q].y - punkty[p].y) ** 2:
                    q = r
        p = q
        if p == start:
            break
    return hull


def main():
    p1 = []
    points1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    for point in points1:
        p1.append(Point(point[0], point[1]))
    #print(jarvis1(p1))
    #print(jarvis2(p1))
    p2 = []
    points2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    for point in points2:
        p2.append(Point(point[0], point[1]))
    #print(jarvis1(p2))
    #print(jarvis2(p2))
    p = []
    points = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    for point in points:
        p.append(Point(point[0], point[1]))
    print(jarvis1(p))
    print(jarvis2(p))

if __name__ == '__main__':
    main()