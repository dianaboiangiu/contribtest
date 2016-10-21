# generate site from static pages, loosely inspired by Jekyll
# run like this:
#   ./generate.py test/source output
# the generated `output` should be the same as `test/expected_output`

import os
import logging
import jinja2
import sys
import json
import re

log = logging.getLogger(__name__)


def list_files(folder_path):
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != '.rst':
            continue
        yield os.path.join(folder_path, name), base


def read_file(file_path):
    with open(file_path, 'rb') as f:
        raw_metadata = ""
        for line in f:
            if line.strip() == '---':
                break
            raw_metadata += line
        content = ""
        for line in f:
            content += line.rstrip('\r\n')
    return json.loads(raw_metadata), content


def write_output(name, html, *args):
    # TODO should not use sys.argv here, it breaks encapsulation
    if not os.path.exists(args[0]):
        os.makedirs(args[0])
    with open(os.path.join(args[0], name + '.html'), 'wb') as f:
        f.write(html)


def generate_site(folder_path, *args):
    log.info("Generating site from %r", folder_path)
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.join(folder_path, 'layout')))
    for file_path, name in list_files(folder_path):
        metadata, content = read_file(file_path)
        template_name = metadata['layout']
        template = jinja_env.get_template(template_name)
        data = dict(metadata, content=content)
        html = template.render(**data)
        html = re.sub(r'(\n)\1+', r'\n\1', html)
        write_output(name, html, args[0])
        log.info("Writing %r with template %r",  name, template_name)


def main():
    generate_site(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    logging.basicConfig()
    main()
