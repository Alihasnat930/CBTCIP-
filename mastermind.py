import tkinter as tk
import random

class MastermindGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind Game")
        self.master.geometry("400x250")
        self.master.configure(bg="#f0f0f0")

        self.player_label = tk.Label(master, text="Player 1", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.player_label.grid(row=0, column=0, padx=10, pady=10)

        self.number_label = tk.Label(master, text="Enter your number:", bg="#f0f0f0", font=("Arial", 10))
        self.number_label.grid(row=1, column=0, padx=10, pady=5)

        self.number_entry = tk.Entry(master, font=("Arial", 10))
        self.number_entry.grid(row=1, column=1, padx=10, pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_number, bg="#007bff", fg="white", font=("Arial", 10, "bold"))
        self.submit_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.message_label = tk.Label(master, text="", bg="#f0f0f0", font=("Arial", 10))
        self.message_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.guess_label = tk.Label(master, text="Player 2: Guess the number", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.guess_label.grid(row=4, column=0, padx=10, pady=10)

        self.guess_entry = tk.Entry(master, font=("Arial", 10))
        self.guess_entry.grid(row=4, column=1, padx=10, pady=5)

        self.check_button = tk.Button(master, text="Check", command=self.check_guess, bg="#007bff", fg="white", font=("Arial", 10, "bold"))
        self.check_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.secret_number = None
        self.guess_count = 0

    def submit_number(self):
        try:
            self.secret_number = int(self.number_entry.get())
            if len(str(self.secret_number)) != 4:
                raise ValueError
            self.number_entry.config(state='disabled')
            self.submit_button.config(state='disabled', bg="#d6d6d6", fg="gray")
            self.message_label.config(text="Number set successfully!", fg="green")
        except ValueError:
            self.message_label.config(text="Please enter a 4-digit number.", fg="red")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if len(str(guess)) != 4:
                raise ValueError
            self.guess_count += 1
            if guess == self.secret_number:
                self.message_label.config(text=f"Congratulations! You guessed the number in {self.guess_count} tries.", fg="green")
                self.guess_entry.config(state='disabled')
                self.check_button.config(state='disabled', bg="#d6d6d6", fg="gray")
            else:
                matching_digits = sum(1 for x, y in zip(str(guess), str(self.secret_number)) if x == y)
                self.message_label.config(text=f"Correct digits: {matching_digits}", fg="black")
        except ValueError:
            self.message_label.config(text="Please enter a 4-digit number.", fg="red")

def main():
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
