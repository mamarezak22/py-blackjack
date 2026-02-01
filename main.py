from functions import exe_round ,print_final_text

def main():
    user_points = 0
    ai_points = 0
    done = False
    while not done:
        winner = exe_round()
        if winner == 0:
            user_points += 1
        else:
            ai_points += 1

        print("\n" + "-" * 30)
        print("🏁 SCOREBOARD")
        print(f"🧑 You : {user_points} rounds")
        print(f"🤖 AI  : {ai_points} rounds")
        print("-" * 30 + "\n") 

        input_ = input("You Want Play Another Round? [y/n]")

        if input_.lower() == "n":
            done = True

    print_final_text(user_points,ai_points)

main()