$('#id_artista').change(function() {
    const faixa = $('#id_nome').val();
    const artista = this.value;

    $.ajax({
        url: "https://api.vagalume.com.br/search.php"
            + "?art=" + artista
            + "&mus=" + faixa
            + process.env.VAGALUME_KEY,
        dataType: 'jsonp',
        crossDomain: true,
        contentType: "application/json",
        statusCode: {
            200: function(data) {
                $("#id_letra").attr("value", data.mus[0].text.replace(/(?:\r\n|\r|\n)/g, '<br>'));
            }
        }
    });
});