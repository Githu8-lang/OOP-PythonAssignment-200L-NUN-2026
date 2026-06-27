import tkinter as tk
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.secret_number = random.randint(1, 100)

        self.root.title("Hive guessing ai game ")
        self.root.geometry("400x400")
        self.root.configure(bg="green")

        self.title = tk.Label(
            root,
            text="Guess the number (1-100)",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="blue"
        )
        self.title.pack(pady=20)

        self.message = tk.Label(
            root,
            text="Enter your guess below",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="blue"
        )
        self.message.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), width=10)
        self.entry.pack(pady=20)

        self.result = tk.Label(
            root,
            text="",
            font=("Arial", 14),
            fg="white",
            bg="blue"
        )
        self.result.pack(pady=30)

        # Buttons
        tk.Button(root, text="Check", command=self.check_guess).pack()
        tk.Button(root, text="Reset", command=self.reset_game).pack()

    # Class function (method)
    def check_guess(self):
        try:
            guess = int(self.entry.get())

            if guess < self.secret_number:
                self.result.config(text="Too low!")
            elif guess > self.secret_number:
                self.result.config(text="Too high!")
            else:
                self.result.config(text="Correct!")

        except ValueError:
            self.result.config(text="Enter a valid number")

    # Another class function
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        self.result.config(text="")


root = tk.Tk()
app = GuessingGame(root)
root.mainloop()