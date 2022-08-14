'''this project moves all the even integers at the beginning of the array followed all the odd integers.'''
nums = [1, 24, 64, 49, 9, 6]
res = []
for num in nums:
        if num % 2 == 0:
               res.append(num)
for num in nums:
         if num % 2 != 0:
              res.append(num)
nums = res 
print(nums)
