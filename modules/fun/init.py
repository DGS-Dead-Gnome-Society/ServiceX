from bs4 import BeautifulSoup
from requests import get
from random import randint
from getopt import getopt, GetoptError

def command_why(self, arguments):
    target, nickname, message = arguments
    req = get('http://developerexcuses.com/')
    soup = BeautifulSoup(req.text, features="html.parser")
    elem = soup.find('a')
    self.msgSend(target, nickname, elem.text.encode('ascii', 'ignore').decode())

def command_digits(self, arguments):
    target, nickname, message = arguments

    numRepr = {
        '0': ('██████', '██  ██', '██  ██', '██  ██', '██████'),
        '1': ('    ██', '    ██', '    ██', '    ██', '    ██'),
        '2': ('██████', '    ██', '██████', '██    ', '██████'),
        '3': ('██████', '    ██', '██████', '    ██', '██████'),
        '4': ('██  ██', '██  ██', '██████', '    ██', '    ██'),
        '5': ('██████', '██    ', '██████', '    ██', '██████'),
        '6': ('██████', '██    ', '██████', '██  ██', '██████'),
        '7': ('██████', '    ██', '    ██', '    ██', '    ██'),
        '8': ('██████', '██  ██', '██████', '██  ██', '██████'),
        '9': ('██████', '██  ██', '██████', '    ██', '██████'),
    }

    digits = [numRepr[digit] for digit in "".join(message)]
    for i in range(5):
        data = " ".join(segment[i] for segment in digits)
        self.msgSend(target, nickname, data)

def command_digiclock(self, arguments):
    target, nickname, message = arguments
    timezoneArg = None

    try:
        opts, args = getopt(message, "t:", ["timezone="])
    except GetoptError as e:
        print(e)

    for opt, arg in opts:
        if opt in ("-t", "--timezone"):
            timezoneArg = arg

    numRepr = {
        '0': ('██████', '██  ██', '██  ██', '██  ██', '██████'),
        '1': ('    ██', '    ██', '    ██', '    ██', '    ██'),
        '2': ('██████', '    ██', '██████', '██    ', '██████'),
        '3': ('██████', '    ██', '██████', '    ██', '██████'),
        '4': ('██  ██', '██  ██', '██████', '    ██', '    ██'),
        '5': ('██████', '██    ', '██████', '    ██', '██████'),
        '6': ('██████', '██    ', '██████', '██  ██', '██████'),
        '7': ('██████', '    ██', '    ██', '    ██', '    ██'),
        '8': ('██████', '██  ██', '██████', '██  ██', '██████'),
        '9': ('██████', '██  ██', '██████', '    ██', '██████'),
        ':': ('  ', '██', '  ', '██', '  '),
    }

    digits = [numRepr[digit] for digit in self.timestamp(timezoneArg, preset='time')]
    for i in range(5):
        data = " ".join(segment[i] for segment in digits)
        self.msgSend(target, nickname, data)

def command_dice(self, arguments):
    target, nickname, message = arguments
    diceCount = 1
    diceSides = 6

    try:
        opts, args = getopt(message, "c:s:", ["count=", "sides="])
    except GetoptError as e:
        print(e)

    for opt, arg in opts:
        if opt in ("-c", "--count"):
            diceCount = int(arg)

        if opt in ("-s", "--sides"):
            diceSides = int(arg)

    diceResults = []

    if diceCount == 0:
        self.msgSend(target, nickname, "You appear to be rolling thin air.")
        return

    if diceSides == 1:
        self.msgSend(target, nickname, "A one sided dice is not possible however a two sided dice is.")
        return

    for _ in range(diceCount):
        diceRoll = randint(1, diceSides)
        diceResults.append(str(diceRoll))

    if len(diceResults) == 1:
        self.msgSend(target, nickname, "You rolled a single dice with %s sides and got a %s." % (diceSides, diceResults[0]))

    if len(diceResults) > 1:
        self.msgSend(target, nickname, "You rolled %s dice with %s sides and got a %s and a %s." % (diceCount, diceSides, ", ".join(diceResults[:-1]), diceResults[-1:][0]))
