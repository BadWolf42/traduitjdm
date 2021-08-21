
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
        Debug ("        Recherche {{..}}\n")
        try:
            with (open(self.__path, "r")) as f:
                content = f.read()
        except Exception as ex:
            info = inspect.currentframe()
            print (ex, "( at line" , info.f_lineno , ")")
            sys.exit(1)

        # Recherche du premier {{
        pos = content.find("{{")
        while pos >= 0:
            # Retrait des premiers {{ et de ce qui précède
            content = content[pos + 2:]

            # On garde ce qui précède le prochains }}
            pos = content.find("}}")
            txt = content[:pos]
            if len(txt) != 0:
                Verbose ("        " + txt)
                self.__textes.add(Texte.by_texte(txt))
            else:
                Warning (f"ATTENTION, il y a un texte de longueur 0 dans le fichier <{self.__path}>")

            # retrait du texte
            content = content[pos:]
            pos = content.find("{{")

        if self.__path[-4:] == ".php":
            Debug ('        Recherche __("...",__FILE__)\n')
            # On remet le contenu du fichier en mémoire
            try:
                with (open(self.__path, "r")) as f:
                    content = f.read()
            except Exception as ex:
                info = inspect.currentframe()
                print (ex, "( at line" , info.f_lineno , ")")
                sys.exit(1)

            # Retrait des éventuels espaces qui entourent __FILE__
            content = re.sub (",\s*__FILE__\s*\)", ",__FILE__)", content)

            pos = content.find("__(")
            while pos >= 0:
                # Retrait du premier __( et de ce qui précède
                content = content[pos + 3:]

                # On garde ce qui précède le prochain ,__FILE)
                pos = content.find(",__FILE__)")
                txt = content[:pos]

                # On enlève les simples ou doubles quotes qui entourent le texte
                if (txt[0] == "'" and txt [-1] == "'") or (txt[0] == '"' and txt [-1] == '"'):
                    txt = txt[1:-1]

                if len(txt) != 0:
                    Verbose ("        " + txt)
                    self.__textes.add(Texte.by_texte(txt))
                else:
                    Warning (f"ATTENTION, il y a un texte de longueur 0 dans le fichier <{self.__path}>")

                # Retrait du prochain __( et de ce qui précède
                content = content[pos:]
                pos = content.find("__(")

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

