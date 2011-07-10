# server_version.py - retrieve and display database server version

import MySQLdb

conn = MySQLdb.connect (host = "127.0.0.1",
                           user = "root",
                           passwd = "",
                           db = "geoip")
cursor = conn.cursor ()

f = open("GeoLiteCity-Blocks.csv", 'r')
lines = f.readlines()
f.close()

i = 0
for line in lines:
    b = line.strip().split(',')
    if len(b) == 3 and line[0] == '"':
        cursor.execute ("insert into blocks values (%s,%s,%s)",
                (b[0][1:-1], b[1][1:-1], b[2][1:-1]))
        i += 1

print "%d Blocks inserted" % i

f = open("GeoLiteCity-Location.csv", 'r')
lines = f.readlines()
f.close()

i = 0
for line in lines:
    b = line.strip().split(',')
    if len(b) > 6 and b[0] != 'locId':
        metroCode = 0
        areaCode = 0
        if len(b) > 7 and b[7] != '':
            metroCode = int(b[7])
        if len(b) > 8 and b[8] != '':
            areaCode = int(b[8])
        cursor.execute ("insert into location values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (b[0], b[1][1:-1], b[2][1:-1], b[3][1:-1], b[4][1:-1], b[5], b[6], metroCode, areaCode))
        i += 1

print "%d Locations inserted" % i

cursor.close ()
conn.close ()

