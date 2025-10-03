import random
symboler = []
frukter = ["🍋", "🍎", "🥑", "🍌", "🍇", "🍆", "🍑", "🍒"]
konto = 200

print("Skriv 'konto' för att se dina pengar.")
print("Skriv 'r' för att rulla.")
print("Skriv 'q' för att avsluta.")
print(" ")
bet = input("Hur mycket vill du betta?")

while True:
    key = input().lower()

    if konto <= 0:
        print("Du har " + str(konto) + " Kr på kontot. Spelet avslutas...")
        exit()      # slut på pengar :(

    if key == "q":
        break
    elif key == "r":

        symboler = []
        for i in range(3):
            slot = random.choice(frukter)
            symboler.append(slot)

        if symboler[0] == symboler[1] == symboler[2]:
            print(symboler, "\t🎉 JACKPOT! 🎉       1 in 64")
            konto += int(bet) * 20
        
        elif symboler[0] == symboler[1] or symboler[1] == symboler[2] or symboler[0] == symboler[2]:
            if symboler[0] == symboler[1] == symboler[2]:
                break
            else:
                print(symboler, "\t+ ", int(bet) * 2, " Kr      1 in 3")
                konto += int(bet) * 2

        else:
            konto -= int(bet)      # drar pengar
            print(symboler)

    elif key == "konto":
        print(str(konto) + str(" kr"))
        
    else:
        print("Ogiltigt val, försök igen.")

exit()
# testar en kommentar i Git
