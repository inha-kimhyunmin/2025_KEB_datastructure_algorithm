class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


def pre_order(node):
    if node is None:
        return
    print(node.data, end=' -> ')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end = ' -> ')
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end = ' -> ')


# n1, n2 ,n3 = [TreeNode(data) for data in range(3)] 이 방법으로 만들어도 된다.

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.right = node7
node6.right = node8

#        1
#    2      3
#  4   5   6
#   7        8
#
pre_order(node1)
print("End")
in_order(node1)
print("End")
post_order(node1)
print("End")
