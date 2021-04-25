
import inspect
import re
from texte import Texte
from verbose import *

class FichierSource(object):

    __fichiersSource = dict()
    __jeedomDir = ""

    # --- Les méthodes de static ---

    @classmethod
    def by_path (cls, txt, create=True):
        if path in cls.__fichiersSource:
            return cls.__fichier.Source[path]
        if create:
            return cls(path)
        return None

    @classmethod
    def get_fichiers_source (cls, trie=False):
        fs = cls.__fichiersSource.values()
        if trie:
            fs = sorted (fs, key=lambda k: k.get_key() )
        return fs

    @staticmethod
    def set_jeedom_dir (dir):
        FichierSource.__jeedomDir = dir

    @staticmethod
    def set_jeedom_dir (dir):
        FichierSource.__jeedomDir = dir

    # --- Les méthodes d'intance ---

    def __new__ (cls, path=""):
        if path == "":
            return None
        return super().__new__(cls)

    def __init__ (self, path):
        FichierSource.__fichiersSource[path] = self
        self.__path = path
        self.__textes = set()

    def __del__ (self):
        del self.__fichiersSource[self.__path]

    def get_key (self):
        return self.__path.replace(FichierSource.__jeedomDir + "/", "").replace("/", "\/")

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
            self.__textes.add(Texte.by_texte(content[:pos]))

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

                self.__textes.add(Texte.by_texte(txt))

                # Retrait du prochain __( et de ce qui précède
                content = content[pos:]
                pos = content.find("__(")

    def get_traduction (self, langue):
        if (len(self.__textes) == 0):
            return ""

        result = 4 * " " + '"' + self.get_key() + '": {\n'
        for texte in sorted (self.__textes, key = lambda t: t.get_texte().upper()):
            traduction = texte.get_traduction(langue)
            result += 8 * " "
            result += '"' + traduction[0] + '": "' + traduction[1] + '",\n'
        result = result[:-2] + "\n    },\n"
        return result

