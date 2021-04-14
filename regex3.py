import re

#extract number
s='Ja$osn 12378893 2378 23 237483 wios'
result=re.search(r'\d+',s)
print(result.group())

#extract nmae
result=re.search(r'\D+',s)
print(result.group())

#starts with an or ak
s='anil akil annsisl aksdjknilss dhjksank amkanakpeace'
result=re.findall(r'a[nk][\w]*',s)
print(result)

#extacr DOB
s='jason 20 15-06-2001, rohit 40 24-09-2019, sita 22 16-05-2019'
result=re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',s)
print(result)

#starts with 
s='hhehehe.llo . world'
print("Ac")
result=re.search(r'he?',s)
print(result.group())
if result:
    print("Starts with He")
else:
    print("Ni")

#ends with
result=re.search(r"world$",s)
if result:
    print("ends with world")
else:
    print("Ni")

#ignorecase
result=re.search(r"World$",s,re.IGNORECASE)
if result:
    print("ends with world")
else:
    print("Ni")

#using .
result=re.search(r"He.",s,re.IGNORECASE)
print(result.group())

#retreive name and marks
s='A Jason 20 , Carter 20, Joseph 30'
names=re.findall(r'[A-Z][a-z]+',s)
print(names)
marks=re.findall(r'\d{2}',s)
print(marks)

#find am or pm
s="its 8am or 9pm"
result=re.findall(r'\dam|\dpm',s)
print(result)