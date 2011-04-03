try:
    import readline
except ImportError:
    pass
import cmd
import sys

import one_hot
import tools

class FSMShell(cmd.Cmd):
    def __init__(self, m):
        cmd.Cmd.__init__(self)
        self.prompt = '> '

        self.m = m

    def do_cur_state(self, args):
        print "Current state:", self.m.get_current_state()

    def help_cur_state(self):
        print "cur_state -- Displays the current FSM state id."

    def do_advance(self, args):
        for i in tools.string_to_bools(args, reverse=False):
            self.m.advance_state(i)
        self.do_cur_state(None)

    def help_advance(self):
        print "advance <input> -- Advances the state machine, using <input> as a sequence of inputs."

    def do_outputs(self, args):
        o = self.m.get_output()
        for k, v in sorted(o.iteritems()):
            print k + ": " + (v and '1' or '0')

    def help_outputs(self):
        print "outputs -- Displays current outputs of the FSM."

    def do_exit(self, args):
        sys.exit(0)

if __name__ == "__main__":
    c = FSMShell(one_hot.SequenceFSM())
    try:
        c.cmdloop("Type 'help' or '?' for help.")
    except KeyboardInterrupt:
        c.do_exit(None)
