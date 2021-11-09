import challenge1
import challenge2
import challenge3


while (True):
    print("1.Challenge1")
    print("2.Challenge2")
    print("3.Challenge3")
    ch = input("Please select challenge: ")
    if ch == "1":
        challenge1.start()
    elif ch == "2":
        challenge2.start()
    elif ch == "3":
        challenge3.start()
    else:
        break

 