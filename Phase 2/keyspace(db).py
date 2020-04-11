from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

db.set_keyspace('datauser')
session.execute("CREATE TABLE customer (nomor_hp text, username text PRIMARY KEY, password text, nama text)")
session.execute("CREATE TABLE admin (nomor_hp text, username text PRIMARY KEY, password text, nama text)")

session.execute("CREATE TABLE datatransaksi (id_payment bigint PRIMARY KEY, username text,\
                    tanggal_transaksi date, nomor_hp text, nomor_meteran text, jenis_pembelian text)")


session.execute("INSERT INTO admin (username, nama, password, nomor_hp) VALUES (%s, %s, %s, %s)",
                ("admin1", "zakiyah", "admin1001", "08199887766"))

session.execute("INSERT INTO customer (username, nama, password, nomor_hp) VALUES (%s, %s, %s, %s)",
                ("lia10", "lia", "lia001", "081122334455"))


results = session.execute("SELECT * FROM admin")row = results[0]
print row.username, row.nama, row.password, row.nomor_hp

