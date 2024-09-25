"""Testing settings."""

from .base import *  # noqa: F403
from .base import BASE_DIR, env

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
	}
}

CACHES = {
	"default": {
		"BACKEND": "django.core.cache.backends.dummy.DummyCache",
	}
}
