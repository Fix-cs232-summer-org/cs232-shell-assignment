from common import *


# Test if you see an error when trying to cd into a non-existent directory
child = start_shell()
child.sendline("cd adsf")
child.expect_exact("No such file or directory: 'adsf'")
expect_prompt(child)
exit_shell(child)
print(f"--> {__file__} passed")
