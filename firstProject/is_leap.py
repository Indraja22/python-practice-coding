def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True
    return False;

year = int(input("Enter a year : "))
print(is_leap(year))

'''
year % 4 == 0 -->Leap 
year % 4 == 0 and year % 100 == 0 --> not leap
year % 100 == 0 and year % 400 == 0 -->leap
'''