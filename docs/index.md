# Documentation de "*traduitjdm*"

*traduitjdm* est un programme, en Python, d'aide à la traduction des plugins de [Jeedom](http://jeedom.com)

Le programme peut être téléchargé depuis la page [release_note](release_notes.html)

## Introduction
Les textes dans les interfaces Jeedom peuvent être affichés en diverses langues selon le context. Pour celà, les textes devant pouvoir être affichés en différentes langues doivent être marqués sous la forme `{ {texte à afficher}}` ou `__("texte à afficher".__FILE__)`. Les traductions de ces textes sont configurées dans des fichiers placés dans le répertoire `core/i18n` du plugin.

Le but de **traduitjdm** est de chercher les occurrences `{ {texte à afficher}}` et `__("texte à afficher",__FILE__)` dans le code d'un plugin et de créer les fichiers de traductions dans `core/i18n`.

## Syntaxe de "*traduitjdm*"
```
Usage:
~~~~~~
    traduitjdm [-V] [-h] [-v] [-d] [-L] [-b] [-j <jeedomDir>] [-f core] -l <langueCible> plugin

    Outils pour la traduction de plugin Jeedom

    -h                Affichage de cette aide
    -V                Affichage de la version
    -v                Un peu de babillage
    -d                Debug (implique -v)
    -b                Backup: le fichier existant est renommé avec l'extention ".bck"
    -L                Affiche la liste des langues reconnues
    -f core           Priorité aux traductions provenant du core de Jeedom
    -j <jeedomDir>    Répertoire d'installation de Jeedom ('/var/www/html' par défaut)
    -l <langueCible>  Langue cible de la traduction
```

- *-h*  
    Affiche l'aide comme ci-dessus puis interromp l'exécution.
- *-V*  
    Affiche la version du programme puis interromp l'exécution.
- *-v*  
    Affiche quelques informations durant l'exécution des programmes.
- *-d*    
    Augmente la quantité d'informations affichées pas *-v*
- *-b*  
    Les 6 versions précédente du fichiers sont conservées.    
    Si le fichier `fr_FR.json` doit être créé, alors    
        - `fr_FR.json.bck.5` est supprimé   
        - `fr_FR.json.bck.4` est renommé `fr_FR.json.bck.5`   
        - ...   
        - `fr_FR.json.bck.1` est renommé `fr_FR.json.bck.2`   
        - `fr_FR.json.bck` est renommé `fr_FR.json.bck.1`   
        - `fr_FR.json` est renommé `fr_FR.json.bck`   
 - *-L*  
    Affiche la liste des langues reconnues
 - *-f core*  
    Les traductions trouvées dans le core de Jeedom sont utilisées en priorité
 - *-j \<jeedomDir>*    
    Répertoire d'installation de jeedom. Les textes à tradtuire seront recherchés sous `<jeedoDir>/plugins/<plugin>` et la fichier de traduction sera générer dans `<jeedoDir>/plugins/<plugin>/core/i18n`    
  - *-l \<langueCible>*    
    *fr_FR* pour le Français, *en-US* pour l'anglais... Voir le contenu du répertoire `<jeedoDir>/core/i18n` pour les langues reconnues par Jeedom.

## Principe de fonctionnement
### Recherche des textes à traduire
**traduitjdm** commence par constuire une lise des texte à traduire en cherchant les textes dans le code du plugin pus en y ajoutant les textes trouvés lors d'exécution précédentes qui se trouvent dans le fichier de traduction existant.

### Recherche de traductions
**traduitjdm** va chercher des traductions dans plusieurs souces pour chaque texte à traduire:
1. Dans la dernière version du fichier de traduction.
    Les traductions se trouvant dans ce fichier sont soit la traduction telle qu'elle a été déterminée lors de la dernière exécution, soit un texte modifié après exécution en éditant le fichier.
2. Dans le **core** de Jeedom.
    Les traductions definies dans le *core* de Jeedom sont récupérées.

### Sélection des traductions
Pour chaque texte à traduire une traduction sera reprise de l'une des soures de traduction dans l'ordre de piorité suivant:

1. Traduction trouvée dans la version précédente.
1. Traduction trouvée dans le core.
1. Si aucune traduction n'a été trouvée, on garde le texte en français comme proposition de tradduction.

L'option `-f core` force l'usage de la traduction trouvée dans le core en priorité 
