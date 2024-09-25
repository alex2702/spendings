"""Development settings."""

from .base import *  # noqa: F403
from .base import BASE_DIR, env

SECRET_KEY = env("SECRET_KEY", default="fe)n0wlj$m&0i4gp^f@$(vq3ctiynq+v4+6_9izgj4gd&5*5g@")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
	}
}
