import './style.css';
import jq from 'jquery';
var $ = jq;
import lf from 'localforage';
var localforage = lf;
$(function(){
    localforage.getItem('table').then(function(value){
        if(value!=null){
            $("tbody").html(value);
        }
    });
   $("#addButton").click(function(){
       var bdy = $("tbody").html();
       var todotext = $("#addTodo").val();
       if(todotext != ""){
            $("#tableBody").append("<tr class='Eintrag'>" +
                "<td class='aktiv'>" +
                todotext +
                "</td>" +
                "<td class='aktiv'>nicht erledigt</td>"+
                "<td class='aktiv'>" +
                "<button class='dele'>Delete</button><br>" +
                "<label>" +
                "<input class='ckBox' type='checkbox'>" +
                "Erledigt" +
                "</label>" +
                "</td>" +
                "</tr>");
        }
        localforage.setItem('table', bdy);
   });

   $(document).on("click", ".dele", function(){
       var parent = $(this).parent().parent();
       $(this).parent().parent().fadeOut("slow", function(){
          $(this).remove();
          var bdy = $("tbody").html();
            localforage.setItem('table', bdy);
       });

   });

    $(document).on("click", ".ckBox", function(){
        if($(this).prop("checked") == false){
           $(this).parent().parent().parent().children()[1].textContent="nicht erledigt";
        }
        else{
           $(this).parent().parent().parent().children()[1].textContent="erledigt";
        }
        var bdy = $("tbody").html();
        localforage.setItem('table', bdy);
    })

});