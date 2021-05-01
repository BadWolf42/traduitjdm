
import sys

verbose = False
debug = False

def set_verbose( v ):
    global verbose
    verbose = v

def set_debug( d ):
    global debug
    debug = d

def Verbose(txt):
    if verbose:
        sys.stderr.write (txt)

def Debug(txt):
    if debug:
        sys.stderr.write (txt)

