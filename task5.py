#def recurs(count):
   # print(count)
    #count+=1
   # recurs(count)

#recurs(1)

def sum(ls):
    #base case
    if len(ls)==1:
        return ls[0]
#recursion case
    return ls[0]+sum(ls[1:])

print(sum([1,2,3,4,5,6,7,8,9]))