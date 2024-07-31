N, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
cut = scores[k-1]
print(cut)