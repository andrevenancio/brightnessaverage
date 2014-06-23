import brightness
import glob

print chr(27) + "[2J"

for filename in glob.iglob('img/*.png'):
  brightness.py.testAll(filename)
