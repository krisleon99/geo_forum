<script type="text/javascript">
$(document).ready(function(){
  //This code is for hashtag of forum comments
{% for agree in forum %}
  var desc = "{{agree.comment|safe}}";
  var id = "{{agree.id|safe}}";
  var p = $("#forum_"+id);

  var expresion = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/ig;
  // var cadena = "https://www.youtube.com/watch?v=gAd2gU0VdJU&list=RDgAd2gU0VdJU";
  var repl_http = desc.replace(expresion, '<a href="$1" target="_blank">$2</a>');
  p.html(repl_http);

  var repl = repl_http.replace(/(^|\W)(#[a-z\d][\w-]*)/ig, '$1<a href="https://twitter.com/hashtag/$2" target="_blank">$2</a>');
  repl=repl.replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/").replace("/#","/");
  p.html(repl);

  var repl_arroba = repl.replace(/(^|\W)(@[a-z\d][\w-]*)/ig, '$1<a href="https://twitter.com/$2" target="_blank">$2</a>');
  repl_arroba=repl_arroba.replace("/@","/").replace("/@","/").replace("/@","/").replace("/@","/").replace("/@","/").replace("/@","/").replace("/@","/").replace("/@","/");
  p.html(repl_arroba);

{% endfor %}
  //End hashtag of forum comments
  //This code is for likes of forum comments
  {% for f in forum %}
  var count_likes_child = 0;
    {% for like in likes %}
      {% if like.forum.id == f.id %}
        count_likes_child = count_likes_child + 1;
      {% endif %}
    {% endfor %}
    var id_f =  "{{ f.id|safe }}";
    $('.count_like_'+id_f).html(count_likes_child);
    $('.count_like_'+id_f).val(count_likes_child);
  {% endfor %}
    //End for likes of forum comments
//Me gusta
$('.chat-main').on("click", "span.like-chat", function(e){
	var id_like_str = $(this).attr('id');
	// var count_likes = $(this).attr('data_count_like');
	var like = id_like_str.replace("like_","");
  count_likes = $('.count_like_'+like).val();
	save_like(like,count_likes,"count-likes");

});
//Open topic
$('#open_topic').click(function(){
  var id_topic = $(this).attr('id-topic');
	close_topic(id_topic,false);

});
//Open topic
$('#close_topic').click(function(){
  var id_topic = $(this).attr('id-topic');
	close_topic(id_topic,true);

});
//getId topic
function get_id_topic(){
  return id_topic;
}
function save_like(like, count_likes, count_like){
  	 query_data = {
        'id_forum': like,
      }
      $.ajax({
        data: {'query_data': JSON.stringify(query_data),
             csrfmiddlewaretoken: '{{ csrf_token }}'
            },
        url: '{% url "save_like_forum" %}',
        type: 'POST',
        success : function(data) {
          if (data) {
            var number_like = parseInt(count_likes);
            if (data[0]) {
              var sumary_likes = number_like+1;
            }
            else {
              var sumary_likes = number_like-1;
            }
            $('.count_like_'+like).html(sumary_likes);
          }
        },
        error : function(message) {
                console.log(message);
             }
        });
}
function close_topic(id_topic, is_closed){
  	 query_data = {
        'id_topic': id_topic,
        'is_closed': is_closed
      }
      $.ajax({
        data: {'query_data': JSON.stringify(query_data),
             csrfmiddlewaretoken: '{{ csrf_token }}'
            },
        url: '{% url "close_topic" %}',
        type: 'POST',
        success : function(data) {
          if (is_closed) {
            $("#close_topic").html("Abrir tema");
            $(".chat_user").hide();

          }else {
            $("#open_topic").html("Cerrar tema");
            $(".chat_user").show();
          }
        },
        error : function(message) {
                console.log(message);
             }
        });
}
});
//Valida que no sean ingresado enter dentro del textarea
function Textarea_Sin_Enter($char, $mozChar, $id){
   //alert ($char+" "+$mozChar);
   $textarea = document.getElementById($id);
   niveles = -1;

   if($mozChar != null) { // Navegadores compatibles con Mozilla
       if($mozChar == 13){
           if(navigator.appName == "Opera") niveles = -2;
           $textarea.value = $textarea.value.slice(0, niveles);
       }
   // navegadores compatibles con IE
 } else if($char == 13){
   $textarea.value = $textarea.value.slice(0,-2);
 }
}
</script>
