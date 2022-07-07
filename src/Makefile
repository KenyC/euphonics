%.md: ../scrap/article.html
	pandoc --from html --to markdown -o $@ $<
	cp -f $@ ../scrap/backup.md
	sed -i -e '/:::/d' $@
	sed -i -e 's/\\\^/\^/g' $@
	sed -i -e 's/\\_/_/g' $@
	sed -i -e 's/\\\\/\\/g' $@
	sed -i -e 's/\\~/~/g' $@
	sed -i -e 's/\\\$$/\$$/g' $@
	sed -i -e 's/\\\[/\\lbrack\{\}/g' $@
	sed -i -e 's/\\\]/\\rbrack\{\}/g' $@
	sed -i -e 's/\\>/>/g' $@
	sed -i -e 's/\\</</g' $@