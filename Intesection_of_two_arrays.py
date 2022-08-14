'''given two integer arrays nums1 and nums2, this project returns an array of their intersection.
each element in the result must be unique and may return result any order.
'''
nums1 = [1, 2, 2, 3]
nums2 = [2, 2]
res = []
for num1 in nums1:
    for num2 in  nums2:
           if num1 == num2 and (num1 not in res):
                 res.append(num1)
print(res)
