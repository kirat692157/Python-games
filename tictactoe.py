import random
print("tictactoe ready")
print("please wait")
def game1():
    tt=[1,2,3,4,5,6,7,8,9]
    def ran(tt):
        b=random.randint(0,9)
        if tt[b-1]!="X" and tt[b-1]!="O":
            tt[b-1]="O"
        else:
            ran(tt)
    def tictac(tt,a=9):
        b=0
        while b <=8:
            for i in range(0,3):
                print(tt[b],end=" ")
                b+=1
                if i == 2:
                    print("  ")
        a=int(input("enter the place where you want to enter cross "))
        if a >0 and a<10:
            if tt[a-1]!="X" and tt[a-1]!="O":
                tt[a-1]="X"
                if tt[0]==tt[1]==tt[2]=="X" or tt[3]==tt[6]==tt[0]=="X" or tt[0]==tt[4]==tt[8]=="X" or tt[1]==tt[4]==tt[7]=="X" or tt[2]==tt[5]==tt[8]=="X" or tt[2]==tt[4]==tt[6]=="X" or tt[3]==tt[4]==tt[5]=="X" or tt[6]==tt[7]==tt[8]=="X":
                    print("you are the winner")
                    a=11
                elif (1 not in tt) and (2 not in tt) and (3 not in tt) and (4 not in tt) and (5 not in tt) and (6 not in tt) and (7 not in tt) and (8 not in tt) and (9 not in tt):
                    print("it's a tie game")
                    a=11
                elif tt[0]==tt[1]==tt[2]=="O" or tt[3]==tt[6]==tt[0]=="O" or tt[0]==tt[4]==tt[8]=="O" or tt[1]==tt[4]==tt[7]=="O" or tt[2]==tt[5]==tt[8]=="O" or tt[2]==tt[4]==tt[6]=="O" or tt[3]==tt[4]==tt[5]=="O" or tt[6]==tt[7]==tt[8]=="O":
                    print("comp is the winner")
                    a=11
                else:
                    ran(tt)
                    if tt[0]==tt[1]==tt[2]=="O" or tt[3]==tt[6]==tt[0]=="O" or tt[0]==tt[4]==tt[8]=="O" or tt[1]==tt[4]==tt[7]=="O" or tt[2]==tt[5]==tt[8]=="O" or tt[2]==tt[4]==tt[6]=="O" or tt[3]==tt[4]==tt[5]=="O" or tt[6]==tt[7]==tt[8]=="O":
                        print("comp is the winner")
                        a=11
                    else:
                        tictac(tt)
            else:
                print("the place you want to enter X is already filled")
                tictac(tt)
        else:
            print("please enter no. between 1 and 9")
            tictac(tt)
    tictac(tt)

