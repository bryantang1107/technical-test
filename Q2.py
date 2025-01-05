#Time: 4 Mins 5 Secs
def findMiddleNode(head):
    length = 0
    dummy = head
    #get length of linked list
    while head:
        head = head.next
        length += 1
    
    #find midpoint of linked list
    mid = length // 2

    #traverse to mid point
    while dummy and mid > 0:
        mid -= 1
        dummy = dummy.next

    #return starting from mid point
    return dummy

