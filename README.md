# ExamCC2_TRUONGDavid_SAMAINJad

## Préparation
```
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip
hdfs dfs -put ml-25m/tags.csv
hdfs dfs -cat tags.csv | head -n 10

yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
sudo su root
yum install https://repo.ius.io/ius-release-el7.rpm https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
su - maria_dev
wget http://dl.fedoraproject.org/pub/archive/epel/7/x86_64/Packages/e/epel-release-7-14.noarch.rpm
sudo rpm -ivh epel-release-7-14.noarch.rpm
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