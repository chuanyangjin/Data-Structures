# Majority Number (element that appears more than [n/2] times)

## Boyer-Moore 投票算法：O(n) runtime, O(1) space complexity 
def majority_number(lissy):  
  count = 0
  for e in lissy:
    if count != 0:
      if candidate == e:
        count += 1  
      else:
        count -= 1
    else: # count == 0
      candidate = e  
      count = 1
            
  # check the majority
  return candidate if lissy.count(candidate) > len(lissy) // 2 else default


## Dictionary: O(n) runtime, O(n) space complexity
def majority_number2(lissy):
  dict1 = {}  #O(n) space complexity 
        
  for item in lissy:
    if item not in dict1:
      dict1[item] = 1
    else:
      dict1[item] += 1

    if dict1[item] >= len(lissy)//2+1:
      return item
  return None

## Sorting: O(nlogn) runtime, need no memory
def majority_number3(nums):
    nums.sort()
    return nums[len(nums)//2]

## 分治法：O(nlogn) runtime, O(logN) memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majority(nums, 0 ,len(nums)-1)
    
    def majority(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        left_majority = self.majorityElement(nums[left:mid+1])
        right_majority = self.majorityElement(nums[mid+1:right+1])
        if nums[left:right+1].count(left_majority) > nums[left:right+1].count(right_majority):
            return left_majority
        else:
            return right_majority

print(majority_number([0,1,5,-1,1,1,-99,1,2,1,1])) # 1
print(majority_number([0,1,5,-1,1,99,99,99,99,99,99])) # 99
print(majority_number2([0,1,5,-1,1,1,-99,1,2,1,1])) # 1
print(majority_number2([0,1,5,-1,1,99,99,99,99,99,99])) # 99
print(majority_number3([0,1,5,-1,1,1,-99,1,2,1,1])) # 1
print(majority_number3([0,1,5,-1,1,99,99,99,99,99,99])) # 99
