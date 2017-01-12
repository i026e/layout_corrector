export SHELL = sh

DIR="$(dirname $(readlink -f "$0"))"

PACKAGE=layout-corrector
_PACKAGE=layout_corrector

VERSION=0.2

ifndef DESTDIR
	DESTDIR = "./debian/$(PACKAGE)/"
endif

all:

install: tar
	pip install --root=$(DESTDIR) "./dist/$(_PACKAGE)-$(VERSION).tar.gz"

tar:
	sed -i 's/version=.*/version="$(VERSION)",/' setup.py
	python3 setup.py sdist

uninstall:
	pip uninstall "$(_PACKAGE)"

clean:
	rm -rf ./dist
	rm -rf ./build

arch: tar
	sed -i 's/pkgver=.*/pkgver=$(VERSION)/' "./arch/$(PACKAGE)/PKGBUILD"
	cp "./dist/$(_PACKAGE)-$(VERSION).tar.gz" "./arch/$(PACKAGE)/"
	cd "./arch/$(PACKAGE)" && makepkg -f

	cp ./arch/$(PACKAGE)/*.tar.xz ./dist/


arch-pynput:
	cd ./arch/pynput && makepkg -f
	cp ./arch/pynput/*.tar.xz ./dist/

arch-xkbgroup:
	cd ./arch/xkbgroup && makepkg -f
	cp ./arch/xkbgroup/*.tar.xz ./dist/

deb:

rpm: tar
	python3 setup.py bdist --formats rpm

git:
	#make git m="message"

	git add -A
	git commit -m "$(m)"
	git push origin master

