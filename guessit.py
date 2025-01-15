import random
import tkinter as tk
words=['skibbidi', 'rizz', 'ohio', 'flapjack', 'vibe', 'bop', 'yeet', 'slay', 'zesty', 'sizzle', 'dank', 'jolt', 'squabble', 'whizz', 'clutch', 'cringe', 'zap', 'mood', 'boink', 'gloopy', 'swag', 'lit', 'flick', 'popcorn', 'plop', 'woah','yeet', 'glitch', 'bop', 'wobble', 'snatched', 'wiggle', 'fling', 'chill', 'squish', 'swoosh', 'whack', 'crack', 'zap', 'chomp', 'boing', 'whoosh', 'zoom', 'squirt', 'splat', 'slap', 'swoop', 'pop', 'fizz', 'plop', 'smack']
word=random.choice(words)
guessword=['_']*len(word)
status=True
attempts=10

def working():
    global attempts,status,guessword,word
    while status:
        if(attempts>0):
            word_display.config(text=" ".join(guessword))
            guess=guess_label.get().lower()
            guess_label.delete(0,tk.END)
            if guess in word:
                for i in range(len(word)):
                    if word[i]==guess:
                        guessword[i]=guess
                result_label.config(text="Great guess!")
            else:
                attempts-=1
                result_label.config(text="Wrong Guess!! "+str(attempts)+" attempts left")
            if '_' not in guessword:
                result_label.config(text="Congrats! You guessed the word: " + word)
                status=False
        else:
            result_label.config(text="Oops! No attempts left. The word was: " + word)
            status=False
    
        
root=tk.Tk()
root.geometry("500x400")
root.title("Guess It!!")
root.configure(bg="ghost white")

label=tk.Label(root, text="Guess The Word", font=("Arial", 12), bg="ghost white")
label.grid(row=0, column=2, columnspan=2, pady=10)

word_display = tk.Label(root, text=" ".join(guessword), font=("Arial", 12), bg="ghost white")
word_display.grid(row=1, column=0, columnspan=2)

guess_label=tk.Text(root,text="Your Guess: ")
guess_label = tk.Label(root, text="Enter a letter: ", bg="ghost white")
guess_label.grid(row=2, column=0, pady=5)
guess_entry = tk.Entry(root, font=("Arial", 12))
guess_entry.grid(row=2, column=1, pady=5)

guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=working)
guess_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Attempts left: " + str(attempts), font=("Arial", 12), bg="ghost white")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()