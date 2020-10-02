def full_name():
    s = "indraja   naik"
    s = s.split(' ')
    for i, n in enumerate(s):
        s[i] = s[i].capitalize()
    name = " ".join(s)
    print(name)
full_name()

# return ' '.join(i.capitalize() for i in s.split(' '))