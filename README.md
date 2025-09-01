# Cat Cafe Bar Project

## Overview
This project is a Django web application for a cat café, featuring various sections to provide information about the café, its offerings, and a gallery of images.

## Project Structure
The project is organized as follows:

```
catcafebar/
├── catcafebar/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── main/
│           ├── home.html
│           ├── quienes_somos.html
│           ├── preguntas_frecuentes.html
│           └── galeria.html
├── manage.py
├── requirements.txt
└── README.md
```

## Sections
1. **Home**: The landing page of the café, featuring a welcome message and links to other sections.
2. **Quienes Somos**: A section that provides information about the café, its mission, and its team.
3. **Preguntas Frecuentes**: A FAQ section addressing common inquiries about the café.
4. **Galería de imágenes**: A gallery showcasing images of the café, its cats, and events.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd catcafebar
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   ```
   python manage.py runserver
   ```

## Dependencies
- Django: The primary framework used for building the web application.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.