include config.mk
MD_FILES=$(filter-out src/todo/%, $(shell find src/ -name "*.md"))

ifeq ($(GLADTEX),yes)
ifeq ($(GLADTEX_CMD),)
GLADTEX_CMD=./gladtex_filter
endif
OPTS= --filter "$(GLADTEX_CMD)"
else
OPTS=
endif


all: build/euphonics.epub

build/euphonics.epub: src/title.txt $(MD_FILES) pandoc.yaml config.mk
	echo \"$(GLADTEX)\"
	echo $(OPTS)
	pandoc -d pandoc.yaml $(OPTS) -o $@ $$(python scripts/sort_md.py src/title.txt $(MD_FILES))
	@echo FINISHED !
	@echo SIZE OUTPUT
	@du -sh $@

ifeq ($(GLADTEX),yes)
	# Clean GladTeX intermediate files
	rm eqn*
	rm gladtex.cache
endif



# Partial compilation
build/%.epub: src/%.md src/title.txt pandoc.yaml 
	pandoc -d pandoc.yaml --filter "./gladtex_filter" -o $@ $(OPTS) $$(python scripts/sort_md.py src/title.txt $<)
	@echo FINISHED !
	@echo SIZE OUTPUT
	@du -sh $@


todo: build/todo.epub

TODO=$(wildcard src/todo/*.md)
build/todo.epub: src/title.txt $(TODO) pandoc.yaml
	pandoc -d pandoc.yaml -o $@ src/title.txt $(TODO)

clean:
	rm eqn*
	rm gladtex.cache
