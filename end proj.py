import tictactoe
import plot4
import teleport
import maths_game
import SQL
playedgames=SQL.tupfet()
playedgames=playedgames[0]
playedgames=list(playedgames)
print()
print("Please enter the game you wish to play")
print()
print("tic for tictactoe")
print("plot for plot4")
print("tele for teleport")
print("math for maths game")
print()
def inp():
    game=input("What game do you wanna play")
    if game=='tic' or game=='plot' or game=='tele' or game=='math':
        pass
    else:
        print("error")
        inp()
    return game
game=inp()
if game=='tic':
    print('playing tictactoe...')
    playedgames[0]=(playedgames[0])+1
    g=tictactoe.game1()
elif game=='plot':
    playedgames[1]=(playedgames[1])+1
    f=open('rules plot4.txt','r')
    ox=f.read()
    print(ox)
    g=plot4.game2()
elif game=='tele':
    playedgames[2]=(playedgames[2])+1
    f=open('Rules teleport.txt','r')
    ox=f.read()
    print(ox)
    g=teleport.game3()
elif game=='math':
    playedgames[3]=(playedgames[3])+1
    g=maths_game.game4()
f=SQL.entry(playedgames)

