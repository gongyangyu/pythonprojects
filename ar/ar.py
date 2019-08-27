def minNoPresence(l):
    min=1
    max=len(l)+1
    sum=0;
    for i in l:
        if i<1 or i>=len(l)+1:
            max-=1
        else:
            sum+=i
    rs=max*(max+1)/2-sum
    return min,max,rs
l1=[1,2,0]
l2=[3,4,-1,1]
print(minNoPresence(l1))
print(minNoPresence(l2))
l3=[7,8,9,11,12]
print(minNoPresence(l3))
l4=[4,6,1,5,2,100]
print(minNoPresence(l4))