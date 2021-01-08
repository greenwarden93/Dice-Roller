from asyncore import dispatcher

from random2 import randrange

# program simulates rolled dice for rpg games

# defined terms

d3_1 = randrange(1, 4)
d3_2 = randrange(1, 4)
d3_3 = randrange(1, 4)
d3_4 = randrange(1,4)
d3_total2 = d3_1 + d3_2
d3_total3 = d3_1 + d3_2 + d3_3
d3_total4 = d3_1 + d3_2 + d3_3 + d3_4
d4_1 = randrange (1,5)
d4_2 = randrange (1,5)
d4_3 = randrange (1,5)
d4_4 = randrange (1,5)
d4_total2 = d4_1 + d4_2
d4_total3 = d4_1 + d4_2 + d4_3
d4_total4 = d4_1 + d4_2 + d4_3 + d4_4
d6_1 = randrange(1, 7)
d6_2 = randrange(1, 7)
d6_3 = randrange(1, 7)
d6_4 = randrange (1,7)
d6_total2 = d6_1 + d6_2
d6_total3 = d6_1 + d6_2 + d6_3
d6_total4 = d6_1 +d6_2 + d6_3 + d6_4
d8_1 = randrange(1, 9)
d8_2 = randrange(1, 9)
d8_3 = randrange(1,9)
d8_4 = randrange(1,9)
d8_total2 = d8_1 + d8_2
d8_total3 = d8_1 + d8_2 + d8_3
d8_total4 = d8_1 + d8_2 + d8_3 + d8_4
d12_1 = randrange(1, 13)
d12_2 = randrange(1,13)
d12_3 = randrange(1,13)
d12_total2 = d12_1 + d12_2
d12_total3 = d12_1 + d12_2 + d12_3
d20 = randrange(1, 21)
d100 = randrange(1, 101)
fate_dice_1 = randrange(1, 7)
fate_dice_2 = randrange(1, 7)
fate_dice_3 = randrange(1, 7)
fate_dice_4 = randrange(1, 7)
Total = 'Total = '


# mechanical code

# rolling d3s

def rolling_d3(d3_1):
    print(d3_1)


def rolling_2_d3s(d3_1, d3_2):
    print(d3_1)
    print(d3_2)
    print(Total + str(d3_total2))


def rolling_3_d3s(d3_1, d3_2, d3_3):
    print(d3_1)
    print(d3_2)
    print(d3_3)
    print(Total + str(d3_total3))


def rolling_4_d3s (d3_1, d3_2, d3_3, d3_4):
    print (d3_1)
    print (d3_2)
    print (d3_3)
    print (d3_4)
    print (Total + str(d3_total4))


# Rolling d4s

def rolling_d4 (d4_1):
    print (d4_1)


def rolling_2_d4s(d4_1, d4_2):
    print (d4_1)
    print (d4_2)
    print (Total + str(d4_total2))


def rolling_3_d4s (d4_1, d4_2, d4_3):
    print (d4_1)
    print (d4_2)
    print (d4_3)
    print (Total + str(d4_total3))


def rolling_4_d4s(d4_1, d4_2, d4_3, d4_4):
    print (d4_1)
    print (d4_2)
    print (d4_3)
    print (d4_4)
    print (Total + str(d4_total4))


# Rolling d6s

def rolling_d6(d6_1):
    print(d6_1)


def rolling_2_d6s(d6_1, d6_2):
    print(d6_1)
    print(d6_2)
    print(Total + str(d6_total2))


def rolling_3_d6s(d6_1, d6_2, d6_3):
    print(d6_1)
    print(d6_2)
    print(d6_3)
    print(Total + str(d6_total3))


def rolling_4_d6s (d6_1, d6_2, d6_3, d6_4):
    print(d6_1)
    print(d6_2)
    print(d6_3)
    print(d6_4)
    print (Total + str(d6_total4))


# Rolling d8s


def rolling_d8(d8_1):
    print(d8_1)


def rolling_2_d8s(d8_1, d8_2):
    print(d8_1)
    print(d8_2)
    print(Total + str(d8_total2))


def rolling_3_d8s(d8_1, d8_2, d8_3):
    print (d8_1)
    print (d8_2)
    print (d8_3)
    print (Total + str(d8_total3))


def rolling_4_d8s (d8_1, d8_2, d8_3, d8_4):
    print (d8_1)
    print (d8_2)
    print (d8_3)
    print (d8_4)
    print (Total + str(d8_total4))


# rolling d12s

def rolling_d12(d12_1):
    print(d12_1)


def rolling_2_d12s(d12_1, d12_2):
    print (d12_1)
    print (d12_2)
    print (Total + str(d12_total2))


def rolling_3_d12s(d12_1, d12_2, d12_3):
    print (d12_1)
    print (d12_2)
    print (d12_3)
    print (Total + str(d12_total3))


# rolling d20s

def rolling_d20(d20):
    if d20 == 20:
        print("Critcal Hit")
    elif d20 == 1:
        print("Critical Fail")
    else:
        print(d20)


# rolling d100

def rolling_d100(d100):
    print(d100)


# rolling fate dice and converting from number to symbol

def rolling_fate_die(fate_dice_1):
    if (fate_dice_1) == 1 or (fate_dice_1) == 2:
        print('+')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6:
        print('-')
    else:
        print("Blank")


