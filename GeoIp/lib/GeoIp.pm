package GeoIp;
use Dancer ':syntax';
use Dancer::Plugin::Database;
use DBI;
use Socket;

our $VERSION = '0.1';

sub ip2ipn {
  return unpack 'N', inet_aton(shift);
}

get '/' => sub {
    template 'index';
};

set serializer => 'JSON';
get '/geo2ip/:ip/' => sub {
  my $ipnumber = ip2ipn(params->{ip});
  my $sth = database->prepare("select l.country, l.region, l.city, l.postalCode, l.latitude, l.longitude from blocks as b, location as l where b.startIpNum < ? and b.endIpNum > ? and b.locId = l.locId");
  $sth->execute($ipnumber, $ipnumber);
  $sth->fetchrow_hashref();
};

true;
