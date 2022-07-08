# %%
import bs4
import sys
import re

input_file  = sys.argv[1]

with open(input_file, "r") as f:
	content = f.read()

content = re.sub(r"\[(NEXT|PREVIOUS)\sSECTION\]\([^\)]*\)", "", content)

pattern = r"!\[([^\]]*)\]\(https:\/\/euphonics\.org\/wp-content\/([^\)]+)\)\{[^\}]+\}"
subst   = r'![\1](\2){width="100%"}'
content = re.sub(pattern, subst, content)

pattern = r"https:\/\/euphonics\.org\/wp-content\/([^\)]+)\)"
subst   = r'\1'
content = re.sub(pattern, subst, content)

pattern = r"(\$\$[^\$]*)(--)(?=[^\$]*\$\$)"
subst   = r'\1-'
content = re.sub(pattern, subst, content)


pattern = r"(\$[^\$]*)(\\\[\s*)(?=[^\$]*\$)"
subst   = r'\1\\lbrack{}'
content = re.sub(pattern, subst, content)



pattern = r"(\$[^\$]*)(\\\]\s*)(?=[^\$]*\$)"
subst   = r'\1\\rbrack{}'
content = re.sub(pattern, subst, content)



with open(input_file, "w") as f:
	f.write(content)

# %%