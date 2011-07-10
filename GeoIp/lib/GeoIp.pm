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
  my $sth = database->prepare("select l.country, l.region, l.city, l.postalCode, l.latitude, l.longitude from blocks as b left join location as l on (b.locId = l.locId) where b.endIpNum >= ? limit 1");
  $sth->execute($ipnumber);
  $sth->fetchrow_hashref();
};

true;
