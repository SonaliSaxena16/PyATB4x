"""
WAP that prints numbers from 1 to 100. for multiples of 3, print "Fizz" instead of the number, and
for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz.

1 Loop run
2 num%3==0 print Fizz
3 num%5==0 print Buzz
4 num%3==0 and num%5==0 print FizzBuzz
"""
for num in range(1, 101):
    print(num)
    if num % 3 == 0:
     print("Fizz")
    elif num % 5 == 0:
         print("Buzz")
    elif num % 3 == 0 and num% 5 == 0:
             print("FizzBuzz")
    else:
        print(num)



