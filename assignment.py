# def common_member(a, b):    
#     a = set(a)
#     b = set(b)
    
#     if len(a.intersection(b)) > 0:
#         return(a.intersection(b))  
#     else:
#         return("no common elements")
    
# a = [1,2,3,4,5]
# b = [5,6,7,8,2]

# print(common_member(a,b))   

class node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = None


def traverse(head):
    current = head
    while current:
        print(current.data, end=" ")
        
        current = current.next
    print()

head = node(1,node(2,node(3,node(4,node(5)))))


traverse(head)