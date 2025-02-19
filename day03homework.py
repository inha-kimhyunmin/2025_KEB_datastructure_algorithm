import random


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
    print(node.data, end=' -> ')
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=' -> ')


def bstfind(root, find_group):
    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}이(가) 존재합니다")
            break
        elif find_group < current.data:
            if current.left is not None:
                current = current.left
            else:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
        else:
            if current.right is not None:
                current = current.right
            else:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break

def findpredcessor(root, max, current):
    if current is None:
        return None
    elif current.left is None and current.right is None: #리프 노드에서 min과 max 사이의 수 아무거나 찾기
        if current.data < max:
            return current.data
        else:
            return None
    right_result = findpredcessor(root, max, current.right)
    if right_result is not None:
        return right_result
    left_result = findpredcessor(root, max, current.left)
    if left_result is not None:
        return left_result

def ischildleaf(current):
    """
    자식 노드가 전부 리프노드인가?
    :param current:
    :return:
    """
    if current.left.left is None and current.left.right is None and current.right.left is None and current.right.left is None:
        return True
    else:
        return False

def bstdel(root, delete):
    current = root
    parent = None
    while current:
        if delete == current.data:
            if current.left == None and current.right == None:  # 자식이 없음
                if parent.left == current:
                    parent.left = None
                else:  # 논리상 current가 parent의 왼쪽에도 없고 오른쪽에도 없는 경우는 없음
                    parent.right = None
                break
            elif current.left != None and current.right == None:  # 왼쪽에 자식하나
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                break
            elif current.left == None and current.right != None:  # 오른쪽에 자식하나
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                break
            else:  # 자식이 둘 다 있는 경우 ->2일차 숙제
                if ischildleaf(current): #자식 노드가 전부 리프 노드
                    current.data = current.right.data
                    current.right = None
                    break
                else: #아닐 때
                    insert = findpredcessor(root, current.right.data, current) #집어 넣을 리프 노드를 찾고
                    bstdel(root, insert) #리프 노드를 제거함(찾는게 리프 노드이기때문에 무한루프에 안빠짐)
                    current.data = insert #현재 data에 삽입
                    break


        elif delete < current.data:
            if current.left == None:
                print(f"{delete}이(가) 트리에 없습니다!")
                break
            parent = current
            current = current.left
        else:
            if current.right == None:
                print(f"{delete}이(가) 트리에 없습니다!")
                break
            parent = current
            current = current.right


if __name__ == "__main__":
    # groups = random.sample(range(1,50), 10)
    groups = [20, 10, 25, 28, 24, 8, 15, 27, 30, 23]
    # groups = [20, 10, 23, 5, 16, 3, 8, 13, 17]
    root = None

    node = TreeNode(groups[0])
    root = node  # 초기화

    # 트리 생성 코드
    for group in groups[1:]:
        node = TreeNode(group)
        current = root
        while True:
            if node.data < current.data:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left

            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right


    # 탐색 코드
    # find_group = input("찾는 그룹명 입력 : ")
    # bstfind(root, find_group)

    pre_order(root)
    print("End")
    in_order(root)
    print("End")
    post_order(root)
    print("End\n")

    # 제거 코드
    deleteName = 25
    bstdel(root, deleteName)
    print("제거 실행")
    pre_order(root)
    print("End")
    in_order(root)
    print("End")
    post_order(root)
    print("End")
