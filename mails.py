def mails(mail):
    '''this function returns real mail name.'''
    ind = mail.index('@')
    name = mail[:ind]
    domain = mail[ind:]
    if  '.' in name:
             name = name.replace('.', '')
             mail = name + domain
    if '+' in name:
              ind1 = mail.index('+')
              mail = mail[:ind1]
              mail += domain
    return mail 
def count_of_mails(_mails):
     count = 0
     for ind in range(len(_mails)):
             for ind1 in range(ind + 1, len(_mails)):
                    if mails(_mails[ind]) != mails(_mails[ind1]):
                         count += 1
     return count
print(f"mails' count in the list is equal to: {count_of_mails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])}")
