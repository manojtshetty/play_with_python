list1=['Physics','Chemistry','Biology']
print(list1[0:2])
list1[0]='Maths'
print(list1[0:2])
list1.append('English')
print(list1)

del(list1[0])
print(list1)

print(len(list1))

list1_orig= list1
list1_rev=list(reversed(list1))
print (list1+list1_rev)

list_num =[10,25,44,5,34,88,77,30]
list_num.sort(reverse=True)
#list_num.reverse()
print(list_num)
print(list_num.count(88))

list_num.extend([101,455,324])
print(list_num)
