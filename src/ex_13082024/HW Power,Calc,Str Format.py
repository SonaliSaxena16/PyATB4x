"""
WAP take 2 no's as user input and fetch
- MAX
- POW
- Add Sub Mul Div
- Format output in String Format
"""
first_num = int(input("Enter your first num"))
second_num =  int(input("Enter your second num"))

max_num = max(first_num , second_num)
print("Maximum no. is " , f"{max_num}")

power = pow(first_num , second_num)
print("Power is " , f"{power}")

sum = first_num+second_num
print("Sum is " , f"{sum}")

sub = first_num-second_num
print("Sub is " , f"{sub}")

mul = first_num*second_num
print("Mul is " , f"{mul}")

div = first_num/second_num
print("Div is " , f"{div}")
