class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):  # abab, ababa
            return False
        if set(A) != set(B):  # they have different chars --> abac, abad
            return False
        if len(A) < 1:  # "" 
            return False
        if A == B:
            if len(A) <2:  # "a" , "a"
                return False 
            if len(set(A)) < 2:   # aa
                return True
            elif len(set(A)) == len(A): ## ab
                return False
            else:  # abcabc
                return True
        i = 0
        pivot = []
        while(i<len(A)):
            if A[i] != B[i]:
                pivot.append(i)
            i +=1
        if len(pivot) == 0:
            return False
        if len(pivot) > 2 or len(set(pivot)) < len(pivot):
            return False
        if A[pivot[0]] == B[pivot[1]] and A[pivot[1]] == B[pivot[0]]:
            return True
        return False
        
            
## optimised solutions

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        
        count = 0
        l_swipe = {}
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                if count == 3:
                    return False
                l_swipe[A[i]] = B[i]
                
        if count == 1:
            return False
        
        if count == 2:
            for l in l_swipe:
                if l not in l_swipe.values():
                    return False
            return True
            
        letter_counter = collections.Counter()
        for i in range(len(A)):
            letter_counter[A[i]] += 1
            if letter_counter[A[i]] == 2:
                return True
            
        return False
