# Objektorientering i Python

## Innehåll

- [Objekt, en tillbakablick](#Objekt-en-tillbakablick-på-ett-känt-exempel)

- [En egen klass](#En-egen-klass)

- [Övningar till klassen `Airplane`](#Övningar-till-klassen-Airplane)

- [Fler övningar - En ny klass](#Fler-övningar---En-ny-klass)

## Objekt, en tillbakablick på ett känt exempel

När du har arbetetat med `Turtle`-biblioteket så har du skapat en eller flera sköldpaddor genom att deklarera

```Python
a_turtle = Turtle()
b_turtle = Turtle()
```

Därefter kunde du bestämma vad sköldpaddan ska göra, t ex

```Python
a_turtle.forward(100) # Gå fram 100 steg
a_turtle.left(30)     # Sväng vänster 30°
```

Du upptäckte säkert också att det gick att ge sköldpaddan vissa egenskaper, t ex

```Python
a_turtle.color('blue') # Gör sköldpaddan blå
a_turtle.speed(10)     # Sätt dess hastighet till 10
```

Sköldpaddan känner också till sitt läge på skärmen, det kan man få fram genom

```Python
a_turtle.xcor() # ger x-koordinaten
a_turtle.ycor() # ger y-koordinaten
```

Alla dessa "kommandon" måste på något sätt definieras, och det görs i **klassen** `Turtle`.

Du ska nu inte gå igenom `Turtle`-klassen, utan jag ska istället visa hur en enklare klass kan skapas och användas.

## En egen klass

Vi ska börja med att skapa klassen `Airplane`. Den kommer att hålla reda på flygplansmodell, vingbredd och passagerarkapacitet. När vi har skapat klassen `Airplane` kommer vi att kunna deklarera **objekt** av den enligt

```Python
a_plane = Airplane("Boeing 747", 30, 200) # Deklarerar en Boeing med vingbredden 30m som kan ta 200 passagerare

print(a_plane.model)                     # Skriver ut modellen
a_plane.model = "Airbus 380"               # Anger modellen
print(a_plane.model)
```

För att implementera detta skapas klassen enligt nedan (denna klass finns i filen `flygplats.py`):

```Python
class Airplane():
    '''
    En klass som håller reda på några egenskaper hos ett flygplan.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, model, wingspan, capacity):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Airplane har egna värden på dessa.
        self.model = model
        self.wingspan = wingspan
        self.capacity = capacity

    def print_info(self):
        '''
        Skriver ut information om ett flygplan (en instans av klassen Airplane).
        '''
        print(
            f"{self.model}. Wingspan: {self.wingspan}. Capacity: {self.capacity}")

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_plane = Airplane("Boeing 747", 64.6, 500)
a_plane.model = 'Airbus 380'
a_plane.print_info()
```

## Övningar till klassen `Airplane`

Nedan finns ett antal uppgifter till klassen ovan. Det kan nog ta lite olika lång tid för olika personer att göra övningarna. I samband med varje lektion är huvudregeln att du ska synkronisera "repon" (projektet på ditt konto på GitHub). På så sätt kommer kodningshistoriken att bli synlig och din process går att följa.

1. Gör en `Fork` av detta projekt till ditt GitHub-konto.
2. Klona projektet från ditt GitHub-konto till lämplig plats på din dator.
3. Öppna filen `flygplats.py` i VS Code och kör programmet. Försök att förklara varför utskriften blir som den blir.
4. Skapa ett objekt `b_plane` och initiera detta med valfri modell, vingbredd och kapacitet.
5. Tillämpa metoden `print_info()` både på `a_plane` och `b_plane`. Resultat?
6. Skapa en ny metod inne i klassen, `set_wingspan(self, new_wingspan)`. Denna metod ska ändra på attributet `wingspan`.
7. För att kunna testa om `set_wingspan(self, new_wingspan)` så kan du direkt komma åt **attributet** `wingspan` genom t ex `print(a_plane.wingspan)` (någonstans i huvudprogrammet) . Observera att du alltså skriver ut en variabel, och inte anropar en metod, på det sättet. Prova att anropa `set_wingspan` på `a_plane` och för att sätta om `wingspan` och skriv sedan ut det nya värdet på attributet `wingspan`.
8. Skapa även metoden `set_capacity(self, new_capacity)`. Testa att den fungerar.
9. Skapa ytterligare en metod, `get_capacity(self)`. Den metoden ska inte skriva ut kapaciteten, utan den ska istället **returnera** kapaciteten. Anropet kan ske genom `the_capacity = a_plane.get_capacity()` (i huvudprogrammet). Därefter kan kapaciteten skrivas ut.
10. Skapa objekten `c_plane`, och `d_plane` med lämpliga modeller, vingbredder och passagerarkapacitet. Nu kan du lägga in alla dina flygplan (fyra stycken bör det vara) i en lista, `planes`. [Här finns presentationen om listor](https://slides.com/nikodemus/listor/fullscreen?token=bPF0RWd0#/3).
11. Loopa genom listan (se ovanstående presentation) för att skriva ut alla flygplan som finns i programmet.
12. **Om du hinner**: Gör en meny som kan skriva ut listan med objektens samtliga attribut sorterad i bokstavsordning / vingbredd eller kapacitet, beroende på vilket menyval som görs.

## Fler övningar - En ny klass

Skapa en klass `Player` där en spelare samlar poäng genom att "skjuta". Varje gång som spelare själv "skjuter" så kommer den också att bli beskjuten. Slumpen avgör såväl om spelaren träffar eller blir träffad. Om spelaren träffar så ökas poängen, men varje gång den blir träffad så minskar antalet liv med ett. Ett kodskelett för klassen med några metoder skulle kunna se ut så här (detta kodskelett finns i filen `pang-pang.py`):

```python
class Player(object):
   def __init__(self, lifes):
      self.lifes = self.lifes
      self.scores = 0
      self.did_hit = False
      self.is_hitted = False

   def fire(self):
      # Här sker "eldväxlingen"

   def inc_scores(self):
      # Här ska poängen öka

   def reduce_lifes(self):
      # Här ska antalet liv minska

a_player = Player(3)       # Initiera en spelare med tre liv
a_player.fire()            # Spelaren skjuter
```

Själva "eldgivningen" kan hanteras genom att trycka på \<Enter> i en `input()`-sats (i huvudprogrammet, alltså utanför klassen), t ex

```python
while True:
    input('Tryck Enter för att skjuta')
    a_player.fire()
    if a_player.did_hit:
       print('Träff!')
       a_player.inc_scores() # Antalet poäng ökas med 1
    else:
       print('Miss, sikta bättre')
    if a_player.is_hitted:
       print('Aaaaaah')
       a_player.reduce_lifes() # Antalet liv minskas med 1
    else:
       print('Du klarade dig denna gång!')
       print(a_player.scores)
       print(a_player.lifes)
    if a_player.lifes <= 0:
       break
```

Slumpen i träff kan hanteras på följande sätt i metoden `fire()` (istället för att "printa" så ska metoden ändra på attributen `did_hit` och `is_hitted`).

```python
from random import randint # Ska deklareras överst i filen, utanför klassen
sikta = randint(1, 5) # Slumpat heltal mellan 1 och 5
if sikta in {1, 2, 3}: # 60 % sannolikhet att sikta rätt / träffa
   print('Du träffade!')
else:
   print('Du missade!')
# Sedan får du försöka lista ut hur man kan implementera
# att spelaren blir beskjuten.
```

Programmet kan givetvis utvecklas med mer funktionalitet, fler spelare och egenskaper (t ex högre träffsäkerhet eller mindre risk att bli träffad) som vinns efter genomförda uppdrag.
