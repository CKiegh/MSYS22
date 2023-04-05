class Producer: #forces user to indicate name and country
    def __init__(self, producer_name, producer_country):
        self.nameProducer = producer_name
        self.countryProducer = producer_country

    def getCountry(self): #returns the country of the producer from the __init__
        return self.countryProducer

    def getName(self): #returns the name of the producer from the __init__
        return self.nameProducer

    def __str__(self): #prints the name and country of the producer (the object)
        # return f"{self.getName}, {self.getCountry}"
        return f"{self.nameProducer}, {self.countryProducer}"

class Wine: 
    def __init__(self, wine_name): #Asks fo the wine_name right when calling the class.
        #might change this to a list
        #might add another list, and each function appends it to the list.
        self.wineName = wine_name
        self.wineVintage = 0 
        self.winePrice = 0
        self.wineProducer = "Unknown Producer"

    def setVintage(self, wine_vintage): #changes the value of self.wineVintage
        self.wineVintage = wine_vintage

    def setPrice(self, wine_price): #changes the value of self.winePrice
        self.winePrice = wine_price
    
    def setProducer(self, producer_name): 
        #changes the value of self.wineProducer, if none indicated, "Unknown Producer" will be returned
        self.wineProducer = producer_name

    def getName(self): #returns the name of the wine
        return self.wineName

    def getVintage(self): #returns the vintage of the wine
        return self.wineVintage

    def getPrice(self): #returns the price of the wine
        return self.winePrice

    def getProducer(self): #returns the name of the producer of the wine
        return self.wineProducer

    def __str__(self): 
        return f"{self.wineName}, {self.wineVintage}. {self.wineProducer}, {self.winePrice}"

class WineList:
    def __init__(self): #initialize lists that will be used here
        self.wineList = [] #the lists of all wine list


    def addWine(self, wine): #add/append the wine object(might be the whole list) to the list, 
        # and then resets the value (?)
        self.wineList.append(str(wine))

    def getWines(self): #returns (print?) the list containing all the wines
        # might need to use for loop here to print all the items in the list
        for x in self.wineList:
            print(x)
    
    def checkWine(self, wine_name, wine_vintage): 
        #requires user to input wine name and vintage and checks if it is on the list or not
        #IF and ELSE
        #if it's on the list, return the actual wine object
        #if not, return "false"
        YesNo = 0 #yes = 1, no = 0

        wine_name_vintage = f"{wine_name}, {wine_vintage}"
        for x in self.wineList:
            if wine_name_vintage in x:
                print(x)
                YesNo = 1
                return
            else:
                YesNo = 0
        if YesNo == 0:
            print("False")
        else:
            return

    def removeWine(self, wine_name, wine_vintage):
        #requires user to input wine name and vintage
        #IF and ELSE
        #if successfully removed... returns a string containing all the details about the wine + "has been removed".
        #if not successfully removed... returns "Wine does not exist."
        YesNo = 0 #yes = 1, no = 0
        wine_name_vintage = f"{wine_name}, {wine_vintage}"

        for x in self.wineList:
            if wine_name_vintage in x:
                print(f"{x} has been removed.")
                self.wineList.remove(x)
                YesNo = 1
                return
            else:
                YesNo = 0
        if YesNo == 0:
            print("Wine does not exist.")
        else:
            return