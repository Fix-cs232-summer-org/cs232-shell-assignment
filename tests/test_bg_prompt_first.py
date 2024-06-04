from common import *

# Test if putting command in background returns prompt before command finishes
child = start_shell()
child.sendline(
    "./sleepecho &"
)  # this command sleeps for 3 seconds and then displays "done sleeping"

# You should see the child pid info, then the prompt and then "done sleeping" output.
res = child.expect(["""(\[Child pid:) (.*) > """, pexpect.TIMEOUT], timeout=4)
if res == 1:
    print("Timeout")
    exit(1)
child.expect("done sleeping", timeout=5)
exit_shell(child)
print(f"--> {__file__} passed")
