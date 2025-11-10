<?php

// new filename
//$filename = 'pic_'.date('YmdHis') . '.jpeg';
$f1=fopen("img.txt","r");
$r=fread($f1,filesize("img.txt"));

$filename = 'img'.$r.'.jpg';

$vv=$r+1;
$f2=fopen("img.txt","w");
fwrite($f2,$vv);

$url = '';
if( move_uploaded_file($_FILES['webcam']['tmp_name'],'upload/'.$filename) ){
	$url = 'http://' . $_SERVER['HTTP_HOST'] . dirname($_SERVER['REQUEST_URI']) . '/upload/' . $filename;
}

// Return image url
echo $url;