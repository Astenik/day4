n = int(input("insert the number n: "))
target = [1, 2, 4, 5]  
lst =  []
res = []
for num in range(1, target[-1] + 1):
       lst.append(num)
       if num in target:
            res.append("push")
       else:
            res.append("push")
            res.append("pop")
print(res)
