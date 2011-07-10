# server_version.py - retrieve and display database server version

import MySQLdb, sys

if len(sys.argv) < 2:
    print "Call: python %s ip-addr" % sys.argv[0]
    exit(1)

ip = sys.argv[1]
b = ip.strip().split('.')
if len(b) != 4:
    print "Wrong IP"
    exit(1)

for i in range(4):
    b[i] = int(b[i])

ipNum = b[3] + b[2] * 256 + b[1] * 256 * 256 + b[0] * 256 * 256 * 256

conn = MySQLdb.connect (host = "127.0.0.1",
                           user = "root",
                           passwd = "",
                           db = "geoip")
cursor = conn.cursor ()
cursor.execute ("""
select 
    l.country, l.region, l.city, l.postalCode, 
    l.latitude, l.longitude i
from 
    blocks as b, 
    location as l 
where 
    b.startIpNum < %s and 
    b.endIpNum > %s and 
    b.locId = l.locId
""", (ipNum, ipNum))
row = cursor.fetchone ()
print row
cursor.close ()
conn.close ()
