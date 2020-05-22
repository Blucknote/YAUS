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
                    if(typeof(data['message'])!=='undefined' && data['message'].length > 0) {
                        self.find('.alert').removeClass('d-none').text(data['message']);
                    } else {
                        window.location = '/';
                    }
                }).fail(function(xhr, status, error) {
                    self.find('.alert').removeClass('d-none').text('connection failure...')
                });
            }
        );
        $('button').click(
            function (e) {
                var self = $(this);
                $('button').attr('aria-selected', false);
                self.attr('aria-selected', true);
                var articles = $(this).closest('section').find('article')
                articles.attr(
                    {
                        "hidden": true,
                        "aria-selected": false
                    }
                );
                articles.filter(
                    function (el) {
                        return $(this).attr('id') == self.attr('aria-controls');
                    }
                ).removeAttr('hidden')
            }
        )
    }
);
