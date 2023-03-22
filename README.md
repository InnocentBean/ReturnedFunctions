# ReturnedFunctions
s = input("What's your name? ")

def reverse(s):
    tx = ""
    for i in s:
        tx = i + tx
    return tx

    

def ready():
    global s
    print(reverse(s))


reverse(s)
ready()
