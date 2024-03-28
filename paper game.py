import tkinter as tk
from tkinter import ttk
import random
from ttkthemes import ThemedTk

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")

        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Use the 'clam' theme for a cleaner appearance
        self.style.configure("Game.TLabel", font=("Helvetica", 14), background="#f0f0f0")  # Label style
        self.style.configure("Game.TButton", font=("Helvetica", 12), background="#007bff", foreground="white")  # Button style

        # Main label
        self.label = ttk.Label(master, text="Choose Rock, Paper, or Scissors:", style="Game.TLabel")
        self.label.pack(pady=20)

        # Buttons
        self.button_rock = ttk.Button(master, text="Rock", style="Game.TButton", command=lambda: self.play("Rock"))
        self.button_rock.pack(side=tk.LEFT, padx=10)

        self.button_paper = ttk.Button(master, text="Paper", style="Game.TButton", command=lambda: self.play("Paper"))
        self.button_paper.pack(side=tk.LEFT, padx=10)

        self.button_scissors = ttk.Button(master, text="Scissors", style="Game.TButton", command=lambda: self.play("Scissors"))
        self.button_scissors.pack(side=tk.LEFT, padx=10)

        # Result label
        self.result_label = ttk.Label(master, text="", style="Game.TLabel")
        self.result_label.pack(pady=20)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        self.result_label.config(text=f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n{result}")

def main():
    root = ThemedTk(theme="clearlooks")  # Change to any available theme for a different look
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
