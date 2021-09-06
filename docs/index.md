# Documentation de "*traduitjdm*"

*traduitjdm* est un programme, en Python, d'aide à la traduction des plugins de [Jeedom](http://jeedom.com)

Le programme peut être téléchargé depuis la page [release_note](release_notes.html)

## Introduction
Les textes dans les interfaces Jeedom peuvent être affichés en diverses langues selon le context. Pour celà, les textes devant pouvoir être affichés en différentes langues doivent être marqués sous la forme `{ {texte à afficher}}` ou `__("texte à afficher".__FILE__)`. Les traductions de ces textes sont configurées dans des fichiers placés dans le répertoire `core/i18n` du plugin.

Le but de **traduitjdm** est de chercher les occurrences `{ {texte à afficher}}` et `__("texte à afficher",__FILE__)` dans le code d'un plugin et de créer les fichiers de traductions dans `core/i18n`.

## Syntaxe de "*traduitjdm*"
```
Usage:
~~~~~
    traduitjdm [-h] 
    traduitjdm [-V]
    traduitjdm [-L]
    traduitjdm [-v] [-d] [-c] [-b] [-C cfgFile] [-j <jeedomDir>] [-f core] -l <langue>[,<langue>,...] [<plugin>]

    Outils pour la traduction de plugin Jeedom

    -h                          Affiche cette aide
    -V                          Affiche la version
    -L                          Affiche la liste des langues reconnues
    -v                          Un peu de babillage
    -d                          Debug (implique -v)
    -c                          Désactive l'affichage en couleur
    -b                          Backup: le fichier existant est renommé avec l'extention ".bck"
    -C <cfgFile>                Fichier de configuration ('/home/chris/traduitjdm/etc/traduitjdm.cfg' par défaut)
    -j <jeedomDir>              Répertoire d'installation de Jeedom
                                ('/var/www/html' par défaut)
    -f core                     Priorité aux traductions provenant du core de Jeedom
    -l <langue>[,<langue>...]   Langue cible de la traduction
    <plugin>                    Nom du plugin à traduire. Argument obligtoire si le
                                plugin n'est pas défini dans le fichier de configuration
```

- *-h*  
    Affiche l'aide comme ci-dessus puis interromp l'exécution.
- *-V*  
    Affiche la version du programme puis interromp l'exécution.
 - *-L*  
    Affiche la liste des langues reconnues
- *-v*  
    Affiche quelques informations durant l'exécution des programmes.
- *-d*    
    Augmente la quantité d'informations affichées pas *-v*
- *-c*    
    Désactive la couleur pour l'affichage des messages à la consoles
- *-b*  
    Les 6 versions précédente du fichiers sont conservées.    
    Si le fichier `fr_FR.json` doit être créé, alors    
        - `fr_FR.json.bck.5` est supprimé   
        - `fr_FR.json.bck.4` est renommé `fr_FR.json.bck.5`   
        - ...   
        - `fr_FR.json.bck.1` est renommé `fr_FR.json.bck.2`   
        - `fr_FR.json.bck` est renommé `fr_FR.json.bck.1`   
        - `fr_FR.json` est renommé `fr_FR.json.bck`   
- *-C <cfgFile>
    Le fichier de configuration (voir le contenu de *traduit.cfg.exemple* pour la syntaxe du fichier de configuration)
- *-f core*  
    Les traductions trouvées dans le core de Jeedom sont utilisées en priorité
- *-j \<jeedomDir>*    
    Répertoire d'installation de jeedom. Les textes à tradtuire seront recherchés sous `<jeedoDir>/plugins/<plugin>` et la fichier de traduction sera générer dans `<jeedoDir>/plugins/<plugin>/core/i18n`    
- *-l \<langueCible>*    
    *fr_FR* pour le Français, *en-US* pour l'anglais... Voir le contenu du répertoire `<jeedoDir>/core/i18n` pour les langues reconnues par Jeedom.

## Principe de fonctionnement
### Recherche des textes à traduire
**traduitjdm** commence par constuire une lise des textes à traduire en cherchant les textes dans le code du plugin puis en y ajoutant les textes trouvés lors d'exécutions précédentes qui se trouvent dans le fichier de traduction existant.

### Recherche de traductions
**traduitjdm** va chercher des traductions dans plusieurs sources pour chaque texte à traduire:
1. Dans la dernière version du fichier de traduction.
    Les traductions se trouvant dans ce fichier sont soit la traduction telle qu'elle a été déterminée lors de la dernière exécution, soit un texte modifié après exécution en éditant le fichier.
2. Dans le **core** de Jeedom.
    Les traductions définies dans le *core* de Jeedom sont récupérées.

### Sélection des traductions
Pour chaque texte à traduire une traduction sera reprise de l'une des soures de traduction dans l'ordre de piorité suivant:

1. Traduction trouvée dans la version précédente.
1. Traduction trouvée dans le core.
1. Si aucune traduction n'a été trouvée, on garde le texte en français comme proposition de traduction.

L'option `-f core` force l'usage de la traduction trouvée dans le core en priorité 
