import sys
input = sys.stdin.readline
def solve():
    V, f, m, t = map(int, input().split())  # 変数名を工夫すると良いこともあります（変数名被りに注意）
    r = V % (f + m + t)
    if r < f:
        return "F"
    if r < f + m:
        return "M"
    return "T"


print(solve())
