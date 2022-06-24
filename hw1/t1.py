"""
Написать метод domain_name, который вернет домен из url адреса:

url = "http://github.com/carbonfive/raygun" -> domain name = "github"
url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
url = "https://www.cnet.com"                -> domain name = "cnet"
"""

import re


def domain_name(url: str) -> str:
    """ Find domain_name from URL
        https://developer.mozilla.org/en-US/docs/Web/API/URL
        https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_domain_name#deeper_dive
    """

    # remove protocol
    output = url.lower().strip().split('://')[-1]
    # remove port
    output = output.split(':')[0]
    # remove endpoint
    output = output.split('/')[0]
    # find domain
    pattern = '([a-z0-9\-]+)(?:\.\w{2})?\.\w+$'
    output = re.findall(pattern, output)[0]

    return output


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"

assert domain_name("https://my.vultr.com") == "vultr"
assert domain_name("https://www.ed.ac.uk") == "ed"
assert domain_name("https://developer.mozilla.org/en-US/docs/Web/API/URL/hostname") == "mozilla"
assert domain_name("https://mydomain.com:80/svn/Repos/") == "mydomain"
