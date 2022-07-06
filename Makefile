MD_FILES=$(sort $(wildcard src/*.md))

all: src/title.txt $(MD_FILES) pandoc.yaml
	pandoc -d pandoc.yaml -o build/euphonics.epub src/title.txt $(MD_FILES) 

