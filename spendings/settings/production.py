"""Production settings."""

from .base import *  # noqa: F403
from .base import env

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql",
		"NAME": env("POSTGRES_DB"),
		"USER": env("POSTGRES_USER"),
		"PASSWORD": env("POSTGRES_PASSWORD"),
		"HOST": "127.0.0.1",
		"PORT": "5432",
	}
}

CACHES = {
	"default": {
		"BACKEND": "django_redis.cache.RedisCache",
		"LOCATION": "redis://127.0.0.1:6379/0",
		"OPTIONS": {
			"CLIENT_CLASS": "django_redis.client.DefaultClient",
		},
	}
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
