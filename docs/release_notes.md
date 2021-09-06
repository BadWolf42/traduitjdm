[Documentation](https://ktn001.github.io/traduitjdm/)

# Release Notes

## v0.6.0 (7/9/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.6.0.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.6.0.zip)

- Amélioration de la recherche des textes à traduire
- Recherche des textes à traduire dans les fichiers (\*.php, \*.js et \*.html). Avant, on cherchait uniquemen dans \*php et \*.js.
- On ne cherche pas de textes à tratuire dans le répertoire *docs*

## v0.5.0 (21/08/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.5.0.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.5.0.zip)

- Le répertoire "core/i18n" du plugin est créé s'il n'existe pas encore
- Quelques corrections de texte

## v0.4.0 (01/05/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.4.0.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.4.0.zip)

- Sélection interractive si le core propose plusieurs traductions pour un même texte.
- Pas de recherche de traduction dans le core pour "fr_FR". En français, la traduction est le texte lui-même.
- Affichage en couleur (peut être désactivé avec l'option -c).
- Utilisation d'un fichier pour définir le plugin et les langues cibles sans avoir à les indiquer dans la ligne de commande.

## v0.3.1 (01/05/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.3.1.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.3.1.zip)

- Détection de texte à traduire de longueur 0.

## v0.3.0 (29/04/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.3.0.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.3.0.zip)

- Reprise des texte du core.

## v0.2.2 (29/04/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.2.2.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.2.2.zip)

Correction d'un bug

## v0.2.1 (27/04/2021)
- Suppression d'un message de traçage.

## v0.2.0 (27/04/2021)
- Modification de la structure du code.
- Vérification de la langue demandée via l'option *-l \<langue>*.
- Les textes traduits précédemment sont conservés.

## v0.1.1 (24/04/2021)
[tgz](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.1.1.tar.gz) [zip](https://github.com/ktn001/traduitjdm/archive/refs/tags/v0.1.1.zip)

- Correction d'une erreur de syntaxe.

## v0.1.0 (24/04/2021)
- Le fichier génére un nouveau fichier de traduction sans tenir compte d'un fichier existant.
- Le fichier générer contient la liste des textes trouvés mais sans traduction.
