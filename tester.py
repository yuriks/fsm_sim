from tools import compare, string_to_bools

class Tester(object):
    def __init__(self, machine, out_names):
        self.m = machine
        self.out_names = out_names
        self.num_tests = 0
        self.failed_test = None

    def _check_state(self, test_outputs, ins):
            val_l = [test_outputs[k] for k in self.out_names]
            return compare(val_l, ins, False)

    def _test_setup(self):
        if self.failed_test is not None:
            return False

        self.num_tests += 1
        return True

    def run_test(self, test_inputs, test_outputs):
        if not self._test_setup(): return

        if isinstance(test_inputs, basestring):
            test_inputs = [test_inputs] * len(test_outputs)

        for ins, outs in zip(test_inputs, test_outputs):
            self.m.advance_state(string_to_bools(ins))
            if not self._check_state(self.m.get_output(), outs):
                self.failed_test = self.num_tests
                return

    def check_output(self, ins):
        if not self._test_setup(): return
        if not self._check_state(self.m.get_output(), ins):
            self.failed_test = self.num_tests

    def status(self):
        return self.failed_test
