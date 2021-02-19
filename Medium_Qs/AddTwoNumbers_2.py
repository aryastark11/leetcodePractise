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
        # till N1 and N2 digits are same.
        while(l2.next and l1.next):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(l1.val, l2.val, carry, resNode)
            listRes.append(resNode)
            l2 = l2.next
            l1 = l1.next   

        # add the last digit (node having Null as addr pointer)
        resNode = ListNode(0)
        resNode, carry = addAndGetVal(l1.val, l2.val, carry, resNode)
        listRes.append(resNode)

        # N1 has more digits
        if (l1.next):
            l1 = l1.next
            l1Count = 1
            while(l1.next):
                resNode = ListNode(0)
                resNode, carry = addAndGetVal(l1.val, 0, carry, resNode)
                listRes.append(resNode)
                l1 = l1.next
        # Last digit of N1
        if (l1Count):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(l1.val, 0, carry, resNode)
            listRes.append(resNode)
            
        # N2 has more digits
        if (l2.next):
            l2 = l2.next
            l2Count = 1
            while(l2.next):
                resNode = ListNode(0)
                resNode, carry = addAndGetVal(0, l2.val, carry, resNode)
                listRes.append(resNode)
                l2 = l2.next
       # Last digit of N2
        if (l2Count):
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(0, l2.val, carry, resNode)
            listRes.append(resNode)

        # cases where theres a overFlow --> sum has more digits than number.
        # create separate node for carry and add to the LinkedList
        if carry:
            resNode = ListNode(0)
            resNode, carry = addAndGetVal(0, 0, carry, resNode)
            listRes.append(resNode)

        # between testcases, these variables are reset.
        # else since they are global, values are added or affected by old testcase values.
        global globalHead
        global resultLinkedList
        globalHead = None
        resultLinkedList = ListNode(0)
        # joining each node to form a linkedList
        for i in range(len(listRes)-1, -1, -1):
            push(listRes[i])
            
        return resultLinkedList
