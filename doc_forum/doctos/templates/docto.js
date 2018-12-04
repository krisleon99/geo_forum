/*
Esta clase es el js para los combos de documentos
*/
<script type="text/javascript">
$(document).ready(function(){
$('#id_description').width(400);
$('#id_dimension').change(function() {
  var dim = $(this).val();
  $('#id_objetive option').remove();

  if (dim==1) {
       $('#id_objetive')
            .append($('<option>', { value : 'a' })
            .text("a"))
            .append($('<option>', { value : 'b' })
           .text("b"))
           .append($('<option>', { value : 'c' })
           .text("c"))
           .append($('<option>', { value : 'd' })
           .text("d"))
            .append($('<option>', { value : 'e' })
            .text("e"))
           .append($('<option>', { value : 'f' })
           .text("f"))
           .append($('<option>', { value : 'g' })
           .text("g"))
           .append($('<option>', { value : 'h' })
            .text("h"))
           .append($('<option>', { value : 'i' })
           .text("i"))
           .append($('<option>', { value : 'j' })
          .text("j"))
          .append($('<option>', { value : 'k' })
          .text("k"))
           .append($('<option>', { value : 'l' })
           .text("l"))
            .append($('<option>', { value : 'm' })
            .text("m"))
           .append($('<option>', { value : 'n' })
           .text("n"))
           .append($('<option>', { value : 'o' })
           .text("o"))
           .append($('<option>', { value : 'p' })
           .text("p"))
           .append($('<option>', { value : 'q' })
           .text("q"))
           .append($('<option>', { value : 'r' })
           .text("r"))
            .append($('<option>', { value : 's' })
            .text("s"))
           .append($('<option>', { value : 't' })
           .text("t"))
           .append($('<option>', { value : 'u' })
           .text("u"))
           .append($('<option>', { value : 'v' })
           .text("v"))
           .append($('<option>', { value : 'w' })
           .text("w"))
           .append($('<option>', { value : 'x' })
           .text("x"))
           .append($('<option>', { value : 'y' })
           .text("y"))
           .append($('<option>', { value : 'z' })
           .text("z"))
           .append($('<option>', { value : 'aa' })
           .text("aa"))
            .append($('<option>', { value : 'bb' })
            .text("bb"))
           .append($('<option>', { value : 'cc' })
           .text("cc"))
           .append($('<option>', { value : 'dd' })
           .text("dd"))
           .append($('<option>', { value : 'ee' })
           .text("ee"))
           .append($('<option>', { value : 'ff' })
           .text("ff"))
           .append($('<option>', { value : 'gg' })
           .text("gg"))
           .append($('<option>', { value : 'hh' })
           .text("hh"))
            .append($('<option>', { value : 'ii' })
            .text("ii"))
           .append($('<option>', { value : 'jj' })
           .text("jj"))
           .append($('<option>', { value : 'zz' })
           .text("zz"));
  }else if (dim==2) {
    $('#id_objetive')
         .append($('<option>', { value : 'a' })
         .text("a"))
         .append($('<option>', { value : 'b' })
        .text("b"))
        .append($('<option>', { value : 'c' })
        .text("c"));

  } else if (dim==3) {
    $('#id_objetive')
        .append($('<option>', { value : 'd' })
        .text("d"))
         .append($('<option>', { value : 'e' })
         .text("e"))
        .append($('<option>', { value : 'f' })
        .text("f"))
        .append($('<option>', { value : 'g' })
        .text("g"))
        .append($('<option>', { value : 'h' })
        .text("h"));
  }else if (dim==4) {
    $('#id_objetive')
         .append($('<option>', { value : 'i' })
         .text("i"))
         .append($('<option>', { value : 'j' })
        .text("j"))
        .append($('<option>', { value : 'k' })
        .text("k"));
  }else if (dim==5) {
    $('#id_objetive')
        .append($('<option>', { value : 'l' })
        .text("l"))
         .append($('<option>', { value : 'm' })
         .text("m"))
        .append($('<option>', { value : 'n' })
        .text("n"))
        .append($('<option>', { value : 'o' })
        .text("o"))
        .append($('<option>', { value : 'p' })
        .text("p"))
        .append($('<option>', { value : 'q' })
        .text("q"));
  }
  else if (dim==6) {
    $('#id_objetive')
        .append($('<option>', { value : 'r' })
        .text("r"))
         .append($('<option>', { value : 's' })
         .text("s"))
        .append($('<option>', { value : 't' })
        .text("t"))
        .append($('<option>', { value : 'u' })
        .text("u"))
        .append($('<option>', { value : 'v' })
        .text("v"))
        .append($('<option>', { value : 'w' })
        .text("w"))
        .append($('<option>', { value : 'x' })
        .text("x"))
        .append($('<option>', { value : 'y' })
        .text("y"))
        .append($('<option>', { value : 'z' })
        .text("z"));
  }
  else if (dim==7) {
    $('#id_objetive')
        .append($('<option>', { value : 'aa' })
        .text("aa"))
         .append($('<option>', { value : 'bb' })
         .text("bb"))
        .append($('<option>', { value : 'cc' })
        .text("cc"))
        .append($('<option>', { value : 'dd' })
        .text("dd"))
        .append($('<option>', { value : 'ee' })
        .text("ee"))
        .append($('<option>', { value : 'ff' })
        .text("ff"))
        .append($('<option>', { value : 'gg' })
        .text("gg"));

  }else if (dim==8) {
    $('#id_objetive')
        .append($('<option>', { value : 'hh' })
        .text("hh"))
         .append($('<option>', { value : 'ii' })
         .text("ii"))
        .append($('<option>', { value : 'jj' })
        .text("jj"));

  }
});
$( "#id_author" ).keypress(function( event ) {
  var url = $('#id_url').val();
  var doc = $('#id_docto_pro').val();
  if (url == "" && doc == "") {
    $('.filter_docto').html("Selecciona un documento o ingresa una URL");
    $('#id_author').val("");
  }else {
    $('.filter_docto').html("");
  }
});
$( "#id_description" ).keypress(function( event ) {
  var url = $('#id_url').val();
  var doc = $('#id_docto_pro').val();
  if (url == "" && doc == "") {
    $('.filter_docto').html("Selecciona un documento o ingresa una URL");
    $('#id_author').val("");
    $('#id_description').val("");
  }else {
      $('.filter_docto').html("");
  }
});
});
</script>
