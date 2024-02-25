install:
	python -m pip install --upgrade pip && pip install -r requirements.txt

format:
	python -m black predictor/dashboard/*.py predictor/predictor/*.py

lint:
	pylint --disable=R,C predictor/dashboard/*.py predictor/predictor/*.py

test:
	#test