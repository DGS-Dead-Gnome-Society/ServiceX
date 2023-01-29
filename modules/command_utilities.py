def run(self, target, nickname, message):
    try:
        subCommand = message[0]
    except IndexError:
        self.msgSend(target, nickname, "A subcommand has not been specified.")
        return

    if subCommand == "echo":
        if len(message) > 1:
            self.msgSend(target, nickname, self.tagParse(message[1]))

        else:
            self.msgSend(target, nickname, "Not enough parameters.")

    elif subCommand == "date" or "time":
        self.msgSend(target, nickname, self.timestamp(subCommand))

    else:
        self.msgSend(target, nickname, "Subcommand not found.")
