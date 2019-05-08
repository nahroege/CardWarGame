from random import shuffle

# Kartlari tanimlamak icin olusturulan degiskenler
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print("Yeni bir deste yaratiliyor.")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Desteyi karistirma")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class Hand:
    "Burda elimizde olan kartlari belirliyoruz."
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} yerlestirildi: {}".format(self.name,drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        """
         Oyuncuda hala kart varsa, True dondurur
         """
        return len(self.hand.cards) != 0



print("Savasa hosgeldin, haydi baslayalim...")


d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# Butun kullanicilari olusturmaliyiz
comp = Player("computer",Hand(half1))
name1 = input("Oyuncunun adi ne?")
user = Player(name1,Hand(half2))


total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Yeni bir raund zamani!")
    print("Iste su anki siralamalar: ")
    print(user.name+" count: "+str(len(user.hand.cards)))
    print(comp.name+" count: "+str(len(comp.hand.cards)))
    print("Iki oyuncu da kart oynuyor!")
    print('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    # table_cards 'a ekliyoruz'
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        #  table_cards'a ekliyoruz
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Kim daha yuksek dereceli
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Kim daha yuksek dereceli
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: "+str(total_rounds))
print("A war occured "+str(war_count)+" times.")
