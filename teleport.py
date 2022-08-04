import random
print("teleport ready")
def game3():
    def teleport():
        numbers=[7,17,26,32,47,56,64,75,82,99]
        flag1=True
        flag2=True
        end = False
        board=[]
        for i in range(1,111):
            board.append(i)
        def draw():
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[99],board[98],board[97],board[96],board[95],board[94],board[93],board[92],board[91],board[90]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}"
            .format (board[80],board[81],board[82],board[83],board[84],board[85],board[86],board[87],board[88],board[89]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[79],board[78],board[77],board[76],board[75],board[74],board[73],board[72],board[71],board[70]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[60],board[61],board[62],board[63],board[64],board[65],board[66],board[67],board[68],board[69]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[59],board[58],board[57],board[56],board[55],board[54],board[53],board[52],board[51],board[50]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[40],board[41],board[42],board[43],board[44],board[45],board[46],board[47],board[48],board[49]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[39],board[38],board[37],board[36],board[35],board[34],board[33],board[32],board[31],board[30]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[20],board[21],board[22],board[23],board[24],board[25],board[26],board[27],board[28],board[29]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[19],board[18],board[17],board[16],board[15],board[14],board[13],board[12],board[11],board[10]))
            print()
            print("{0:<9}{1:<9}{2:<9}{3:<9}{4:<9}{5:<9}{6:<9}{7:<9}{8:<9}{9:<9}" .format (board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))
            print()
            print()
            print()
        def diceroll():
            dicenos=[1,1,1,1,2,2,2,3,3,4,4,5,6]
            g=random.choice(dicenos)
            return g
        def p1one():
            print("player1"," press enter to roll dice")
            entry=input("press enter to roll dice 1")
            dice=diceroll()
            n=dice-1
            print()
            print(dice)
            print()
            board[n]="l--X--l"
            draw()
            return n
        def p1two(x):
            print("player1"," press enter to roll dice")
            entry=input("press enter to roll dice 2")
            dice=diceroll()
            n=x+dice
            print()
            print(dice)
            print()
            board[n]="l--X--l"
            board[x]=x+1
            draw()
            return n
        def p1three(x):
            telno=random.randint(0,100)
            board[telno]="l--X--l"
            board[x]=x+1
            draw()
            return telno
        def p2one():
            print("player2", "press enter to roll dice")
            entry=input("press enter to roll dice 3")
            dice=diceroll()
            n=dice-1
            print()
            print(dice)
            print()
            board[n]="l--O--l"
            draw()
            return n
        def p2two(x):
            print("player2", "press enter to roll dice")
            entry=input("press enter to roll dice 4")
            dice=diceroll()
            n=x+dice
            print()
            print(dice)
            print()
            board[n]="l--O--l"
            board[x]=x+1
            draw()
            return n
        def p2three(x):
            telno=random.randint(0,100)
            board[telno]="l--O--l"
            board[x]=x+1
            draw()
            return telno

        for i in range(1):
            pos1=p1one()
            print()
            pos2=p2one()
            print()
            if board[pos1]=="O":
                pos1=p1one()
                pos2=p2two(pos2)
        for i in range(150):
            for ox in numbers:
                if pos1==ox:
                    flag1=True
                    break
                else:
                    flag1=False
            if flag1==True:
                pos1=p1two(pos1)
                print("TELEPORTED")
                pos1=p1three(pos1)
            else:
                pos1=p1two(pos1)
            if pos1 < 99 and pos2 < 99:
                if board[pos2]=="X":
                    pos2=p2one()
                    pos1=p1two(pos1)
                for ox in numbers:
                    if pos2==ox:
                        flag2=True
                        break
                    else:
                        flag2=False
                    if flag2==True:
                        pos2=p2two(pos2)
                        print("TELEPORTED")
                        pos2=p2three(pos2)
                    else:
                        pos2=p2two(pos2)
                    if pos1 < 99 and pos2 < 99:
                        if board[pos1]=="O":
                            pos1=p1one()
                            pos2=p2two(pos2)
                        if pos1 > 100 :
                            print("Player 1 wins")
                            break
                        if pos2 > 100:
                            print("Player 2 wins")
                            break
                        else:
                            continue
    teleport()
