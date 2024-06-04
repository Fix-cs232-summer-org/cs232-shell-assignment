from common import *

# Test if putting multiple & at the end fails
child = start_shell()
child.sendline("sleep 1 & &")
child.expect_exact("only one & allowed")
expect_prompt(child)
exit_shell(child)

# Test if putting & before the end fails
child = start_shell()
child.sendline("& sleep 1 &")
child.expect_exact("only one & allowed")
expect_prompt(child)
exit_shell(child)

# Test if putting & not at the end fails (even if there is only 1)
child = start_shell()
child.sendline("sleep & 1")
child.expect_exact("& must be last item on the command line", timeout=1)
expect_prompt(child)
exit_shell(child)
print(f"{__file__} passed")
