class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        parties = {"R": "Radiant", "D" : "Dire"}
        enemy = {"R": "D", "D" : "R"}
        senate = list(senate)
        while True:
            turn = senate.pop(0)
            if enemy[turn] in senate:
                #ban one enemy
                senate.remove(enemy[turn])
                #current senator survies
                senate.append(turn)
            else: return parties[turn]