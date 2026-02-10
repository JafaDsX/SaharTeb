import os
import sys

# فعال‌سازی virtualenv
VENV_PATH = "/home/sdvilydq/virtualenv/saharteb/3.10"
activate_this = os.path.join(VENV_PATH, "bin/activate_this.py")
with open(activate_this) as f:
    exec(f.read(), {"__file__": activate_this})

# مسیر پروژه
PROJECT_PATH = "/home/sdvilydq/repositories/SaharTeb/saharteb"
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# تنظیمات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saharteb.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
