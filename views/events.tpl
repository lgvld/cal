<!doctype html>
<html lang="en">
<head>
<title>{{ master }} :: calendrier</title>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<link href="static/style.css" rel="stylesheet">
</head>
<body>
<div id="wrapper">

<a id="left" href="https://cal.louis.ga/"><div></div></a>

<div id="middle">
<nav id="events"><ul>
% for event in events:
% event.name = event.name.split("-", 1)[-1]
  <li><span class="name">{{ event.name }}</span><span class="location">{{ event.location }}</span><span class="begin">{{ event.begin.humanize() }}</span><span class="date">{{ event.begin }}</span></li>
% end
</ul></nav>
</div>

<a id="right" href="https://cal.louis.ga/"><div></div></a>

</div>
</body>
</html>
