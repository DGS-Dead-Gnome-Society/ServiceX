def command_chanjoin(self, arguments):
    target, nickname, message = arguments

    try:
        channelName = message[0]
    except IndexError:
        channelName = target

    self.chanJoin(channelName, target)

def command_chanpart(self, arguments):
    target, nickname, message = arguments

    try:
        channelName = message[0]
    except IndexError:
        channelName = target

    self.chanPart(channelName, target)

def command_chancycle(self, arguments):
    target, nickname, message = arguments

    try:
        channelName = message[0]
    except IndexError:
        channelName = target

    self.chanPart(channelName, target, False)
    self.chanJoin(channelName, target, False)

def command_chanlist(self, arguments):
    target, nickname, message = arguments

    if len(message) == 0:
        self.msgSend(target, nickname, ", ".join(self.channels))

    elif message[0] == "count":
        self.msgSend(target, nickname, len(self.channels))

    elif message[0] == "fancy":
        if len(self.channels) == 0:
            self.msgSend(target, nickname, "I am not in any channels on this IRC network.")

        elif len(self.channels) == 1:
            self.msgSend(target, nickname, "I am just in %s on this IRC network." % self.channels[0])

        else:
            self.msgSend(target, nickname, "I am in %s and %s on this IRC network, a total of %s channels." % (", ".join(self.channels[:-1]), self.channels[-1:][0], len(self.channels)))
