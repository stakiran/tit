# encoding: utf-8

import glob
import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def get_directory(path):
    return os.path.dirname(path)

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)
FILENAME_HEADER = 'readme_header.md'
FILENAME_FOOTER = 'readme_footer.md'
FILENAME_OUTPUT = 'readme.md'

lines_header = file2list(FILENAME_HEADER)
lines_footer = file2list(FILENAME_FOOTER)

searchee_dir = os.path.join(MYDIR)
query = '{}/**/*.md'.format(searchee_dir)
searchee_files = glob.glob(query, recursive=True)

targetpaths = []
for filepath in searchee_files:
    if filepath.endswith('{}'.format(FILENAME_OUTPUT)):
        continue
    if filepath.endswith('{}'.format(FILENAME_HEADER)):
        continue
    if filepath.endswith('{}'.format(FILENAME_FOOTER)):
        continue
    targetpaths.append(filepath)

lines_toc = []
for filepath in targetpaths:
    cur_fullpath = filepath
    cur_filename = get_filename(cur_fullpath)
    # D:\work\github\stakiran\tit\folder\file.md
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^               replace
    #                            ^              strip
    cur_related_path = cur_fullpath.replace(MYDIR, '')[1:]
    cur_related_path = cur_related_path.replace('\\', '/')

    # 2019/11/tansaku.md
    #                ^^^ remove here.
    # For removing '.md' from display text because noisy on search.
    cur_related_path_without_ext = cur_related_path[:-3]

    cur_contents_lines = file2list(cur_fullpath)
    cur_firstline = cur_contents_lines[0]
    # `# Title and keywords`
    #    ^^^^^^^^^^^^^^^^^^   pick here.
    cur_title_in_section = cur_firstline[2:]

 
    linkstr = '- [{} {}]({})'.format(
        cur_related_path_without_ext,
        cur_title_in_section,
        cur_related_path
    )
    lines_toc.append(linkstr)
# Add a blank line for easy to read.
lines_toc.append('')

# Construct with header, footer and body lines.
lines_for_output = []
lines_for_output.extend(lines_header)
lines_for_output.extend(lines_toc)
lines_for_output.extend(lines_footer)

# to file
list2file(FILENAME_OUTPUT, lines_for_output)
