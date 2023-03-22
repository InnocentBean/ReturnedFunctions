inpu = input("What's your name? ")

def reverse():
    global inpu
    inpu = list(reversed(inpu))
    return inpu

def ready():
    print("".join(inpu))

reverse()
ready()