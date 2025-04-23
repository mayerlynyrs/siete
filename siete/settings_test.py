from siete.settings import *

# Establecer SECRET_KEY para pruebas
SECRET_KEY = "django-insecure-kxg!z+=471m9_nhc#$01qrxli8xb@hxqe--oalys$fv5fqf!g("

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}