l1 = lambda x:2*x
l2 = lambda x:x/2

l = lambda x:l1(x)*l2(x)

print(l(5))
