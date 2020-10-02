def split_and_join():
    line = input()
    line = line.split()
    return ("-".join(line))
result = split_and_join()
print(result)