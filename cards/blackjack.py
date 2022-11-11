#create an interactive blackjack game
import random

#create a deck of cards
deck = []
sign = ["Hearts", "Diamonds", "Spades", "Clubs"]
#create numbers 2-10
for i in range(2,11):
    for j in sign:
        deck.append(str(i) + " of " + j)
#create face cards
for i in sign:
    deck.append("Jack of " + i)
    deck.append("Queen of " + i)
    deck.append("King of " + i)
    deck.append("Ace of " + i)
#choose how many players are playing with user input
num_players = int(input("How many players are playing? "))
#create a list of players and their balances (100$ each)
players = []
for i in range(1, num_players + 1):
    players.append("Player " + str(i))
balances = []
for i in range(1, num_players + 1):
    balances.append(100)
#link the players and their balances
player_and_balance = dict(zip(players, balances))
#shuffle the deck
random.shuffle(deck)
#new round
new_round = "yes"
while new_round == "yes":
    #entry bet (10$)
    bet = 10
    #bets on the table
    bets_on_table = []
    for i in range(1, num_players + 1):
        bets_on_table.append(bet)
    #deal the cards
    player_and_cards = {}
    for i in players:
        player_and_cards[i] = []
    for i in range(2):
        for j in players:
            player_and_cards[j].append(deck.pop())
    dealer_cards = []
    for i in range(2):
        dealer_cards.append(deck.pop())
    #show the dealer's cards
    print("The dealer's cards are: " + str(dealer_cards))
    #turn by turn, ask the players if they want to hit or stand
    for i in players:
        print("It is " + i + "'s turn.")
        print("Your cards are: " + str(player_and_cards[i]))
        print("your balance is: " + str(player_and_balance[i]))
        print("your bet amount is: " + str(bet))
        wanna_raise = input("Do you want to raise your bet? ")
        while wanna_raise == "yes":
            #input the raised amount (min 2$)
            raising_by = 2
            raising_by = int(input("How much do you want to raise by?"))
            if raising_by < 2:
                wanna_raise = input("You must raise by at least 2$. still wanna raise? ")
                if wanna_raise == "no":
                    break
                raising_by = int(input("How much do you want to raise by? "))
                #add the raised amount to the bet
            bet += raising_by
            break
        while wanna_raise == "no":
            break
        hit_or_stand = input("Do you want to hit or stand? ")
        while hit_or_stand == "hit":
            player_and_cards[i].append(deck.pop())
            print("Your cards are: " + str(player_and_cards[i]))
            print("your bet amount is: " + str(bet))
            hit_or_stand = input("Do you want to hit or stand? ")
        while hit_or_stand == "stand":
            break
    #dealer's turn
    print("It is the dealer's turn.")
    #sum the dealer's cards
    dealer_cards_sum = 0
    for i in dealer_cards:
        if i[0] == "A":
            dealer_cards_sum += 11
        elif i[0] == "J" or i[0] == "Q" or i[0] == "K":
            dealer_cards_sum += 10
        else:
            dealer_cards_sum += int(i[0])
    #dealer hits if the sum is less than 17
    while dealer_cards_sum < 17:
        dealer_cards.append(deck.pop())
        #show the dealer's cards
        print("The dealer's cards are: " + str(dealer_cards))
        #resum the player's cards
        dealer_cards_sum = 0
        for i in dealer_cards:
            if i[0] == "A":
                dealer_cards_sum += 11
            elif i[0] == "J" or i[0] == "Q" or i[0] == "K":
                dealer_cards_sum += 10
            else:
                dealer_cards_sum += int(i[0])
    while dealer_cards_sum >= 17:
        break
    #turn by turn, did the player win or lose?
    for i in players:
        #sum the player's cards
        player_cards_sum = 0
        for j in player_and_cards[i]:
            if j[0] == "A":
                player_cards_sum += 11
            elif j[0] == "J" or j[0] == "Q" or j[0] == "K":
                player_cards_sum += 10
            else:
                player_cards_sum += int(j[0])
        print("the sum of your cards is: " + str(player_cards_sum))
        print("the sum of the dealer's cards is: " + str(dealer_cards_sum))
        #if the player's sum is less than 21, compare the sum to the dealer's sum
        if player_cards_sum < 21:
            if player_cards_sum > dealer_cards_sum:
                print(i + " won!")
                #add the bet to the player's balance
                player_and_balance[i] += bet
            elif player_cards_sum < dealer_cards_sum:
                print(i + " lost!")
                #subtract the bet from the player's balance
                player_and_balance[i] -= bet
            else:
                print(i + " tied!")
        #if the player's sum is 21, they win
        elif player_cards_sum == 21:
            print(i + " won!")
            #add the bet to the player's balance
            player_and_balance[i] += bet
        #if the player's sum is greater than 21, they lose
        else:
            print(i + " lost!")
            #subtract the bet from the player's balance
            player_and_balance[i] -= bet
        print("Your balance is: " + str(player_and_balance[i]))
    new_round = input("Do you want to play another round? ")
