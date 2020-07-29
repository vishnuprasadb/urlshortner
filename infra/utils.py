def _is_valid_url(url):
    """
    Function used to check if its a valid url or not
    input: <URL string>
    output: Boolean
    """
    import re
    regex = re.compile(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9A-Z]+([\-\.]{1}[a-z0-9A-Z]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$')
    return re.match(regex, url) is not None
