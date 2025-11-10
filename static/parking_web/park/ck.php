  <?php
extract($_REQUEST);

/*if($a=="1")
{
$f2=fopen("log.txt","w");
fwrite($f2,"1");
$msg="Accepted";
}*/
/*else if($a=="1")
{
$f2=fopen("log.txt","w");
fwrite($f2,"2");
$msg="Rejected";
}
else
{
$f2=fopen("log.txt","w");
fwrite($f2,"3");
$msg="";
}*/
if(isset($btn3))
{
//accept
$val="1-".$amount;
$f2=fopen("log.txt","w");
fwrite($f2,$val);
?>
<script language="javascript">
window.location.href="ck.php?bc=<?php echo $bc; ?>&act=success";
</script>
<?php
}
if(isset($btn2))
{
//reject
$val="2-0";
$f2=fopen("log.txt","w");
fwrite($f2,$val);
?>
<script language="javascript">
window.location.href="ck.php?bc=<?php echo $bc; ?>&act=reject";
</script>
<?php
}
?><html>
  <head>
    <title>Smart Parking</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <link href="https://fonts.googleapis.com/css?family=Poppins:200,300,400,500,600,700,800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/open-iconic-bootstrap.min.css">
    <link rel="stylesheet" href="css/animate.css">
    
    <link rel="stylesheet" href="css/owl.carousel.min.css">
    <link rel="stylesheet" href="css/owl.theme.default.min.css">
    <link rel="stylesheet" href="css/magnific-popup.css">

    <link rel="stylesheet" href="css/aos.css">

    <link rel="stylesheet" href="css/ionicons.min.css">

    <link rel="stylesheet" href="css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="css/jquery.timepicker.css">

    
    <link rel="stylesheet" href="css/flaticon.css">
    <link rel="stylesheet" href="css/icomoon.css">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    
	  <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
	    <div class="container">
	      <a class="navbar-brand" href="../templates/index.html">Smart <span>Parking</span></a>
	      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
	        <span class="oi oi-menu"></span> Menu
	      </button>

	      <div class="collapse navbar-collapse" id="ftco-nav">
	        <ul class="navbar-nav ml-auto">
	          <li class="nav-item active"><a href="/userhome" class="nav-link">Home</a></li>
	         
	        </ul>
	      </div>
	    </div>
	  </nav>
    <!-- END nav -->
    
    <section class="hero-wrap hero-wrap-2 js-fullheight" style="background-image: url(images/sp1.png);" data-stellar-background-ratio="0.5">
      <div class="overlay"></div>
      <div class="container">
        <div class="row no-gutters slider-text js-fullheight align-items-end justify-content-start">
          <div class="col-md-9 ftco-animate pb-5">
          
            <h1 class="mb-3 bread"></h1>
          </div>
        </div>
      </div>
    </section>

    <section class="ftco-section contact-section">
      <div class="container">
        <div class="row d-flex mb-5 contact-info">
        	<div class="col-md-4">
        		<div class="row mb-5">
		          <div class="col-md-12">
		          	<div class="border w-100 p-4 rounded mb-2 d-flex">
			          	<div class="icon mr-3">
			          		<span class="icon-map-o"></span>
			          	</div>
			            <p><span>Smart </span> Parking System</p>
			          </div>
		          </div>
		          
		        </div>
          </div>
          <div class="col-md-8 block-9 mb-md-5">
		  <h3>Verification</h3>
		 
            <form name="form1" method="post" class="bg-light p-5 contact-form">
              <div class="col-md-12">
			  <p align="center"><img src="upload/<?php echo $bc; ?>.png" /></p>
              </div>
             
              
              <p>&nbsp;</p>
			  <?php
						if($act=="")
						{
						?>
						<p align="center">
						
						<input name="btn" type="submit" class="btn btn-primary py-3 px-5" value="Accept">&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp; 
						
						<input type="submit" name="btn2" class="btn btn-primary py-3 px-5" value="Reject"></p>
						<?php
						}
						?>
						
						<?php
						if(isset($btn))
						{
						$val="accept-1";
						$f2=fopen("log.txt","w");
						fwrite($f2,$val);
						
						}
						?>
						
						<?php
						if($act=="success")
						{
						?>
						<span style="color:#009900">Accepted..</span>
						<?php
						}
						if($act=="reject")
						{
						?>
						<span style="color:#FF0000">Rejected!</span>
						<?php
						}
						?>
            </form>
       
          </div>
        </div>
        
      </div>
    </section>
	

    <footer class="ftco-footer ftco-bg-dark ftco-section">
      <div class="container">
        
        <div class="row">
          <div class="col-md-12 text-center">

            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
  Smart Parking <a href="https://colorlib.com" target="_blank"></a>
  <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
          </div>
        </div>
      </div>
    </footer>
    

  <script src="js/jquery.min.js"></script>
  <script src="js/jquery-migrate-3.0.1.min.js"></script>
  <script src="js/popper.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/jquery.easing.1.3.js"></script>
  <script src="js/jquery.waypoints.min.js"></script>
  <script src="js/jquery.stellar.min.js"></script>
  <script src="js/owl.carousel.min.js"></script>
  <script src="js/jquery.magnific-popup.min.js"></script>
  <script src="js/aos.js"></script>
  <script src="js/jquery.animateNumber.min.js"></script>
  <script src="js/bootstrap-datepicker.js"></script>
  <script src="js/jquery.timepicker.min.js"></script>
  <script src="js/scrollax.min.js"></script>
  <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBVWaKrjvy3MaE7SQ74_uJiULgl1JY0H2s&sensor=false"></script>
  <script src="js/google-map.js"></script>
  <script src="js/main.js"></script>
    
  </body>
</html>