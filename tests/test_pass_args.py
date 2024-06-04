from common import *

# Test if entering running `which sleep` works: tests passing args to command
child = start_shell()
child.sendline("which sleep")
res = child.expect_exact(["/bin/sleep", pexpect.TIMEOUT], timeout=1)
if res == 1:
    print("ERROR: should have seen '/bin/sleep' for output")
    exit(1)
expect_prompt(child)
exit_shell(child)
print(f"--> {__file__} passed")
