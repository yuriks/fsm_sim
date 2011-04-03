import fsm
import tester

def run_tests(verbose=True):
    m = fsm.ControlFSM()
    t = tester.Tester(m, ['RegDst', 'RegWrite', 'ALUSrcA', 'MemRead', 'MemWrite', 'MemToReg', 'lorD', 'IRWrite', 'PCWrite', 'PCWriteCond', 'AluOP1', 'AluOP0', 'AluSrcB1', 'AluSrcB0', 'PCSrc1', 'PCSrc0'])

    out = [
        "-0010-0110000100", # 0
        "-0000--0000011--", # 1
        "-0100--0000010--", # 2
        "-0-10-1000------", # 3
        "11-000-000------", # 4
        "-0-01-1000------", # 5
        "-0100--0001000--", # 6
        "11-000-000------", # 7
        "-0100--001010001", # 8
        "-0-00--010----10"] # 9

    t.check_output(out[0])
    t.run_test("100011", [out[1], out[2], out[3], out[4], out[0]])
    t.run_test("101011", [out[1], out[2], out[5], out[0]])
    t.run_test("000000", [out[1], out[6], out[7], out[0]])
    t.run_test("000100", [out[1], out[8], out[0]])
    t.run_test("000010", [out[1], out[9], out[0]])

    return t.status()

if __name__ == "__main__":
    failed_test = run_tests()
    if failed_test is None:
        print "Tests completed sucessfully."
    else:
        print "Test", failed_test, "failed!"
