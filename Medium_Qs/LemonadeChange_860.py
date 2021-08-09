class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if 5 not in bills:
            return False
        noteListAtHand = {5:0, 10:0, 20:0}  # initially all change=0
        for b in bills:
            if b == 5:
                noteListAtHand.update({5:(noteListAtHand[5]+1)})
            elif b == 10:
                if noteListAtHand[5] > 0:
                    noteListAtHand.update({5:(noteListAtHand[5]-1)}) 
                    noteListAtHand.update({10:(noteListAtHand[10]+1)}) 
                else:
                    return False
            else:
                if noteListAtHand[10] > 0 and noteListAtHand[5] > 0 :
                    noteListAtHand.update({5:(noteListAtHand[5]-1)}) 
                    noteListAtHand.update({10:(noteListAtHand[10]-1)})
                    noteListAtHand.update({20:(noteListAtHand[20]+1)})
                elif noteListAtHand[5] >= 3:
                    noteListAtHand.update({5:(noteListAtHand[5]-3)})  # get 15 from the change
                    noteListAtHand.update({20:(noteListAtHand[20]+1)})
                else:
                    return False
            print(b, noteListAtHand)
        if noteListAtHand[5] >=0 and noteListAtHand[10] >=0 and noteListAtHand[20] >=0:
            return True
        return False
                    
            
## ======================================================================================================
# optimized solution

class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True