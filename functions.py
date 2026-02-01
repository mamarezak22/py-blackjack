import time

from cards import Card,get_cards
from random import shuffle

def shuffle_cards(cards : list[Card]) -> list[Card]:
    return shuffle(cards)

def deal_card(cards : list[Card]):
    return cards.pop()

def caculate_point(cards : list[Card]):
    return sum(cards.point)

#and user_points and ai points
def exe_round() -> tuple[int,int]:
    cards = get_cards()
    done = False
    i = 1
    user_points = 0
    ai_points = 0

    while not done and user_points < 21:
        card = deal_card(cards)
        user_points += card.point
        print(f"🃏 Card {i}: {card}", end="", flush=True)
        time.sleep(0.6)
        print(f"  → Total: {user_points}")

        # print(f"🃏 Card {i}: {card}  → Total: {user_points}")

        i += 1
        input_ = input("more ? [y/n]")
        if input_.lower() == "n":
            done = True
    
    if done:
        print(f"your point {user_points}")
    
    elif user_points == 21:
        print("congratulations . you reach 21...")
    
    elif user_points > 21:
        print("sorry to say that but you reach more than 21 and lose that round.")
    
    ai_done = False
    while not ai_done:
        card = deal_card(cards)
        ai_points += card.point
        if ai_points >= 17:
            ai_done = True

    print("\n" + "=" * 30)
    print("🃏 ROUND RESULT")
    print(f"🧑 Your points : {user_points}")
    print(f"🤖 AI points   : {ai_points}")
    print("=" * 30)

    return winner_state(user_points,ai_points)

#if based on the points user is winner. it return 0.
#if ai it return 1.
def winner_state(user_points,
                ai_points):
    if user_points == 21 and ai_points != 21:
        return 0
    elif ai_points == 21 and user_points != 21:
        return 1
    elif user_points < 21 and ai_points < 21:
        if user_points < ai_points:
            return 1
        else:
            return 0
    
    elif user_points > 21 and ai_points < 21:
        return 1

    elif user_points < 21 and ai_points > 21:
        return 0 

def print_final_text(user_points , ai_points):
    print("\n" + "=" * 40)
    print("FINAL SCORE")
    print("=" * 40)
    print(f"🧑 You : {user_points} points")
    print(f"🤖 AI  : {ai_points} points")

