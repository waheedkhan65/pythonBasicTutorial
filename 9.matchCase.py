v = str(input("Are you want to cast vote if yes type yes othervise type No \n "))
match v:
    case "yes" | "Yes" | "YES":
        print ("For whom you want to cast vote")
        n= int(input("Select number of candidate \n 1.Imran khan \n 2.Nawaz shareef \n 3.Zardare \n 4.Mulana Fazal Rahman \n 5.siraj-Ul-haq \n"))
        print ("sir your vote is cast to ",n)
    case "no" | "No" | "NO" :
        print ("Thank you sir , Allah Hafix")  
    case _ :
        print ("invalid input") 