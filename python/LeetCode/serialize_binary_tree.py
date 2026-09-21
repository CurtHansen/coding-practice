# Based on https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Main class.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_recur(node):
            if node is None:
                return {}
            nodedict = dict()
            nodedict['val'] = node.val
            nodedict['left'] = serialize_recur(node.left) if node.left else None
            nodedict['right'] = serialize_recur(node.right) if node.right else None
            return nodedict

        return str(serialize_recur(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        treestruct = eval(data)
        if len(treestruct) == 0:
            return None

        def deserialize_recur(structure):
            node = TreeNode(structure['val'])
            if structure['left'] is not None:
                node.left = deserialize_recur(structure['left'])
            if structure['right'] is not None:
                node.right = deserialize_recur(structure['right'])
            return node

        root = deserialize_recur(treestruct)
        return root


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2
    node3 = TreeNode(3)
    node1.right = node3
    node4 = TreeNode(4)
    node2.left = node4
    codec = Codec()
    serialized = codec.serialize(node1)
    print(serialized)
    root = codec.deserialize(serialized)

    def explore(node):
        print(f'node {node.val}')
        print(f'  left node: {node.left}')
        if node.left: print(f'    ...with val {node.left.val}')
        print(f'  right node: {node.right}')
        if node.right: print(f'    ...with val {node.right.val}')
        if node.left: explore(node.left)
        if node.right: explore(node.right)

    explore(root)
