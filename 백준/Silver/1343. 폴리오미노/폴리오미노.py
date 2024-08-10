board=input()
board=board.replace("XXXX", "AAAA")
board=board.replace("XX", "BB")
if board.find("X")!=-1:
    print("-1")
else:
    print(board)