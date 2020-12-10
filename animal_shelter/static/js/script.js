
ymaps.ready(init);
function init() {

    // Создание карты.
    var myMap = new ymaps.Map("map", {
        center: [52.283385, 104.291836],
        zoom: 14,
    });

    // Строка с адресом, который необходимо геокодировать
    // var address = 'Иркутск, ул. Уритского, 16';

    // Ищем координаты указанного адреса
    // https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/geocode-docpage/
    // var geocoder = ymaps.geocode(address);

    // После того, как поиск вернул результат, вызывается callback-функция
    geocoder.then(
        function (res) {

            // координаты объекта
            // var coordinates = res.geoObjects.get(0).geometry.getCoordinates();

            // Добавление метки (Placemark) на карту
            var placemark = new ymaps.Placemark(
                [52.283385, 104.291836], {
                    'hintContent': 'Ул. Уритского, 16',
                    'balloonContent': 'Время работы: Пн-Пт, с 9 до 20'
                }, {
                    'preset': 'islands#redDotIcon'
                }
            );

            myMap.geoObjects.add(placemark);
        }
    );

}