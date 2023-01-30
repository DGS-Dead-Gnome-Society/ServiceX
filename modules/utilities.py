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

def command_modlist(self, arguments):
    target, nickname, message = arguments
    modlist = []

    for module in self.modules:
        modlist.append(module.__name__)

    self.msgSend(target, nickname, ", ".join(modlist))

def command_modload(self, arguments):
    target, nickname, message = arguments

    if len(message) == 1:
        self.loadModule(message[0])
    elif len(message) > 1:
        for moduleName in message:
            self.loadModule(moduleName)
    else:
        self.msgSend(target, nickname, "You have not specified a module to load.")

def command_modunload(self, arguments):
    target, nickname, message = arguments

    if len(message) == 1:
        self.unloadModule(message[0])
    elif len(message) > 1:
        for moduleName in message:
            self.unloadModule(moduleName)
    else:
        self.msgSend(target, nickname, "You have not specified a module to unload.")
