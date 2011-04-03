import tools
from tools import compare

class ControlFSM(object):
    def __init__(self):
        self.cur_state = [False]*4

    def advance_state(self, o):
        s = self.cur_state
        next_state = [
            # S*0
            (
                (compare(s, "0000")) or
                (compare(s, "0001") and compare(o, "000010")) or
                (compare(s, "0010")) or
                (compare(s, "0110"))),
            # S*1
            (
                (compare(s, "0001") and compare(o, "10-011")) or
                (compare(s, "0001") and compare(o, "000000")) or
                (compare(s, "0010") and not o[3]) or
                (compare(s, "0110"))),
            # S*2
            (
                (compare(s, "0001") and compare(o, "000000")) or
                (compare(s, "0010") and o[3]) or
                (compare(s, "0011")) or
                (compare(s, "0110"))),
            # S*3
            (compare(s, "0001") and compare(o, "000--0") and (o[2] ^ o[1]))
        ]

        self.cur_state = next_state

    def get_output(self):
        s = self.cur_state
        return {
            'RegDst': True,
            'RegWrite': compare(s, "-111") or compare(s, "-100"),
            'ALUSrcA': s[3] or s[1],
            'MemRead': compare(s, "-011") or compare(s, "0000"),
            'MemWrite': compare(s, "-101"),
            'MemToReg': False,
            'lorD': s[0],
            'IRWrite': compare(s, "0000"),
            'PCWrite': compare(s, "1--1") or compare(s, "0000"),
            'PCWriteCond': compare(s, "1--0"),
            'AluOP1': s[2],
            'AluOP0': s[3],
            'AluSrcB1': s[0] or compare(s, "-01-"),
            'AluSrcB0': compare(s, "0-0-"),
            'PCSrc1': s[0],
            'PCSrc0': compare(s, "1--0")
        }

    def get_current_state(self):
        return tools.bools_to_int(self.cur_state)

