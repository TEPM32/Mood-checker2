print("Welcome to the mood checker!")

mood = input("Please enter one of the provided moods - "
             "happy, sad, bored, stressful, sleepy, phlegmatic, romantic, funny: ")

if mood == "happy":
    print("Great to see you happy!")
elif mood == "sad":
    print("Cheer up! Life is to short to be sad.")
elif mood == "bored":
    print("Don't waste your time. Find something to do!")
elif mood == "stressful":
    print("Stress is bad for your body and your mind. Please calm down.")
elif mood == "sleepy":
    print("Take a nap.")
elif mood == "phlegmatic":
    print("Not bad. Your a step closer to being happy than the sad one.")
elif mood == "romantic":
    print("Love is in the air, isn't it?")
elif mood == "funny":
    print("Make me laugh to!")

else:
    print("Sorry, but try with some of the offered moods.")
