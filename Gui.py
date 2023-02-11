import random
import tkinter as tk

def guess(event=None):
    user_input = int(entry.get())
    global p
    if user_input == k:
        result_label.config(text="Your Answer: " + str(user_input) + "\nRight Answer: " + str(k) + "\nCongratulations!\nTotal number of tries: " + str(p))
        entry.config(state='disabled')
        submit_button.config(state='disabled')
    else:
        p += 1
        result_label.config(text="Your guess is wrong, try again")

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")

n = random.randint(1, 10)
j = random.randint(10, 50)
k = random.randint(n, j)
p = 1

instruction_label = tk.Label(root, text="Guess a number between " + str(n) + " and " + str(j), font=("Helvetica", 14))
instruction_label.pack(pady=30)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=20)
entry.bind("<Return>", guess)

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=guess)
submit_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
