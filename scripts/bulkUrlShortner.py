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
    print("Please provide a txt file with urls to be shortned\nUsage: python <scriptname> <filename.txt>")
    exit(0)
else:
    filename = sys.argv[1]

def _is_valid_extension(extension):
    return extension == "txt"

if os.path.exists(filename):
    file_extension = filename.split(".")[-1]
    if _is_valid_extension(file_extension):
        output_filename = filename.replace(".txt", "-output.txt")
        output = open(output_filename, "w+")
        with open(filename, "r") as f:
            for long_url in f.readlines():
                output.write("%s,%s\n"%(
                    long_url.strip(),
                    shortner(long_url.strip())
                    ))
        print("Please find all the corresponding short_urls in %s"%output_filename)
    else:
        print("Please provide a 'txt' file as an input")
else:
    print("Given filename '%s' doesn't exist"%(filename))
