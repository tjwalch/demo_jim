$(function () {
    $('#id_car').change(function () {
        var carId = $(this).val();
        if (carId) {
            $.getJSON(Urls['retreive-odometer'](carId), function (data) {
                $('#id_mileage_start').val(data.odometer);
            });
        }
    });
});
