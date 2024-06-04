from common import *

# Test if putting sleep in the background executes
child = start_shell()
child.sendline("sleep 2 &")
expect_no_output_and_only_child_pid_prompt(child)
exit_shell(child)
print(f"--> {__file__} passed")
