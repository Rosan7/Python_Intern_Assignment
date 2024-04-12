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

A = [1,2,3,4,5]
E = 1
B = [2,1,6,4,3]
print(findifAisB(A,B,E))






