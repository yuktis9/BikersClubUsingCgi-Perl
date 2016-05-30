#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Fcntl qw(:flock :seek);
use File::Basename;
use strict;
use Data::Dumper;


# Image upload code starts here

$CGI::POST_MAX = 1024 * 5000;
my $safe_filename_characters = "a-zA-Z0-9_.-";
my $upload_dir = "/home/ysarwadia/public_html/upload";
my $query = new CGI;
my $filename = $query->param("photo");
if ( !$filename )
{
print $query->header ( );
print "There was a problem uploading your photo (try a smaller file).";
exit;
}
my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
$filename = $name . $extension;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;
if ( $filename =~ /^([$safe_filename_characters]+)$/ )
{
$filename = $1;
}
else
{
die "Filename contains invalid characters";
}
my $upload_filehandle = $query->upload("photo");
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;
while ( <$upload_filehandle> )
{
print UPLOADFILE;
}
close UPLOADFILE;

# Image upload code ends here


my $passfile = 'passwd.txt';
print header;
print start_html("Registration Results");
my $cgi = new CGI;

my %data;
$data{username} = $cgi->param('username');
$data{email} = $cgi->param('email');
$data{address} = $cgi->param('address');
$data{city} = $cgi->param('city');
$data{state} = $cgi->param('state');
$data{zip} = $cgi->param('zip');
$data{social_security} = $cgi->param('social_security');
$data{dob} = $cgi->param('date');
$data{age} = $cgi->param('age');

$ENV{PATH} = '';
sendmail(
     $data{email},
    'Bikers Club Message',
     'Hello'. Dumper(\%data),
    'Bikers Club <sarwadiayukti@gmail.com>');
 
sub sendmail {
    my ($tofield, $subject, $text, $fromfield) = @_;
    my $mailprog = "/usr/lib/sendmail";
 
    open my $ph, '|-', "$mailprog -t -oi" or die $!;
    print $ph "To: $tofield\n";
    print $ph "From: $fromfield\n";
    print $ph "Reply-To: $fromfield\n";
    print $ph "Subject: $subject\n";
    print $ph "\n";
    print $ph "$text";
    close $ph;
    return ;
}

my $username = $cgi->param( "username" );
my $password = $cgi->param( "password" ); 
my $email = $cgi->param( "email" );
my $address = $cgi->param( "address" );
my $city = $cgi->param( "city" );
my $state = $cgi->param( "country_name" );
my $zip = $cgi->param( "zip" );
my $home_phone = $cgi->param( "home_phone" );
my $work_phone = $cgi->param( "work_phone" );
my $social_security = $cgi->param( "social_security" );
my $maiden_name = $cgi->param( "maiden_name" );
my $dob = $cgi->param( "date" );
my $age = $cgi->param( "age" );
my $gender = $cgi->param( "gender" );

my @membership= $cgi->param( "activity");
my $membership2="";
foreach my $mem (@membership) {
   $membership2 .= "$mem ";
}

my @interests = $cgi->param( "interests" );
my $interests2="";
foreach my $interests (@interests) {
   $interests2 .= "$interests ";
}



my $salt = "21";
my $encpass = crypt($password,$salt);

open(PASSF,"+<$passfile") or &dienice("Can't open Details file.");
flock(PASSF, LOCK_EX);          # lock the file (exclusively)
seek(PASSF, 0, SEEK_SET);       # rewind to beginning
my @passf = <PASSF>;            # read entire file


seek(PASSF, 0, SEEK_END);       # go to EOF
print PASSF "$username:$encpass\n";
close(PASSF);



