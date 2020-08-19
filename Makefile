build:
	virtualenv venv
	source venv/bin/activate && pip3 install -r requirements.txt && python3 init_db.py

run:
	source venv/bin/activate && bash run.sh
