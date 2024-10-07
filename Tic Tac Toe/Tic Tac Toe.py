import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Global variables
player = 'X'
board = ['' for _ in range(9)]  # Empty board

# Function to check if there's a winner
def check_winner():
    # All possible winning combinations
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                        (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != '':
            return board[a]  # Return the winner ('X' or 'O')
    if '' not in board:
        return 'Tie'  # Return 'Tie' if the board is full and there's no winner
    return None  # No winner yet

# Function to handle button click
def on_click(index):
    global player
    if board[index] == '' and check_winner() is None:
        buttons[index].config(text=player, state=tk.DISABLED)
        board[index] = player
        winner = check_winner()
        if winner:
            if winner == 'Tie':
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"{winner} won!")
            disable_all_buttons()
        else:
            player = 'O' if player == 'X' else 'X'  # Switch player

# Function to disable all buttons after the game is over
def disable_all_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

# Function to reset the game
def reset_game():
    global player, board
    player = 'X'
    board = ['' for _ in range(9)]
    for button in buttons:
        button.config(text='', state=tk.NORMAL)

# Create buttons for Tic Tac Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text='', width=10, height=3, font=('Arial', 20),
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Create Reset button
reset_button = tk.Button(root, text="Reset-Game", command=reset_game, font=('Arial', 12))
reset_button.grid(row=3, column=0, columnspan=3)

# Run the Tkinter event loop
root.mainloop()