from bs4 import BeautifulSoup
from requests import get
import random

def command_why(self, arguments):
    target, nickname, message = arguments
    req = get('http://developerexcuses.com/')
    soup = BeautifulSoup(req.text, features="html.parser")
    elem = soup.find('a')
    self.msgSend(target, nickname, elem.text.encode('ascii', 'ignore').decode())

def command_digiclock(self, arguments):
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
        ':': ('  ', '██', '  ', '██', '  '),
    }

    digits = [numRepr[digit] for digit in self.timestamp(preset='time')]
    for i in range(5):
        data = " ".join(segment[i] for segment in digits)
        self.msgSend(target, nickname, data)

def command_dice(self, arguments):
    target, nickname, message = arguments
    try:
        diceCount = int(message[0])
    except IndexError:
        diceCount = 1

    try:
        diceSides = int(message[1])
    except IndexError:
        diceSides = 6

    diceResults = []

    if diceCount == 0:
        self.msgSend(target, nickname, "You appear to be rolling thin air.")
        return

    if diceSides == 1:
        self.msgSend(target, nickname, "A one sided dice is not possible however a two sided dice is.")
        return

    for _ in range(diceCount):
        diceRoll = random.randint(1, diceSides)
        diceResults.append(str(diceRoll))

    if len(diceResults) == 1:
        self.msgSend(target, nickname, "You rolled a single dice with %s sides and got a %s." % (diceSides, diceResults[0]))

    if len(diceResults) > 1:
        self.msgSend(target, nickname, "You rolled %s dice with %s sides and got a %s and a %s." % (diceCount, diceSides, ", ".join(diceResults[:-1]), diceResults[-1:][0]))
