import itertools

minsum = 10000000000000000
l = [int(input()) for _ in range(12)]
ind = [i for i in range(12)]
for ia in itertools.combinations(ind, 3):
    cow1 = [l[j] for j in ia]
    l1 = [k for k in ind if k not in ia]

    for ib in itertools.combinations(l1, 3):
        cow2 = [l[j] for j in ib]
        l2 = [k for k in l1 if k not in ib]

        for ic in itertools.combinations(l2, 3):
            cow3 = [l[j] for j in ic]
            l3 = [k for k in l2 if k not in ic]

            for ie in itertools.combinations(l3, 3):
                cow4 = [l[j] for j in ie]

                skilllevel = [sum(cow1), sum(cow2), sum(cow3), sum(cow4)]
                maximum = max(skilllevel)
                minimum = min(skilllevel)
                if minsum >= maximum - minimum:
                    minsum = maximum - minimum
print(minsum)