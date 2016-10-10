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
<?php
	if(isset($_POST['_SONG_'])){
		$song = $_POST['_SONG_'];
		exec("sudo python Player_Sys.py --add ".$song);
		echo "<script>alert(\"La cancion ha sido agregada\")</script>";
	}
	if(isset($_POST['_START_'])){
		exec("sudo python Player_Sys.py --start");
		echo "<script>alert(\"El sistema ha comenzado a sonar\")</script>";
	}
	if(isset($_POST['_STOP_'])){
		exec("sudo python Player_Sys.py --stop");
		echo "<script>alert(\"El sistema ha detenido la cancion\")</script>";
	}
?>
<center><h1>BIENVENIDO A SU BIBLIOTECA MUSICAL<h1></center>
<center><a href="playlist.xml" type="button" class="btn btn-default" aria-label="Left Align">
  <span class="glyphicon glyphicon-list" aria-hidden="true"></span>  Playlist
</a></center>
<center>
<form action="<?php $_PHP_SELF?>" method="POST">
	<button type="submit" name="_START_" class="btn btn-default btn-lg">
		<span class="glyphicon glyphicon-play"></span> Play
	</button>
	<button type="submit" name="_STOP_" class="btn btn-default btn-lg">
                <span class="glyphicon glyphicon-fast-forward"></span> Step
        </button>
</form>
</center>
<div class="container">
	<h2>Biblioteca Musical</h2>
	<p>BIENVENIDO A TU BIBLIOTECA MUSICAL, ELIJE LA CANCION DE TU AGRADO Y PRESIONA "ADD" PARA AGREGARLA A LA LISTA DE REPRODUCCION</p>
	<form action="<?php $_PHP_SELF ?>" method="POST">
   		<table class="table table-striped table-inverse">
		<thead>
		   <tr>
			<td>Button</td>
			<td>SONG</td>
			<td>ARTIST</td>
			<td>ALBUM</td>
		  </tr>
		</thead>
		<tbody>
<?php
		$xml=simplexml_load_file("songlist.xml");
		if ($xml === false) {
    			echo "Failed loading XML: ";
    			foreach(libxml_get_errors() as $error) {
		        	echo "<br>", $error->message;
    			}
		} else {
			foreach($xml->song as $song){
				echo "<tr>";
				echo "<td><button type=\"submit\" name=\"_SONG_\"  class=\"btn btn-default btn-lg\" value=\"".$song['id']."\"><span class=\"glyphicon glyphicon-plus\" aria-hidden=\"true\"></span></button></td>";
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
<center><a href="index.php">REGRESAR AL INICIO</a></center><br>

</body>
</html>
