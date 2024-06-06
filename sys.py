import sys
print(sys.version)
import platform
x=platform.system()
print(x)
y = dir(platform)
print(y)
# Processors
print(platform.processor())
# Machine
print(platform.machine())
# Node
print(platform.node())
# Release
print(platform.release())