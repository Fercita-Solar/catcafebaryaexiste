from pathlib import Path  # Pathlib sirve para manejar rutas de carpetas y archivos de forma moderna y multiplataforma

# BASE_DIR representa la carpeta raíz del proyecto (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

#  Clave secreta usada por Django para seguridad interna (tokens, sesiones, etc.)
# En producción siempre debes cambiarla por una clave real y segura.
SECRET_KEY = 'django-insecure-reemplaza_esto_por_una_llave_segura'

# DEBUG = True → muestra errores detallados (solo en desarrollo).
# En producción debe estar en False.
DEBUG = True

# '*' significa que acepta conexiones desde cualquier host/IP (útil para pruebas locales).
ALLOWED_HOSTS = ['*']

#  Aplicaciones que se cargan en tu proyecto
INSTALLED_APPS = [
    'django.contrib.admin',          # Panel de administración
    'django.contrib.auth',           # Sistema de usuarios y autenticación
    'django.contrib.contenttypes',   # Permite trabajar con distintos tipos de datos
    'django.contrib.sessions',       # Manejo de sesiones (cookies, login)
    'django.contrib.messages',       # Mensajes temporales entre vistas (ej: "usuario creado con éxito")
    'django.contrib.staticfiles',    # Manejo de archivos estáticos (css, js, imágenes locales)
    'core',                          # Tu aplicación principal (no cambiar nombre porque lo pidieron)
]

#  Middleware = funciones que procesan cada petición/respuesta
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF en formularios
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo principal de urls
ROOT_URLCONF = 'catcafebar.urls'

#  Configuración de plantillas (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Aquí indicamos la carpeta global de plantillas → /templates/
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # Django también buscará plantillas dentro de cada app (ej: core/templates/)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',        # Info extra en modo debug
                'django.template.context_processors.request',      # Permite acceder a "request" en los templates
                'django.contrib.auth.context_processors.auth',     # Datos de usuario autenticado disponibles en los templates
                'django.contrib.messages.context_processors.messages',  # Permite mostrar mensajes temporales
            ],
        },
    },
]

# Archivo de configuración WSGI (para servidores de producción)
WSGI_APPLICATION = 'catcafebar.wsgi.application'

#  Configuración de base de datos
# Por defecto usa SQLite (un archivo db.sqlite3 en tu carpeta raíz).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#  Validación de contraseñas (para usuarios del admin o futuros logins)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

#  Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-es'    # Español
TIME_ZONE = 'America/Santiago'  # Zona horaria Chile
USE_I18N = True            # Traducción de interfaces
USE_TZ = True              # Manejo de tiempo con zona horaria

#  Archivos estáticos (CSS, JS, imágenes locales)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Carpeta donde puedes poner archivos estáticos globales

#  Archivos subidos por usuarios (ej: fotos, adjuntos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Carpeta para guardar archivos subidos

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

