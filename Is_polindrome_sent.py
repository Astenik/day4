def is_polindrom(sentence):
        '''this function checs if the string polindrom or not
        '''
        res = []
        nums = sentence.split()
        for num in nums:
               num1 = num.lower()
               for n in range(len(num1)):
                     if num1[n] in (',', '.', ':', '!', ';', '?', '`', '(', ')'):
                            line = num1[:n]     
                            line += num1[n + 1:]
                            num1 = line
               res.append(num1)
        ind = len(res) - 1
        rev_res = []
        while ind >= 0:
            rev_res.append(res[ind])
            ind -= 1
        if res == rev_res:
               return True
        return False 
string = input("insert the string: ")
print(f"is your string polindrom? {is_polindrom(string)}")
