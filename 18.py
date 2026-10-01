def f(s:str,start:int,end:int):
    return s[0:start]+s[end:]
else:
    print('index and is not valid')

a=input('enter string: ')
b=int(input('enter start:'))
c=int(input('enter end:'))
g=f(a,b,c)
print(g)


