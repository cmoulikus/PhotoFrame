import os
import fnmatch
import subprocess
from os import walk
import time
import webbrowser
#os.system("sudo mount -t nfs -o udp,vers=3,soft,intr,rsize=8192,wsize=8192 192.168.0.101:/nfs/Public /home/debian/Public")
#os.system("/home/pi/mount.sh")
os.environ['DISPLAY']=":0"
#subprocess.call('export DISPLAY=:0', shell=True)
os.system("echo $DISPLAY")
#subprocess.call(['sudo', 'fbi', '-a', '--noverbose', '-1', '-T 2', '-t 10', '/home/pi/test/IMG_4584.JPG'])
cmd = 'sudo fbi -a --noverbose -1 -T 2 -t 10 /home/pi/test/IMG_4584.JPG'
#print cmd
#subprocess.call(cmd, shell=True)
p=subprocess.Popen(['feh', '-Y', '-F','--cycle-once', '-D 30', '/home/pi/test/IMG_4584.JPG'])
time.sleep(10)
print 'killing process'
p.terminate()
#webbrowser.register('epiphany')
#ctrl = webbrowser.get('epiphany')
#print ctrl
#webbrowser.open_new("http://www.google.com")
#webbrowser.open("http://calendar.google.com")
#subprocess.Popen(['epiphany-browser','https://www.wunderground.com/cgi-bin/findweather/getForecast?query=97229'])
subprocess.call(['epiphany','http://calendar.google.com'])
