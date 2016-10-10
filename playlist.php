<html>
<head>
	<title>MUSIC</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width-device-width, initial-scale=1">
	<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body background="bg3.jpg">
<center><h1>CANCIONES SONANDO Y EN ESPERA<h1></center>
<center><a href="index.php" type="button" class="btn btn-default" aria-label="Left Align">
  <span class="glyphicon glyphicon-list" aria-hidden="true"></span>  HOME
</a></center>
<center>
</center>
<div class="container">
	<h2>Lista de reproduccion actual</h2>
	<p>Canciones : </p>
	<form action="<?php $_PHP_SELF ?>" method="POST">
   		<table class="table table-striped table-inverse">
		<thead>
		  <tr>
				<td>Track</td>
				<td>Artista</td>
				<td>Album</td>
		  </tr>
		</thead>
		<tbody>
<?php
		$xml=simplexml_load_file("playlist.xml");
		if ($xml === false) {
    			echo "Failed loading XML: ";
    			foreach(libxml_get_errors() as $error) {
		        	echo "<br>", $error->message;
    			}
		} else {
			foreach($xml->song as $song){
				echo "<tr>";
				echo "<td>".$song['name']."</td>";
				echo "<td>".$song['artist']."</td>";
				echo "<td>".$song['album']."</td>";
				echo "</tr>";
			}
		}
?>
	</tbody>
  </table>
</form>
</div>

</body>
</html>
