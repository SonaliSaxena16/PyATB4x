# WAP to create a Grade Calculator
# Grades are as follows :
# A = 90-100
# B = 80-89
# C = 60-79
# D = 40-59
# F = 0-39

# Gather input -> User wud input int score
# O/p -> Str Grade
# Rough logic
# score>=90 and score<=100 - A
# score>=80 and score<=89 - B
# score>=60 and score<=79 - C
# score>=40 and score<=59 - D
# score>=0 and score<=39 - F

score = int(input("Enter the score"))

if score>=90 and score<=100:
    print("You got grade A")
elif score>=80 and score<=89:
    print("You got grade B")
elif score>=60 and score<=79:
    print("You got grade C")
elif score>=40 and score<=59:
    print("You got grade C")
elif score>=100:
    print("Superhuman!")
else:
    print("You got fail with grade F")


