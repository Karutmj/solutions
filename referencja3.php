<html>
<body>
<form action="referencja3.php" method="POST">
<h1>Chcesz obliczyć pierwiastki równania  ax<sup>2</sup> + bx + c = 0</h1>
<i>Podaj "a"   <input type="text" name="a"/></i><br>
<br><i>Podaj "b" <input type="text" name="b"/></i><br>
<br><i>Podaj "c" <input type="text" name="c"/></i><br>
<br><input  type="submit" value="Oblicz" name="Oblicz"/>
</form>
</body>
<?php
$a= $_POST['a'];
$b= $_POST['b'];
$c= $_POST['c'];
if($a!=0){
$wynik=($b*$b)-(4*$a*$c);
if($wynik>0){
 $pier1=(-$b-sqrt($wynik))/(2*$a);
 $pier2=(-$b+sqrt($wynik))/(2*$a);
 echo"Pierwszy pierwiastek to".$pier1.", a drugi to".$pier2;
}
else if($wynik==0){
 $pier3=(-$b)/(2*$a);
 echo" Pierwiastek to".$pier3." ponieważ delta wyszła zero";

}
else echo "Delta wyszła ujemna więc nie ma pierwiastków";

}
else echo "(a) nie może być równe zero";
?>
</html>