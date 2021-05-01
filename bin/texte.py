
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

    @staticmethod
    def select_traduction(source, langue, texte, choix):
        print ('\nLa source <' + source + '> propose plusieurs traductionsi en <' + langue + '> pour : "' + texte + '"\n')
        for i in range (len(choix)):
            print (i+1, ":", choix[i])
        print ()
        while True:
            try:
                reponse = int(input ("Laquelle de ces traductions doit être utilisée (#) ? "))
            except ValueError:
                print ("Prière de saisir le numéro de la traduction voulue")
                reponse = 0
            reponse = reponse -1
            if reponse >= 0 and reponse < len(choix):
                return (texte[reponse -1])

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

    def add_traduction (self, langue, traduction, source, fileKey=None):
        self.__traduction.setdefault(langue,dict())
        if source == "core":
            self.__traduction[langue].setdefault(source, list())
            if not traduction in self.__traduction[langue][source]:
                self.__traduction[langue][source].append(traduction)
        else:
            self.__traduction[langue][source] = traduction

    def get_traduction (self, langue):
        traduction = self.__texte
        if langue in self.__traduction:
            for source in self.__priorite:
                if source in self.__traduction[langue]:
                    if source == "core":
                        if len(self.__traduction[langue][source]) == 1:
                            traduction = self.__traduction[langue][source][0]
                        else:
                            traduction = self.select_traduction(source,
                                                                langue,
                                                                self.__texte,
                                                                self.__traduction[langue][source])
                    else:
                        traduction = self.__traduction[langue][source]
                    break
        return (self.__texte, traduction)

    def get_texte (self):
        return self.__texte
