def clean(floor):
    m=len(floor)
    n=len(floor[0])
    for i in range(m):
        if i%2==0:
            for j in range(n):
                if(floor[i][j]==1):
                    print("STATUS:DIRTY")
                    print_floor(floor,i,j)
                    floor[i][j]=0
                else:
                    print("STATUS:CLEAN")
                    print_floor(floor,i,j)
                    
        else:
            for j in range(n-1,-1,-1):
                if floor[i][j]==1:
                    print("STATUS:DIRTY")
                    print_floor(floor,i,j)
                    floor[i][j]=0
                else:
                    print("STATUS:CLEAN")
                    print_floor(floor,i,j)
    print("STATUS: ALL STATES CLEANED") 
    print_floor(floor,i,j)
    return
def print_floor(floor, row, col): 
    print("Row :",row," Column :",col)
    print(floor)
    print("-----------------")

floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]

clean(floor)
