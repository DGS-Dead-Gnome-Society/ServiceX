def command_echo(self, arguments):
    target, nickname, message = arguments

    if len(message) == 1:
        self.msgSend(target, nickname, self.variableParse(message[0]))

    elif len(message) > 1:
        message = " ".join(message[1:])
        self.msgSend(target, nickname, self.variableParse(message))

    else:
        self.msgSend(target, nickname, "Not enough parameters.")

def command_date(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("date"))

def command_time(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("time"))
