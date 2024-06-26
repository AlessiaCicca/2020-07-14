from dataclasses import dataclass

@dataclass
class Squadra:
    TeamID:int
    Name:str
    tot:int


    def __hash__(self):
        return hash(self.TeamID)

    def __str__(self):
        return f"{self.Name}"