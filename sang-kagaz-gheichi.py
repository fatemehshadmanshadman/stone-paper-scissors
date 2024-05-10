import random

item=["r","p","s"]
userp=0
pcp=0
flag=input("Do you want play base score or base turn: ")
if "turn" in flag:
    count=int(input(" how much your turn? or "))
    print(" r:rock,  p:paper,    s:scissors")

    while count>0:  
        user=input("enter your selected: r - p - s: ")
        pc=random.choice(item)
        print(f"pc selected {pc}")
        if user==pc:
            print("equal next time")
        elif user=="r":
            if pc=="p":
                pcp+=1
            else:
                userp+=1
        elif user=="p":
            if pc=="r":
                userp+=1
            else:
                pcp+=1
        elif user=="s":
            if pc=="r":
                pcp+=1
            else:
                userp+=1
        count-=1
else:
    run=True
    print(" r:rock,  p:paper,    s:scissors")

    while run:  
        user=input("enter your selected: r - p - s: ")
        # if user in item:
        pc=random.choice(item)
        print(f"pc selected {pc}")
        if user==pc:
            print("equal")
        elif user=="r":
            if pc=="p":
                pcp+=1
            # else pc=="s": niazi nist
            else:
                userp+=1
        elif user=="p":
            if pc=="r":
                userp+=1
            else:
                pcp+=1
        elif user=="s":
            if pc=="r":
                pcp+=1
            else:
                userp+=1
        
        if userp==2 or pcp==2:
            run=False

print(f"point of user:{userp}\npoint of pc: {pcp}")