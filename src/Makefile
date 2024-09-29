.PHONY: all install uninstall clean dvi dist tests format check build
PYTHON=python3.12
VENV=.venv
PYEXEC=poetry run
OS:=$(shell uname -s)
CC=g++
FLAGS:=-lstdc++ -std=c++17 -Wall -Wextra -Werror -g
OBJ_DIR=build/obj

ifeq ($(OS), Darwin)
	FLAGS_PLATFORM =-lgtest 
else ifeq ($(OS), Linux)
	FLAGS_PLATFORM =-lgtest -lrt -lm -lpthread
endif

all: run

clean:
	rm -rf main test build

build:
ifeq ("", "$(wildcard build/obj/)")
	mkdir -p build/obj/
endif
ifeq ("", "$(wildcard .venv/)")
	make venv
endif
	$(CC) -c -fPIC lib/model.cc -Wextra -Wall -o $(OBJ_DIR)/model.o
	$(CC) -c -fPIC lib/credit_model.cc -Wextra -Wall -o $(OBJ_DIR)/credit_model.o
ifeq ($(OS), Darwin)
	$(CC) -shared -Wl,-install_name,model.so -o $(OBJ_DIR)/model.so $(OBJ_DIR)/model.o $(OBJ_DIR)/credit_model.o
else ifeq ($(OS), Linux)
	$(CC) -shared -Wl,-soname,model.so -o $(OBJ_DIR)/model.so $(OBJ_DIR)/model.o $(OBJ_DIR)/credit_model.o
endif

install: build
	$(PYEXEC) pyinstaller --onefile --windowed view.py
	./dist/mainwindow

uninstall:
	rm -r dist

dvi:
# TODO: Добавить документацию
	open README.md

dist:
	tar -czf dist.tar.gz dist

format:
	$(PYEXEC) isort .
	$(PYEXEC) ruff format .

check:
	$(PYEXEC) ruff check

tests: build
	$(CC) tests/test.cc -Wl,-rpath,$(OBJ_DIR) $(OBJ_DIR)/model.so -o dist/test $(FLAGS_PLATFORM) $(FLAGS)
	./dist/test

# cov:
# 	$(PYEXEC) pytest --cov --cov-report=html #-W ignore::DeprecationWarning
# 	open htmlcov/index.html


venv:
	# $(PYTHON) -m poetry config --local virtualenvs.in-project true
	$(PYTHON) -m poetry env use $(PYTHON)
	$(PYTHON) -m poetry install

run:
	$(PYEXEC) python main.py