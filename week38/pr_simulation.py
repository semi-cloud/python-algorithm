# 이긴 상황(O, X 이긴 상황 두가지로 나뉨)에서 거꾸로 조건을 되돌아가기

def play_game(arr):
    bingos_o, bingos_x = 0, 0  # 각 빙고 개수를 알아야함

    for i in range(len(arr)):  # 가로줄 검사
        if arr[i][0] == arr[i][1] == arr[i][2]:
            if arr[i][0] == 'O':
                bingos_o += 1
            elif arr[i][0] == 'X':
                bingos_x += 1

    for i in range(len(arr)):  # 세로줄 검사
        if arr[0][i] == arr[1][i] == arr[2][i]:
            if arr[0][i] == 'O':
                bingos_o += 1
            elif arr[0][i] == 'X':
                bingos_x += 1

    if arr[0][0] == arr[1][1] == arr[2][2]:  # 왼쪽 위 대각선 검사
        if arr[0][0] == 'O':
            bingos_o += 1
        elif arr[0][0] == 'X':
            bingos_x += 1

    if arr[0][2] == arr[1][1] == arr[2][0]:  # 오른쪽 위 대각선 검사
        if arr[0][2] == 'O':
            bingos_o += 1
        elif arr[0][2] == 'X':
            bingos_x += 1
    return bingos_o, bingos_x

def solution(board):
    num_o, num_x = 0, 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'O':
                num_o += 1
            elif board[i][j] == 'X':
                num_x += 1

    if num_o == 0 and num_x == 0: return 1  # 아무것도 안 놓여져 있는 상태
    if num_o - num_x < 0 or num_o - num_x >= 2: return 0  # 2. X가 더 많거나, O가 2개 이상 많아지는 경우 번갈아서 해야하는 규칙 위반

    bingos_o, bingos_x = play_game(board)
    if bingos_o > 0 and bingos_x == 0:
        if num_o != num_x + 1:
            return 0  # O이 이겼을 경우 하나 더 많아야함
    elif bingos_o == 0 and bingos_x > 0:
        if num_o != num_x:
            return 0  # X가 이겼을 경우 같아야함
    elif bingos_o > 0 and bingos_x > 0:
        return 0  # 둘이 동시에 이기는 경우(O, X 줄이 각각 만들어져 있는 경우) 불가능
    return 1

# 처음부터 검사해서 누가 이겼는지 체크하는 방식은
# 배열 위쪽에서 만나는 문자에 따라 달라지기 때문에 정확하게 알 수 X (ex) XXX ... OOO => X가 이긴 상태로 판별됌)
# 틀린 방식)
# ans = True
# prev = arr[0][2]
# for i in range(len(arr)):   # 오른쪽 위 대각선 검사
#     if prev != arr[0 + i][2 - i]:
#         ans = False
# if ans: return True, prev
