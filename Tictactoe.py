board=[' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo,le):
    return ((bo[1]==le and bo[2]==le and bo[3]==le) or                          #left to right
    (bo[4]==le and bo[5]==le and bo[6]==le) or
    (bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[1]==le and bo[4]==le and bo[7]==le) or                                  #top to bottom
    (bo[2]==le and bo[5]==le and bo[8]==le) or
    (bo[3]==le and bo[6]==le and bo[9]==le) or
    (bo[1]==le and bo[5]==le and bo[9]==le) or                                  #diagonally
    (bo[3]==le and bo[5]==le and bo[7]==le))

def playerMove():
    run=True
    while run:
        move=input("Where would you like to place 'X'(1-9): ")
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertLetter('X',move)
                else:
                    print("Sorry, space is occupied")
            else:
                print("Please insert number within the range!!")
        except:
            print("Please type a number!!")

def compMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter==' ' and x!=0]
    move=0
    for let in ['O','X']:                                                       #checking if the comp can win in the next move or if the opponent can win and hence block it
        for i in possibleMoves:
            boardCopy=board[:]                                                  #creating a copy for the board
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move

    cornersOpen=[]
    for i in possibleMoves:                                                     #checking if corners are free
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:                                                      #choosing one of the corners
        move=selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:                                                      #checking and choosing the middle
        move=5
        return move

    edgesOpen=[]
    for i in possibleMoves:                                                     #checking if corners are free
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:                                                        #choosing one of the corners
        move=selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcom to Tic Tac Toe')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry computer won the game')
            break

        if not(isWinner(board,'X')):
            move = compMove()
            if move==0:
                print("Game is tied!")
            else:
                insertLetter('O',move)
                print("Computer placed in position ",move)
                printBoard(board)
        else:
            print('Congrats you won')
            break



    if isBoardFull(board):
        print('Game is tied')

main()
