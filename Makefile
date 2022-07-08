MD_FILES=$(shell find src/ -name "*.md")

all: build/euphonics.epub

build/euphonics.epub: src/title.txt $(MD_FILES) pandoc.yaml
	pandoc -d pandoc.yaml -o $@ $$(python scripts/sort_md.py src/title.txt $(MD_FILES))
	@echo FINISHED !
	@echo SIZE OUTPUT
	@du -sh $@



todo: build/todo.epub

UNPROCESSED=$(wildcard src/unprocessed/*.md)
build/todo.epub: src/title.txt $(UNPROCESSED) pandoc.yaml
	pandoc -d pandoc.yaml -o $@ src/title.txt $(UNPROCESSED)
