import thread
import time


def dontStop():
    var = 1
    while var == 1 :
        print "xxx"
try:
    thread.start_new_thread(dontStop)
except:
    print "Error: unable to start thread"