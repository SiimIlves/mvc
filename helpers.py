elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        raise exceptions.ElementJubaOlemas("Element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})

# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

# loeme ELEMENDID korraga
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid

# loeme KONKREETNE element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei eksisteeri".format(nimetus)
    else:
       return elemendid[nimetused.index(nimetus)]

# uuendame KONKREETSET elementi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei saa uuendada, kuna ta ei eksisteeri".format(nimetus)
    else:
        elemendid[nimetused.index(nimetus)] = {"nimetus":nimetus, "hind":hind, "kogus":kogus}

# kustutame KONKREETSET elementi
def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei saa kustutada, kuna ta ei eksisteeri".format(nimetus)
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])

# kustutame KÕIK
def kustuta_elemendid():
    global elemendid
    elemendid.clear()

def main():
    # loome katseandmestiku
    katse_elemendid = [
        {"nimetus": "leib", "hind":0.80, "kogus": 20},
        {"nimetus": "piim", "hind":0.50, "kogus": 15},
        {"nimetus": "viin", "hind":5.60, "kogus": 5},
    ]

    # testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    # testime üksiku elemendi lisamist
    lisa_element("kohupiim", 0.90, 15)
    lisa_element("viin", 5.60, 5)

    # testime elementide lugemist
    print(loe_element("viin"))
    print(loe_element("limonaad"))

    #testime elemendi uuendamist
    uuenda_element("viin", 10.0, 10)
    print(loe_element("viin"))

    # testime elemendi uuendamist
    kustuta_element("viin")
    print(loe_element("viin"))

    # testime kõige kustutamist
    kustuta_elemendid()
    print(loe_elemendid())

# käivitame
if __name__ == "__main__":
    main()