<html>
<head>
	<title>Never look at me</title>
</head>
<body>

<?php
function formatJSON($sensor_data)
{
	$data = array();
	$data["sensor1"] = $sensor_data[0];
	$data["sensor2"] = $sensor_data[1];
	//$data["sensor3"] = 0;

	return $data
}

function writeSignal($signal)
{
	$f = fopen("sensor.json", 'w') or die("Failed to create file");
	fwrite($f, $signal) or die("Could not write to file");
	fclose($f);
}

$posted_data = $_POST['sensor_status'];
$json_data = formatJSON($posted_data);
writeSignal($json_data);
echo "Signal data written successfully";





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


