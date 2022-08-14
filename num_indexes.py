lst = [1, 2, 3, 4, 4, 4]
number = int(input("insert number: "))
def num_index(lst, num):
        '''this function findes the firs and last indexes 
        of num in lst list, if num is not in list function returns 
        [-1, -1].'''
        res = []
        ind = 0
        while lst[ind] <= num:
               if lst[ind] == num:
                     res.append(ind)
                     break 
               ind += 1
        if len(res) == 0:
             res = [-1, -1]
        elif res[0] == (len(lst) - 1):
                res.append(-1)
        else:
              for ind1 in range(res[0], len(lst)):
                       if lst[ind1] == num and (len(res) == 1):
                                 res.append(ind1)
                       elif lst[ind1] == num:
                              res.pop()
                              res.append(ind1)
                       else:
                           break
        return res 
print(num_index(lst, number))
