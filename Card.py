from __future__ import annotations
import random

class Card:
    color: str
    number: int

    def __init__(self, color: str, number: int) -> None:
        self.color = color
        self.number = number

    def generate_color(self) -> str:
        value: int = random.randint(0,3)
        if value == 0:
            return "red"
        if value == 1:
            return "yellow"
        if value == 2:
            return "green"
        if value == 3:
            return "blue"
        
    def generate_card(self) -> Card:
        new_card = Card(Card.generate_color(),random.randint(0,9))
        return new_card
    
    def __str__(self):
        return self.color
    
