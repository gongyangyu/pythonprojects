ns=['a','tom','lilie','lucy']
print(ns)

for x in ns:
    print(x)
for h in list(range(4,20)):
    print(h)

str='32425egdf,sdfsf'
for x in str:
    print(x)

ns.append('a')
print(ns)

print(ns.count('lilie'))

x=1
while x<30:
    x+=2/x
    print(x)
d=('234','df',['tom','kate','msd',2],'dfdf','df')
print(d[2][2][2])

d[2][1]='change'
print(d)
print(d.count('df'))
print(len(ns))
print(len('sssssssssssssfffff'))

t=('dfd','dsf','e')

dc={t:'dfd','344':[d],3:ns}
print(dc)
dc.popitem()
print(dc)