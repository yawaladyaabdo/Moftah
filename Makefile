build:
	python3 -m PyInstaller moftah.py
	mv dist/* .
	rm -rf build dist logs moftah.spec
clean:
	rm -rf moftah moftah.spec