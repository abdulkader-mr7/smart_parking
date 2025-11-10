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
?>
<html>
<head>

  <!-- Basic Page Needs
  ================================================== -->
  <meta charset="utf-8">
  <title>Smart ATM</title>

  <!-- Mobile Specific Metas
  ================================================== -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="description" content="Bootstrap App Landing Template">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <meta name="author" content="Themefisher">
  <meta name="generator" content="Themefisher Small Apps Template v1.0">

  <!-- Favicon -->
  <link rel="shortcut icon" type="image/x-icon" href="../static/images/favicon.png" />
  
  <!-- PLUGINS CSS STYLE -->
  <link rel="stylesheet" href="plugins/bootstrap/bootstrap.min.css">
  <link rel="stylesheet" href="plugins/themify-icons/themify-icons.css">
  <link rel="stylesheet" href="plugins/slick/slick.css">
  <link rel="stylesheet" href="plugins/slick/slick-theme.css">
  <link rel="stylesheet" href="plugins/fancybox/jquery.fancybox.min.css">
  <link rel="stylesheet" href="plugins/aos/aos.css">

  <!-- CUSTOM CSS -->
  <link href="css/style.css" rel="stylesheet">
<script language="javascript">
function validate()
{
    if(document.form1.password.value=="")
    {
	alert("Enter Your Pin No.");
	document.form1.password.focus();
	return false;
	}
	if(document.form1.password.value.length!=4)
    {
	alert("Incorrect Pin No.");
	document.form1.password.select();
	return false;
	}
	return true;
}
function getpin(id)
{
var x;
x=document.form1.password.value+id;
document.form1.password.value=x;
}	
	

</script>
<style type="text/css">
<!--
.st1 {
	font-size: 24px;
	font-style: italic;
	font-weight:bold;
	color:#CCCCCC;
  text-shadow: 2px 2px 9px #ffffff;
}
.st2
{
  border-radius: 25px;
  background:#003399;
  padding: 20px;
}
.st3
{
  border-radius: 25px;
  background:#FFFFFF;
  padding: 20px;
}
.st4
{
  border-radius: 25px;
  background:#003399;
  padding: 10px;
}
.txt1
{
	color:#003366;
	font-weight:bold;
	font-family:Arial, Helvetica, sans-serif;
	font-size: 16px;
	font-variant: small-caps;

}
-->
</style>
</head>

<body class="body-wrapper" data-spy="scroll" data-target=".privacy-nav">



