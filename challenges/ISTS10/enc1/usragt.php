<?php
#echo $_SERVER['HTTP_USER_AGENT'] . "\n\n";
if(preg_match("/iPhone|Android|BlackBerry|PlayBook/",$_SERVER['HTTP_USER_AGENT'])) 
{
	echo '<img src="woot.jpg">';
}
else {
	echo '<object width="425" height="350" data="http://www.youtube.com/v/8ZcmTl_1ER8&autoplay=1" type="application/x-shockwave-flash"><param name="src" value="http://www.youtube.com/v/8ZcmTl_1ER8&autoplay=1"/></object>';

}
?>
