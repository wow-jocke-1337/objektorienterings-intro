# En klass beskriver ett objekt med egenskaper (attribut och metoder).
class Klassen:
    klassattribut = "Ett attribut alla instanser av klassen har."

    # __init__ är en specialmetod som körs för att skapa instanser av klassen.
    def __init__(self):
        '''
        Inparametern self är en instans av klassen (ett objekt) som python redan skapat.
        Det kan man nu initiera, alltså skapa attribut m.m.
        '''
        self.attribut1 = ""
        self.attribut2 = 0

    def detta_ar_en_metod(self):
        '''
        En metod är en funktion som verkar på en instans av en klass. 
        Inparametern self är den aktuella instansen som metoden anropas på.
        self anges inte i anropet av metoden utan "stoppas in" automatiskt av Python.
        '''
        print(self.__dict__)  # __dict__ är en så kallad dictionary, med alla objektets attribut (och dess värden)


# Vi kan skapa hur många objekt (instanser av klassen) vi vill.
k = Klassen()
k2 = Klassen()

print(k.attribut1)
print(k.attribut2)
print(k.klassattribut)
print("-"*10)

# Vi kan sätta om värdena på attributen.
k.attribut1 = "Hej"
k.attribut2 = 10000
k.klassattribut = "även klassattribut kan ändras på en instans"

print(k.attribut1)
print(k.attribut2)
print(k.klassattribut)
print("-"*10)

# att ändra atttibut på en insans av en klass påverkar inte andra
# instanser av samma klass
print(k2.attribut1)
print(k2.attribut2)
print(k2.klassattribut)
print("-"*10)

# Vi kan anropa metoder på våra instanser.
k.detta_ar_en_metod()
k2.detta_ar_en_metod()
