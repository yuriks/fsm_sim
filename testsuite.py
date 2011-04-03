import one_hot
import tester
import itertools

def run_tests(verbose=True):
    m = one_hot.SequenceFSM()
    t = tester.Tester(m, ['z'])

    t.check_output(["0"])
    for test in itertools.product(('0','1'), repeat=4):
        test = ''.join(test)
        if test == "1101":
            expected_output = "1"
        else:
            expected_output = "0"
        t.run_test(test, [expected_output])

    return t.status()

if __name__ == "__main__":
    failed_test = run_tests()
    if failed_test is None:
        print "Tests completed sucessfully."
    else:
        print "Test", failed_test, "failed!"
