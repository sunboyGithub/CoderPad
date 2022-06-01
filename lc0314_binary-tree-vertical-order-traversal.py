class Solution:
    def verticalOrder(self, root):
        if root is None:
            return []

        from collections import deque, defaultdict
        node_vorder_queue = deque([])
        node_vorder_queue.append((root, 0))
        # vorder_nodes = defaultdict([])                            # Note1: not work
        vorder_nodes = defaultdict(list)
        min_vorder = 0
        max_vorder = 0
        while node_vorder_queue:
            cur_node, cur_vorder = node_vorder_queue.popleft()
            # if cur_vorder not in vorder_nodes:                    # work if defaultsdict(list) is not used.
            #     vorder_nodes[cur_vorder] = []

            # xx = vorder_nodes.get(cur_vorder, [])                 # Note2: note wor
            # xx.append(cur_node.val)
            vorder_nodes[cur_vorder].append(cur_node.val)
            if cur_node.left:
                node_vorder_queue.append((cur_node.left, cur_vorder - 1))
                min_vorder = min(min_vorder, cur_vorder - 1)
            if cur_node.right:
                node_vorder_queue.append((cur_node.right, cur_vorder + 1))
                max_vorder = max(max_vorder, cur_vorder + 1)
        res = []
        for vorder in range(min_vorder, max_vorder + 1):
            res.append(vorder_nodes[vorder])
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node3 = TreeNode(3)
node9 = TreeNode(9)
node20 = TreeNode(20)
node15 = TreeNode(15)
node7 = TreeNode(7)
node3.left = node9
node20.left = node15
node3.right = node20
node20.right = node7

test = Solution()
print(test.verticalOrder(node3))

