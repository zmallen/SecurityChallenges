<?php
#echo $_SERVER['HTTP_USER_AGENT'] . "\n\n";
if(preg_match("/iPhone|Android|BlackBerry|PlayBook/",$_SERVER['HTTP_USER_AGENT'])) {
	echo 'Mobile web surfing? Dont you have something better to do?!';
	echo 'md5 "garbageplate" to redeem your points';
}else {
	echo '<object width="425" height="350" data="http://www.youtube.com/v/KHy7DGLTt8g" type="application/x-shockwave-flash"><param name="src" value=http://www.youtube.com/v/KHy7DGLTt8g"/></object>';

}
?>
