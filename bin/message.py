
import sys

__verbose = False
__debug = False
__color = True

__style = { "normal" :  "\33[0m",
            "verbose" : "\33[37;2m",
            "debug" : "\33[37;2m",
            "warning" : "\33[31m",
            "error" : "\33[37;41m",
          }

def set_verbose( v ):
    global __verbose
    __verbose = v

def set_debug( d ):
    global __debug
    __debug = d

def set_color( c ):
    global __color
    __color = c

def __Color(style):
    if __color:
        return __style[style]
    else:
        return ""

def __build_texte (txt, sep, end):
        textes = []
        for arg in txt:
            textes.append(str(arg))
        return ( sep.join(textes) + end )

def Verbose(*txt, sep=" ", end="\n"):
    if __verbose:
        msg = __build_texte (txt, sep, "")
        sys.stderr.write (__Color("verbose") + msg + __Color("normal") + end)

def Warning(*txt, sep=" ", end="\n"):
    msg = __build_texte (txt, sep, "")
    sys.stderr.write (__Color("warning") + msg + __Color("normal") + end)

def Error(*txt, sep=" ", end="\n"):
    msg = __build_texte (txt, sep, "")
    sys.stderr.write (__Color("error") + msg + __Color("normal") + end)

def Debug(*txt, sep=" ", end="\n"):
    if __debug:
        msg = __build_texte (txt, sep, "")
        sys.stderr.write (__Color("debug") + msg + __Color("normal") + end)

