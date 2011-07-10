Project GeoIP.
==============

This project is about making a location available as accurate as possible
to IP adresses. It base on GeoLite City from MaxMind. 

Installation
------------

First, download the GeoLite City in latest version from folllowing site:

    http://www.maxmind.com/app/geolitecity

We need it in csv format, which is about 117 MB in blocks and 16 MB in
locations. The data get updated regulary by MaxMind - so you can clean
your database and import it again at any time. The link to the zip file
is here:

    http://geolite.maxmind.com/download/geoip/database/GeoLiteCity_CSV/GeoLiteCity_20110705.zip

On update, you need to clean both tables in MySQL. On first install, you
can create the tabled with the mysql_geoip.sql script.

    mysql -u root -psecret geoip < mysql_geoip.sql

To import and test the locacation service, python and mysql module for
python is required. The import.py expect the two csv files to be in the
same directory. Depending in the speed of the database, it takes a while
to import over 3 mio blocks and ~350 k locations.

At this point, we can use the location.py script to test our service. The
script is called the following way:

    python location.py 123.234.243.132

The result will be printed to console as an array. Of couse, you can use
it already this way, but we have a web service too. The WebService is
done on Perl Dancer. On Debian, you need the packeage 
libdancer-plugin-database-perl too. For regulary use, configure the 
project as FastCGI to you favorite web server. To test the service, you
can call the app.pl script in bin directory to start a perl web server
from dancer on port 3000.

    http://localhost:3000/

The form is simple. Give it a IP adress and get the country and if 
available, the city and GPS location too. The form use JQuery to make
an ajax call to /geo2ip/:ip/ and print the result below. It also
create a img tag with a cooked URL to Google Maps.

This project is licenced under GPLv3. Send me feedback or report bugs
to jens at nons dot de. I love to hear, what you use it for.

