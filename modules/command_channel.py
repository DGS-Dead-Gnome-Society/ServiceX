def run(self, target, nickname, message):
    try:
        subCommand = message[0]
    except IndexError:
        self.msgSend(target, nickname, "A subcommand has not been specified.")
        return

    if subCommand == "join" or "part" or "cycle":
        try:
            channelName = message[1]
        except IndexError:
            channelName = target

        if subCommand == "join":
            self.chanJoin(channelName, target)

        if subCommand == "part":
            self.chanPart(channelName, target)

        if subCommand == "cycle":
            self.chanPart(channelName, target, False)
            self.chanJoin(channelName, target, False)

    if subCommand == "list":
        if len(message) == 1:
            self.msgSend(target, nickname, ", ".join(self.channels))

        if message[1] == "count":
            self.msgSend(target, nickname, len(self.channels))

        if message[1] == "fancy":
            if len(self.channels) == 0:
                self.msgSend(target, nickname, "I am not in any channels on this IRC network.")

            elif len(self.channels) == 1:
                self.msgSend(target, nickname, "I am just in %s on this IRC network." % self.channels[0])

            else:
                self.msgSend(target, nickname, "I am in %s and %s on this IRC network, a total of %s channels." % (", ".join(self.channels[:-1]), self.channels[-1:][0], len(self.channels)))

    else:
        self.msgSend(target, nickname, "Subcommand not found.")
