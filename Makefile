.PHONY: venv
venv:
    virtualenv venv
.PHONY: active
active:
    source venv/bin/activate

.PHONY: install
install:
	pip install -r requeirements.txt

.PHONY: runserver
run-server:
	python manage.py runserver

.PHONY: makemigration
makemigration:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate   

.PHONY: create_payment_user
superuser:
	python manage.py create_payment_user 

