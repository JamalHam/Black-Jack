import random

cardTypes = ['Heart', 'Spade', 'Club', 'Diamond']
cardNums = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
bjack = False

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
    CardDeck = [Card(Suit, Rank, Val) for Suit in cardTypes for Rank, Val in cardNums.items()]
    hand = Hand()
    dealer = Dealer()
    random.shuffle(CardDeck)

    bet = 0
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

    # if hand.cardTotal == 21:
    #     print('you won the round!')
    #     hand.chips += bet*1.5
    #     bjack = True
    # elif hand.cardTotal > 21:
    #     print('you lost the round')
    #     bet = 0
    #     bjack = False

    
    while bjack == False:
        print('bjack status')
        print(bjack)

        if checkWinner(hand, dealer, bet) == False: 
            hit = input('Would you like to hit? (yes or no)')

            if hit == "yes":
                hand.cards.append(CardDeck.pop(0))
                print('your hand')
                for card in hand.cards:
                    print(card.name())
                hand.cardTotal = hand.getCardTotal()
                print('your cartd total')
                print(hand.cardTotal)
                print('--------------------------------------')
                

            else:
                "No worries we'll skip your hit!!"

            if 18 > dealer.cardTotal:
                dealer.cards.append(CardDeck.pop(0))
                for card in dealer.cards[:-1]:
                    print(card.name())

        
        
def checkWinner(hand, dealer, bet):
    global bjack
    dealer.cardTotal = dealer.getCardTotal()
    hand.cardTotal = hand.getCardTotal()

    if dealer.cardTotal > 21 and 21 > hand.cardTotal:
        print('you won the round!')
        hand.chips += bet*1.5
        bjack = True
        bet = 0

        return True

    elif hand.cardTotal > 21 and 21 > dealer.cardTotal:
        print('you lost the round')
        bjack = True
        bet = 0
        return True

    elif dealer.cardTotal > 17 and hand.cardTotal > dealer.cardTotal:
        print('you won the round!')
        hand.chips += bet*1.5
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