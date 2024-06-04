from common import *


# Test if pwd command works
child = start_shell()
# the prompt is the current working directory
prompt = child.match.group(1).decode()
child.sendline("pwd")
child.expect_exact([prompt, pexpect.TIMEOUT], timeout=1)
exit_shell(child)
print(f"--> {__file__} passed")
