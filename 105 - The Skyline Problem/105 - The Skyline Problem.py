import sys


def main():
    recs = iter(sys.stdin.readlines())
    skylines = [0] * 10001
    rightmost = 0
    while True:
        try:
            left, height, right = list(map(int, next(recs).split()))
            for idx in range(left, right):
                if height > skylines[idx]:
                    skylines[idx] = height
            rightmost = max(rightmost, right)

        except (StopIteration):
            ans = ["{} {}".format(idx, skylines[idx])
                   for idx in range(1, rightmost + 1)
                   if skylines[idx - 1] != skylines[idx]]
            print(" ".join(ans))
            break


if __name__ == '__main__':
    main()
