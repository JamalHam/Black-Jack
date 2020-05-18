import random

cardTypes = ['Heart', 'Spade', 'Club', 'Diamond']
cardNums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
bjack = True

class Card():
    def __init__(self, Suit, Rank, Value):
        self.Suit = Suit
        self.Rank = Rank
        self.Value = Value

    def name(self):
       return self.Rank + ' of ' + self.Suit + 's'

class Hand():
    def __init__(self):
        self.cards = []
        self.chips = 20
        self.cardTotal = 0

    def getCardTotal(self):
        total = 0

        for card in self.cards:
            total += card.Value
        
        for card in self.cards:
            if card.Suit == 'Ace':
                if total > 21:
                    total = total - 10

        return total
            

class Dealer():
    def __init__(self):
        self.cards = []
        self.cardTotal = 0

    def getCardTotal(self):
        total = 0

        for card in self.cards:
            total += card.Value
        
        for card in self.cards:
            if card.Suit == 'Ace':
                if total > 21:
                    total = total - 10

        return total
            
    

def BlackJack():
    global bjack
    hand = Hand()
    dealer = Dealer()
    bet = 0

    while bjack == True and hand.chips > 0:
        continueGame = input("would you like to play a round round? (yes/no)")
        if continueGame == 'yes':
            bjack = False

        CardDeck = [Card(Suit, Rank, Val) for Suit in cardTypes for Rank, Val in cardNums.items()]
        random.shuffle(CardDeck)
        hand.cards = []
        dealer.cards = []

        while bet == 0:
            betInfo = input("how much are you betting? ")

            if hand.chips >= int(betInfo):
                print('thats a good amount')
                bet = betInfo
                hand.chips = hand.chips - int(betInfo)
            else:
                print('you bet too much, pick a lower number')

        if len(hand.cards) == 0:
            startDealing(hand, dealer, CardDeck)
        
        while bjack == False:
            stand = False
            checkWinner(hand, dealer, bet, stand)

            if bjack == False and stand == False: 
                hit = input('Would you like to hit? (yes or no or stand)')
                if hit == 'stand':
                    stand = True

                if hit == "yes":
                    hand.cards.append(CardDeck.pop(0))
                    print('your hand')
                    for card in hand.cards:
                        print(card.name())
                    hand.cardTotal = hand.getCardTotal()
                    print('your card total')
                    print(hand.cardTotal)
                    print('--------------------------------------')
                
                elif hit == 'stand':
                    hand.cardTotal = hand.getCardTotal()
                    dealer.cardTotal = dealer.getCardTotal()

                    print('your card total:')
                    print(str(hand.cardTotal))
                    print('dealer card total:')
                    print(str(dealer.cardTotal))
                    print('--------------------------------------')

                else:
                    "No worries we'll skip your hit!!"

            if 18 > dealer.cardTotal:
                dealer.cards.append(CardDeck.pop(0))
                for card in dealer.cards[:-1]:
                    print(card.name())

    if hand.chips == 0:
        print(' haha you gambled away all your money!!!')

        
def checkWinner(hand, dealer, bet, stand):
    global bjack
    dealer.cardTotal = dealer.getCardTotal()
    hand.cardTotal = hand.getCardTotal()

    if dealer.cardTotal > 21 and 21 > hand.cardTotal:
        print('you won the round!')
        print('yout card total: ' + str(hand.cardTotal))
        print('dealer card total: ' + str(dealer.cardTotal))
        hand.chips += int(bet)*1.5
        bjack = True
        bet = 0

        return True

    elif hand.cardTotal > 21 and 21 > dealer.cardTotal:
        print('you lost the round')
        print('yout card total: ' + str(hand.cardTotal))
        print('dealer card total: ' + str(dealer.cardTotal))
        bjack = True
        bet = 0
        return True

    elif hand.cardTotal > 21 and dealer.cardTotal > 21:
        print('bust')
        print('yout card total: ' + str(hand.cardTotal))
        print('dealer card total: ' + str(dealer.cardTotal))
        hand.chips += bet
        bjack = True
        bet = 0
        return True


    elif dealer.cardTotal > 17 and hand.cardTotal > dealer.cardTotal:
        print('you won the round!')
        print('yout card total: ' + str(hand.cardTotal))
        print('dealer card total: ' + str(dealer.cardTotal))
        hand.chips += int(bet)*1.5
        bjack = True
        bet = 0

        return True

    elif stand == True:
        if hand.cardTotal > dealer.cardTotal and 22 > hand.cardTotal:
            print('you won the round!')
            print('yout card total: ' + str(hand.cardTotal))
            print('dealer card total: ' + str(dealer.cardTotal))
            hand.chips += int(bet)*1.5
            bjack = True
            bet = 0
        else:
            print('you lost the round')
            print('yout card total: ' + str(hand.cardTotal))
            print('dealer card total: ' + str(dealer.cardTotal))
            bjack = True
            bet = 0
            return True

    else:
        return False

def startDealing(hand, dealer, CardDeck):
    print('about to start dealing')
    dealer.cards.append(CardDeck.pop(0))
    hand.cards.append(CardDeck.pop(0))

    dealer.cards.append(CardDeck.pop(0))
    hand.cards.append(CardDeck.pop(0))

    print('this is the dealers first card: ' + str(dealer.cards[0].name()))
    print('--------------------------------------')
    print('This is your hand: ')
    for card in hand.cards:
        print(card.name())

    dealer.cardTotal = dealer.getCardTotal()
    hand.cardTotal = hand.getCardTotal()    
    print('Your hand total is...')
    print(str(hand.cardTotal))
    print('--------------------------------------')



BlackJack()