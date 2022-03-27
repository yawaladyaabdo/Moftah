build:
	python3 -m PyInstaller -D project/moftah.py
	mv dist/* .
clean:
	rm -rf moftah.spec dist build