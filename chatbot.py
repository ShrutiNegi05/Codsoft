print("simple question and answering program")
print("-------------------------------------")
print("you may ask anyone of these question")
print("Hi")
print("How are you?")
print("Are you working")
print("What is your name?")
print("What did you do yesterday")
print("Quit")

while True:
    question=input("Enter one question from above list:")
    question= question.lower()
    if question in['hi']:
        print("Hello")
    elif question in['how are you?','how do you do?']:
        print("I am fine")
    elif question in['are you working','are you doing any job']:
        print("Yes,i am working in Banglore")
    elif question in['what is your name?']:
        print("my name is Shruti")
        name=input("Enter your name")

        print("Nice name and Nice meeting you",name)
    elif question in['what did you do yesterday']:
        print("I saw a movie 5 times")

    elif question in['quit']:
        break

else:
    print("I dont understand what you said")