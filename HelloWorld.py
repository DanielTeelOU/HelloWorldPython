print("Hello World!")
print("What is your name?")
myName = input()
print("It is nice to meet you " + myName)
print("The length of your name is:")
print(len(myName))
print("What is your age?")
myAge = int(input())
if myAge > 19:
    print("You are an adult")
elif myAge < 20:
    if myAge >= 13:
        print("You are a teenager.")
    else:
        print("You are a child.")
