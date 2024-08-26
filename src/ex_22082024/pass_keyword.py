# Pass keyword means ignore. Pass can be used with Statements, Objects, Classes & Functions.
for i in range(7):
    if i == 3:
        print(i)
    else:
        pass

# dryrun of logic :
    # value_of_i || condtion || o/p
    # i starts from 0 || 0==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # i starts from 1 || 1==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # i starts from 2 || 2==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # i starts from 3 || 3==3 -> true || print i that is 3
    # i starts from 4 || 4==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # i starts from 4 || 5==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # i starts from 4 || 6==3 -> false || No O/P shown on console it wud simply PASS like ghost
    # Execution ended as for loop run i-1 that's 6

for i in range(7):
        if i == 3 or i==2:
            print(i)
        else:
            pass

for i in range(7):
        if i == 3 and i==2:  # Invalid combination with and. As 2 and 3 wudn't be find together so how can this condition be satisfied
            print(i)
        else:
            pass

for i in range(27):
        if i == 2 and i==3:   # Invalid combination with and. As 2 and 3 wudn't be find together so how can this condition be satisfied
            print(i)
        else:
            pass


