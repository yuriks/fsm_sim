import tools
from tools import compare

class SequenceFSM(object):
    """Finite State Machine that detects the sequence '1101'."""

    def __init__(self):
        self.cur_state = [False]*5
        self.cur_state[0] = True

    def advance_state(self, x):
        q = self.cur_state
        next_state = [
            # Q*0
            (not x and not q[2]),
            # Q*1
            (x and q[0]),
            # Q*2
            (x and (q[1] or q[2] or q[4])),
            # Q*3
            (not x and q[2]),
            # Q*4
            (x and q[3])
        ]

        self.cur_state = next_state

    def get_output(self):
        s = self.cur_state
        return {
            'z': s[4]
        }

    def get_current_state(self):
        try:
            return self.cur_state.index(True)
        except ValueError:
            return "Invalid"

