# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bk(nums, tem):
            if not nums:
                res.append(tem)
                return
            visi = set()
            for i in range(len(nums)):
                if nums[i] in visi:
                    continue
                else:
                    bk(nums[:i] + nums[i + 1:], tem + [nums[i]])
                    visi.add(nums[i])

        bk(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
