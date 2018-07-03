import unittest
def delete_node(node):
    ptr = node.next
    if ptr:
        node.next = ptr.next
        node.value = ptr.value
    else:
        raise ValueError("Cannot delete the tail node..")