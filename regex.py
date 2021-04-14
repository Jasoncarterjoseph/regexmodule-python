import re
#using compile
prog=re.compile(r'm\w\w')
s='mat map mop'
result=prog.search(s)
print(result.group())

#################
#using search
result=re.search(r'm\w\w',"formt")
if(result):
    print(result.group())
else:
    print("Not Found")
#using findall
result=prog.findall(s)
for i in result:
    print(i,end=' ')

#using match
result=prog.match(s)
print()
print(result.group())

#using split
st='This is amaing $$% jas34on&* carter Jose*ph'
result=re.split(r'\W+',st)
print(result)

#using sub
s='Jason Carter JOseph Joseph Carter'
result=re.sub('Carter','Jason',s)
print(result)