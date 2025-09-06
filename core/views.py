from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')


def news_sales(request):
    return render(request, 'core/news_sales.html')


def galeria(request):
    imagenes = [
        {
            "url": "https://cdn.shopify.com/s/files/1/0607/5167/5547/files/el-gato-sagrado-birmano_600x600.jpg?v=1683735400",
            "descripcion": "Gato Birmano en el café"
        },
        {
            "url": "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg",
            "descripcion": "Michi jugando en la sala"
        },
        {
            "url": "https://img.freepik.com/fotos-premium/imagen-fotografica-stock-fondo-pantalla-hd-8k-personaje-nino-lindo_915071-63216.jpg?semt=ais_incoming&w=740&q=80",
            "descripcion": "Momento de relax con café"
        },
        {
            "url": "https://img.freepik.com/fotos-premium/gato-cafe-gatos-huele-taza-cafe-mesa_1048944-11873130.jpg?semt=ais_hybrid&w=740&q=80",
            "descripcion": "Saboreando el café"
        },
        {
            "url": "https://www.guiarepsol.com/content/dam/repsol-guia/contenidos-imagenes/viajar/con-mi-mascota/la-gatoteca-madrid/gr-cms-media-featured_images-none-c897d947-0e73-4a30-8aef-2ffb57912f5d-01_gatoteca-26.jpg.transform/rp-rendition-xs/image.jpg",
            "descripcion": "Disfruta la compañia de nuestros michis"
        },
        {
            "url": "",
            "descripcion": "Saboreando el café"
        },
        {
            "url": "",
            "descripcion": "Saboreando el café"
        },
    ]
    return render(request, 'core/galeria.html', {'imagenes': imagenes})
