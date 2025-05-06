# ExamCC2_TRUONGDavid_SAMAINJad

## Préparation
```
wget https://files.grouplens.org/datasets/movielens/ml-25m.zip
unzip ml-25m.zip
hdfs dfs -put ml-25m/tags.csv
hdfs dfs -cat tags.csv | head -n 10

yum-config-manager --save --setopt=HDP-SOLR-2.6-100.skip_if_unavailable=true
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && sudo python get-pip.py 
pip install pathlib && pip install mrjob==0.7.4 && pip install PyYAML==5.4.1

curl -O https://update.cs2c.com.cn/Mirror/centos/7/os/x86_64/Packages/nano-2.3.1-10.el7.x86_64.rpm && sudo rpm -ivh nano-2.3.1-10.el7.x86_64.rpm      
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