from models.myclasses import Producer
from models.myclasses import Wine
from models.myclasses import WineList

Prod1 = Producer("Famille Perrin", "France")
Prod2 = Producer("Thierry & Guy", "France")
Prod3 = Producer("Gabriel Meffre", "France")

wineList = WineList()

WineA = Wine("La Vieille Ferme Rouge")
WineA.setVintage("2017")
WineA.setPrice("470.00")
WineA.setProducer(Prod1)

WineB = Wine("Fat Bastard Pinot Noir")
WineB.setVintage("2016")
WineB.setPrice("650.00")
WineB.setProducer(Prod2)

WineC = Wine("Fat Bastard Cabernet Sauvignon")
WineC.setVintage("2016")
WineC.setPrice("650.00")
WineC.setProducer(Prod2)

WineD = Wine("Laurus Viognier")
WineD.setVintage("2015")
WineD.setPrice("780.00")
WineD.setProducer(Prod3)

WineE = Wine("Laurus Viognier")
WineE.setVintage("2017")
WineE.setPrice("780.00")
WineE.setProducer(Prod3)

wineList.addWine(WineA)
wineList.addWine(WineB)
wineList.addWine(WineC)
wineList.addWine(WineD)
wineList.addWine(WineE)
wineList.getWines()

print("-----------")
wineList.checkWine("Fat Bastard Pinot Noir", "2016")
wineList.checkWine("Fat Bastard Pinot Noir", "2017")
wineList.checkWine("Fat Bastard Merlot", "2016")
wineList.getWines()

print("-----------")
wineList.removeWine("Laurus Viognier", "2018")
wineList.removeWine("Laurus Viognier", "2017")
wineList.removeWine("La Vieille Ferme Blanc", "2017")
wineList.getWines()
