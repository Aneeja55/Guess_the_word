import random
words=['skibbidi', 'rizz', 'ohio', 'flapjack', 'vibe', 'bop', 'yeet', 'slay', 'zesty', 'sizzle', 'dank', 'jolt', 'squabble', 'whizz', 'clutch', 'cringe', 'zap', 'mood', 'boink', 'gloopy', 'swag', 'lit', 'flick', 'popcorn', 'plop', 'woah','yeet', 'glitch', 'bop', 'wobble', 'snatched', 'wiggle', 'fling', 'chill', 'squish', 'swoosh', 'whack', 'crack', 'zap', 'chomp', 'boing', 'whoosh', 'zoom', 'squirt', 'splat', 'slap', 'swoop', 'pop', 'fizz', 'plop', 'smack']
word=random.choice(words)
guessword=['_']*len(word)
status=True
attempts=10
while status:
    if(attempts>0):
        print('\nGuess the word:'+' '.join(guessword))
        guess=input("Guess a letter: ").lower()
        if guess in word:
            for i in range(len(word)):
                if word[i]==guess:
                    guessword[i]=guess
            print("Great guess!")
        else:
            attempts-=1
            print("Wrong Guess!! "+str(attempts)+" attempts left")
        if '_' not in guessword:
            print("Congrats you got it!! The word is: "+word)
            status=False
    else:
        print('Oopss!!No attempts left\n the word was: '+word)
        status=False
        
