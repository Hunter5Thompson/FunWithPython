from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
# Erstelle eine leere Liste, um die Bieter-Einträge zu speichern
bids = []

while True:
    # Frage den Benutzer nach dem Namen und dem Gebot
    name = input("Wie ist dein Name? ")
    bid = float(input("Wie viel bietest du? $"))

    # Füge das Gebot als Key-Value-Paar zum Biet-Dictionary hinzu
    bid_dict = {"Name": name, "Bid": bid}
    bids.append(bid_dict)

    # Frage den Benutzer, ob noch jemand bieten möchte
    more_bids = input("Gibt es noch weitere Gebote? Ja oder Nein: ").lower()
    if more_bids == "ja":
      clear()

    # Wenn niemand mehr bieten möchte, beende die Schleife
    else:
      clear()
      break

# Finde den Gewinner (die Person mit dem höchsten Gebot)
winner = max(bids, key=lambda x: x["Bid"])


# Gib den Gewinner aus
print(f"Der Gewinner ist {winner['Name']} mit einem Gebot von ${winner['Bid']:.2f}.")