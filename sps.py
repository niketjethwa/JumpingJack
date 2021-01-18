import random

#print(cans)
#print(ans)
p1p = 0
cp = 0

for i in range(0,3):

    while(p1p != 3 and cp != 3):
    
        ans = input("Enter the answer")
        wordList = ["stone","paper","scissor","stone","paper","scissor",
                    "stone","paper","scissor","stone","paper","scissor"]
        cans = random.choice(wordList)
        
        if(ans=="stone" and cans=="scissor"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Player1 Won")
            p1p = p1p + 1
            print("Player1 Points:",p1p,"\n")
            
            
        elif(ans=="stone" and cans=="paper"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Computer Won")
            cp = cp + 1
            print("Computer Points:",cp,"\n")
            
        elif(ans=="stone" and cans=="stone"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Tie\n")

        elif(ans=="paper" and cans=="scissor"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Computer Won")
            cp = cp + 1
            print("Computer Points:",cp,"\n")
            
            
        elif(ans=="paper" and cans=="paper"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Tie\n")

            
        elif(ans=="paper" and cans=="stone"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Player1 Won")
            p1p = p1p + 1
            print("Player1 Points:",p1p,"\n")

        elif(ans=="scissor" and cans=="scissor"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Tie\n")
            
        elif(ans=="scissor" and cans=="paper"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Player1 Won")
            p1p = p1p + 1
            print("Player1 Points:",p1p,"\n")
            
        elif(ans=="scissor" and cans=="stone"):
            print("Player1: ",ans,"\t","Computer: ",cans)
            print("Computer Won")
            cp = cp + 1
            print("Computer Points:",cp,"\n")