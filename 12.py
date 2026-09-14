x=float(input('first:'))
y=float(input('third:'))
z=float(input('third:'))
def m(a,b):
    if a>b:
        return a
    else:
        return b
    
    
    def g(d,h,i):
        return m(h,m(d,i))
    
  f=g(z,x,y)
  print(f)