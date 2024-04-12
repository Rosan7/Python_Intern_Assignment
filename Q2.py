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