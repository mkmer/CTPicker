import os
import datetime
import sys
import logging

def logme(log_event):
    logfile = "/temp/scriptlogs.log"
    me = os.path.basename(sys.argv[0])
    os.system("/usr/bin/touch " + logfile)
    now = datetime.datetime.now()
    log = open(logfile, "a")
    log.write(now.strftime("%Y-%m-%d.%H:%M:%S") + ":(" + me + "):" + log_event + "\n")
    log.close()

def logged(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info("started '{0}', parameters : {1} and {2}".
                         format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(e)
    return wrapper
# decorator

