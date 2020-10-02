def count_substring():
    myStr = "ABCDCDCPCPCDC"
    mySubStr = "CDC"
    num = 0
    for i in range(0,len(myStr)):
        while(myStr.find(mySubStr) >=1):
            num +=1
    print(num)
count_substring()