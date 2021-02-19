# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

globalHead = None
resultLinkedList = ListNode(0)

def push(newLinkedNode):
    global globalHead
    global resultLinkedList
    resultLinkedList = newLinkedNode
    resultLinkedList.next = globalHead
    globalHead = newLinkedNode

def addAndGetVal(intA, intB, intC, resList):
    carry = 0
    resList.val = intA + intB + intC
    if resList.val > 9:
        carry = int(resList.val / 10)
        resList.val -= 10
    resList.next = None
    return [resList, carry]

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listRes = []
        l1Count = 0
        l2Count = 0
        carry = 0
        while(l2.next and l1.next):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(l1.val, l2.val, carry, resNode)
            listRes.append(resNode)
            l2 = l2.next
            l1 = l1.next   

        resNode = ListNode(0)
        resNode, carry = addAndGetVal(l1.val, l2.val, carry, resNode)
        listRes.append(resNode)
        
        if (l1.next):
            l1 = l1.next
            l1Count = 1
            while(l1.next):
                resNode = ListNode(0)
                resNode, carry = addAndGetVal(l1.val, 0, carry, resNode)
                listRes.append(resNode)
                l1 = l1.next
        if (l1Count):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(l1.val, 0, carry, resNode)
            listRes.append(resNode)
            
        if (l2.next):
            l2 = l2.next
            l2Count = 1
            while(l2.next):
                resNode = ListNode(0)
                resNode, carry = addAndGetVal(0, l2.val, carry, resNode)
                listRes.append(resNode)
                l2 = l2.next
        if (l2Count):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(0, l2.val, carry, resNode)
            listRes.append(resNode)

        if carry:
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(0, 0, carry, resNode)
            listRes.append(resNode)

        global globalHead
        global resultLinkedList
        globalHead = None
        resultLinkedList = ListNode(0)
        for i in range(len(listRes)-1, -1, -1):
            push(listRes[i])
        
        
        return resultLinkedList


        
