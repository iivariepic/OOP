# Määritellään lista nimillä
def main():
    jono = ["Matti", "Riikka", "Antti",
            "Jenni", "Anu", "Ville", "Jarno"]

    # Jonon ensimmäinen poistuu maksettuaan ostoksensa.
    jono.pop(0)

    # Ville värvää Annin jonottamaan puolestaan
    ville_index = jono.index("Ville")
    jono[ville_index] = "Anni"

    # Jarno poistuu väsyttyään ainaiseen odottamiseen
    jono.remove("Jarno")

    # Marjo liittyy jonon päähän.
    jono.append("Marjo")

    # Herrasmiehenä Antti päästää kaksi jäljessään olevaa henkilöä eteensä
    antti_index = jono.index("Antti")
    jono.insert(antti_index + 3, "Antti")
    jono.pop(antti_index)

    if "Jenni" in jono:
        print("Jenni on jonossa")
    else: print("Jenni ei ole jonossa")
    print(f"Kolmanneksi viimeinen on {jono[-3]}")


if __name__ == "__main__":
    main()