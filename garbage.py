class Solution:
    def rob(self, sum, nums: List[int]) -> int:
        position = 0
        length_of_array = len(nums)
        if length_of_array == 0:
            return sum
        if length_of_array == 1:
            return sum + nums[0]
        zeroth_position_profit = nums[0] - nums[1]
        last_position_profit = nums[length_of_array-1] - nums[length_of_array-2]
        addition = 0
        if last_position_profit > zeroth_position_profit:
        opportunity_cost = last_position_profit
        position = length_of_array - 1
        addition = nums[length_of_array-1]
        else:
            opportunity_cost = zeroth_position_profit
            addition = nums[0]
        for i in range(1, length_of_array-1):
            if (nums[i] - nums[i+1] - nums[i-1]) > opportunity_cost:
                opportunity_cost = (nums[i] - nums[i+1] - nums[i-1])
                position = i
                addition = nums[i]
        if position == 0:
            return rob(total + addition, nums[2:])
        elif position == length_of_array-1:
            return rob(total + addition, nums[:length_of_array - 2])
        else:
            return rob(total + addition, nums[:position - 1] + nums[position + 2:])