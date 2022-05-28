#!/usr/bin/env python3
import gdb

global stype
class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offset', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')
        sym = gdb.lookup_symbol(argv[0])
        var = ""
        if sym[0] == None:
            var = "struct "+str(argv[0])
        elif "const" in str(sym[0].type):
            var = str(sym[0].type)
            var = var[6:]
        else:
            var = str(sym[0].type)
        stype = gdb.lookup_type(var)
        print("[+] This struct is:\033[1;31m{}\033[0m".format(stype))
        print(argv[0], '{')
        for field in stype.fields():
            print('\033[1;34m    %s \033[0m=>\033[1;31m 0x%x\033[0m' % (field.name, field.bitpos//8))
        print('}')

Offsets()