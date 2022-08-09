def solution(array, commands):
    return [sorted(array[i - 1:j])[k - 1] for i, j, k in commands]

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# @방법 1
# return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# @방법 2(내 풀이)
# answer = []
# for i, j, k in commands:
#     num = sorted(array[i-1:j])[k-1]
#     answer.append(num)
# return answer
