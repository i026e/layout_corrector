export SHELL = sh

DIR="$(dirname $(readlink -f "$0"))"

PACKAGE=layout-corrector
_PACKAGE=layout_corrector

VERSION=0.4

ifndef DESTDIR
	DESTDIR = "./debian/$(PACKAGE)/"
endif

all:

install:
	[ ! -d "$(DESTDIR)" ] || rm -r "$(DESTDIR)"

	mkdir -p "$(DESTDIR)usr/bin/"
	mkdir -p "$(DESTDIR)usr/share/$(PACKAGE)/"

	cp -r ./src/layout_corrector/* "$(DESTDIR)usr/share/$(PACKAGE)/"

	echo '#!/usr/bin/env sh' > "$(DESTDIR)usr/share/$(PACKAGE)/data/layout-corrector"
	echo "cd usr/share/$(PACKAGE)" >> "$(DESTDIR)usr/share/$(PACKAGE)/data/layout-corrector"
	echo -e 'python layout_corrector_control.py \044@' >> "$(DESTDIR)usr/share/$(PACKAGE)/data/layout-corrector"
	chmod 755 "$(DESTDIR)usr/share/$(PACKAGE)/data/layout-corrector"

	install -D -m 0755 "$(DESTDIR)usr/share/$(PACKAGE)/data/layout-corrector" "$(DESTDIR)usr/bin/layout-corrector"

clean:
	rm -rf ./dist
	rm -rf ./build

arch: FORCE
	sed -i 's/pkgver=.*/pkgver=$(VERSION)/' "./arch/$(PACKAGE)/PKGBUILD"
	cp "./dist/$(_PACKAGE)-$(VERSION).tar.gz" "./arch/$(PACKAGE)/"
	cd "./arch/$(PACKAGE)" && makepkg -f

	cp ./arch/$(PACKAGE)/*.tar.xz ./dist/

deb:

rpm: tar
	python3 setup.py bdist --formats rpm

git:
	#make git m="message"

	git add -A
	git commit -m "$(m)"
	git push origin master

.PHONY: FORCE
FORCE:

