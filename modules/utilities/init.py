import platform
import getopt

def variable_nick(self):
    return self.nickname

def variable_date(self):
    return self.timestamp(preset="date")

def variable_time(self):
    return self.timestamp(preset="time")

def command_help(self, arguments):
    target, nickname, message = arguments
    self.msgSend(target, nickname, "Hello there, I am a ServiceX bot called %s. For a list of commands, send '%scommands' into a channel or 'commands' to me as a PM.\\nFor more information on how to use ServiceX as an end user: https://github.com/DGS-Dead-Gnome-Society/ServiceX/wiki/User-Guide" % (self.nickname, self.factory.commandTrigger))

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

    if commandCount > 1:
        firstString = "are %s commands" % commandCount

    if moduleCount == 1:
        secondString = "%s from a single module" % firstString

    if moduleCount > 1:
        secondString = "%s from %s modules" % (firstString, moduleCount)

    self.msgSend(target, nickname, "There %s available, these commands are:\\n%s" % (secondString, self.dataGrid(self.chunkifyList(commands, 2))), escapes=True)

def command_date(self, arguments):
    target, nickname, message = arguments
    tz = False
    format = False
    preset = False
    timezoneArg = None

    try:
        opts, args = getopt.getopt(message, "f:p:t:", ["format=", "preset=", "timezone="])
    except getopt.GetoptError as e:
        print(e)

    for opt, arg in opts:
        if opt in ("-t", "--timezone"):
            timezoneArg = arg

        if opt in ("-f", "--format"):
            format = True
            formatArg = arg

        if opt in ("-p", "--preset"):
            preset = True
            presetArg = arg

    if format is True:
        self.msgSend(target, nickname, self.timestamp(timezoneArg, format=formatArg))
        return

    if preset is True:
        self.msgSend(target, nickname, self.timestamp(timezoneArg, preset=presetArg))
        return


     #   else:
     #       self.msgSend(target, nickname, "Invalid option specified: %s" % opt)

def command_time(self, arguments):
    target, nickname, message = arguments

    self.msgSend(target, nickname, self.timestamp(preset="time"))

def command_uname(self, arguments):
    target, nickname, message = arguments

    try:
        opts = []
        opts, args = getopt.getopt(message, ":snrvmoa", ["kernel-name", "nodename", "kernel-release", "kernel-version", "machine", "operating-system", "all"])
        unameString = []

        optsSpecified = {
            "system": False,
            "node": False,
            "release": False,
            "version": False,
            "machine": False,
            "os": False
        }

    except getopt.GetoptError as e:
        e = str(e)

        if e.startswith("option") and e.endswith("not recognized"):
            e = e.split()
            self.msgSend(target, nickname, "Invalid option has been specified: %s" % e[1])
            return

        else:
            print(e)

    os = "GNU/Linux"

    if len(opts) == 0:
        self.msgSend(target, nickname, "%s %s %s %s %s %s" % (platform.system(), platform.node(), platform.release(), platform.version(), platform.machine(), os))

    else:
        for opt, arg in opts:
            if opt in ("-s", "--kernel-name", "-a", "all"):
                optsSpecified["system"] = True

            if opt in ("-n", "--nodename", "-a", "all"):
                optsSpecified["node"] = True

            if opt in ("-r", "--kernel-release", "-a", "all"):
                optsSpecified["release"] = True

            if opt in ("-v", "--kernel-version", "-a", "all"):
                optsSpecified["version"] = True

            if opt in ("-m", "--machine", "-a", "all"):
                optsSpecified["machine"] = True

            if opt in ("-o", "--operating-system", "-a", "all"):
                optsSpecified["os"] = True

        if optsSpecified['system'] is True:
            unameString.append(platform.system())

        if optsSpecified['node'] is True:
            unameString.append(platform.node())

        if optsSpecified['release'] is True:
            unameString.append(platform.release())

        if optsSpecified['version'] is True:
            unameString.append(platform.version())

        if optsSpecified['machine'] is True:
            unameString.append(platform.machine())

        if optsSpecified['os'] is True:
            unameString.append(os)

        self.msgSend(target, nickname, " ".join(unameString))

def command_echo(self, arguments):
    target, nickname, message = arguments
    escapes = False
    newline = False

    try:
        opts, args = getopt.getopt(message, ":en")
        lastOpt = opts[:1]

    except getopt.GetoptError as e:
        e = str(e)

        if e.startswith("option") and e.endswith("not recognized"):
            e = e.split()
            self.msgSend(target, nickname, "Invalid option has been specified: %s" % e[1])
            return

        else:
            print(e)

    for opt, arg in opts:
        if opt in ("-e"):
            escapes = True

        if opt in ("-n"):
            newline = True

    if len(args) == 0:
        self.msgSend(target, nickname, "")
    else:
        self.msgSend(target, nickname, self.variableParse(target, nickname, " ".join(args)), escapes=escapes, newline=newline)

#    if len(message) == 1:
#        self.msgSend(target, nickname, self.variableParse(target, nickname, message[0]), escapes=escapes)

#    elif len(message) > 1:
#        message = " ".join(message)
#        self.msgSend(target, nickname, self.variableParse(target, nickname, message), escapes=escapes)

#    else:
#        self.msgSend(target, nickname, "Not enough parameters.")

def command_nick(self, arguments):
    target, nickname, message = arguments

    self.changeNick(message[0])

def command_module(self, arguments):
    target, nickname, message = arguments
    try:
        subCommand = message[0]
    except IndexError:
        return

    arguments = message[1:]

    if subCommand == "help":
        self.msgSend(target, nickname, "This is the ServiceX module manager.\\nCommands: %s" % self.dataGrid(self.chunkifyList(['list', 'load', 'unload', 'enable', 'disable'], 1)))

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
