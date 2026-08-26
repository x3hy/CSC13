"""
Basic vannila (no-import) command-line argument parser
"""

# Handy little argument helper object
class args:
    def __init__(self, args, appname = None, description = None):
        self.argv = args
        self.argc = len(args)
        self.allowed = []

        self.description = description
        self.appname = appname

    def addcheck(self, name, desc):
        self.allowed.append([name, desc])

    def argc(self):
        return self.argc

    def argv(self):
        return self.argv

    # Function to strip key:value from argument
    def __getmethod(self, arg):
        part = arg.split('=');
        if (len(part) != 2):
            return None

        return part;

    def __allowed(self):
        allowed = [];
        for pair in self.allowed:
            allowed.append(pair[0]);
        return allowed;

    # Locate start of argument in argv
    def index(self, argname):
        for i, arg in enumerate(self.argv):
            if (arg.startswith(argname)):
                return i;
        return -1;

    # Return value of a searched argument
    def getv(self, arg):
        index = self.index(arg)
        if (index == -1):
            return None;

        string = self.argv[index];
        value = self.__getmethod(string);
        if (value != None):
            return value[1]

        return None;

    # Return boolean if an argument exists
    def hasv(self, arg):
        return (self.index(arg) != -1);

    # Argument whitelist, pass in "allowed" argument
    def check(self, skip = 1):
        errors = []
        for i, arg in enumerate(self.argv):
            if (i < skip):
                continue

            key =  self.__getmethod(arg)
            if (key != None):
                arg = key[0];

            if arg not in self.__allowed():
                errors.append(arg)
        return errors;

    def no_args(self):
        return (self.argc == 1)

    # No args where provided OR an invalid arg was provided
    def risk(self):
        return (len(self.check()) > 0 or self.no_args())

    def help(self):
        print(f"{self.appname} [OPTIONS]:")
        for arg in self.allowed:
            print(f" {arg[0]} {arg[1]}")
