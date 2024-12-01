<sub>*`Un readme général est disponible à la racine du git.`*</sub>

# Renoir et Blanc

Rendu de l'image. La quatrième étape, appelée Renoir Et Blanc, va depuis les contours de l'image déjà récupérés établir un k-d tree, qui servira à déterminer diverses manières de mettre en relation les pixels à dessiner. L'objectif est de dessiner via ce k-d tree les différents pixels en formant des lignes davantage humaines. Il faut abandonner le style "impression" de l'étape précédente, pour faire du trait par trait.


## Logique Algorithmique

Pour démarrer, nous allons répertorier les points à dessiner en les transformant en liste de coordonnées (list[tuple[int, int]]) depuis l'image binaire utilisée précédemment, ici tous les pixels noirs, de sorte à générer le k-d tree à l'aide de Scipy.

De sorte à humaniser, on selectionne un point de départ qui servira d'entrée du crayon, évitant ainsi de toujours démarrer dans la même direction.

Pour démarrer le dessin, on duplique la liste de points à dessiner, de sorte à tracer les points restants à dessiner, en omettant pas de supprimer le point de départ ni de le dessiner.

Ainsi, pour chaque point restant à dessiner on va rechercher les points restants triés par ordre de distance du point actuel, puis déterminer le point qui n'a pas encore été dessiné le plus proche.

On met ensuite à jour le point actuel au point qu'on a dessiné et on le retire des points restants à dessiner.

### Installation des dépendances

`python3 -m pip install -r ./requirements.txt`

### Lancement du programme

`python3 main.py`

paramètres utilisable :

`--name / -n` : corresponds au chemin d'une image voulu

`--lower / -l` : corresponds à la valeur du thresholds minimum ( conseillé entre 50 et 200 )

`--ratio / -r`   : corresponds au ratio qui permet d'avoir le thresholds maximum ( conseillé entre 2:1 et 3:1)

`--blur / -b` : permet de définir le blur voulu entre `classic` , `gaussian` et `median`

`--bintensity / -bi` : permet de définir l'intensité du blur ( chiffre impair uniquement )

exemple :

`python3 main.py --name ./images/lion.jpg --lower 100 --ratio 2 --blur gaussian --bintensity 3 --pixel 10`

ou

`python3 main.py -n ./images/lion.jpg -l 100 -r 2 -b gaussian -bi 3 -p 10`
