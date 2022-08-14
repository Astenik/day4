def str1_in_str2(string1, string2):
        '''given two strings, this function returns the index of the 
        first occurrence of the first string in the second string.
        the two strings are the arguments of mthis function.
        '''
        n = len(string1)
        for ind in range(len(string2)):
                 if string2[ind:(ind +n)] == string1:
                         return ind 
        return -1
print(f"the index of occurrence is: {str1_in_str2('ik', 'astenik')}")
