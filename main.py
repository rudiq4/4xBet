# Totalizator 0.1
# Author by rudiq4
# https://github.com/rudiq4

#  Ставка
s = 0
#  Доля
d = 0
#  Чистий виграш
c = 0
#  Виграш
v = 0

min_bet = 5
max_bet = 100

bets = []

TeamChoice = True
while TeamChoice:
    a = int(input('Виберіть команду яка виграє (1/2)'))
    if 3 > a > 0:
        print('Вибрана команда - ', a)
        TeamChoice = False
    else:
        print('Неправильно')

SumChoice = True
while SumChoice:
    b = int(input('Введіть суму ставки ({0}-{1})'.format(min_bet, max_bet)))
    if max_bet >= b >= min_bet:
        print('Введена сума - ', b)
        SumChoice = False
    else:
        print('Неправильна сума !')
