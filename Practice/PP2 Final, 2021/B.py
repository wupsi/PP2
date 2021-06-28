import sys

s = input()
L = list(map(str, sys.stdin.read().split()))

for i in sorted(L):
    print(i, end = ' ') if sorted(s) != sorted(i)