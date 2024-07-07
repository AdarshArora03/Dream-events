T = int(input())

for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    v = list(map(int, input().split()))
    X = int(input())
    max_value = 0
    for i in range(N):
        sum_a = 0
        sum_v = 0
        for j in range(i, N):
            sum_a += a[j]
            sum_v += v[j]
            if sum_a == X * (j-i+1) and sum_v > max_value:
                max_value = sum_v
    print(max_value)
