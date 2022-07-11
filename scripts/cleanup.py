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

# brackets
pattern = r"(\\left)\\\[\s*"
# pattern = r"(\$[^\$]*)(\\\[\s*)(?=[^\$]*\$\$\s*\n)"
subst   = r'\1\\lbrack{}'
content = re.sub(pattern, subst, content)

pattern = r"(\\right)\\\]\s*"
# pattern = r"(\$[^\$]*)(\\\]\s*)(?=[^\$]*\$\$\s*\n)"
subst   = r'\1\\rbrack{}'
content = re.sub(pattern, subst, content)


# star exponent ^\*
content = content.replace("^\\*", r"^{\star}")


# angled brackets < >
pattern = r"(\\left)\\?<\s*"
subst   = r'\1\\langle{}'
content = re.sub(pattern, subst, content)

pattern = r"(\\right)\\?>\s*"
subst   = r'\1\\rangle{}'
content = re.sub(pattern, subst, content)




# primes in maths mode
pattern = r"(\^?\\?')(?=[^\$]*\$\$\n)"
subst   = r'^{\\prime}'
content = re.sub(pattern, subst, content)

pattern = r"(\\\w+|\s\w)(\^?\\?')"
subst   = r'\1^{\\prime}'
content = re.sub(pattern, subst, content)

# See more details

pattern = r"(\[\[SEE MORE DETAIL\]\{[^\}]*\}\]\()https:\/\/euphonics\.org\/(\d+-)+([^\)]*[^\)\/])\/?\)"
subst   = r'\1#\3)'
content = re.sub(pattern, subst, content)

with open(input_file, "w") as f:
	f.write(content)

# %%