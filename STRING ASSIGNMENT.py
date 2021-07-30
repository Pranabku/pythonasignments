B1=input("ENTER YOUR MAIN STRING")
A1=B1.lower()
print("YOUR STRING IS",B1)
B2=input("Enter the main word of your string")
A2=B2.lower()
if A1.find(A2)==-1:
    print("You have enterd an wrong input")
else:    
    print("NO OF LETTER IN YOUR MAIN WORD IS", len(A2.strip()))
    print("No of times main word occurs in String is", A1.count(A2))

B3=input("ENTER THE WORD TO SEARCH IN THE MAIN STRING")
A3=B3.lower()
if A1.find(A3)== -1:
 
    print("the word you are searching doent exit the Main string")
else:
    print("your word starts with index",A1.find(A3))
    print("No of times you word occurs in String is", A1.count(A3))
    print("Your word ocuurs Ist time at index ", A1.find(A3))
    print("Your word ocuurs 2nd time at index ", A1.find(A3,A1.find(A3)+1))
    
    

    
    





