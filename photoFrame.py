import os
import fnmatch
import subprocess
from os import walk
import time
#os.system("sudo mount -t nfs -o udp,vers=3,soft,intr,rsize=8192,wsize=8192 192.168.0.101:/nfs/Public /home/debian/Public")
os.system("/home/pi/PhotoFrame/mount.sh")
os.environ['DISPLAY']=":0"
#os.system("echo $DISPLAY")
#time.sleep(10)
#os.system("setterm -powersave off -blank 0")
os.system("xset dpms force on")
while(True):
  for(root, dirs, files) in walk("/home/pi/Public/Shared Pictures",topdown=False):
#for(root, dirs, files) in walk("/home/pi/test",topdown=False):
  # print('dirpath: %s, dirnames: %s filenames' %(dirpath, dirnames, filenames))
    files.sort()
    dirs.sort()
    for name in files:
      if fnmatch.fnmatch(name, '*.JPG') | fnmatch.fnmatch(name,'*.jpg'):
         name = os.path.join(root, name)
 #        print('Displaying file', name)
         p =subprocess.Popen(['feh', '-Y', '-F', '-D 60','--cycle-once', name])
         time.sleep(50)
         date = subprocess.check_output(['date'])
         if fnmatch.fnmatch(date, '* 23:*'):
           #print "Turning monitor off"
           os.system("/opt/vc/bin/tvservice -o")
           time.sleep(25200);
           os.system("/opt/vc/bin/tvservice -p")
           os.system("xset dpms force on") 
    #  else:
         # print('Not a picture %s' %(name))
    for name in dirs:
     # print(os.path.join(root,name))
     os.path.join(root,name)
