from common import *

# Test if entering just newlines works
child = start_shell()
for i in range(5):
    child.sendline("\n")
    expect_prompt(child)
exit_shell(child)
print(f"--> {__file__} passed")
