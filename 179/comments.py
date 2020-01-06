import re


def strip_comments(code):
    single_and_inline_comment_regex = re.compile(r'\s*#.*')
    code = single_and_inline_comment_regex.sub('', code)

    multiline_comments_regex = re.compile(r'\s*\"\"\".*?\"\"\"', re.DOTALL)
    return multiline_comments_regex.sub('', code)


single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''

print(strip_comments(single_docstring))