import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        if line.count(",") != 1:
            continue
        if "https://" not in line:
            continue

        link, text = line.strip().split(",")
        for in_link in INTERNAL_LINKS:
            if in_link in line:
                output = f'<a href="{link.strip()}">{text.strip()}</a>'
                break
        else:
            output = f'<a href="{link.strip()}" target="_blank">{text.strip()}</a>'
        print(output)


if __name__ == '__main__':
    make_html_links()