'''this project findes the list that has the same degree as the given list and has minimum length.'''
nums = [1, 2, 2, 3, 1]
def degree(lst):
      '''this function counts the degree of the list.
      degree of array is defined as the maximum frecuency of any one its elements.'''
      res = []
      for ind in range(len(lst)):
           count = 1
           for ind1 in range(ind + 1, len(lst)):
                    if lst[ind] == lst[ind1]:
                            count += 1
           res.append(count)
      max = res[0]
      for num in res:
            if num > max:
                   max = num
      return max 

n = len(nums) - 1
m = 0
res = []
for num in nums:
   while n > m:
      if degree(nums[:n]) == degree(nums):
              res.append(nums[:n])
      if degree(nums[m:]) == degree(nums):
              res.append(nums[m:])
      if degree(nums[m:n]) == degree(nums):
              res.append(nums[m:n])
      n -= 1
      m += 1
min = len(res[0])
for  num in res:
     if len(num) < min:
          min = len(num)
print(min)
