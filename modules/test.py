def command_test(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.frameData(['Product', 'Weight'], [['Rice', '500g'], ['Pasta', '250g']]))
