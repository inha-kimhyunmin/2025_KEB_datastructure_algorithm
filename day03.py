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


if __name__ == "__main__":
    groups = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    root = None

    node = TreeNode(groups[0])
    root = node #초기화
    
    #트리 생성 코드
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

    find_group = input("찾는 그룹명 입력 : ")
    
    # 탑색 코드
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

    #제거 코드
    deleteName = '마마무'

    current = root
    parent = None
    while True:
        if deleteName == current.data:
            if current.left == None and current.right == None: #자식이 없음
                if parent.left == current:
                    parent.left = None
                else: #논리상 current가 parent의 왼쪽에도 없고 오른쪽에도 없는 경우는 없음
                    parent.right = None
            elif current.left != None and current.right == None: #왼쪽에 자식하나
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
            elif current.left == None and current.right != None: #오른쪽에 자식하나
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else: #자식이 둘 다 있는 경우 ->2일차 숙제
                pass
        elif deleteName < current.data:
            if current.left == None:
                print(f"{deleteName}이(가) 트리에 없습니다!")
                break
            parent = current
            current = current.left
        else:
            if current.right == None:
                print(f"{deleteName}이(가) 트리에 없습니다!")
                break
            parent = current
            current = current.right


    #                 블랙핑크
    #          레드벨벳      에이핑크
    #     걸스데이   마마무        트와이스
    pre_order(root)
    print("End")
    in_order(root)
    print("End")
    post_order(root)
    print("End")
