#Program to print Odd and Even numbers in range(0,100) in Python

def check_odd_even():
       for num in range(0,100):
            if num % 2 == 0:
                print(f"Even Numbers are : {num}")
            else:
                print(f"Odd Numbers are : {num}")

