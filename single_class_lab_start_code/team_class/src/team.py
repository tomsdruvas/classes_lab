class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)
    
    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False



    def play_game(self, boolean):
        if boolean:
            self.points += 3