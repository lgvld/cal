<!doctype html>
<html lang="en">
<head>
<title>cal.louis.ga :: calendrier des masters d’informatique de la Sorbonne</title>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<link href="static/style.css" rel="stylesheet">
</head>
<body>
<div id="wrapper">

<a id="left" href=""><div></div></a>

<div id="middle">
<nav id="masters"><ul>
% for master in MASTERS:
  <li><a href="{{ master }}">{{ master }}</a></li>
% end
</ul></nav>
<footer id="infos">
  <p><a href="mailto:louis@gavalda.fr">contact</a></p>
</footer>
</div>

<a id="right" href=""><div></div></a>

</div>

</div>
</body>
</html>

