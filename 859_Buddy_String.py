## From Leetcode 859. Buddy Strings
##

def buddyStrings(self, A, B):

    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    # if two strings' length differ 
    if len(A) != len(B): return False
    
    # inititate parameter
    diff = 0
    idx = []
    
    # if two strings are different 
    for i, e in enumerate(A):
        if B[i] != e:
            diff += 1
            idx.append(i)
    
    # dictionary
    my_dict = {}
    
    # if two strings are the same
    if diff == 0:
        for i in range(len(A)):
            if A[i] in my_dict and my_dict[A[i]]:
                return True
            else:
                my_dict[A[i]] = True
    
    # if more than 2 different characters
    if diff != 2: return False
    
    return A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]