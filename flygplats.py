# Klasser namnges alltid med inledande stor bokstav.
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
