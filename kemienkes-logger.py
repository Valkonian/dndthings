import time as t

print('[INFO] Initialising...')
t.sleep(1)

itemList = []
running = True

with open('kemienkes-data.txt') as fileRead:
    lines = fileRead.read().splitlines()

for i in range(len(lines)):
    items = lines[i].split(':')
    itemList.append(items)

while running:
    print("\n[INPUT REQUIRED] \nPlease select an option \n1: View all kemienkes \n2: Update all kemienkes \n3: Update 1 player's kemienkes")
    option = input('')
    print('\n[INFO] Working...')
    t.sleep(1)

    if option == "1":
        print('')
        for i in range(len(itemList)):
            print(f"{itemList[i][0]}: {itemList[i][1]}")
    elif option == "2":
        addSubtract = input("\n[INPUT REQUIRED]\n1: Add \n2: Subtract\n")
        if addSubtract == "1":
            toAdd = input("\n[QUESTION] How much to add? ")
            try:
                toAdd = int(toAdd)
            except ValueError:
                print("\n[ERROR] That's not an integer!")
            print("\n[INFO] Working...")
            for i in range(len(itemList)):
                item = int(itemList[i][1]) #takes item
                item += toAdd #adds to item
                itemList[i][1] = item #replaces item
                # print(f"{itemList[i][0]}: {itemList[i][1]}")
            fileClear = open('kemienkes-data.txt', 'w').close() #clears file
            with open('kemienkes-data.txt', 'a') as fileAppend: #appends to file
                for i in range(len(itemList)):
                    string = f"{itemList[i][0]}: {itemList[i][1]}\n" #string to append
                    fileAppend.write(string)
            # print(itemList)
            t.sleep(0.5)
        elif addSubtract == "2":
            toSubtract = input("\n[QUESTION] How much to subtract? ")
            try:
                toSubtract = int(toSubtract)
            except ValueError:
                print("\n[ERROR] That's not an integer!")
            print("\n[INFO] Working...")
            for i in range(len(itemList)):
                item = int(itemList[i][1])
                item -= toSubtract
                itemList[i][1] = item
                # print(f"{itemList[i][0]}: {itemList[i][1]}")
            fileClear = open('kemienkes-data.txt', 'w').close()
            with open('kemienkes-data.txt', 'a') as fileAppend:
                for i in range(len(itemList)):
                    string = f"{itemList[i][0]}: {itemList[i][1]}\n"
                    fileAppend.write(string)
            # print(itemList)
            t.sleep(0.5)
        else:
            print('[ERROR] Invalid choice!')

    elif option == "3":
        addSubtract = input("\n[INPUT REQUIRED]\n1: Add \n2: Subtract\n")
        if addSubtract == "1":
            print("\n[INPUT REQUIRED]\nWho would you like to change?")
            for i in range(len(itemList)):
                print(f"{i+1}: {itemList[i][0]}")
            who = input('')
            try:
                who = int(who)
            except ValueError:
                print("[ERROR] That's not an integer!")
            
            print("\n[INFO] Working...")

            toAdd = input("\n[QUESTION] How much to add? ")
            try:
                toAdd = int(toAdd)
            except ValueError:
                print("\n[ERROR] That's not an integer!")

            t.sleep(0.5)
            pos = who-1
            item = int(itemList[pos][1])
            item += toAdd
            itemList[pos][1] = item
            print("\n[INFO] Working...")

            t.sleep(0.5)
            
            # print(f"{itemList[i][0]}: {itemList[i][1]}")

            fileClear = open('kemienkes-data.txt', 'w') #clears file
            with open('kemienkes-data.txt', 'a') as fileAppend: #appends to file
                for i in range(len(itemList)):
                    string = f"{itemList[i][0]}: {itemList[i][1]}\n" #string to append
                    fileAppend.write(string)
            # print(itemList)

            t.sleep(0.5)

        elif addSubtract == "2":
            print("\n[INPUT REQUIRED]\nWho would you like to change?")
            for i in range(len(itemList)):
                print(f"{i+1}: {itemList[i][0]}")
            who = input('')
            try:
                who = int(who)
            except ValueError:
                print("[ERROR] That's not an integer!")
            
            print("\n[INFO] Working...")

            toSubtract = input("\n[QUESTION] How much to subtract? ")
            try:
                toSubtract = int(toSubtract)
            except ValueError:
                print("\n[ERROR] That's not an integer!")

            t.sleep(0.5)
            pos = who-1
            item = int(itemList[pos][1])
            item -= toSubtract
            itemList[pos][1] = item
            
            # print(f"{itemList[i][0]}: {itemList[i][1]}")

            fileClear = open('kemienkes-data.txt', 'w') #clears file
            with open('kemienkes-data.txt', 'a') as fileAppend: #appends to file
                for i in range(len(itemList)):
                    string = f"{itemList[i][0]}: {itemList[i][1]}\n" #string to append
                    fileAppend.write(string)
            # print(itemList)

            t.sleep(0.5)

        else:
            print('[ERROR] Invalid choice!')

    print('\n[INFO] Finishing up...')

    t.sleep(1)

    done = input('\n[QUESTION] Are you done? ').upper()

    if done == 'Y':
        print("\n[INFO] Shutting down...")
        running = False
    elif done == 'N':
        running = True
        print('\n[INFO] Working...')
        t.sleep(1)
    else:
        print("\n[ERROR] That's not valid! Shutting down anyway..")
        running = False