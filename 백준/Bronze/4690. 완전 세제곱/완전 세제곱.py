for i in range(2, 101):
    cube=i**3
    for j in range(2, 101):
        for k in range(j+1, 101):
            for l in range(k+1, 101):
                if cube==j**3+k**3+l**3:
                    print(f"Cube = {i}, Triple = ({j},{k},{l})")