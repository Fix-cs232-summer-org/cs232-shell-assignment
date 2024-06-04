from common import *

# Test if entering a command that is not in the PATH works
child = start_shell()
child.sendline("not_a_command")
res = child.expect_exact(["Command not found in the path", pexpect.TIMEOUT], timeout=1)
if res == 1:
    print('ERROR: Should have see "Command not found in the path"')
    exit(1)
exit_shell(child)
print(f"--> {__file__} passed")
