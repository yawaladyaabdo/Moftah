build:
	python3 -m PyInstaller -D project/moftah.py
	mv dist/* .
	rm -rf build dist logs moftah.spec
clean:
	rm -rf moftah moftah.spec
install:
	git clone https://git.horus64.org/abdul/moftah.git /tmp/moftah
	cd /tmp/moftah
	mkdir ~/.config/moftah
	mv project/db ~/.config/moftah/
	mv project/log ~/.config/moftah

	python3 -m PyInstaller -D project/moftah.py
	mv dist/* ~/.config/moftah
	rm -rf build dist logs moftah.spec
	mv moftah ~/.local/bin