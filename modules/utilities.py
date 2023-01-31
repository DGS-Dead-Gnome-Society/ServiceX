def variable_date(self):
    return self.timestamp("date")

def variable_time(self):
    return self.timestamp("time")

def command_date(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("date"))

def command_time(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, self.timestamp("time"))

def command_echo(self, arguments):
    target, nickname, message = arguments

    if len(message) == 1:
        self.msgSend(target, nickname, self.variableParse(target, nickname, message[0]))

    elif len(message) > 1:
        message = " ".join(message)
        self.msgSend(target, nickname, self.variableParse(target, nickname, message))

    else:
        self.msgSend(target, nickname, "Not enough parameters.")

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
        self.databaseCursor.execute("SELECT * FROM modules")

        for module in self.databaseCursor:
            moduleID, networkID, moduleName, moduleEnabled = module

            if int(moduleEnabled) == 0 and moduleName == arguments[0]:
                tuple = (1, self.factory.networkID, arguments[0])
                query = '''UPDATE modules SET moduleEnabled=? WHERE networkID=? AND moduleName=?'''
                self.databaseCursor.execute(query, tuple)
                self.databaseConnection.commit()

    if subCommand == "disable":
        self.databaseCursor.execute("SELECT * FROM modules")

        for module in self.databaseCursor:
            moduleID, networkID, moduleName, moduleEnabled = module

            if int(moduleEnabled) == 1 and moduleName == arguments[0]:
                tuple = (0, self.factory.networkID, arguments[0])
                query = '''UPDATE modules SET moduleEnabled=? WHERE networkID=? AND moduleName=?'''
                self.databaseCursor.execute(query, tuple)
                self.databaseConnection.commit()
