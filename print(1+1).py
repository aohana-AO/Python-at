import sys
input = sys.stdin.readline

C = 2 ** 31
N = int(input())
print("Yes" if -C <= N < C else "No")  # 以上、未満です
