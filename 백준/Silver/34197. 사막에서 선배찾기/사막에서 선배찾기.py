import sys

input = sys.stdin.readline


def findYume():
    #아비도스 고등학교의 좌표
    curr_r, curr_c = 0, 0

    #당근 스파이럴
    def carrot_spiral():
        length = 1
        while True:
            for _ in range(length): yield 'L'
            for _ in range(length): yield 'D'
            length += 1
            for _ in range(length): yield 'R'
            for _ in range(length): yield 'U'
            length += 1

    gen = carrot_spiral()

    #호시노 시야
    def Hoshino_view():
        try:
            grid = [input().strip() for _ in range(3)]
            return grid
        except:
            return []

    #유메선배를 찾자
    #나선형으로 유메를 찾을때까지 이동

    #호시노의 시야를 확인
    view = Hoshino_view()

    target_r, target_c = None, None  #유메선배의 예상 위치

    #혹시 바로 보이는지 확인
    for r in range(3):
        for c in range(3):
            if view[r][c] == 'G':
                target_r = curr_r + (r - 1)
                target_c = curr_c + (c - 1)

    #안보이면 나선형 이동 시작
    if target_r is None:
        while True:
            #이동방향결정
            move_dir = next(gen)

            #이동명령출력
            print(f"? {move_dir}")
            sys.stdout.flush()

            #호시노 좌표 갱신
            if move_dir == 'L':
                curr_c -= 1
            elif move_dir == 'R':
                curr_c += 1
            elif move_dir == 'U':
                curr_r -= 1
            elif move_dir == 'D':
                curr_r += 1

            #이동 후 호시노 시야
            view = Hoshino_view()

            #유메선배 발견했는지 체크
            found_Yume = False
            for r in range(3):
                for c in range(3):
                    if view[r][c] == 'G':
                        #유메선배 예상 위치 수정후 저장
                        target_r = curr_r + (r - 1)
                        target_c = curr_c + (c - 1)
                        found_Yume = True
                        break
                if found_Yume: break

            #유메선배를 찾음
            if found_Yume:
                break

    #이제 유메선배를 찾았으니까 그 위치로 이동

    while curr_r != target_r or curr_c != target_c:
        move_dir = ''
        #먼저 가로로 이동후 세로로 이동해서 유메선배에 도착
        if curr_c > target_c:
            move_dir = 'L'
        elif curr_c < target_c:
            move_dir = 'R'
        elif curr_r > target_r:
            move_dir = 'U'
        elif curr_r < target_r:
            move_dir = 'D'

        print(f"? {move_dir}")
        sys.stdout.flush()

        if move_dir == 'L':
            curr_c -= 1
        elif move_dir == 'R':
            curr_c += 1
        elif move_dir == 'U':
            curr_r -= 1
        elif move_dir == 'D':
            curr_r += 1

        #이동후 확실히 찾았는지 확인
        Hoshino_view()

    #유메선배를 찾았으니 아비도스 고등학교로 복귀

    while curr_r != 0 or curr_c != 0:
        move_dir = ''
        if curr_c > 0:
            move_dir = 'L'
        elif curr_c < 0:
            move_dir = 'R'
        elif curr_r > 0:
            move_dir = 'U'
        elif curr_r < 0:
            move_dir = 'D'

        print(f"? {move_dir}")
        sys.stdout.flush()

        if move_dir == 'L':
            curr_c -= 1
        elif move_dir == 'R':
            curr_c += 1
        elif move_dir == 'U':
            curr_r -= 1
        elif move_dir == 'D':
            curr_r += 1

        #아비도스 도착확인
        Hoshino_view()

    #도착
    print("!")
    sys.stdout.flush()


if __name__ == "__main__":
    findYume()