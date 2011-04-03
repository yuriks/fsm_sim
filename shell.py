try:
    import readline
except ImportError:
    pass
import cmd
import sys

import fsm
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
        if len(args) != 6:
            print "You must provide 6 input bits."
            return
        self.m.advance_state(tools.string_to_bools(args))
        self.do_cur_state(None)

    def help_advance(self):
        print "advance <input> -- Advances the state machine, using <input> as it's input."

    def do_outputs(self, args):
        o = self.m.get_output()
        for k, v in sorted(o.iteritems()):
            print k + ": " + (v and '1' or '0')

    def help_outputs(self):
        print "outputs -- Displays current outputs of the FSM."

    def do_exit(self, args):
        sys.exit(0)

if __name__ == "__main__":
    c = FSMShell(fsm.ControlFSM())
    try:
        c.cmdloop("Type 'help' or '?' for help.")
    except KeyboardInterrupt:
        c.do_exit(None)
