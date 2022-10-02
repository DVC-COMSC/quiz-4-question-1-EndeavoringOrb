adjacent=0
chain = 0
num_arr=[]


for i in range(10):
    num_arr.append(int(input()))


for i in range(9):
    if num_arr[i]%2==0 and num_arr[i+1]%2==0:
        if chain == 0:
            adjacent += 1
        chain = 1
    else:
        chain = 0

#print("-----------------")
print(adjacent)