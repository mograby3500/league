class Group:
    def __init__(self, teams):
        self.teams = teams
        self.matches = []
        self.points = {}
        for team in teams:
            self.points[team] = 0
    
        for i in range(0, len(teams)):
            for j in range(i+1, len(teams)):
                self.matches.append((teams[i], teams[j]))

    
    def play(self, match, result):
        self.points[match[0]] += result[0]
        self.points[match[1]] += result[1]
    
    def top(self):      
        return sorted(self.points.items(), key=lambda x: x[1], reverse=True)[:2]


    
