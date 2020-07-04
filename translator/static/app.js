$(function () {
    $('.input-text').keyup(function () {
        const inputText = $('.input-text').val()
        console.log(inputText)

        $.ajax({
            type: 'POST',
            url: '127.0.0.1:8000/translate',
            data: {
                value: inputText
            }
        })

        $('.output-text').val(getInputText.val());
        return getInputText;
    })

})
