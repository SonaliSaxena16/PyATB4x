# String Formatting

number = 3.14159 # pie value
print(number)
formatted_nummber = f"{number:.4f}" # It'll print 3.1416 bcz of rounding off
print(formatted_nummber)
print("Type is " , type(formatted_nummber))

num = 90
print("This is the number you're working with " f"{num}")

table = 2
print(type(table))
print(f"{table}*1 = {table*1}") # LHS before equalsTo is {Val}*1[1 is a Str] now we are telling the Py thon interpreter that we want output to be this way table*1 is a string part now on RHS we wud be doing actual int part the calculation which is table=2 hence 2*1=2
print(f"{table}*2 = {table*2}")
print(f"{table}*3 = {table*3}")
print(f"{table}*4 = {table*4}")
print(f"{table}*5 = {table*5}")
print(f"{table}*6 = {table*6}")
print(f"{table}*7 = {table*7}")
print(f"{table}*8 = {table*8}")
print(f"{table}*9 = {table*9}")
print(f"{table}*10 = {table*10}")