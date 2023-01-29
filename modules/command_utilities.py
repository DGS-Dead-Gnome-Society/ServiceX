def run(self, target, nickname, message):
    try:
        subCommand = message[0]
    except IndexError:
        self.msgSend(target, nickname, "A subcommand has not been specified.")
        return

    if subCommand == "echo":
        if len(message) > 1:
            strings = message[1].split('\\n')

            for string in strings:
                self.msgSend(target, nickname, string)
        else:
            self.msgSend(target, nickname, "Not enough parameters.")

    elif subCommand == "date":
        self.msgSend(target, nickname, self.timestamp("date"))

    elif subCommand == "time":
        self.msgSend(target, nickname, self.timestamp("time"))

    else:
        self.msgSend(target, nickname, "Subcommand not found.")
