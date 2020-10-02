#Program to find the runner up score.
def runner_up_scores():
    myList = []
    n = 1
    players = int(input("Enter the number of participants : "))
    while n <= players:
        score = int(input("Enter the scores of the " +str(n)+" participant : "))
        myList.append(score)
        n +=1
    print("The participant scores are : " +str(myList))
    myList.sort()
    if myList[-2] == myList[-3]:
        print("There are 2 runner ups.")
    runnerUp_score = myList[-2]
    print("The runner up has a score of "+str(runnerUp_score)+ " points")
runner_up_scores()