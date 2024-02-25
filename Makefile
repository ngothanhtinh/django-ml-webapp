install:
	H:\django-ml-webapp\.venv\Scripts\python.exe -m pip install --upgrade pip &&\
	 pip install -r requirements.txt
format:
	#format code
lint:
	#pylint
test:
	#test