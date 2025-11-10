<?php
//include("dbconnect.php");
extract($_REQUEST);




	// requires php5
	define('UPLOAD_DIR', 'upload/');
	
	$f1=fopen("img.txt","r");
$r=fread($f1,filesize("img.txt"));



$filename = $bc.'.png';

/*$q1=mysqli_query($connect,"select * from atm_face where bcode='$bc'");
$n1=mysqli_num_rows($q1);
if($n1==0)
{
$mq=mysqli_query($connect,"select max(id) from atm_face");
$mr=mysqli_fetch_array($mq);
$id=$mr['max(id)']+1;

$qry=mysqli_query($connect,"insert into atm_face(id,bcode,imgname) values($id,'$bc','$filename')");

}
else
{

}*/

$vv=$r+1;
$f2=fopen("img.txt","w");
fwrite($f2,$vv);

$f3=fopen("log.txt","w");
fwrite($f3,"3-0");

	$img = $_POST['imgBase64'];
	$img = str_replace('data:image/png;base64,', '', $img);
	$img = str_replace(' ', '+', $img);
	$data = base64_decode($img);
	$file = UPLOAD_DIR . $filename; //uniqid() . '.png';
	$success = file_put_contents($file, $data);
	print $success ? $file : 'Unable to save the file.';
?>