from sys import argv
# Fuck PEP8

# Handy little argument helper object
class args:
    def __init__(self, args, allowed = []):
        self.allowed = allowed;
        self.argv = args
        self.argc = len(args)

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

        return None

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

            if arg not in self.allowed:
                errors.append(arg)
        return errors;
