def run(self, target, nickname, message):
    try:
        subCommand = message[0]
    except IndexError:
        self.msgSend(target, nickname, "A subcommand has not been specified.")
        return

    try:
        channelName = message[1]
    except IndexError:
        channelName = target

    if subCommand == "join":
        self.chanJoin(channelName, target)

    elif subCommand == "part":
        self.chanPart(channelName, target)

    elif subCommand == "cycle":
        self.chanPart(channelName, target, False)
        self.chanJoin(channelName, target, False)

    elif subCommand == "list":
        if len(self.channels) == 0:
            self.msgSend(target, nickname, "I am not in any channels on this IRC network.")

        elif len(self.channels) == 1:
            self.msgSend(target, nickname, "I am in %s on this IRC network." % self.channels[0])

        else:
            self.msgSend(target, nickname, "I am in %s and %s on this IRC network." % (", ".join(self.channels[:-1]), self.channels[-1:][0]))
    else:
        self.msgSend(target, nickname, "Subcommand not found.")
