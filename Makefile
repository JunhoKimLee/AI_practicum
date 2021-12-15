play:
	python3 main.py 0 0

install:
	pip install -r requirements.txt

zip:
	rm -f jocalf.zip
	zip -r checkers.zip *