num=[1,2,3,4,5,6]
filtered=list(filter(lambda x:x%2==0,num))
square=list(map(lambda x: x**2,filtered))
sum=(reduce(lambda x,y:x+y,square))
print(filtered,square,sum)