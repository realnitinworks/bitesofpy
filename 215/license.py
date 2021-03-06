import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    license_key_regex = re.compile(r'^PB-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}$')
    mo = license_key_regex.search(key)

    return mo is not None
