from bs4 import BeautifulSoup
from requests import get

def command_why(self, arguments):
    target, nickname, message = arguments
    req = get('http://developerexcuses.com/')
    soup = BeautifulSoup(req.text, features="html.parser")
    elem = soup.find('a')
    self.msgSend(target, nickname, elem.text.encode('ascii', 'ignore').decode())
