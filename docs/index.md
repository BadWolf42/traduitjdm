# Documentation de "*traduitjdm*"

*traduitjdm* est un programme, en Python, d'aide à la traduction des plugins de [jeedom](http://jeedom.com)

Le programme peut être téléchargé depuis la page [release_note](release_notes.html)

## Introduction
Les textes dans les interfaces Jeedom peuvent être affichés en diverses langues selon le context. Pour celà, les textes devant pouvoir être affichés en différentes langues doivent être marqués sous la forme `{{texte à afficher}}` ou `__("texte à afficher".__FILE__)`. Les traductions de ces textes sont configurées dans des fichiers placés dans le répertoire `core/i18n` du plugin.

Le but de **traduitjdm** est de chercher les occurrences `{{texte à afficher}}` et `__("texte à afficher",__FILE__)` dans le code d'un plugin et de créer les fichiers de traductions dans `core/i18n`

Les textes trouvés par **traduitjdm** dans le code source du plugin sont ajoutés au fichier de traduction de la langue choisie mais avec une *tradruction* en Français. Les textes trouvés lors d'une exécution prédédente sont conservés avec leurs traductions.

Après avoir exécuté **traduitjdm**, il faut éditer le fichier de traduction et remplacer les *traductions* en français par de vraies traductions dans la langue cible.

## Syntaxe de "*traduitjdm*"
```
Usage:
~~~~~~
    traduitjdm [-V] [-h] [-v] [-d] [-b] [-j <jeedomDir>] -l <langueCible> plugin
    
    Outils pour la traduction de plugin Jeedom
    
    -h                Affichage de cette aide
    -V                Affichage de la version
    -v                Un peu de babillage
    -d                Debug (implique -v)
    -b                Backup: le fichier existant est renommé avec l'extention ".bck"
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
 - *-j \<jeedomDir>*    
     Répertoire d'installation de jeedom. Les textes à tradtuire seront recherchés sous `<jeedoDir>/plugins/<plugin>` et la fichier de traduction sera générer dans `<jeedoDir>/plugins/<plugin>/core/i18n`    
  - *-l \<langueCible>*    
      *fr_FR* pour le Français, *en-US* pour l'anglais... Voir le contenu du répertoire `<jeedoDir>/core/i18n` pour les langues reconnues par Jeedom.
