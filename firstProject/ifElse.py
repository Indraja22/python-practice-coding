#Demonstration of the if elif else in Python
def weird_not_weird(n):
    if n % 2 == 0 and ((n in range(2,5) or (n>20))):
        print("Not Weird")
    elif n % 2 == 0 and (n > 6 and n <= 20):
        print("Weird")
    elif  n % 2 !=0:
        print("Weird")

weird_not_weird(5)

