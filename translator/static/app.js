$(function () {
    $('.input-text').keyup(function () {
        const inputText = $('.input-text').val()
        console.log(inputText)

        $.ajax({
            type: 'GET',
            url: '/translation/',
            data: {
                value: inputText
            }
        }).done(function(data) {
          $('.output-text').val(data);
        });

        //$('.output-text').val(getInputText.val());
        //return getInputText;
    })

})
