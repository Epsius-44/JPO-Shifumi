# Information sur un bonus avec coloration de l'affichage
Le schéma de 16 couleurs comprend deux ensembles de 8 couleurs chacun (8 arrière-plans et 8 avant-plans) et ils peuvent être affichés dans le terminal en utilisant la syntaxe suivante :

![Image bonus dispo sur github](https://github.com/Epsius-44/JPO-Shifumi/blob/main/doc/img/bonus-couleur-terminal.png?raw=true)

Par exemple si l'on veut mettre du texte en gras rouge sur fond jaune il nous faudra tapper

```python
print('\033[1;31;43m' + "Le message de test")
```

Cependant si nous utilisons ce code l'ensemble du terminal à partir du print sera modifié.

Si nous voulons seulement le faire sur une ligne il faut taper

```python
print('\033[1;31;43m' + "Le message de test" + "\033[0;0m")
```