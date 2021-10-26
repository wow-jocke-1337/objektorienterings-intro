class Player():
    def __init__(self, lifes):
        self.lifes = lifes
        self.scores = 0
        self.did_hit = False
        self.is_hitted = False

    def fire(self):
        pass
       # Här sker "eldväxlingen"

    def inc_scores(self):
        pass
       # Här ska poängen öka

    def reduce_lifes(self):
        pass
        # Här ska antalet liv minska


a_player = Player(3)       # Initiera en spelare med tre liv
a_player.fire()            # Spelaren skjuter
