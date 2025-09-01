from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def news_sales(request):
    return render(request, 'core/news_sales.html')

def galeria(request):
    # Ejemplo de imágenes remotas para el bloque dinámico
    imagenes = [
        "https://lovapets.es/cdn/shop/articles/el-gato-de-bengala_d3cf8aa2-02e3-4cb8-b0e2-42604d13da57.jpg?height=450&v=1748529061",
        "https://cdn.shopify.com/s/files/1/0607/5167/5547/files/el-gato-sagrado-birmano_600x600.jpg?v=1683735400",
        "https://www.blogdelfotografo.com/wp-content/uploads/2023/08/gatito-bonito-blanco.webp",
        # ...más URLs remotas...
    ]
    return render(request, 'core/galeria.html', {'imagenes': imagenes})