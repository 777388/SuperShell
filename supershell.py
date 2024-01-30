import sys
import os
class runner:
    def __init__(self, run, lists):
        self.run = run
        self.list = lists

    def superrun(self):
        #for i in range(self.list.size()):
        #intel = self.list[i]
        with open(self.list) as f:
            for line in f:
                intel  = line.strip()
                (lambda v: os.popen(self.run+os.popen(v).read()))(intel)

class cypher:
    def __init__(self, encodeamount, encode):
        self.encodeamount = 0
        self.encode = encode
        for charsin in encodeamount:
            self.encodeamount += int(ord(charsin))

    def encoded(self):
        ret = ""
        for charsss in self.encode:
            ret += str(chr(ord(charsss)+self.encodeamount))
        return ret
    
    def decypher(self):
        decode = ""
        for charred in self.encode:
            decode += str(chr(ord(charred) - self.encodeamount))
        return decode
class First:
    def __init__(self, firsts, seconds):
        self.firsts = 0
        self.seconds  = 0
        for chars in firsts:
            self.firsts += int(ord(chars))
        for charsi in seconds:
            self.seconds = int(ord(charsi))
    def attributemod(self):
        attributeamount = self.firsts
        attributemod = self.seconds
        return attributeamount % attributemod
    def attributebuff(self):
        attributeamount = self.firsts
        attributebuff = self.seconds
        return attributeamount ** attributebuff

class superstantiate(runner):
    def __init__(self, run, lists):
        super(superstantiate, self).__init__(run, lists)
class superbuff(First):
    def __init__(self, firsts, seconds):
        super(superbuff, self).__init__(firsts, seconds)
class supershell(cypher):
    def __init__(self, encodeamount, encode):
        super(supershell, self).__init__(encodeamount, encode)
testrun = superstantiate(sys.argv[1], sys.argv[2])
analyze = superbuff(sys.argv[1], sys.argv[2])
decypher = supershell(sys.argv[1], sys.argv[2])
if sys.argv[3] == "run":
    testrun.superrun()
if sys.argv[3] == "buff":
    print(analyze.attributebuff())
if sys.argv[3] == "mod":
    print(analyze.attributemod())
if sys.argv[3] == "cypher":
    print(decypher.encoded())
if sys.argv[3] == "decypher":
    print(decypher.decypher())
if sys.argv[3] == "all":
    testrun.superrun()
    print(analyze.attributebuff())
    print(analyze.attributemod())
    print(decypher.encoded())
    decypher = supershell(sys.argv[1], decypher.encoded())
    print(decypher.decypher())