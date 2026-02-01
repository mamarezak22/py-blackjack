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
    print("now the round starts.")

    while not done and user_points < 21:
        card = deal_card(cards)
        user_points += card.point
        print(f"{i} card : {card}")
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

    print("this round points : ") 
    print(f"you : {user_points}")
    print(f"ai : {ai_points}")
 
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
    if user_points > ai_points:
        print("you're the winner baby.")
        print(f"you won {user_points}-{ai_points}")
    
    elif user_points < ai_points :
        print("sorry for your loss to a bloody computer.")
        print(f"you lose {ai_points}-{user_points}")
    
    else:
        print("you draw. not bad . not good either.")
        print(f"you draw by {ai_points}-{user_points}")