def rolling_2_fate_dice(fate_dice_1, fate_dice_2):
    if (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2:
        print('+ +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4:
        print('+')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6:
        print('+ -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4:
        print('Blank')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6:
        print('-')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4:
        print('-')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6:
        print('- -')
    else:
        print('Error please try again!')


def rolling_3_fate_dice(fate_dice_1, fate_dice_2, fate_dice_3):
    if (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (fate_dice_3) == 1 or (
    fate_dice_3) == 2:
        print('+ + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('+ +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('+ + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_2) == 2:
        print('+ +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('+')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('+ -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_2) == 2:
        print('+ - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('+ -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('+ - -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('+ +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('+ -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('Blank')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('-')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('- +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('-')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('- + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('- + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('-')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2:
        print('- - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6:
        print('- - -')
    else:
        print('Error please try again!')


def rolling_4_fate_dice(fate_dice_1, fate_dice_2, fate_dice_3, fate_dice_4):
    if (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (fate_dice_3) == 1 or (
    fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ + + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ + + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ + - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ + - -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+  +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ - -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ - + +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ - + -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ - -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ - - +')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ - -')
    elif (fate_dice_1) == 1 or (fate_dice_1) == 2 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ - - -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print("+ + +")
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ + -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ - +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+ -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ - -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+ +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('+ -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('+')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('Blank')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('-')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('-')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- + +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- + -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('-')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- - +')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- -')
    elif (fate_dice_1) == 3 or (fate_dice_1) == 4 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- - -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- + + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- + + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- + - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 1 or (fate_dice_2) == 2 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- + - -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('-')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 3 or (fate_dice_2) == 4 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- - -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- - + +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 1 or (fate_dice_3) == 2 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- - + -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 3 or (fate_dice_3) == 4 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- - -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 1 or (fate_dice_4) == 2:
        print('- - - +')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 3 or (fate_dice_4) == 4:
        print('- - -')
    elif (fate_dice_1) == 5 or (fate_dice_1) == 6 and (fate_dice_2) == 5 or (fate_dice_2) == 6 and (
    fate_dice_3) == 5 or (fate_dice_3) == 6 and (fate_dice_4) == 5 or (fate_dice_4) == 6:
        print('- - - -')
    else:
        print('Error please try again!')


# user interface

def dice_choice(dice_choice):
    dice_choice = int(input('Choose your weapon: \n\n 1) d3 \n\n 2) d4 \n\n 3) d6 \n\n 4) d8 \n\n 5)d12 \n\n 6) d20 \n\n 7) d100 \n\n 8) fate dice. Please enter the corrosponing number and hit enter >>>'))
    dice_number = int(input('How many dice? >>>'))
    if dice_choice == int(1) and dice_number == int(1):
       rolling_d3(d3_1)
    elif dice_choice == int(1) and dice_number == int(2):
       rolling_2_d3s(d3_1, d3_2)
    elif dice_choice == int(1) and dice_number == int(3):
        rolling_3_d3s(d3_1, d3_2, d3_3)
    elif dice_choice == int(1) and dice_number == int(4):
        rolling_4_d3s(d3_1, d3_2, d3_3, d3_4)
    elif dice_choice == int(2) and dice_number == int(1):
        rolling_d4(d4_1)
    elif dice_choice == int(2) and dice_number == int(2):
        rolling_2_d4s(d4_1, d4_2)
    elif dice_choice == int(2) and dice_number == int(3):
        rolling_3_d4s(d4_1, d4_2, d4_3)
    elif dice_choice == int(2) and dice_number == int(4):
        rolling_4_d4s (d4_1, d4_2, d4_3, d4_4)
    elif dice_choice == int(3) and dice_number == int(1):
        rolling_d6(d6_1)
    elif dice_choice == int(3) and dice_number == int(2):
        rolling_2_d6s(d6_1, d6_2)
    elif dice_choice == int(3) and dice_number == int(3):
        rolling_3_d6s(d6_1, d6_2, d6_3)
    elif dice_choice == int(3) and dice_number == int(4):
        rolling_4_d6s(d6_1, d6_2, d6_3, d6_4)
    elif dice_choice == int(4) and dice_number == int(1):
        rolling_d8(d8_1)
    elif dice_choice == int(4) and dice_number == int(2):
        rolling_2_d8s(d8_1, d8_2)
    elif dice_choice == int(4) and dice_number == int(3):
        rolling_3_d8s(d8_1, d8_2, d8_3)
    elif dice_choice == int(4) and dice_number == int(4):
        rolling_4_d8s(d8_1, d8_2, d8_3, d8_4)
    elif dice_choice == int(5) and dice_number == int(1):
        rolling_d12(d12_1)
    elif dice_choice == int(5) and dice_number == int(2):
        rolling_2_d12s(d12_1, d12_2)
    elif dice_choice == int(5) and dice_number == int(3):
        rolling_3_d12s(d12_1, d12_2, d12_3)
    elif dice_choice == int(6) and dice_number == int(1):
        rolling_d20(d20)
    elif dice_choice == int(7) and dice_number == int(1):
        rolling_d100(d100)
    elif dice_choice == int(8) and dice_number == int(1):
        rolling_fate_die(fate_dice_1)
    elif dice_choice == int(8) and dice_number == int(2):
        rolling_2_fate_dice(fate_dice_1, fate_dice_2)
    elif dice_choice == int(8) and dice_number == int(3):
        rolling_3_fate_dice(fate_dice_1, fate_dice_2, fate_dice_3)
    elif dice_choice == int(8) and dice_number == int(4):
        rolling_4_fate_dice(fate_dice_1, fate_dice_2, fate_dice_3, fate_dice_4)
    else:
        print ('Please try another selection')

dice_choice(dice_choice)




