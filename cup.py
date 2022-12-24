class Cup:
    def __init__(self, teams):
        self.teams = teams
        self.matches = []
        for i in range(0, len(teams) // 2):
            self.matches.append((teams[i], teams[i + len(teams) // 2]))
    

    def play(self, results):
        for i in range(len(self.matches)):
            if results[i][0] > results[i][1]:
                self.teams.remove(self.matches[i][1])
            else:
                self.teams.remove(self.matches[i][0])


        #reset matches
        self.matches = []
        for i in range(0, len(self.teams), 2):
            self.matches.append((self.teams[i], self.teams[i + 1]))

    def winner(self):
        return self.teams[0]