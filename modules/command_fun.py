from bs4 import BeautifulSoup
from requests import get

def run(self, target, nickname, message):
    try:
        subCommand = message[0]
    except IndexError:
        self.msgSend(target, nickname, "A subcommand has not been specified.")
        return

    if subCommand == "why":
        req = get('http://developerexcuses.com/')
        soup = BeautifulSoup(req.text, features="html.parser")
        elem = soup.find('a')
        self.msgSend(target, nickname, elem.text.encode('ascii', 'ignore').decode())

    else:
        self.msgSend(target, nickname, "Subcommand not found.")
