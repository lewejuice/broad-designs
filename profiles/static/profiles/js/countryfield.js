// Change colour of country field to suit the rest of the form
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#6e767e');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#6e767e');
    } else {
        $(this).css('color', '#000');
    }
});