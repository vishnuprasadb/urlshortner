import django,os,sys
os.environ['DJANGO_SETTINGS_MODULE']='urlshortner.settings'
try:
    django.setup()
except ModuleNotFoundError:
    print("Please copy this script to the project root folder <urlshortner> and run again")
    exit(0)

from django.conf import settings

sys.path.insert(0, os.path.join(getattr(settings, "BASE_DIR"), "shortner"))
from views import original

short_url = sys.argv[1]

print(original(short_url))
