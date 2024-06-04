from common import *
import shutil

# Test if cd command works
try:
    shutil.rmtree("x")  # possible clean-up
except:
    pass
child = start_shell()
child.sendline("mkdir x")
expect_no_output_and_prompt(child)
child.sendline("cd x")
expect_prompt(child)
new_prompt = child.match.group(1).decode()
if not new_prompt.endswith("/x"):
    print("Prompt did not change correctly for cd command")
    exit(1)
exit_shell(child)
print(f"--> {__file__} passed")
