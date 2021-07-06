inp = list(map(str, input().split()))
print(max(inp, key=len))
print(len(max(inp, key=len)))