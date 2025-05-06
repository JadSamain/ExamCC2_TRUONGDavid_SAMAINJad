# ExamCC2_TRUONGDavid_SAMAINJad

## Préparation
```
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip
hdfs dfs -put ml-25m/tags.csv
hdfs dfs -cat | head -n 10
```

## Avec la configuration par défaut de Hadoop

1. Combien de tags chaque film possède-t-il ?
```
```

2. Combien de tags chaque utilisateur a-t-il ajoutés ?
```
```

## Avec la configuration de Hadoop suivante (taille du bloc par défaut et taille du bloc = 64 Mo)

3. Combien de blocs le fichier occupe-t-il dans HDFS dans chacune des configurations ?
```
```

4. Combien de fois chaque tag a-t-il été utilisé pour taguer un film ?
```
```