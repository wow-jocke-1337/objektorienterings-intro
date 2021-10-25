# En klass beskriver ett objekt med egenskaper (attribut och metoder).
class Klassen:
    # __init__ är en specialmetod som körs för att skapa instanser av klassen.
    def __init__(self, varde1: str, varde2: int):
        '''
        Inparametern self är en instans av klassen (ett objekt) som python redan skapat.
        Det kan man nu initiera, alltså skapa attribut m.m.
        __init__ kan ta emot ytterligare inparametrar som man sedan skickar in 
        värden på när man skapar en instans.
        '''
        self.attribut1 = varde1
        self.attribut2 = varde2

    def detta_ar_en_metod(self):
        '''
        En metod är en funktion som verkar på en instans av en klass. 
        Inparametern self är den aktuella instansen som metoden anropas på.
        self anges inte i anropet av metoden utan "stoppas in" automatiskt av Python.
        '''
        print(self.__dict__)  # __dict__ är en så kallad dictionary, med alla objektets attribut (och dess värden)

    def en_metod_med_inparameter(self, parameter):
        # self är en referens till den aktuella instansen (objektet)
        # parameter är inparametern som kommer innehålla värdet från argumentet
        print(self.attribut1, parameter)


# Vi kan skapa hur många objekt (instanser av klassen) vi vill.
k = Klassen("hej", 10000)

# Så här anropar vi en metod utan inparameter
k.detta_ar_en_metod()

# Så här anropar vi en metod med inparameter
k.en_metod_med_inparameter("värdet på en parameter")
