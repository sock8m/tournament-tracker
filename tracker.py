def Startup():
    # Startup:
    print("Welcome to Tournaments R Us")
    print("===========================")
    slotTotal = int(input("Enter the number of participants: "))
    print(f"There are {slotTotal} participant slots ready for sign-ups.")
    participantList = {}

    # initializing the participant list
    for i in range(1,slotTotal+1):
        participantList[i] = "[empty]"

    Redirect(participantList)

def repeatFunc(var):
    wrongInput = True
    while wrongInput:
        repeat = str(input("Continue? [y/n] "))
        if repeat == 'n':
            var = False
            wrongInput = False
        elif repeat == 'y':
            var = True
            wrongInput = False
        else:
            print("Wrong input.")
    return var

def SignUp(participantList):
    # Sign Up:
    print("Participant Sign Up")
    print("==========================")
    slotTotal = len(participantList)

    newEntry = True
    while newEntry:
        name = str(input("Participant Name: "))
        slotWorks = True
        while slotWorks:
            slot = int(input(f"Desired starting slot #[1-{slotTotal}]: "))

            if slot in participantList.keys():
                if participantList[slot]=="[empty]":
                    participantList[slot] = name
                    print("Success:")
                    print(f"{name} is signed up in starting slot #{slot}.")
                    break
                else:
                    print("Error:")
                    print(f"Slot #{slot} is filled. Please try again.")
            else:
                print(f"There is no registration for starting slot #{slot}.")
        newEntry = repeatFunc(newEntry)

    Redirect(participantList)

def CancelSignUp(participantList):
    # Cancel Sign Up
    print("Participant Cancellation")
    print("===========================")
    slotTotal = len(participantList)

    slotWorks = True
    while slotWorks:
        slot = int(input(f"Starting slot #[1-{slotTotal}]: "))
        name = str(input("Participant Name: "))

        if slot in participantList.keys():
            if participantList[slot] == name:
                participantList[slot] = "[empty]"
                print("Success:")
                print(f"{name} has been cancelled from starting slot #{slot}.")
                slotWorks = repeatFunc(slotWorks)
            else:
                print("Error:")
                print(f"{name} is not in that starting slot.")
                slotWorks = repeatFunc(slotWorks)
        else:
            print(f"There is no registration for starting slot #{slot}.")
            slotWorks = repeatFunc(slotWorks)

    Redirect(participantList)

# View Participants
def ViewParticipants(participantList):
    print("View Participants")
    print("========================")
    lengthList = len(participantList)

    viewList = True
    while viewList:
        slotDisplay = int(input(f"Starting slot #[1-{len(participantList)}]: "))
        if slotDisplay <= 5:
            minDisplay = 1
        else:
            minDisplay = slotDisplay-5
        if slotDisplay > lengthList-5:
            maxDisplay = lengthList
        else:
            maxDisplay = slotDisplay+5
        print("Starting Slot: Participant")
        for i in range(minDisplay, maxDisplay+1):
            print(f"{i}: {participantList[i]}")
        viewList = repeatFunc(viewList)

    Redirect(participantList)

# Save Changes
def SaveChanges(participantList):
    import csv
    print("Save Changes")
    print("===================")

    while True:
        save = str(input("Save your changes to CSV? [y/n] "))
        if save == "y":
            break
        elif save == "n":
            Redirect(participantList)
            break
        else:
            print("Invalid input.")
    
    new_path = open("test.csv","w")
    z = csv.writer(new_path)
    for slot, name in participantList.items():
        z.writerow([slot, name])
    new_path.close()

    Redirect(participantList)

# Exit
def Exit(participantList):
    print("Exit")
    print("===================")
    print("Any unsaved changes will be lost.")

    exitStatus = True
    while exitStatus:
        exit = str(input("Are you sure you want to exit? [y/n] "))
        if exit == "y":
            print("Goodbye!")
            exitStatus = False
        elif exit == "n":
            Redirect(participantList)
        else:
            print("Invalid input. Please input [y/n] ")

def MainMenu():
    # Main Menu:
    print("Participant Menu")
    print("===========================")
    print("1. Sign Up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save Changes")
    print("5. Exit")
    nextpage = int(input("Enter the number (1, 2, 3, 4, 5) of your choice: "))

    print("===========================")
    return nextpage

def Redirect(Plist):
    print("===========================")
    print("===========================")
    while True:
        redirect = MainMenu()
        if redirect >= 1 and redirect <= 5:
            break

    if redirect == 1:
        SignUp(Plist)
    elif redirect == 2:
        CancelSignUp(Plist)
    elif redirect == 3:
        ViewParticipants(Plist)
    elif redirect == 4: 
        SaveChanges(Plist)
    elif redirect == 5:
        Exit(Plist)

Startup()