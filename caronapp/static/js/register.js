$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

$('#reg_form').on('submit', function(event){
    event.preventDefault();
    
    var must_return = false;

    
    $("#post-pass").next().html("Digite uma senha válida.");

    $("#reg_form input").each(function(){
        if(!$(this).val() && !$(this).hasClass("optional")){ 
            console.log($(this).attr("id")+" is empty");
            must_return = true;
        }
    });


    if($("#post-pass").val() != $("#post-pass-repeat").val()){
        console.log("Senhas diferentes");

        $("#post-pass-repeat").next().html("As senhas não conferem.");
        $("#post-pass").next().html("");
        $("#post-pass-repeat").removeClass("is-valid");
        $("#post-pass").removeClass("is-valid");

        $("#post-pass").addClass("is-invalid");
        $("#post-pass-repeat").addClass("is-invalid");
        must_return = true;
    }else{
        $("#post-pass-repeat").removeClass("is-invalid");
        $("#post-pass").removeClass("is-invalid");
    }

    if(must_return) return;

    register();
});

// AJAX for posting
function register() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url: '/signup/register/',
        type: 'POST',
        data: {
            fname: $('#post-fname').val(),
            lname: $('#post-lname').val(),
            email: $('#post-email').val(), 
            bdayday: $('#id_birthday_day').val(),
            bdaymonth: $('#id_birthday_month').val(),
            bdayyear: $('#id_birthday_year').val(),
            password: $('#post-pass').val(), 
            city: $('#post-city').val(),
            state: $('#post-state').val()
        },

        success: function(json){
            if(json['error'] == 'user_already_exists'){
                alert('Usuário já existe!');
                return;
            }
            else{
                window.location.replace("/");
            }

        },

        error: function(xhr,errmsg,err) {
            alert('error!!');
            $('#post-pass').val() = "";
        }

    });
};


// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';

  window.addEventListener('load', function() {
    var form = document.getElementById('reg_form');
    form.addEventListener('submit', function(event) {
      if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  }, false);
})();