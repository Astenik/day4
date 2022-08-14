def sum_of_unique_el(lst):
       ''' this function counts the sum of unique numbers in the list. '''
       res = []
       fr = []
       for ind in range(len(lst)):
             count = 0
             for ind1 in range(ind + 1, len(lst)):
                     if lst[ind] == lst[ind1]:
                            count += 1 
                            fr.append(lst[ind])
             if (count == 0) and (lst[ind] not in fr):
                  res.append(lst[ind]) 
       sum = 0
       for num  in res:
           sum += num 
       return sum 

print(f'sum of unique number is equal to: {sum_of_unique_el([2, 3, 4, 4, 5, 2, 7])}')
