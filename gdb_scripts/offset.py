#!/usr/bin/env python3
import gdb

class Offsets(gdb.Command):
    def __init__(self):
        super (Offsets, self).__init__ ('offset', gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError('offsets-of takes exactly 1 argument.')

        
        sym = gdb.lookup_symbol(argv[0])
        print("[+] This symbol's type is:\033[1;31m{}\033[0m".format(sym[0].type))
        stype = gdb.lookup_type(str(sym[0].type))
        print(argv[0], '{')
        for field in stype.fields():
            print('\033[1;34m    %s \033[0m=>\033[1;31m 0x%x\033[0m' % (field.name, field.bitpos//8))
        print('}')
    

Offsets()
