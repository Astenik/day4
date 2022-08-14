lst = [1, 2, 3, 4, 4, 4]
number = int(input("insert number: "))
def num_index(lst, num):
         '''this function findes the firs and last indexes 
        of num in lst list, if num is not in list function returns 
        [-1, -1].'''
        if (lst[-1] < num) or (lst[0] > num):
                return [-1, -1]
        res = []
        ind = 0
        rev_lst = lst[::-1]
        while lst[ind] <= num:
               if lst[ind] == num:
                     res.append(ind)
                     break 
               ind += 1
        else:
             return [-1, -1]
        if res[0] == (len(lst) - 1):
                res.append(res[0])
        else:
              for i in range(len(lst) - res[0]):
                  if rev_lst[i] == num:
                      res.append(len(lst) - i - 1)
                      break 
        return res 
print(f"firs and last indexes of num in lst are: {num_index(lst, number)}")

