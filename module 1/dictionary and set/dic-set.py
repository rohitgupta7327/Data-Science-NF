# 1. Write a program to create a dictionary from two lists: one of keys and one of values. 
key=["name","copurse","rollno"]
value=["abhishek","Btech","35346364"]
dic=dict(zip(key,value))
print(dic)
# 2. Merge two dictionaries into one 
dic1={'a':1,"b":2,"c":3}
dic2={'d':4,'e':5}
dic1.update(dic2)
print(dic1)
# 3. Write a program to sort a dictionary by its values. 
d = {"a": 3, "b": 1, "c": 2}
d=sorted(d.items(),key=lambda x:x[1])
print(d)
# 4. Given two sets, check if one set is a subset of another. 
s1={1,2,3,4,5,1,88,906,7,8,9,6}
s2={3,4,5,6}
print(s2.issubset(s1))
# 5. Write a program to check whether two lists have at least one common element using sets. 
l1=[32,43,54,65]
l2=[3,4,5,6,7,8]
print(True if set(l1)&set(l2) else False)