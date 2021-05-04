started = False
command = ""
print("Please Enter help to know about the game ✌")
while True:
    command = input(">> ").lower()

    if command == "start":
        if started:
            print("Car is already started dude")
        else:
            started = True
            print("Car is started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped")
    elif command == "help":
        print("""
Instructions are as follows:
start - to start a car
stop - to stop a car
quit - to terminate the programme
        """)

    elif command == "quit":
        break
    else:
        print("Sorry I haven't understood")
