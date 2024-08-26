# break keyword is used, to chk if condition==true, exit the loop
for i in range(1,10):
    print(i)  # 1   , 2,    3,  4,    5
    if i==5:  # 1==5 False, 2==5 False, 3==5 False, 4==5 False, 5==5 true
        break                         #-------------Now it'll break here and stop the loop to come out