y = ['rr','rrr','(5.5,5.5)']
x = []
array = []

print(y[2])
value = y[2].split(',')
print(value)


for idx in y:
    x.append(idx.split(','))
for idy in x:
    try:
        buff = list(idy)
        value =  buff.split(',')
        print(value)
    finally:
        continue


print(x)
print(array)