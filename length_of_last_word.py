def length_of_last_word(_str):
           ''' this function returns the length of the last word of string.'''
           names = _str.split()
           n = len(names) - 1
           return len(names[n])  
string = 'Hello! How are you my dear friend?'
print(f"the length of the last word of {string} is: {length_of_last_word(string)}")
