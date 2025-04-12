x=int(input('Enter 1st number:    '))
print(x)
y=int(input('Enter 2nd number:    '))
print(y)
z=int(input('Enter interval number:    '))
print(z)

data=range(x,y,z)
print(data)

def cal_mean(data):
    return(sum(data)/len(data))

print('mean',cal_mean(data))
