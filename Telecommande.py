while True:
    choix = int(input("Entrez le numéro d'une chaîne de télévision : "))

    match choix:
        case 0:
            print("Mosaïque")
        case 1:
            print("TF1")
        case 2:
            print("France 2")
        case 3:
            print("France 3")
        case 4:
            print("Canal +")
        case 5:
            print("France 5")
        case 6:
            print("M6")
        case 7:
            print("Arte")
        case 8:
            print("C8")
        case 9:
            print("W9")
        case 10:
            print("TMC")
        case 11:
            print("TFX")
        case 12:
            print("NRJ 12")
        case 13:
            print("LCP")
        case 14:
            print("France 4")
        case 15:
            print("BFM TV")
        case 16:
            print("CNEWS")
        case 17:
            print("CStar")
        case 18:
            print("Gulli")
        case 20:
            print("TF1 Séries Films")
        case 21:
            print("La chaîne l'Équipe")
        case 22:
            print("6ter")
        case 23:
            print("RMC Story")
        case 24:
            print("RMC Découverte")
        case 25:
            print("Chérie 25")
        case 26:
            print("LCI")
        case 27:
            print("France Info")
        case 41:
            print("Paris Première")
        case 42:
            print("Canal+ Sport")
        case 43:
            print("Canal+ Cinema(s)")
        case 45:
            print("Planète+")
        case 52:
            print("France 2 UHD")
        case _:
            print("Votre numéro que vous venez de taper ne correspond à aucune chaîne")
