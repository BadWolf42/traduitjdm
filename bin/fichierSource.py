
import inspect
import re
from texte import Texte
from message import *

class FichierSource(object):

    __fichiersSource = dict()
    __jeedomDir = ""

    # --- Les méthodes de static ---

    @classmethod
    def by_key (cls, key, create=True):
        if key in cls.__fichiersSource:
            return cls.__fichiersSource[key]
        if create:
            return cls(key)
        return None

    @classmethod
    def by_path (cls, txt, create=True):
        key = key_from_path(path)
        if key in cls.__fichiersSource:
            return cls.__fichiersSource[key]
        if create:
            return cls(key)
        return None

    @classmethod
    def get_fichiers_source (cls):
        fs = cls.__fichiersSource.values()
        return fs

    @staticmethod
    def set_jeedom_dir (dir):
        FichierSource.__jeedomDir = dir

    @staticmethod
    def key_from_path (path):
        return path.replace(FichierSource.__jeedomDir + "/", "")

    # --- Les méthodes d'intance ---

    def __new__ (cls, path=""):
        if path == "":
            return None
        return super().__new__(cls)

    def __init__ (self, path):
        self.__path = path
        self.__key = self.key_from_path(path)
        FichierSource.__fichiersSource[self.__key] = self
        self.__textes = set()

    def __del__ (self):
        del self.__fichiersSource[self.__key]

    def get_key (self):
        return self.__key

    def add_texte(self, txt):
        self.__textes.add(txt)

    def search_textes(self):
        try:
            with (open(self.__path, "r")) as f:
                content = f.read()
        except Exception as ex:
            info = inspect.currentframe()
            print (ex, "( at line" , info.f_lineno , ")")
            sys.exit(1)

        Debug ("        Recherche {{..}}\n")
        for txt in re.findall("{{(.*?)}}",content):
            if len(txt) != 0:
                Verbose ("        " + txt)
                self.__textes.add(Texte.by_texte(txt))
            else:
                Warning (f"ATTENTION, il y a un texte de longueur 0 dans le fichier <{self.__path}>")

        if self.__path[-4:] == ".php":
            Debug ('        Recherche __("...",__FILE__)\n')
            for txt in re.findall('__\s*\(\s*"(.*?)\s*"\s*,\s*__FILE__',content):
                if len(txt) != 0:
                    Verbose ("        " + txt)
                    self.__textes.add(Texte.by_texte(txt))
                else:
                    Warning (f"ATTENTION, il y a un texte de longueur 0 dans le fichier <{self.__path}>")

    def get_traduction (self, langue):
        if (len(self.__textes) == 0):
            return None

        result = dict()
        for texte in self.__textes:

            Debug ("\n==========\nfichier: " + self.__path + "\n")
            Debug ("\n  ".join(dir(self)))
            Debug ("\n-----------\ntexte: "+ texte.get_texte() + "\n")
            Debug ("  " + "\n  ".join(dir(texte)) + "\n")

            traduction = texte.get_traduction(langue)
            result[traduction[0]] = traduction[1]

        return result

