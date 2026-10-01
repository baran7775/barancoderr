add1='c://users//my pc//desktop//first//f.txt'
with open (add1,'w') as f1:
    for i in range (3):
        s=input('enter:')
        f1.write(s)
        f1.write('\n')