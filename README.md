# ExamCC2_TRUONGDavid_SAMAINJad

## A) Préparation

1) Téléchargement des fichiers nécessaires
```
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip
```

2) Push des données dans HDFS
```
hdfs dfs -put ml-25m/tags.csv
hdfs dfs -cat tags.csv | head -n 10
```

3) Config de l'OS
```
yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
```

4) Installation de python et des packages nécessaires
```
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && sudo python get-pip.py 
pip install pathlib && pip install mrjob==0.7.4 && pip install PyYAML==5.4.1
```

5) Installation de nano
```
curl -O https://update.cs2c.com.cn/Mirror/centos/7/os/x86_64/Packages/nano-2.3.1-10.el7.x86_64.rpm && sudo rpm -ivh nano-2.3.1-10.el7.x86_64.rpm      
```

## B) Avec la configuration par défaut de Hadoop

1. Combien de tags chaque film possède-t-il ?
```
rm MovieTagCount.py &&
wget https://raw.githubusercontent.com/JadSamain/ExamCC2_TRUONGDavid_SAMAINJad/refs/heads/main/MovieTagCount.py &&
python MovieTagCount.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/tags.csv > MovieTagCount.txt
```
Dans notre jeu de données, chaque ligne représente un tag ajouté par un utilisateur à un film, à une date précise. Autrement dit, une ligne = un tag associé à un film, par un utilisateur.
Pour compter combien de tags chaque film possède, voici les étapes :
Mapper :

Lors du mapping, on lit chaque ligne et on en extrait l’identifiant du film (movieID).
À chaque fois qu’on rencontre un film, on émet la paire (movieID, 1) pour indiquer qu’il a reçu un tag.
🔹 Reducer :

Dans l’étape de réduction, on regroupe toutes les paires ayant le même movieID, puis on additionne les 1.
Cela nous donne le nombre total de tags associés à chaque film.

2. Combien de tags chaque utilisateur a-t-il ajoutés ?
```
rm UserTagCount.py &&
wget https://raw.githubusercontent.com/JadSamain/ExamCC2_TRUONGDavid_SAMAINJad/refs/heads/main/UserTagCount.py &&
python UserTagCount.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar hdfs:///user/maria_dev/tags.csv > UserTagCount.txt
```

## C) Avec la configuration de Hadoop suivante (taille du bloc par défaut et taille du bloc = 64 Mo)

3. Combien de blocs le fichier occupe-t-il dans HDFS dans chacune des configurations ?

Par défaut :
```
hdfs fsck /user/maria_dev/tags.csv -files -blocks
```

Résultat
```
Status: HEALTHY
 Total size:    38810332 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 38810332 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Wed Mar 26 11:44:49 UTC 2025 in 30 milliseconds
```
On obtient un seul bloc avec le fichier tags.csv car la taille du fichier est de 37 mo alors que la taille par défaut est de 128 mo. Il est donc normal qu'on ai un seul bloc.

Config 64 mo :
```
hdfs dfs -D dfs.blocksize=67108864 -put tags.csv
hdfs fsck /user/maria_dev/tags.csv -files -blocks
```

Résultat
```
Status: HEALTHY
 Total size:    38810332 B
 Total dirs:    0
 Total files:   1
 Total symlinks:                0
 Total blocks (validated):      1 (avg. block size 38810332 B)
 Minimally replicated blocks:   1 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)
 Number of data-nodes:          1
 Number of racks:               1
FSCK ended at Wed Mar 26 11:44:49 UTC 2025 in 30 milliseconds
```
D'après le résultat du cmd, le "Total blocks" est de 1. Le fichier faisant 37Mo, soit inférieur à notre condition de 64Mo, 1 seul bloc est utilisé.

4. Combien de fois chaque tag a-t-il été utilisé pour taguer un film ?
```
```

5. Bonus : Pour chaque film, combien de tags le même utilisateur a-t-il introduits ?
```
```
