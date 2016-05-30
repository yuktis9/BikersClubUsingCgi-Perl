#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Fcntl qw(:flock :seek);
use strict;

print "Content-type: text/html\n\n";

my $passfile = 'passwd.txt';

print start_html("Registration Results");

my $cgi = new CGI;

            my $Uname = $cgi->param( "Uname" );
            my $password1 = $cgi->param( "pword1" );

# my $encpass = &encrypt($password1);
# &dienice("Half script read");

my $salt = "21";
my $enpass = crypt($password1,$salt);

open(PASSF,"+<$passfile") or &dienice("Can't open Details file.");
flock(PASSF, LOCK_EX);          # lock the file (exclusively)
seek(PASSF, 0, SEEK_SET);       # return to the beginning
my @passf = <PASSF>;            # read entire file

# the structure of the file is:
# username:passwd:email
# username:passwd:email
# with each user's record on a separate line.
# here we're going to loop through and make sure the new username
# doesn't already exist in the file.


my $flag = "true";

foreach my $i (@passf) {
    chomp($i);
    my ($User,$pass) = split(/:/,$i);
    if ($User eq $Uname && $pass eq $enpass) {

	$flag = "false";
seek(PASSF, 0, SEEK_END);       # go to EOF
close(PASSF);
   }

}


if($flag eq "true"){

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

  
				
				
				

<!--header end-->
<!--content -->
		

<br>
<ul>
<li></div>
<h2>Username/Password did not match</h2>
<a href = "http://cs99.bradley.edu/~ysarwadia/site/Login.html">Click Here to Login Again</a><br></li></ul>
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

}else{

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

  <h3>Welcome $Uname to Biker's Club. Below are some fun making stuff for you </h3>
				
				
				

<!--header end-->
<!--content -->
		
		<div class="bg1">
			<div class="main">
				<article id="content2">
					<div class="wrapper">
						<h3>&nbsp;</h3>
					    <div class="col1 marg_right1">
						<a href="#" class="button1"></a>
							<h3 class="color1"><a href = 'http://cs99.bradley.edu/~ysarwadia/site/Craps.html'> Craps Game</a></h3>
							<p>Craps is a dice game in which the players make wagers on the outcome of the roll, or a series of rolls, of a pair of dice.</p>
						  <a href="#" class="button1"></a>	
					</div>
					    <div class="col1">
							<h3 class="color1"><a href = 'http://cs99.bradley.edu/~ysarwadia/site/BlackJack.html'>Black Jack </a></h3>
							<p>Play casino famous Black Jack Game and have fun. </p>
						<a href="#" class="button1"></a>						</div>
					  <div class="col1 marg_right1">
							<h3 class="color1"><a href = 'http://cs99.bradley.edu/~ysarwadia/site/animationlist.html'>Events	</a></h3>
							<p>Check the upcomming events where you can enjoy and have fun with family and friends. </p>
					    <a href="#" class="button1"></a>						</div>
						<div class="col1 marg_right1">
							<h3 class="color1"><a href = 'http://cs99.bradley.edu/~ysarwadia/site/draw.html'>Paint  Canvas</a> </h3>
							<p>Paint the canvas with the color of your choice. </p>
					     <a href="#" class="button1"></a>						</div>
						<div class="col1 marg_right1">
							<h3 class="color1"><a href = 'http://cs99.bradley.edu/~ysarwadia/site/Canvas.html'>Canvas Drawing</a> </h3>
							<p>Draw with the color of your choice. </p>
						<a href="#" class="button1"></a>						</div>
						
					</div>
				</article>
			</div>
		</div>
<br>
<br>
<br>
<br>
<ul>
<li></div>

<a href = "http://cs99.bradley.edu/~ysarwadia/site/Logout.html">Logout</a><br></li></ul>
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

}


#seek(PASSF, 0, SEEK_END);       # go to EOF
#print PASSF "$Uname:$password1\n";
#close(PASSF);



#print end_html;



sub dienice {
    my($msg) = @_;
    print "<h2>Error</h2>\n";
    print $msg;
    exit;
}
