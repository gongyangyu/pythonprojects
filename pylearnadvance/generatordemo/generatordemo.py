list5=[x*x for x in range(5)]
print(list5)
gen5=(x**3 for x in range(5))
print(gen5)
for n in gen5:
    print(n)

def fibnacite(n):
    a,b=0,1
    current=0
    while current<=n:
        yield a
        a,b=b,a+b
        current+=1
    return 'done'

fib=fibnacite(9)

for f in fib:
    print(f)