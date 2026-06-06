# 1. Write a program to find the largest and smallest elements in a list. 
list=[4,6,7,2,1]
list=sorted(list)
print(list)
print("largest: ",list[len(list)-1]) 
print("smallest: ",list[0])
# 2. Write a program to remove duplicate elements from a list.  
list=[3,4,5,6,7,4,3,3,3]
list=set(list)
print(list)
# 3. Write a program to reverse a list without using built-in reverse functions.  
list=[1,2,3,4,5,6]
rlist=[]
for i in range(len(list)-1,-1,-1):
    rlist.append(list[i])
list=rlist
print(list)
# 4. Write a program to count even and odd numbers in a list.  
list=[3,5,6,7,2,4,5,7]
even=0
odd=0
for i in list:
    if i %2==0:
        even+=1
    else:
        odd+=1
print("total even",even)
print("total odd",odd)
# 5. Write a program to merge two lists and sort the final list.  
l1=[2,3,5,6]
l2=[3,4,6,7]
l1=sorted(l1+l2)
print(l1)
# 6. Write a program to find the second largest element in a list. 
l1=[2,4,5,7,8,9]
l1=sorted(l1)
print("second largest: ",l1[-2]) 
# 7. Write a program to check whether an element exists in a tuple.  
tuple=(2,3,5,5,6,7,8)
x=81
print(x in tuple)
# 8. Write a program to count the occurrence of an element in a tuple.  
tuple=(3,4,5,8,6,7,8,8)
x=8
print(tuple.count(x))
# 9. Write a program to sort a list of tuples based on tuple values.  
list=[(212,3),(52,6),(9,0)]
list.sort()
print(list)
# 10. Write a program to convert a tuple into a list and a list into a tuple.
l=[2,3,4,5,6]
t=tuple(l)
print("tuple: ",t)
l=list(t)
print("list:",l)
