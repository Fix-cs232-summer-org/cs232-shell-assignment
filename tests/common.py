import pexpect
import sys


VERBOSE = False
if len(sys.argv) > 1:
    if sys.argv[1] == "-v":
        VERBOSE = True


def start_shell():
    child = pexpect.spawn("python3 main.py")
    if VERBOSE:
        child.logfile = sys.stdout.buffer
    expect_prompt(child)
    return child


def exit_shell(child):
    child.sendline("exit")
    child.expect(pexpect.EOF)


def expect_no_output_and_prompt(child, timeout=1):
    # Should see child pid info and then child exits with 0 result.
    res = child.expect_exact(["[Child pid: ", pexpect.TIMEOUT], timeout=timeout)
    if res == 1:
        print("ERROR: Timeout")
        exit(1)
    res = child.expect_exact([" -> 0]", pexpect.TIMEOUT], timeout=timeout)
    if res == 1:
        print("ERROR: Timeout")
        exit(1)
    # then we should see the prompt
    res = child.expect(["(.*) > ", pexpect.TIMEOUT], timeout=timeout)
    if res != 0:
        print("Timeout")
        exit(1)


def expect_no_output_and_only_child_pid_prompt(child):
    # Should see child pid info and then child exits with 0 result.
    res = child.expect_exact(["[Child pid: ", pexpect.TIMEOUT], timeout=1)
    if res == 1:
        print("ERROR: Timeout")
        exit(1)
    res = child.expect(["(.*) > ", pexpect.TIMEOUT], timeout=1)
    if res != 0:
        print("ERROR: Timeout waiting for prompt")
        exit(1)


def expect_prompt(child):
    res = child.expect(["(.*) > ", "Errno", pexpect.TIMEOUT], timeout=1)
    if res != 0:
        print("ERROR: Timeout or Error")
        exit(1)


# Test if exit command works
def test_exit():
    child = start_shell()
    exit_shell(child)
    print("!!!!!!! start and exit passed !!!!!!!")
