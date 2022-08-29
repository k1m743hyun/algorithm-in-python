def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for idx in range(len(board)):
            if board[idx][move - 1]:
                stack.append(board[idx][move - 1])
                board[idx][move - 1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break

    return answer
