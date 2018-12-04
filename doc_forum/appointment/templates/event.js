<script type="text/javascript">
$(document).ready(function(){
  //This code is for hashtag of events comments
  var desc = "{{event.name|safe}}";
  var id = "{{event.id|safe}}";
  var p = $(".event-hash");

  var expresion = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/ig;
  // var cadena = "https://www.youtube.com/watch?v=gAd2gU0VdJU&list=RDgAd2gU0VdJU";
  var repl_http = desc.replace(expresion, '<a href="$1" target="_blank">$2</a>');
  p.html(repl_http);

  var repl = repl_http.replace(/(^|\W)(#[a-z\d][\w-]*)/ig, '$1<a href="https://twitter.com/hashtag/$2" target="_blank">$2</a>');
  repl=repl.replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/");
  p.html(repl);

  //End hashtag of forum comments
});
</script>
