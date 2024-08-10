def count_claps(n):
    total_claps = 0
    for i in range(1, n + 1):
        str_i = str(i)
        total_claps += str_i.count('3') + str_i.count('6') + str_i.count('9')
    return total_claps
n=int(input())
print(count_claps(n))