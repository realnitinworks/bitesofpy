import re


def strip_comments(code):
    # see Bite description
    doc_string_regex = re.compile(r'\s*"{3}.*?"{3}', re.DOTALL)
    result = doc_string_regex.sub(r'', code)

    comment_regex = re.compile(r'\s*#\s.*')
    return comment_regex.sub(r'', result)
