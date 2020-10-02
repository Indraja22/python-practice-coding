#Print the list of integers from 1 through n as a string, without spaces.
def print_func():
    ls = []
    n = int(input())
    for i in range(1,n+1):
        ls.append(str(i))
    st = "".join(ls)
    print(st)
print_func()