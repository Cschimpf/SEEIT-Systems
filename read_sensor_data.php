<?php

// open file for reading 
$file_name = 'sensor.json';
$file_handle = fopen($file_name, 'r');

// read file content
$file_content = fread($file_handle, filesize($file_name));

// possibly process file content in some way

// output results
echo $file_content;

?>