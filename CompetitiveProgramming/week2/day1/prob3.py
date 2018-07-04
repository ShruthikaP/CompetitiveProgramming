jimport unittest
def contains_cycle(node):
    p1 = p2 = node
    while(p1 and p2 and p2.next):
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return True       
    return False