#!/usr/bin/perl -T
use strict;
use warnings;
use 5.008;
 
use Data::Dumper;
use CGI;
my $q = CGI->new;
#my $conf = CGI::Application::Plugin::Config::Context->get_current_context;
my %data;
$data{name} = $q->param('name');
$data{email} = $q->param('email');
$data{message} = $q->param('message');
 
#print $conf;
print $q->header;
if ($data{name} !~ /^[\s\w.-]+$/) {
	print "Name must contain only alphanumerics, spaces, dots and dashes.";
	exit;
}
 
# print "response " . Dumper \%data;
# print "Mail sent successfully";

# my %data;
# $data{name} = $q->param('name');
# $data{email} = $q->param('email');
# $data{message} = $q->param('message');

# if ($data{name} !~ /^[\s\w.-]+$/) {
#	print "Name must contain only alphanumerics, spaces, dots and dashes.";
#	exit;
# }

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
				
				<h1>Email Sent Successfully !!! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br></h1>
				<h2>Thanks for getting in touch with us. We will contact you shortly...<br></h2>	
				 <p>&nbsp;</p>
				</div>
			
		<br>
<br>
<br>
<br>
<ul>
<li>
<a href = "http://cs99.bradley.edu/~ysarwadia/site/Contacts.html">Back</a>
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


       









