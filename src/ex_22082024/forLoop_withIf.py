# for i in range(5): or
# for i in range(0,5): or
# for i in range(0,5,1):
#above all 3 ststements are same
#     print(i)

for i in range(5):
    if i==3:
        print(i)
    else:
        print("No O/P")

# dryrun of logic :
# value_of_i || condtion || o/p
# i starts from 0 || 0==3 -> false || No O/P
# i starts from 1 || 1==3 -> false || No O/P
# i starts from 2 || 2==3 -> false || No O/P
# i starts from 3 || 3==3 -> true || print i that is 3
# i starts from 4 || 4==3 -> false || No O/P
