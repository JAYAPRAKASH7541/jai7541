'''def f (*args,**kwargs):
	print(args)
	print(kwargs)
	
c=[1,2,3,3,4,4,4]
d={'a':5,'b':6,'c':"fgh"}

f(*c,**d)'''
l=[1,2,3,3,3,3,3,3,3]
print(type(l[0]))
d={l[3]:l.count(l[3]) for i in l}
print(d)