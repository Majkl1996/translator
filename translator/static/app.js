$(function () {
    $('.input-text').keyup(function () {
        const getInputText = $('.input-text').val();
        //console.log(getInputText)
        $.ajax()
        $('.output-text').val(getInputText);
        return getInputText;
    })

})
