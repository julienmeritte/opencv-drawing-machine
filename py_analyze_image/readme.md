<sub>*`Un readme général est disponible à la racine du git.`*</sub>

# Big Fernand Léger

Pré-processing de l'image. La première étape, appelée Big Fernand Léger, récupère les niveaux de gris d'une image et détoure ses contours à l'aide de l'algorithme de détection des bords conçu par John F. Canny. Puis affine les contours par seuillage d'image (Thresholding), une méthode permettant de remplacer les niveaux de gris et ressortir une image binaire déterminant un ensemble de pixels selon une valeur seuil.


### Installation du projet

`python3 -m pip install -r ./requirements.txt`

### Execution du projet

`python3 main.py`

paramètres utilisable :

`--name / -n` : corresponds au chemin d'une image voulu

`--lower / -l` : corresponds à la valeur du thresholds minimum ( conseillé entre 50 et 200 )

`--ratio / -r` : corresponds au ratio qui permet d'avoir le thresholds maximum ( conseillé entre 2:1 et 3:1)

exemple :

`python3 main.py --name ./images/licorne.png --lower 100 --ratio 2`

ou 

`python3 main.py -n ./images/licorne.png -l 100 -r 2`
