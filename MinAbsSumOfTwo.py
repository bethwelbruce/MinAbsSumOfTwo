def solution(A):
    A.sort()
    i = 0
    j = len(A) - 1
    min_sum = abs(A[i] + A[j])
    while i <= j:
        cur_sum = abs(A[i] + A[j])
        min_sum = min(min_sum, cur_sum)
        if cur_sum == 0:
            return 0
        elif A[i] + A[j] < 0:
            i += 1
        else:
            j -= 1
    return min_sum
