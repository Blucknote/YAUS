$(document).ready(
    function (e) {
        $('form#login, form#register').submit(
            function (e) {
                var self = $(this);
                e.preventDefault();
                self.find('.alert').addClass('d-none');
                $.post(
                    $(this).attr('action'),
                    $(this).serialize()
                ).done(function(data){
                    if(data['message'].length > 0) {
                        self.find('.alert').removeClass('d-none').text(data['message']);
                    }
                }).fail(function(xhr, status, error) {
                    self.find('.alert').removeClass('d-none').text('connection failure...')
                });
            }
        )
    }
);
