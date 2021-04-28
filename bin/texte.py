
from verbose import *

class Texte(object):

    __textes = dict()
    __priorite = ["precedent", "core"]

    # --- Les méthodes de static ---

    @classmethod
    def by_texte (cls, txt, create=True):
        if txt in cls.__textes:
            return cls.__textes[txt]
        if create:
            return cls(txt)
        return None

    @classmethod
    def set_priorite(cls, p):
        result = []
        for prio in p.split(",") + cls.__priorite:
            if not prio in result:
                result.append(prio)
        cls.__priorite = result

    # --- Les méthodes d'intance ---

    def __new__ (cls,txt=""):
        if txt == "":
            return None
        return super().__new__(cls)

    def __init__ (self,txt):
        self.__textes[txt] = self
        self.__texte = txt
        self.__traduction = dict()

    def __del__ (self):
        del self.__textes[self.__texte]

    def set_traduction (self, langue, texteTraduit, source, fileKey=None):
        self.__traduction.setdefault(langue,dict())
        self.__traduction[langue][source] = texteTraduit

    def get_traduction (self, langue):
        traduction = self.__texte
        if langue in self.__traduction:
            for source in reversed (self.__priorite):
                if source in self.__traduction[langue]:
                        traduction = self.__traduction[langue][source]
        return (self.__texte, traduction)

    def get_texte (self):
        return self.__texte
