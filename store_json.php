<html>
<head>
	<title>Never look at me</title>
</head>
<body>

<?php
function formatJSON($sensor1, $sensor2)
{
	$data = array();
	$data['sensor1'] = $sensor1;
	$data['sensor2'] = $sensor2;
	//$data["sensor3"] = 0;
	$formattedData = json_encode($data);
	return $formattedData;
}

function writeSignal($signal)
{
	$f = fopen('sensor.json', 'w') or die('Failed to create file');
	fwrite($f, $signal) or die('Could not write to file');
	fclose($f);
}

/*$posted_data = $_POST['sensor1'];
$post_data2 = $_POST['sensor2'];
$post_array = array($posted_data, $post_data2);
$f2 = fopen('text.txt', 'w');
fwrite($f2, $post_array);
fclose($f2);*/

$json_data = formatJSON($_POST['sensor1'], $_POST['sensor2']);
writeSignal($json_data);
//echo "Signal data written successfully";





/*print_r ($_POST);*/
//$REQUESTS or _REQUEST or $POST
/*if(evaluate_signal($current_status) == 0)
{
	echo "<svg width='120' height='210'>
  	<rect width='100' height='200' style='fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)'/>
	</svg>";	
}
else 
{
	echo "<svg width='120' height='210'>
  	<rect width='100' height='200' style='fill:rgb(0,0,0);stroke-width:3;stroke:rgb(0,0,0)'/>
	</svg>";		
}*/

/*function evaluate_signal($signal)
{
	if($signal === 0)
	{
		return FALSE;
	}
	elseif($signal === 1) 
	{
		return TRUE; 
	}
	else 
	{
		echo "Bad signal, unable to read";
	}
}*/
?>
</body>
</html>


