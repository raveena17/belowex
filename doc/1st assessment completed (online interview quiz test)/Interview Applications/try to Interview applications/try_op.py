def chek():
    score=0
    wrong=0
    

    while True:
        print "..........?"
        A = 'Development_environment'
        B = 'programming_language'
        
        ans = input ("ans : ")
        if ans == "A":
            wrong+=1
        elif ans == "B":
            score+=1
        elif ans == "Q":
            break

    return score

chek()
