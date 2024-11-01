import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():
    print("\n" * 100)
    print(logo)

    # Dealing both user and computer a starting hand of 2 random card values
    user_starting_hand = random.sample(cards, 2)
    computer_starting_hand = random.sample(cards, 2)
    blackjack = [11, 10]

    # Checking if user or computer has blackjack cards
    user_blackjack = sorted(user_starting_hand) == sorted(blackjack)
    computer_blackjack = sorted(computer_starting_hand) == sorted(blackjack)
    user_sum = sum(user_starting_hand)
    computer_sum = sum(computer_starting_hand)

    #defining function to check for blackjack
    def check_blackjack():
        if user_blackjack  and not computer_blackjack:
            print(f"Your cards: {user_starting_hand}, current score: 0")
            print(f"Computer's first card: {computer_starting_hand[0]}")
            print(f"Your final hand: {user_starting_hand}, final score: 0")
            print(f"Computer's final hand: {computer_starting_hand[0]}, final score: {computer_sum}")
            print("You win with a Blackjack 😎")
            return True


        elif user_blackjack and computer_blackjack:
            print(f"Your cards: {user_starting_hand}, current score: {user_sum}")
            print(f"Computer's first card: {computer_starting_hand[0]}")
            print(f"Your final hand: {user_starting_hand}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_starting_hand}, final score: 0")
            print("Opponent won with a Blackjack 😱 ")
            return True

        elif not user_blackjack and computer_blackjack:
            print(f"Your cards: {user_starting_hand}, current score: {user_sum}")
            print(f"Computer's first card: {computer_starting_hand[0]}")
            print(f"Your final hand: {user_starting_hand}, final score: {user_sum}")
            print(f"Computer's final hand: {computer_starting_hand}, final score: 0")
            print("Opponent won with a Blackjack 😱 ")
            return True

        else:
            print(f"Your cards: {user_starting_hand}, current score: {user_sum}")
            print(f"Computer's first card: {computer_starting_hand[0]}")
            return False

    #When there's no blackjack at the beginning of the dealership
    if check_blackjack():
        return #Exits game if there's an initial Blackjack

    #define final print function
    def final_print():
        print(f"Your final hand: {user_starting_hand}, final score: {sum(user_starting_hand)}")
        print(f"Computer's final hand: {computer_starting_hand}, final score: {sum(computer_starting_hand)}")

    #prompt to continue or pass
    while True:
        continue_blackjack = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        max_card_sum = 21
        ace = 11

        if continue_blackjack == "y":
            add_card = random.choice(cards)
            user_starting_hand.append(add_card)
            user_sum = sum(user_starting_hand)
            print(f"Your cards: {user_starting_hand}, current score: {user_sum}")
            print(f"Computer's first card: {computer_starting_hand[0]}")

            #handle if user goes over max sum
            if user_sum > max_card_sum:
                if ace in user_starting_hand:
                    #replace ace card value '11' with '1' and recalculate
                    user_starting_hand[user_starting_hand.index(ace)] = 1
                    user_sum = sum(user_starting_hand)

                if user_sum > max_card_sum: #check again after ace adjustment
                    final_print()
                    print("You Lose 😨")
                    return

        elif continue_blackjack == "n":

            #computer's turn to take cards if their total is less than 17
            while sum(computer_starting_hand) < 17:
                add_card = random.choice(cards)
                computer_starting_hand.append(add_card)
            computer_sum = sum(computer_starting_hand)

            if computer_sum > max_card_sum:
                final_print()
                print("You Win 😁")

            elif computer_sum > user_sum:
                final_print()
                print("You Lose 😩")

            elif computer_sum < user_sum:
                final_print()
                print("You Win 🤩")

            else:
                final_print()
                print("You Draw")
            return

def choice_play_main():
    should_continue = True
    while should_continue:
        choice_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if choice_play == "y":
            play_blackjack()
        elif choice_play == "n":
            print("We are sad to see you go 😊, play with us next time\nBye!! 👋")
            should_continue = False


choice_play_main()






