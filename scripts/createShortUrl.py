import django,os,sys
os.environ['DJANGO_SETTINGS_MODULE']='urlshortner.settings'
try:
    django.setup()
except ModuleNotFoundError:
    print("Please copy this script to the project root folder <urlshortner> and run again")
    exit(0)

from django.conf import settings

sys.path.insert(0, os.path.join(getattr(settings, "BASE_DIR"), "shortner"))
from views import shortner

if len(sys.argv) < 2:
    print("Please provide an url to be shortned\nUsage: python <scriptname> '<longurl>'")
    exit(0)
else:
    long_url = sys.argv[1]
    print(shortner(long_url))
