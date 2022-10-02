
# ******************************
# Make your Code
# ******************************

adjacent=0
num_arr=[]

for i in range(10):
    num_arr.append(int(input("Enter number "+str(i+1)+ ": ")))

for i in range(9):
    if num_arr[i]%2==0 and num_arr[i+1]%2==0:
        adjacent += 1

print(adjacent)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
