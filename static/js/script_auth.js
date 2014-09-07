$(document).ready(function(){
    $('#auth_login_form').validate({
        submitHandler: function(form){
            $form = $(form);
            $.ajax({
                type: $form.attr('method'),
                url: $form.attr('action'),
                data: $form.serialize(),
                dataType : 'json'
            })
            .done(function (response) {
                alert(response)
            });
        },
    });
});