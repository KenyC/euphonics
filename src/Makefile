%.md: ../scrap/article.html
	pandoc --from html --to markdown -o $@ $<
	cp -f $@ ../scrap/backup.html
	sed -i -e '/:::/d' $@
	sed -i -e 's/\\\^/\^/g' $@
	sed -i -e 's/\\_/_/g' $@
	sed -i -e 's/\\\\/\\/g' $@
	sed -i -e 's/\\~/~/g' $@
	sed -i -e 's/\\\$$/\$$/g' $@
	sed -i -e 's/\\left\\\[/\\left\\lbrack\{\}/g' $@
	sed -i -e 's/\\right\\\]/\\right\\rbrack\{\}/g' $@
	sed -i -e 's/\\>/>/g' $@
	sed -i -e 's/\\</</g' $@