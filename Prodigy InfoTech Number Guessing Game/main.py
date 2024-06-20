import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        master.configure(bg='#ADD8E6')  # Set background color

        # Create custom fonts
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)
        self.button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        self.random_number = random.randint(1, 100)
        self.attempts = 0

        # Game title
        self.title_label = tk.Label(master, text="Guessing Game", font=self.title_font, bg='#ADD8E6', fg='black')
        self.title_label.pack(pady=10)

        # Instructions
        self.instructions_label = tk.Label(master, text="Guess the number between 1 and 100", font=self.label_font, bg='#ADD8E6')
        self.instructions_label.pack(pady=5)

        # Separator line
        self.separator1 = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN, bg='#ADD8E6')
        self.separator1.pack(fill=tk.X, padx=5, pady=5)

        # Input field for guesses
        self.guess_entry = tk.Entry(master, font=self.label_font)
        self.guess_entry.pack(pady=5)

        # Guess button
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=self.button_font, bg='#32CD32', fg='white')
        self.guess_button.pack(pady=5)

        # Separator line
        self.separator2 = tk.Frame(master, height=2, bd=1, relief=tk.SUNKEN, bg='#ADD8E6')
        self.separator2.pack(fill=tk.X, padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(master, text="", font=self.label_font, bg='#ADD8E6')
        self.result_label.pack(pady=5)

        # Attempts label
        self.attempts_label = tk.Label(master, text="Attempts: 0", font=self.label_font, bg='#ADD8E6')
        self.attempts_label.pack(pady=5)

        # New game button
        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game, font=self.button_font, bg='#FF4500', fg='white')
        self.new_game_button.pack(pady=5)

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, font=self.button_font, bg='#FF4500', fg='white')
        self.quit_button.pack(pady=5)

        # Copyright notice
        self.copyright_label = tk.Label(master, text="© 2024 Manoj Paloi", font=self.label_font, bg='#ADD8E6', fg='black')
        self.copyright_label.pack(side=tk.BOTTOM, pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < 1 or guess > 100:
                messagebox.showerror("Invalid input", "Please enter a number between 1 and 100.")
                return

            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.random_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.random_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.")
                messagebox.showinfo("Result", f"Congratulations! You guessed the correct number {self.random_number} in {self.attempts} attempts.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")

    def new_game(self):
        self.reset_game()
        messagebox.showinfo("New Game", "A new game has started! Guess the new number between 1 and 100.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
