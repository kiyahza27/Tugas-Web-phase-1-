from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

session.set_keyspace('datauser')

#untuk memnjalankan program ini harus menjalankan cassandra.bat -f nya terlebih dahulu di command prompt(run as admin)
