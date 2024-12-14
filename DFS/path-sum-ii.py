# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.__ans = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        nodes_list = []
        self.__perform_dfs(root, 0, targetSum, nodes_list)
        return self.__ans

    def __perform_dfs(self, node, currSum, targetSum, nodes_list):
        if not node:
            return

        currSum += node.val
        nodes_list.append(node.val)
        
        if (currSum == targetSum) and (not node.left) and (not node.right):
            self.__ans.append(copy.deepcopy(nodes_list))
        else:
            self.__perform_dfs(node.left, currSum, targetSum, nodes_list)
            self.__perform_dfs(node.right, currSum, targetSum, nodes_list)

        nodes_list.pop()
