import random
from turtle import clear

from art import logo


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)


def compare(user, computer):
    if user == computer:
        return "Draw."
    elif computer == 0:
        return "Lose, opponent has Blackjack."
    elif user == 0:
        return "You win with a Blackjack."
    elif user > 21:
        return "You went over. You lose."
    elif computer > 21:
        return "The computer went over. You win."
    elif computer > user:
        return "You lose."
    elif user > computer:
        return "You win"


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def game():
    global user_score, computer_score
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        new_card1 = deal_card()
        computer_cards.append(new_card1)

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = str(input("Type 'y' to get another card, type 'n' to pass: "))
            if draw_card == 'y':
                user_cards.append(deal_card())
                computer_cards.append(deal_card())
            else:
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                is_game_over = True
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))
    question = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
    if question == 'y':
        game()


question = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
if question == 'y':
    clear()
    game()
