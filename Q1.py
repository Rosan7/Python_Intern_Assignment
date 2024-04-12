def findifAisB(A,B,E):
    if len(A) == 0:
        return True
    if len(A) != len(B):
        return False
    min_no = min(A) - 1
    max_no = max(A) + 1
    for i in B:
        if min_no <= i <= max_no:
            continue
        else:
            return False
    diff = abs(sum(A) - sum(B))
    if E == 1:

        if len(A)%2 == 0:

            if diff % 2 == 0:
                if 0 <= diff <= len(A):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if diff % 2 == 1:
                if 0 <= diff <= len(A):
                    return True
                else:
                    return False
            else:
                return False
    else:
        if diff % E == 0:
            return True
        else:
            return False

# A = [1,2,3,4,5]
# E = 1
# B = [2,1,6,4,3]
# print(findifAisB(A,B,E))

from collections import defaultdict







def findmaxlength(A,N,target):
    idx_sum = defaultdict(lambda : 0)
    curr_sum = 0
    soln = []
    maxlength = 0
    start = 0
    end = 0
    for i in range(len(A)):
        curr_sum += A[i]

        if curr_sum == target:

            maxlength = max(maxlength,i+1)

        if curr_sum-k in idx_sum:
            start = idx_sum[curr_sum-target] + 1
            end = i
            maxlength = max(maxlength,end-start+1)
        idx_sum[curr_sum] = i

    return maxlength


A = [10,2,-2,-20,10]
k = -10
N = 5
print(findmaxlength(A,N,k))




