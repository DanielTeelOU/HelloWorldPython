print("Hello World!")
print("What is your name?")
myName = input()
print("It is nice to meet you " + myName + ".")
print("The length of your name is:")
print(len(myName))
print("What is your age?")
myAge = int(input())
if myAge >= 21:
    print("You are an adult")
elif myAge < 20:
    if myAge >= 13:
        print("You are a teenager.")
    elif myAge <= 13:
        print("You are a child.")
else:
    print("You're technically an adult but you're in this weird limbo stage until you turn 21.")
