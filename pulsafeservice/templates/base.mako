<!DOCTYPE html>
<html lang="en">
<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no"/>
<title>PulSafe</title>

<link href="/static/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
<!-- CSS  -->
<%def name="css()"></%def>
${self.css()}

</head>

<body>

<nav class="blue-grey lighten-1" role="navigation">
    <div class="container">
        <div class="nav-wrapper"><a id="logo-container" href="#" class="brand-logo">PulSafe</a></div>
    </div>
</nav>

<div class="container">
    <div class="section">
        ${self.body()}
    </div>
</div>

<!--  Scripts-->
<script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
<script src="/static/js/materialize.min.js"></script>

<%def name="javascript()"></%def>
${self.javascript()}

</body>

</html>
