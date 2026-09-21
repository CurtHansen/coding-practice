class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):

    vals = []

    def preorder_recur(node):
        if node is None:
            return
        nonlocal vals
        vals.append(node.val)
        preorder_recur(node.left)
        preorder_recur(node.right)

    preorder_recur(root)
    print(vals)


def bstFromPreorder(preorder):

    if len(preorder) == 0:
        return None

    def recur_construct(sequence, start_idx, end_idx):
        if start_idx > end_idx:
            return None
        node = TreeNode(val=sequence[start_idx])

        i = start_idx
        while i <= end_idx:
            if sequence[i] > node.val:
                break
            i += 1

        node.left = recur_construct(sequence, start_idx+1, i-1)
        node.right = recur_construct(sequence, i, end_idx)

        return node

    return recur_construct(preorder, 0, len(preorder)-1)


if __name__ == '__main__':
    sequence = [15, 10, 8, 12, 20, 16, 25]
    tree = bstFromPreorder(sequence)
    preorder(tree)