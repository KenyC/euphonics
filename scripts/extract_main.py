# %%
import bs4
import sys

print(sys.argv)

input_file  = sys.argv[1]
output_file = sys.argv[2]

# file = "appendix-2.2.2-the-undamped-harmonic-oscillator.md"
with open(input_file, "r") as f:
	content = f.read()

# %%

soup = bs4.BeautifulSoup(content)

main_article = soup.find("article")

# %%

with open(output_file, "w") as f:
	f.write(str(main_article))

# %%