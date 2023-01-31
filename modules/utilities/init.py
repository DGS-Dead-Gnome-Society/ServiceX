import platform

def variable_date(self):
    return self.timestamp("date")

def variable_time(self):
    return self.timestamp("time")

def command_help(self, arguments):
    target, nickname, message = arguments

def command_commands(self, arguments):
    target, nickname, message = arguments
    commands = []
    modules = []

    for command in self.commands:
        commands.append(command[0])

        if command[1] in modules:
            continue
        else:
            modules.append(command[1])

    commandCount = len(commands)
    moduleCount = len(modules)

    if commandCount == 1:
        firstString = "is %s command" % commandCount
    elif commandCount > 1:
        firstString = "are %s commands" % commandCount
    else:
        firstString = "are no commands"

    if moduleCount == 1:
        secondString = "%s from a single module" % firstString
    elif moduleCount > 1:
        secondString = "%s from %s modules" % (firstString, moduleCount)
    else:
        secondString = "%s" % firstString

    self.msgSend(target, nickname, "There %s available, these commands are:" % secondString)
    self.msgSend(target, nickname, self.dataGrid(self.chunkifyList(commands, 2)))

def command_date(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("date"))

def command_time(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("time"))

def command_uname(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, "%s %s %s %s %s GNU/Linux" % (platform.system(), platform.node(), platform.release(), platform.version(), platform.machine()))

def command_echo(self, arguments):
    target, nickname, message = arguments

    if len(message) == 1:
        self.msgSend(target, nickname, self.variableParse(target, nickname, message[0]))

    elif len(message) > 1:
        message = " ".join(message)
        self.msgSend(target, nickname, self.variableParse(target, nickname, message))

    else:
        self.msgSend(target, nickname, "Not enough parameters.")

def command_nick(self, arguments):
    target, nickname, message = arguments
    self.setNick(message[0])

def command_module(self, arguments):
    target, nickname, message = arguments
    subCommand = message[0]
    arguments = message[1:]

    if subCommand == "list":
        modlist = []

        for module in self.modules:
            modlist.append(module.__name__)

        self.msgSend(target, nickname, ", ".join(modlist))

    if subCommand == "load":
        if len(arguments) == 1:
            self.loadModule(arguments[0])
        elif len(arguments) > 1:
            for moduleName in arguments:
                self.loadModule(moduleName)
        else:
            self.msgSend(target, nickname, "You have not specified a module to load.")

    if subCommand == "unload":
        if len(arguments) == 1:
            self.unloadModule(arguments[0])
        elif len(arguments) > 1:
            for moduleName in arguments:
                self.unloadModule(moduleName)
        else:
            self.msgSend(target, nickname, "You have not specified a module to unload.")

    if subCommand == "enable":
        if len(arguments) == 1:
            self.enableModule(arguments[0])
        elif len(arguments) > 1:
            for moduleName in arguments:
                self.enableModule(moduleName)
        else:
            self.msgSend(target, nickname, "You have not specified a module to enable.")

    if subCommand == "disable":
        if len(arguments) == 1:
            self.disableModule(arguments[0])
        elif len(arguments) > 1:
            for moduleName in arguments:
                self.disableModule(moduleName)
        else:
            self.msgSend(target, nickname, "You have not specified a module to disable.")
