class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = buildTree(preorder, inorder[:index])
        root.right = buildTree(preorder, inorder[index+1:])
        return root

        



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]



buildTree(preorder, inorder).left.val