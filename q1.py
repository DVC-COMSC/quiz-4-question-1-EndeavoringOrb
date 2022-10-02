# ******************************
# Make your Code
# ******************************

adjacent=0
num = int(input())

for i in range(9):
    t_num = int(input())
    if num%2 == 0 and t_num%2 == 0:
        adjacent += 1
    num = t_num

print(adjacent)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
