# Domain
- Given a list of ints, return indices of the two numbers such that they add up to a specific target. 


Questions:
- Is the list sorted?
- Are there duplicated numbers?


# Visual
- Nums = [2, 7, 11, 15]
- Target = 9
- nums[0] is 2, nums[1] is 7. 
- 2 + 7 = 9
- Output = [0, 1] 


# Data Structure 
- Dictionary


# Algorithm
- Create function called two_sums that takes in a list of nums and a target sum
- Create empty dictionary to store visited nums
- For each num in nums:
-- Calc the difference between the target and the current num
-- If the difference is not in the dictionary:
--- Add to dictionary with num as key and value as index.
-- If the difference is in the dictionary:
--- Return list of these two vals... 
----- 1. the index of the current num
----- 2. from the dictionary, the value of the difference (the value is the index)


# Big O
- Time: O(N) complexity. The solution has to loop through as many numbers in list_nums as it takes until it finds the difference in the dictionary.

- Space: O(N) complexity. Each time the solution adds to the dictionary, another value is stored in memory.


# Testing
- Function exists
- Empty list_nums
- Only one value in list_nums
- Values in list_nums cannot equal target_sum
- Correct sum with first two indices
- Correct sum with first index and random index
- Correct sum with random indices


# Verification
 __________________________________________________
| index | num  | target | difference | visited_nums|
 -------------------------------------------------- 
|   0   |  2   |    9   |     7      |    {2:0}    |
|   1   |  7   |    9   |     2      |    {2:0}    |
|_______|______|________|____________|_____________|
