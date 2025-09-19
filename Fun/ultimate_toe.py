#DD Period 7 For Fun :D

def print_small_board(board, claimed=None):
    # If claimed, show simple X or O in all cells
    if claimed == "X" or claimed == "O":
        return [" | ".join([f"{claimed:^3}" for _ in row]) for row in board]
    # Each cell is 3 chars wide for alignment
    return [" | ".join([f"{cell:^3}" for cell in row]) for row in board]

def print_ultimate_board(boards, board_status=None):
    # boards is a 3x3 grid of 3x3 boards
    lines = []
    big_separator = "=" * 33
    for big_row in range(3):
        small_board_lines = []
        for col in range(3):
            claimed = board_status[big_row][col] if board_status else None
            small_board_lines.append(print_small_board(boards[big_row][col], claimed=claimed))
        # Use 5 lines for each small board (for ASCII art)
        for small_row in range(5):
            line = " || ".join([small_board_lines[col][small_row] for col in range(3)])
            lines.append(line)
        if big_row < 2:
            lines.append(big_separator)
    print("\n".join(lines))
def check_winner(board):
    # For a 3x3 board
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
def ultimate_tic_tac_toe():
    # 3x3 grid of boards
    boards = [[[ [" "]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
    board_status = [[None for _ in range(3)] for _ in range(3)] # None, "X", "O", or "D" for draw
    current_player = "X"
    active_board = None # (row, col) or None for any
    while True:
        print_ultimate_board(boards, board_status)
        if active_board and board_status[active_board[0]][active_board[1]] is None:
            print(f"Active small board: (row {active_board[0]+1}, col {active_board[1]+1})")
        else:
            print("You can play in any unfinished small board.")
        # Choose small board
        while True:
            if active_board and board_status[active_board[0]][active_board[1]] is None:
                br, bc = active_board
            else:
                br = int(input(f"Player {current_player}, choose board row (1-3): ")) - 1
                bc = int(input(f"Player {current_player}, choose board col (1-3): ")) - 1
                if not (0 <= br < 3 and 0 <= bc < 3):
                    print("Invalid board position. Try again.")
                    continue
                if board_status[br][bc] is not None:
                    print("That board is finished. Choose another.")
                    continue
            # Choose cell
            while True:
                try:
                    row = int(input(f"Player {current_player}, enter cell row (1-3): ")) - 1
                except ValueError:
                    print("AHHHHHHH I'M GONNA EXPLODE!!! YOU DIDN'T ENTER AN INTEGER FOR CELL ROW!!!")
                    continue
                if not (0 <= row < 3):
                    print("Invalid cell row. Enter a number from 1 to 3.")
                    continue
                break
            while True:
                try:
                    col = int(input(f"Player {current_player}, enter cell col (1-3): ")) - 1
                except ValueError:
                    print("AHHHHHHH I'M GONNA EXPLODE!!! YOU DIDN'T ENTER AN INTEGER FOR CELL COL!!!")
                    continue
                if not (0 <= col < 3):
                    print("Invalid cell col. Enter a number from 1 to 3.")
                    continue
                break
            if boards[br][bc][row][col] != " ":
                print("Invalid move. Try again.")
                continue
            boards[br][bc][row][col] = current_player
            break
        # Check if small board is won/drawn
        winner = check_winner(boards[br][bc])
        if winner:
            board_status[br][bc] = winner
            print(f"Player {winner} wins small board ({br}, {bc})!")
        elif is_draw(boards[br][bc]):
            board_status[br][bc] = "D"
            print(f"Small board ({br}, {bc}) is a draw.")
        # Check if ultimate board is won
        ultimate_winner = check_winner(board_status)
        if ultimate_winner:
            print_ultimate_board(boards)
            print(f"Player {ultimate_winner} wins the game!")
            break
        # Check for overall draw
        if all(board_status[r][c] is not None for r in range(3) for c in range(3)):
            print_ultimate_board(boards)
            print("The game is a draw!")
            break
        # Next active board is based on cell played
        if 0 <= row < 3 and 0 <= col < 3 and board_status[row][col] is None:
            active_board = (row, col)
        else:
            active_board = None # Any unfinished board
        current_player = "O" if current_player == "X" else "X"

try:
    ultimate_tic_tac_toe()
except Exception as e:
    print("AHHHHHHH I'M GONNA EXPLODE!!! UNEXPECTED ERROR:", e)
    import sys; sys.exit()