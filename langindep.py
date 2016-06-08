#langindep.py
import time
import subprocess

sub1py = subprocess.Popen(['python', 'sub1.py'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
sub2cpp = subprocess.Popen(['./sub2'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# The content of the output is fairly meaningless, other than just demonstrating that you can redirect standard in/out/err.
# And by doing so, allowing a script (sub1.py) and a compiled c++ program (sub2) to pass messages back and forth,
# facilitated by this python script (langindep.py).
# There is a possibility of deadlocking when using PIPE, especially with stderr (although not likely
# to happen unless you are putting a strain on the system resources)  
# For professionial projects use interprocess communication, not IO piping/redirection, to facilitate back and forth communication
# between programs/apps/processes/etc.

for i in range(5):
  sub2cpp.stdin.write('%d\n' % i)
  outputsub2 = str(sub2cpp.stdout.readline())
  print "sub2cpp received: " + str(outputsub2)
  sub1py.stdin.write('%s\n' % outputsub2)
  outputsub1 = str(sub1py.stdout.readline())
  print "sub1py received: " + str(outputsub1)
  time.sleep(1)
  sub1py.kill()
  sub2cpp.kill()
  exit()
 
    
   
