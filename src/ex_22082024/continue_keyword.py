# continue skips the current iteration of a loop and moves to next iteration.
# Means if u get the current condition/stmnt true continue doing ur work or go back to above start doing agn

for i in range(5):
    if i%2==0:
        continue # Odd no program
    else:
        print(i)

# dryrun of logic :
    # value_of_i || condtion || o/p
    # i starts from 0 || 0%2==0-> true || continue means no o/p in console silently move to next iteration
    # i starts from 1 || 1%2==1-> false || now conditions not matched it'll print i that's 1. Now next iteration i is 2 now
    # i starts from 2 || 2%2==0-> true || continue
    # i starts from 3 || 3%2==0-> false || print i
    # i starts from 4 || 4%2==0-> true || continue


for i in range(10):
    if i%2==0:
        pass # same o/p like above program.Bcz pass also used to ignor so whenever we get i%2==0 it'll pass else when i%2==0 false it'll print the number
    else:
        print(i)


