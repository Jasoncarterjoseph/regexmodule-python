import re
#find words straing with a
s="A doctor a day keeps apple away"
result=re.findall(r'a[\w]*',s)
print(result)

#with spaces
resul=re.findall(r'\ba[\w]*\b',s)
print(resul)

#find numbers
s='1st and 2nd will be 2 days holidays'
resul=re.findall(r'\d[\w]*',s)
print(resul)

#find words with specific lenght
s='one two three four five six seven eight nine ten eleven'
resul=re.findall(r'\b\w{3}\b',s)
print(resul)

#min lenght 
s='one two three four five six seven eight nine ten eleven'
resul=re.findall(r'\b\w{5,}\b',s)
print(resul)

#checking start
s='one two three four five six seven eight nine ten eleven'
resul=re.findall(r'\Ao[\w]*',s)
print(resul)

#checking ending
s='one two three four five six seven eight nine ten eleven'
resul=re.findall(r'e[\w]*\Z',s)
print(resul)

