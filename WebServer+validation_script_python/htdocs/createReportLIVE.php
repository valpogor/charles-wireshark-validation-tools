<?php
$command = escapeshellcmd('python validation_report.py');
$output = shell_exec($command);
echo $output;
$files = glob('uploadsLIVE/*'); // get all file names
foreach($files as $file){ // iterate files
  if(is_file($file))
    unlink($file); // delete file
}
echo "Report created in ";
echo '<a href="http://10.0.0.77:8888/reportsLIVE/">folder</a>';
?>