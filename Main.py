import random
from card import Card
import sys, pygame 

#if chris == sexy
    #print("Heyyyyyy shawty")


#deck: list[Card]
p1: list[Card] = []
p2: list[Card] = []
p3: list[Card] = []
p4: list[Card] = []

def main():
    players: int = int(input("How many players do you have (1-4)?"))
    while players > 4 or players < 1:
        players = int(input("How many players do you have (1-4)?"))
    
    for player in range(0,players):
        for number in range(1,7):
            if player == 0:
                p1.append(Card.generate_card)
            elif player == 1:
                p2.append(Card.generate_card)
            elif player == 2:
                p3.append(Card.generate_card)
            elif player == 3:
                p4.append(Card.generate_card)
    
    print("Player 1's turn:")
    # print(p1)
    print(p1[0])

# def draw(player: list[Card]) -> list[Card]:
#     new_card: Card = 
#     player.append

if __name__ == '__main__':
    main()