<!--====================================
=            Hero Section            =
=====================================-->
<section class="section gradient-banner">
	
	<div class="container">
		<div class="row align-items-center">
			<div class="col-md-6 order-2 order-md-1 text-center text-md-left">
				<div class="st4 image align-self-center"><img class="img-fluid" src="atm4.jpg"
							alt="desk-image"></div>
				<p class="text-white mb-5"></p>
				
			</div>
			<div class="col-md-6 text-center order-1 order-md-2">
					
					<div class="block">
					<div class="st3 content text-center">
					
						<div class="logo">
							<a href="/"><img src="logo2.png" alt=""></a>
						</div>
						<div class="title-text">
						<h3 align="center">Verification</h3>
						</div>
						
						<div class="title-text">
						<img src="upload/<?php echo $bc; ?>.png" />
						</div>
						<form name="form1" method="post">
						
						<?php
						if($act=="")
						{
						?>
						<p align="center">
						
						<input name="btn" type="submit" class="btn btn-main-sm" value="Accept">&nbsp;&nbsp;&nbsp; /&nbsp;&nbsp; 
						
						<input type="submit" name="btn2" class="btn btn-main-sm" value="Reject"></p>
						<?php
						}
						?>
						</form>
						<form name="form2" method="post">
						<?php
						if(isset($btn))
						{
						$val="accept-1";
						$f2=fopen("log.txt","w");
						fwrite($f2,$val);
						?>
						<input class="form-control main" type="text" name="amount" placeholder="Enter Amount" maxlength="5" required>
						
						<input type="submit" name="btn3" class="btn btn-main-sm" value="Withdraw Cash">
						<?php
						}
						?>
						
						<?php
						if($act=="success")
						{
						?>
						<span style="color:#009900">Cash Withdraw Success..</span>
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
		</div>
	</div>
</section>
<!--====  End of Hero Section  ====-->

<section class="section pt-0 position-relative pull-top">
	<div class="container">
		<div class="rounded shadow p-5 bg-white">
			<div class="row">
				<div class="col-lg-4 col-md-6 mt-5 mt-md-0 text-center">
					<i class="ti-paint-bucket text-primary h1"></i>
					<h3 class="mt-4 text-capitalize h5 ">Smart ATM</h3>
					<p class="regular text-muted">Smart ATMs are automated teller machines (ATMs) that have more functionality than simply dispensing cash.</p>
				</div>
				<div class="col-lg-4 col-md-6 mt-5 mt-md-0 text-center">
					<i class="ti-shine text-primary h1"></i>
					<h3 class="mt-4 text-capitalize h5 ">Face Recognition</h3>
					<p class="regular text-muted">Face recognition technology helps the machine to identify each and every user uniquely thus making face as a key.</p>
				</div>
				<div class="col-lg-4 col-md-12 mt-5 mt-lg-0 text-center">
					<i class="ti-thought text-primary h1"></i>
					<h3 class="mt-4 text-capitalize h5 ">Magic PIN</h3>
					<p class="regular text-muted">Features like face recognition and Magic PIN are used for the enhancement of security</p>
					</p>
				</div>
			</div>
		</div>
	</div>
</section>

<!--==================================
=            Feature Grid            =
===================================-->



<!--====  End of Feature Grid  ====-->

<!--==============================
=            Services            =
===============================-->

<!--====  End of Services  ====-->


<!--=================================
=            Video Promo            =
==================================-->

<!--====  End of Video Promo  ====-->

<!--=================================
=            Testimonial            =
==================================-->

<!--====  End of Testimonial  ====-->



<!--============================
=            Footer            =
=============================-->
<footer>
  <div class="footer-main">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-md-12 m-md-auto align-self-center">
          <div class="block">
            <a href="index.html"><img src="images/logo.png" alt="footer-logo"></a>
            <!-- Social Site Icons -->
            <ul class="social-icon list-inline">
              <li class="list-inline-item">
                <a href="https://www.facebook.com/themefisher"><i class="ti-facebook"></i></a>
              </li>
              <li class="list-inline-item">
                <a href="https://twitter.com/themefisher"><i class="ti-twitter"></i></a>
              </li>
              <li class="list-inline-item">
                <a href="https://www.instagram.com/themefisher/"><i class="ti-instagram"></i></a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
          <div class="block-2">
            <!-- heading -->
            <!--<h6>Product</h6>-->
            <!-- links -->
            <ul>
              <li><a href="/">Home</a></li>
              <!--<li><a href="blog.html">Blogs</a></li>
              <li><a href="FAQ.html">FAQs</a></li>-->
            </ul>
          </div>
        </div>
        <div class="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
          <div class="block-2">
            <!-- heading -->
            <!--<h6>Resources</h6>-->
            <!-- links -->
            <ul>
              <li><a href="">ATM</a></li>
              <!--<li><a href="sign-in.html">Login</a></li>
              <li><a href="blog.html">Blog</a></li>-->
            </ul>
          </div>
        </div>
        <div class="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
          <div class="block-2">
            <!-- heading -->
            <!--<h6>Company</h6>-->
            <!-- links -->
           <ul>
              <li><a href="">Sign-Up</a></li>
              <!--<li><a href="contact.html">Contact</a></li>
              <li><a href="team.html">Investor</a></li>
              <li><a href="privacy.html">Terms</a></li>-->
            </ul>
          </div>
        </div>
        <div class="col-lg-2 col-md-3 col-6 mt-5 mt-lg-0">
          <div class="block-2">
            <!-- heading -->
            <!--<h6>Company</h6>-->
            <!-- links -->
            <ul>
              <li><a href="">Admin</a></li>
              <!--<li><a href="contact.html">Sign Up</a></li>
              <li><a href="team.html">Admin</a></li>-->
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="text-center bg-dark py-4">
    <small class="text-secondary">Smart ATM <a href="https://themefisher.com/"></a></small class="text-secondary">
  </div>
</footer>


  <!-- To Top -->
  <div class="scroll-top-to">
    <i class="ti-angle-up"></i>
  </div>
  
  <!-- JAVASCRIPTS -->
  <script src="plugins/jquery/jquery.min.js"></script>
  <script src="plugins/bootstrap/bootstrap.min.js"></script>
  <script src="plugins/slick/slick.min.js"></script>
  <script src="plugins/fancybox/jquery.fancybox.min.js"></script>
  <script src="plugins/syotimer/jquery.syotimer.min.js"></script>
  <script src="plugins/aos/aos.js"></script>
  <!-- google map -->
  <script src="../static/js/script.js"></script>
</body>

</html>