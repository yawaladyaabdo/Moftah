build:
	python3 -m PyInstaller -F project/moftah.py
	mv dist/* .
clean:
	rm -rf moftah.spec dist build logs moftah
