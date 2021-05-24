import random

suits = ('Девы', 'Бубны', 'Пики', 'Трефы')
ranks = ('Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка',
         'Семерка', 'Восьмерка', 'Девятка', 'Десятка',
         'Валет', 'Дама', 'Король', 'Туз')
values = {'Двойка': 2, 'Тройка': 3, 'Четверка': 4, 'Пятерка': 5,
          'Шестерка': 6,
          'Семерка': 7, 'Восьмерка': 8, 'Девятка': 9,
          'Десятка': 10,
          'Валет': 1, 'Дама': 2, 'Король': 3, 'Туз': 11}
playing = True


# инициализация карт
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' ' + self.suit


# инициализация колоды карт
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'В колоде находятся карты: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        # pop берет последний элемент списка
        return single_card


# карты в руке у игрока
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # атрибут чтобы учитывать тузы

    def __str__(self):
        comp = ''
        for c in self.cards:
            comp += c.__str__() + '\n'
        return comp

    def cards_for_dealer(self):
        count = ''
        for w in self.cards[1:]:
            count += str(w) + '\n'
        return count

    def add_card(self, card):
        # card из объекта Deck
        self.cards.append(card)
        self.value += values[card.rank]
        # тузы
        if card == 'Туз':
            self.aces += 1

    def adjust_for_ace(self):
        # сумма > 21 и еще есть тузы
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Какая будет ставка? '))
        except:
            print('Пожалуйста введите число')
        else:
            if chips.bet > chips.total:
                print('Извините, не достаточно фишек. Доступное '
                      'колличество: {}'.format(chips.total))
            else:
                break


# игрок берет дополнительные карты
def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Взять дополнительную карту(hit) или остаться при '
                  'текущих картах(stand). Введите h или s: ')
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Игрок остается при текущих картах. Ход диллера')
            playing = False
        else:
            print('Извините, ответ не понятен. Пожалуйста введите h или '
                  's: ')
            continue
        break


def show_some(player, dealer):
    print('Карты Дилера: \n{}\n{}'.format('<Карта не известна>',
                                          dealer.cards_for_dealer()))
    print('Карты Игрока: \n{}Карты Игрока = {}'.format(player, player.value))


def show_all(player, dealer):
    print('\nКарты Дилера: \n{}Карты дилера = {}'.format(dealer,
                                                         dealer.value))
    print('\nКарты Игрока: \n{}Карты Игрока = {}'.format(player,
                                                         player.value))


# обработка сценариев завершения игры
def player_busts(player, dealer, chips):
    print('Превышение суммы 21 для Игрока!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Игрок выиграл!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Игрок выиграл! Диллер превысил 21')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Диллер выиграл!')
    chips.lose_bet()


def push(player, dealer):
    print('Ничья!')


# РЕШЕНИЕ
print('Добро пожаловать в игру Black Jack')
# установим кол-во фишек для игрока
player_chips = Chips(int(input('Введите начальный банк: ')))

while True:

    # создение и перемешивание колоды карт, каждый игрок получает по две
    # карты
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # какая будет ставка?
    take_bet(player_chips)

    # вскрыть карты(!одна из карт диллера скрыта)
    show_some(player_hand, dealer_hand)

    while playing:
        # хочет ли игрок взять дополнительную карту
        hit_or_stand(deck, player_hand)

        # показываем карты
        show_some(player_hand, dealer_hand)

        # если карты игрока превысили 21, выходим из цикла
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # если карты не превысили 21, переход к картам диллера
    if player_hand.value <= 21:

        while dealer_hand.value < 17 or dealer_hand.value < \
                player_hand.value:
            hit(deck, dealer_hand)

            # показываем все карты
        show_all(player_hand, dealer_hand)

        # проверяем различные варианты завершения игры
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # сообщить Игроку сумму его фишек
    print('\n Колличество фишек игрока: {}'.format(player_chips.total))

    # хочет ли игрок сыграть снова?
    new_game = input('Хотите ли сыграть снова? y или n: ')

    if new_game[0] == 'y':
        playing = True
        continue
    else:
        print('Спасибо за игру')
        break
