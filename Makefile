MD_FILES=$(filter-out src/todo/%, $(shell find src/ -name "*.md"))

all: build/euphonics.epub

build/euphonics.epub: src/title.txt $(MD_FILES) pandoc.yaml
	pandoc -d pandoc.yaml -o $@ $$(python scripts/sort_md.py src/title.txt $(MD_FILES))
	@echo FINISHED !
	@echo SIZE OUTPUT
	@du -sh $@



todo: build/todo.epub

TODO=$(wildcard src/todo/*.md)
build/todo.epub: src/title.txt $(TODO) pandoc.yaml
	pandoc -d pandoc.yaml -o $@ src/title.txt $(TODO)
