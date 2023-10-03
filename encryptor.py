print('''========================== Made By Nimitt Sharma =====================\n''')
print(''' Created 2-Jan-2023 ''')
print(''' Edited 3-Oct-2023 \n''')
imp = input("Your Password after Encryption : ")


for i in imp:
    i = i.upper()
    
    if i == "A":
        print("x$a*",end="")
    
    elif i == "B":
        print("j%s#",end="")
        
    elif i == "C":
        print("k*2m",end="")
        
    elif i == "D":
        print("n$a2K",end="")
        
    elif i == "E":
        print("l#n%",end="")
        
    elif i == "F":
        print("1o*m",end="")
        
    elif i == "G":
        print("6$q#",end="")
        
    elif i == "H":
        print("4q#k",end="")
        
    elif i == "I":
        print("j8%4",end="")
        
    elif i == "J":
        print("l*ne",end="")
        
    elif i == "K":
        print("Q8@n",end="")
        
    elif i == "L":
        print("0m*a",end="")
        
    elif i == "M":
        print("7@g0",end="")
        
    elif i == "N":
        print("!h&k",end="")
        
    elif i == "O":
        print("%fak6",end="")
        
    elif i == "P":
        print("%k*@",end="")
        
    elif i == "Q":
        print("N%4#",end="")
        
    elif i == "R":
        print("l*n!",end="")
        
    elif i == "S":
        print("z9m&",end="")
        
    elif i == "T":
        print("x8C8",end="")
        
    elif i == "U":
        print("n9ak",end="")
        
    elif i == "V":
        print("n$70",end="")
        
    elif i == "W":
        print("!nk7",end="")
        
    elif i == "X":
        print("n&k8",end="")
        
    elif i == "Y":
        print("g&k0",end="")
        
    elif i == "Z":
        print("a%b9",end="")
        
    else:
        print(i,end="")


if len(imp)<1:
    print("\nYour Password will take 1 milliesecond to crack !")
elif len(imp)<5:
    print("\nYour password is slightly weak try adding more !")
elif len(imp)>12:
    print("\nhmm... Strong enough to be cracxked in 100 years !")

elif len(imp)>20:
    print("\nSafest Password... will take 1 Million Years :)")

else:
    ("\n                                  Strong Enough !")
print("\n==============  Don't forget to Like if you find it useful! ============")

        
        


