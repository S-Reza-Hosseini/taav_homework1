import re

def init_repeat_replacer():
    repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
    repl = r'\1\2\3'
    return repeat_regexp, repl

