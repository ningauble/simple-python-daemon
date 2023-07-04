import sys
import os
import inspect

class Commands(object):
    """
    It do mapping of cli commands into daemon's methods like start, stop.
    """
    
    def __init__(self):
        
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        self.filename = os.path.basename(module.__file__)
    
    def serve(self, obj):
        
        if len(sys.argv)==1:
            self.show_usage()
            
        command = sys.argv[1]
        
        method = getattr(obj, command, None)
        
        if callable(method):
            method()
        else:
            self.show_unknown(command)

    def show_usage(self):
        sys.stderr.write("Usage: {} start|stop|restart\n".format(self.filename))
        sys.exit(1)

    def show_unknown(self, command):
        sys.stderr.write(f"Unknown command: {command}\n")
        sys.exit(1)