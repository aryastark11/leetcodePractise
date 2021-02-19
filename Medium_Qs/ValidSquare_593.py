from itertools import combinations 

def Diff(li1, li2):
    for element in li1:
        if element not in li2:
            return element

def getDist(p1, p2List):
    resList = []
    for i in p2List:
        diffX, diffY = p1[0] - i[0], p1[1] - i[1]
        resList.append((abs(diffX)** 2 + abs(diffY)** 2)**0.5)
    return resList

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        resLen = []
        pointList = [p1, p2, p3, p4]
        for nodeA in pointList:
            # check for duplicate points
            if pointList.count(list(nodeA)) > 1:
                return False

        res = [com for com in combinations(pointList, 3)]
            
        for node in res:
            # get the element not present in the combination
            element = Diff(pointList, node)
            # get all distances with the corresponding other 3 points
            dist1 = getDist(element, node)
            # 2 out of 3 distances should be equal
            if len(set(dist1)) == 2:
                # get the unique one
                    # check for 90 degree angle.
                    lineLen = [x for x in dist1 if dist1.count(x) > 1][0]
                    diagLen = [x for x in dist1 if dist1.count(x) < 2][0]
                    if abs(diagLen - ((2*(lineLen**2))**0.5)) <= 1e-01:
                        resLen.append(lineLen)
                    else:
                        return False
            else:
                return False

        if len(resLen) == 4 and len(set(resLen)) == 1:  ## all 4 dists are equal
            return True
        return False

            
            
            
        
        