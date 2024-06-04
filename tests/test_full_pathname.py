from common import *

# Test running command with full pathname (/bin/sleep) finishes
child = start_shell()
child.sendline("/bin/sleep 1")
# You should see the child pid info, then the prompt.
expect_no_output_and_prompt(child, timeout=2)
print(f"--> {__file__} passed")
