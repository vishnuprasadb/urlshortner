import sys, os, random, string
from django.conf import settings
from django.contrib.sites.models import Site

from shortner.models import TinyUrl

sys.path.insert(0, os.path.join(getattr(settings, "BASE_DIR"), "infra"))
from utils import _is_valid_url


def _create_short_id():
    """
    Calculation for number of short urls which can be made.
    Total characters - 26+26+10 = 62 characters
    Length of short code - 6
    62*6 = 56800235584 combinations.
    """
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        # If the newly created short_id doesn't exist already
        # Then return the short_id
        short_id = ''.join(random.choice(char) for x in range(
            getattr(settings, 'SHORT_URL_CODE_LENGTH')))
        if (not TinyUrl.objects.filter(short_url=short_id).exists()):
            return short_id

def _create_tiny_url():
    """
    Creating the final short url to be stored in the database.
    """
    # Site object will return the TLD for the website
    # Which is set as "https://xyz.com" for now.
    site = Site.objects.get(id=getattr(settings, 'SITE_ID'))
    return "%s/%s"%(site.domain,_create_short_id())

def shortner(longUrl):
    """
    Function used to shorten a valid url to a six digit short url.
    input: long_url (string)
    output: short url (string)
    """
    # Check weather the given url is valid or not.
    if _is_valid_url(longUrl):
        # Check if a DB entry pertaining to the "longUrl" exists or not.
        tinyUrlObj, created = TinyUrl.objects.get_or_create(long_url=longUrl)

        # if created is true, then new instance created
        if created:
            tinyUrlObj.short_url=_create_tiny_url()
            tinyUrlObj.save(update_fields=["short_url"])

        return tinyUrlObj.short_url
    else:
        return "Invalid url"

def original(shortUrl):
    """
    Function used to return the orginial url
    input: short url (string)
    output: long_url (string)
    """
    # Check weather the given url is valid or not.
    if _is_valid_url(shortUrl):
        shortUrlObjs = TinyUrl.objects.filter(short_url=shortUrl)
        if shortUrlObjs.exists():
            return shortUrlObjs.first().long_url
        else:
            return "This '%s' short url is invalid."%(shortUrl)
    return "Invalid url"
