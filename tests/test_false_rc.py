from common import *

# Test if running the false command returns a non-zero exit code
child = start_shell()
child.sendline("false")
res = child.expect_exact(["[Child pid: ", pexpect.TIMEOUT], timeout=1)
if res == 1:
    print("Timeout running the false command")
    exit(1)
res = child.expect_exact([" -> 1]", pexpect.TIMEOUT], timeout=1)
if res == 1:
    print("Value returned from running `false` was not 1 as required")
    exit(1)
exit_shell(child)
print(f"--> {__file__} passed")
