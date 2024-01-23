#--------User Input's Section------------------------------------
Queen = int(input("give me a input please : "))
chess_Board=[[0 for i in range(Queen)]for i in range(Queen)]
#print(chess_board)

#------------Apply def function -------------
def chess_column(chess_Board,row,column):
    for i in range(row,-1,-1):
        if chess_Board[i][column]=="♕":     #---- Agar row or column equal hujai g tu voh mujh false dega-----
            return False
    return True        

def diagonal(chess_Board,row,column):
    for i,j in zip(range(row,-1,-1),range(column,-1,-1)):
        if chess_Board[i][j]=="♕":
            return False
    for i,j in zip(range(row,-1,-1),range(column,Queen)):
        if chess_Board[i][j]=="♕":
            return False                 
    return True
# Now we do the main part and the final part of Our project we do "Backtracking"-----

def n_queen(chess_Board,row):
    if row == Queen:
        return True
    for i in range(Queen):
        if(chess_column(chess_Board,row,i)==True and diagonal(chess_Board,row,i)==True):
            chess_Board[row][i]="♕"
            if n_queen(chess_Board,row+1):
                return True
            chess_Board[row][i]=0
    return False                              
n_queen(chess_Board,0)
for row in chess_Board:
    print(row)
print("Thank's You Playing")
                            #-------------------------- THE END ----------------------------------
                            