from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

import sys
import logging

from pydocx import PyDocX

from bs4 import BeautifulSoup

def get_html_file_content(html):
	soup = BeautifulSoup(html, features='lxml')
	html_content_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4']#,'div']
	contents = []
	for child in soup.findAll(html_content_tags):
		inner_text = child.text.strip() if child.text else ""
		if inner_text:
			contents.append(inner_text)
	result = '\n'.join(contents) + '\n'
	return result

def convert(output_type, docx_path, output_path):
    if output_type == '--html':
        output = PyDocX.to_html(docx_path)
    elif output_type == '--markdown':
        output = PyDocX.to_markdown(docx_path)
    elif output_type == '--text':
        output = PyDocX.to_html(docx_path)
        output = get_html_file_content(output)
    else:
        print('Only valid output formats are --html and --markdown')
        return 2
    with open(output_path, 'wb') as f:
        f.write(output.encode('utf-8'))
    return 0


def usage():
    print('Usage: pydocx --html|--markdown|--text input.docx output')
    return 1


def main(args=None):
    logging.basicConfig(level=logging.DEBUG)

    if args is None:
        return usage()

    try:
        output_type = args[0]
        docx_path = args[1]
        output_path = args[2]
    except IndexError:
        return usage()

    return convert(output_type, docx_path, output_path)


def cli():
    # Entry point for PyDocX CLI tool
    sys.exit(main(args=sys.argv[1:]) or 0)


if __name__ == "__main__":
    sys.exit(main(args=sys.argv[1:]) or 0)
