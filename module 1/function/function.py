# 1. Create a Function to Check Whether Two Strings are Anagrams 
# Problem 
# Write a function that accepts two strings and returns True if both are anagrams, otherwise False. 
def is_anagrams(s1,s2):
    return sorted(s1)==sorted(s2)
print(is_anagrams("mom","omm"))
# 2. Create a Function to Find Second Largest Number in a List 
# Problem 
# Write a function that accepts a list and returns the second largest number. 
def second_largest_num(l1):
    l1=list(set(l1))
    l1.sort()
    print(l1)
    return l1[-2]
print(second_largest_num([2,3,6,3,2,2,4,99]))
# 3. Create a Function to Count Vowels in a Sentence 
# Problem 
# Write a function that accepts a sentence and returns the count of each vowel. 
def count_vowel(sentence):
    vowels='aeiou'
    count_dic={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in sentence:
        if(i in vowels):
            count_dic[i]+=1
    return count_dic

print(count_vowel('abhishek singh'))

# 4. Create a Function to Check Whether a Number is an Armstrong Number 
# Problem 
# Write a function that returns True if a number is an Armstrong number. 
def is_armstring(num):
    power=len(str(num))
    total=0
    for i in str(num):
        total+=int(i)**power
    return total==num

print(is_armstring(1634))# 1^4+6^4+3^4+4^4


# 5. Create a Function to Find Common Elements Between Multiple Lists 
# Problem 
# Write a function that accepts three lists and returns common elements.
def common_element(l1,l2,l3):
    return set(l1) & set(l2) & set(l3)
l1=[34,5,6,7,8,3]
l2=[4,45,5,56,67,67,67,6,3]
l3=[23,54,56,67,7,7,3,3,2]

print(common_element(l1,l2,l3))