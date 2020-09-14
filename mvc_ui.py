from model import Model
from view import View
from controller import Controller

elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "viin", "hind":5.60, "kogus": 5},
]
# testimine
# loome uus andmestik
pood = Controller(Model(elemendid), View())
# kõikide elementide kuvamine
pood.kuva_elemendid()
# konkreetse elemendi kuvamine
pood.kuva_element("piim")
# elemendi lisamine
pood.lisa_element("tort", 0.60, 15)
print("lisa veel üks kohuke")
pood.lisa_element("kohuke", 0.60, 15)
pood.kuva_element("kohuke")
# loeme elemendi mis ei eksisteeri
pood.kuva_element("küpsis")
# elemendi uuendamine
pood.uuenda_element("viin", 10.0, 10)
# elemendi kustutamine
pood.kuva_elemendid()
pood.kustuta_element("viin")
pood.kuva_elemendid()