import Image
import ImageStat
import time
import math


"""
INFO:
http://effbot.org/imagingbook/image.htm
"""


#gets current time
def getCurrentTime():
  return int(round(time.time() * 1000))


#get elapsed time between 2 values
def getElapsedTime(start, end):
  duration = end-start
  return str(duration) + 'ms'


#performs all 5 tests
def testAll(path):
  print ''
  print '\033[91mtesting\033[0m', path
  grayscaleAverage(path)
  grayscaleRMS(path)
  averagePerceived(path)
  rmsPerceivedBrightness(path)
  perceivedBrightnessAverage(path)
  print ''


#Covert image to greyscale, return average pixel brightness.
def grayscaleAverage(path):
  print '\033[92mgrayscale average\033[0m'
  
  start = getCurrentTime()
  
  im = Image.open(path).convert('L')
  stat = ImageStat.Stat(im)
  print '\033[90maverage:\033[0m', stat.mean[0]
  
  end = getCurrentTime()
  print '\033[90mtime:\033[0m', getElapsedTime(start, end)


#Covert image to greyscale, return RMS pixel brightness.
def grayscaleRMS(path):
  print '\033[92mgrayscale RMS\033[0m'
  
  start = getCurrentTime()
  
  im = Image.open(path).convert('L')
  stat = ImageStat.Stat(im)
  print '\033[90maverage:\033[0m', stat.rms[0]
  
  end = getCurrentTime()
  print '\033[90mtime:\033[0m', getElapsedTime(start, end)


#Average pixels, then transform to "perceived brightness".
def averagePerceived(path):
  print '\033[92maverage Perceived\033[0m'
  
  start = getCurrentTime()
  
  im = Image.open(path)
  stat = ImageStat.Stat(im)
  r,g,b = stat.mean
  print '\033[90maverage:\033[0m', math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
  
  end = getCurrentTime()
  print '\033[90mtime:\033[0m', getElapsedTime(start, end)


#RMS of pixels, then transform to "perceived brightness".
def rmsPerceivedBrightness(path):
  print '\033[92maverage Perceived\033[0m'
  
  start = getCurrentTime()
  
  im = Image.open(path)
  stat = ImageStat.Stat(im)
  r,g,b = stat.rms
  print '\033[90maverage:\033[0m', math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
  
  end = getCurrentTime()
  print '\033[90mtime:\033[0m', getElapsedTime(start, end)


#RMS of pixels, then transform to "perceived brightness".
def perceivedBrightnessAverage(path):
  print '\033[92maverage Perceived\033[0m'
  
  start = getCurrentTime()
  
  im = Image.open(path)
  stat = ImageStat.Stat(im)
  gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
         for r,g,b in im.getdata())
  print '\033[90maverage:\033[0m', sum(gs)/stat.count[0]
  
  end = getCurrentTime()
  print '\033[90mtime:\033[0m', getElapsedTime(start, end)

