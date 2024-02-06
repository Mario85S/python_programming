#Create a function that takes a grid of # and -, where each hash (#) represents a
#mine and each dash (-) represents a mine-free spot.
def mine_sweeper(board):
    num_rows = len(board)
    num_cols = len(board[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == '-':
                count = 0
                # check adjacent cells
                for i_adj_cell, j_adj_cell in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if i_adj_cell >= 0 and i_adj_cell < num_rows and j_adj_cell >= 0 and j_adj_cell < num_cols and board[i_adj_cell][j_adj_cell] == '#':
                        count += 1
                # update cell with number of adjacent mines
                board[i][j] = str(count)
    return board

#Create argument for the function mine_sweeper
board = [ ["-", "-", "-", "#", "#"], 
          ["-", "#", "-", "-", "-"],
          ["-", "-", "#", "-", "-"],
          ["-", "#", "#", "-", "-"],
          ["-", "-", "-", "-", "-"] ]

#Create a variable to store the function mine_sweeper and call the function
new_mine_board = mine_sweeper(board)
for row in new_mine_board:
    print(" ".join(row))