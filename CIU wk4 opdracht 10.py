"""
Woord hussel

Raad een woord, houd punten bij, multiplayer
"""

import random

def kies_woord():
    """
    Kiest een willekeurig woord uit een lijst
    """

    # Maak lijstje met woorden
    woorden = ["bergen", "fietsen", "sinaasappel"]

    # Geef een willekeurig woord uit de lijst terug
    return random.choice(woorden)

def hussel(woord):
    """
    Husselt de lettters van het woord en voeg ze samen tot 1 str
    """

    # Maak variabele met gehusselde letters van woord uit argument
                                # seq.  # lenght of sample, dus heel woord
    hussel_woord = random.sample(woord, len(woord))

    # Voeg de husselletters samen in een str
    return "".join(hussel_woord)

def goed_of_fout(naam, gekozen_woord, score, beurt):
    """
    Controleert of het antwoord goed of fout is en geeft score terug en of speler moet stoppen
    """

    print(f"{naam}, het is jouw beurt!")

    # Vraag om keuze en stop in variabele
    antwoord = input("Wat denk je dat het woord is\t")

    # Als het antwoord goed is
    if antwoord == gekozen_woord:

        # geef een punt
        score += 1

        # print deze score
        print(f"Goed! {naam}, jouw score is {score}.")
    
    # Als het antwoord fout is
    else:

        # print score
        print(f"Helaas, dat is niet goed. {naam} jouw score blijft {score}")

    # en geef beurt (volgende speler) en score terug
    return beurt + 1, score 
    
def speel_spel():
    """
    Houdt scores en puten bij
    """ 

    # Vraag spelers om naam een stop elke in een variabele
    p1_naam = input("Speler 1 wat is jouw naam? \t")
    p2_naam = input("Speler 2 wat is jouw naam? \t")

    # Zet score en beurten op 0 en sla op in variabelen
    p1_score = p2_score = beurt = 0

    # Loop totdat spelers stoppen
    while True:

        # Sla het gekozen woord sla op in een variabele
        gekozen_woord = kies_woord()
        # Hussel het gekozen word en sla op in een variabele
        gehusseld = hussel(gekozen_woord)

        # Print gehusselde woord voor speler
        print(f"Gehusselde woord: {gehusseld}")

        # Als beurt even is, is speler 1 aan de beurt (incl 0 dus)
        if beurt % 2 == 0:
            # geef beurt en score van speler 1 nieuwe waarden aan de hand van de goed_of_fout() functie
            beurt, p1_score = goed_of_fout(p1_naam, gekozen_woord, p1_score, beurt)

        # Als beurt even is, is speler 2 aan de beurt (incl 1)
        else:
            # geef beurt en score van speler 2 nieuwe waarden aan de hand van de goed_of_fout() functie
            beurt, p2_score = goed_of_fout(p2_naam, gekozen_woord, p2_score, beurt)

            # Vraag na speler 2 of het spel verder gaat
            doorgaan = input("Wil je doorgaan? ja/nee\t")

            # Als het spel niet doorgaat
            if doorgaan == "nee":
                # print dit
                print("Einde spel!")
                # en stop de loop
                break

# Roep het spel aan
speel_spel()