print <<END_HTML;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<html lang="en">
	<head>
		<title>Logged In</title>
		<meta charset="utf-8">
		
		<link rel="stylesheet" href="http://cs99.bradley.edu/~ysarwadia/site/css/reset.css" type="text/css" media="all">
		<link rel="stylesheet" href=http://cs99.bradley.edu/~ysarwadia/site/"css/layout.css" type="text/css" media="all">
		<link rel="stylesheet" href="http://cs99.bradley.edu/~ysarwadia/site/css/style.css" type="text/css" media="all">
		<link rel="stylesheet" href="http://cs99.bradley.edu/~ysarwadia/site/css/styles.css" type="text/css" media="all">
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/jquery-1.6.js" ></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/styles.js" ></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/cufon-yui.js"></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/cufon-replace.js"></script>  
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/Vegur_300.font.js"></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/PT_Sans_700.font.js"></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/PT_Sans_400.font.js"></script>
		<script type="text/javascript" src="http://cs99.bradley.edu/~ysarwadia/site/js/atooltip.jquery.js"></script>
        <script>
	
	
	$(function(){
      var slider = new BeaverSlider({
        structure: {
          container: {
            id: "my-slider",
            width: 720,
            height: 420
          }
        },
        content: {
          images: [
            "img/1.jpg",
            "img/2.jpg"
          ]
        },
        animation: {
          effects: effectSets["slider: big set 2"],
          interval: 1000
        }
      });   
	});
	
	</script>
	</head>
	<body id="page3">
		<div class="main">
<!--header -->
			<header>
				<div class="wrapper">
					<h1>BIKERS <span class="Logo">CLUB</span></h1>
					
				</div><nav>
				<div class='nav'>
				  <ul>
					<li><a href='http://cs99.bradley.edu/~ysarwadia/site/index.html'>Home</a>
					
					</li>
					<li><a href='http://cs99.bradley.edu/~ysarwadia/site/About.html'>About Us</a>
					
					 <ul>
					  <li><a href='http://cs99.bradley.edu/~ysarwadia/site/Membership.html'>Membership</a></li>
					  <li><a href='http://cs99.bradley.edu/~ysarwadia/site/Events.html'>Events</a></li>
					  </ul>
					 </li>
					
					<li><a href='http://cs99.bradley.edu/~ysarwadia/site/Gallery.html'>Gallery</a></li>
					
					<li><a href='http://cs99.bradley.edu/~ysarwadia/site/Login.html'>Login</a></li>
					<li><a href='http://cs99.bradley.edu/~ysarwadia/site/Contacts.html'>Contacts</a></li>
					
					<li class='lamp'><span></span></li>
				  </ul>
				</div>

				</nav>
			</header>
<!--header end-->
<!--content -->


<div class="wrapper">
				<H2> Your Details:</h2><br>
				</br>
				<img src="http://cs99.bradley.edu/~ysarwadia/upload/$filename" alt="Photo" height="200" width="200"  border="1" /></br>
				<br/>User Name: $username 
				<br/>Maiden Name: $maiden_name 
				<br/>Email: $email 
				<br/>Address: $address 
				<br/>City: $city 
				<br/>Country: $state 
				<br/>Zip: $zip 
				<br/>Home Phone: $home_phone  
				<br/>Work Phone: $work_phone 
				<br/>Social Security: $social_security 
				<br/>Membership type: $membership2
				<br/>Interest: $interests2
				<br/>DOB: $dob
				<br/>How long you have been Riding: $age years
                                <br/>Gender: $gender
			<br/>	<br/><h1>Details have been sent to your email Id</h1>
</div>
<br>
<br>
<br>
<br>
<ul>
<li>
<a href = "http://cs99.bradley.edu/~ysarwadia/site/Login.html">Login Here</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href = "http://cs99.bradley.edu/~ysarwadia/site/Register.html">Back</a><br></li></ul>
		<div class="main">
        
<!--content end-->


<!--footer -->
			<footer>
				<ul id="icons">
					<li class="first">Follow Us:</li>
					<li><a href="#" class="normaltip" title="Facebook"><img src="http://cs99.bradley.edu/~ysarwadia/site/images/icon1.jpg" alt=""></a></li>
					<li><a href="#" class="normaltip" title="Twitter"><img src="http://cs99.bradley.edu/~ysarwadia/site/images/icon2.jpg" alt=""></a></li>
					<li><a href="#" class="normaltip" title="Picasa"><img src="http://cs99.bradley.edu/~ysarwadia/site/images/icon3.jpg" alt=""></a></li>
					<li><a href="#" class="normaltip" title="YouTube"><img src="http://cs99.bradley.edu/~ysarwadia/site/images/icon4.jpg" alt=""></a></li>
				</ul>
               
				
			  <!-- {%FOOTER_LINK} -->
		  </footer>
<!--footer end-->
	</div>
		<script type="text/javascript"> Cufon.now(); </script>
	</body>
</html>





END_HTML



sub dienice {
    my($msg) = @_;
    print "Error\n";
    print $msg;
    exit;
}
