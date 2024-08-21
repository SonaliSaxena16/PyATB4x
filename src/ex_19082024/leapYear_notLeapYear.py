"""
Leap year checker:

A year is a leap year if its divisible by 400 or 4 or not by 100.
Not leap - if it is divisible by 100 or 4 or not by 400.

1 Input -> int year which user wants to chk if leap or not
2 O/P -> Str
3 Rough Logic
if year%400==0 or year%4==0 and not year%100==0
print- Leap yr
else - not leap
"""
year = int(input("Enter the year"))

if year%400==0 or year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Not leap")


#/ // %