class NArray:
    @staticmethod
    def n2(n: int):
        """
        2D array with same rows and cols
        """
        arr = [[0 for _ in range(n)] for _ in range(n)]
        return arr

    @staticmethod
    def flip_x(arr: list):
        """
        arr = [
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
        ]

        x_arr = [
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 1]
        ]
        """
        f_arr = []

        for row in arr:
            f_arr.append(row[::-1])

        return f_arr

    @staticmethod
    def flip_y(arr: list):
        """
        arr = [
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
            [1, 0, 0, 1],
        ]

        y_arr = [
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1],
            [1, 0, 0, 1]
        ]
        """
        return [row for row in reversed(arr)]

    @staticmethod
    def unfold(arr: list):
        """
        Unfold 6x6 array to make 11x11 array; 1 pixel is padding
        that means it can transform

        0 0 1 P
        0 1 0 P
        1 0 0 P
        P P P P

        to

        0 0 1 P 1 0 0
        0 1 0 P 0 1 0
        1 0 0 P 0 0 1
        P P P P P P P
        1 0 0 P 0 0 1
        0 1 0 P 0 1 0
        0 0 1 P 1 0 0

        P is margin of folded pattern and can be 0 or 1
        """

        fx = NArray.flip_x(arr)
        fy = NArray.flip_y(arr)
        fxy = NArray.flip_y(fx)

        N = len(arr)
        D = N * 2 - 1
        out = NArray.n2(D)

        out = NArray.copy(out, arr, (0, 0))
        out = NArray.copy(out, fx, (N - 1, 0))
        out = NArray.copy(out, fy, (0, N - 1))
        out = NArray.copy(out, fxy, (N - 1, N - 1))

        return out

    @staticmethod
    def copy(org, part, start: tuple = (0, 0)):
        """
        start = (x,y)
        """
        rN = len(part)
        cN = len(part[0])
        for r in range(start[1], start[1] + rN):
            for c in range(start[0], start[0] + cN):
                org[r][c] = part[r - start[1]][c - start[0]]

        return org

    @staticmethod
    def visualize(arr: list, _map={0: "-", 1: "#"}):
        """ """

        for row in arr:
            for cel in row:
                print(_map[cel], end="  ")
            print()

    def rotate90(arr):
        return [row[::-1] for row in [list(row) for row in zip(*arr)]]


if __name__ == "__main__":
    print(NArray.n2(5))

    arr = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 0],
        [1, 0, 0, 0],
    ]

    NArray.visualize(NArray.unfold(arr))
