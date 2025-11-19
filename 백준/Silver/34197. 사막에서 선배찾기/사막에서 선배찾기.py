import sys

# 표준 입출력 설정
input = sys.stdin.readline


def solve():
    # 태윤이의 현재 글로벌 좌표 (시작점 0,0)
    curr_r, curr_c = 0, 0

    # 나선형 이동 생성기
    def spiral_generator():
        length = 1
        while True:
            for _ in range(length): yield 'L'
            for _ in range(length): yield 'D'
            length += 1
            for _ in range(length): yield 'R'
            for _ in range(length): yield 'U'
            length += 1

    gen = spiral_generator()

    # 시야 정보를 읽어오는 함수 (입력 버퍼 처리용)
    def get_view():
        try:
            grid = [input().strip() for _ in range(3)]
            return grid
        except:
            return []

    # --- 1단계: 탐색 (Searching) ---
    # G를 발견할 때까지 나선형으로 이동

    # 초기 시야 확인
    view = get_view()

    target_r, target_c = None, None  # 국렬이의 글로벌 좌표 예정지

    # 먼저 시작하자마자 보이는지 확인 (운이 좋은 경우)
    for r in range(3):
        for c in range(3):
            if view[r][c] == 'G':
                target_r = curr_r + (r - 1)
                target_c = curr_c + (c - 1)

    # 안 보이면 나선형 이동 시작
    if target_r is None:
        while True:
            # 1. 이동 방향 결정 (나선형)
            move_dir = next(gen)

            # 2. 이동 명령 출력
            print(f"? {move_dir}")
            sys.stdout.flush()

            # 3. 내 좌표 갱신
            if move_dir == 'L':
                curr_c -= 1
            elif move_dir == 'R':
                curr_c += 1
            elif move_dir == 'U':
                curr_r -= 1
            elif move_dir == 'D':
                curr_r += 1

            # 4. 이동 후 시야 확인
            view = get_view()

            # 5. 국렬이 발견 체크
            found_in_view = False
            for r in range(3):
                for c in range(3):
                    if view[r][c] == 'G':
                        # 국렬이의 "절대 좌표" 계산해서 저장
                        target_r = curr_r + (r - 1)
                        target_c = curr_c + (c - 1)
                        found_in_view = True
                        break
                if found_in_view: break

            # 발견했으면 탐색 루프 종료 -> 접근 단계로
            if found_in_view:
                break

    # --- 2단계: 접근 (Approaching) ---
    # 국렬이의 좌표(target_r, target_c)를 알았으므로,
    # 시야에서 사라지든 말든 그 좌표까지 무조건 이동

    while curr_r != target_r or curr_c != target_c:
        move_dir = ''
        # 가로 이동 우선 (순서 상관 없음)
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

        # 이동했으니 입력은 무조건 받아줘야 함 (안 쓰더라도 버퍼 비우기)
        get_view()

    # --- 3단계: 귀환 (Returning) ---
    # 국렬이를 만났으니(현재 위치 == target), 거주지(0,0)로 복귀

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

        # 역시 입력 버퍼 비우기
        get_view()

    # 도착 완료!
    print("!")
    sys.stdout.flush()


if __name__ == "__main__":
    solve()