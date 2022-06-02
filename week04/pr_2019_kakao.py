import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node, nodelist):
    preorderList.append(nodelist.index(node.data) + 1)
    if node.left:      # 왼쪽 탐색
        preorder(node.left, nodelist)
    if node.right:      # 오른쪽 탐색
        preorder(node.right, nodelist)

def postorder(node, nodelist):
    if node.left:      # 왼쪽 탐색
        postorder(node.left, nodelist)
    if node.right:      # 오른쪽 탐색
        postorder(node.right, nodelist)
    postorderList.append(nodelist.index(node.data) + 1)


n = int(input())
nodeinfo = [list(map(int, input().split())) for _ in range(n)]

preorderList = []
postorderList = []

# 1. y좌표 큰 순, x 좌표 작은 순으로 정렬(트리 형태)
sortedNodeInfo = sorted(nodeinfo, key=lambda x: [-x[1], x[0]])

# 2. 트리 구조에 추가
root = None
for node in sortedNodeInfo:
    if not root:      # 루트 설정
        root = Tree(node)
    else:             # 하위 노드들 설정
        cur = root
        while True:
            if node[0] < cur.data[0]:   # 왼쪽 노드 탐색
                if cur.left:            # 이미 왼쪽 노드가 있으면 재탐색(추가 될 때까지)
                    cur = cur.left
                    continue
                else:
                    cur.left = Tree(node)      # 왼쪽 노드가 없다면 추가
                    break
            if node[0] > cur.data[0]:       # 오른쪽 노드 탐색
                if cur.right:               # 이미 오른쪽 노드가 있으면 재탐색
                    cur = cur.right
                    continue
                else:
                    cur.right = Tree(node)    # 왼쪽 노드가 없다면 추가
                    break
            break

# 3.전위/후위 탐색 수행
preorder(root, nodeinfo)
postorder(root, nodeinfo)
print([preorderList, postorderList])



