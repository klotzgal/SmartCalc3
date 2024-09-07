.PHONY: all install uninstall clean fclean dvi dist tests format check lib_cpp
PYTHON=python3.11
VENV=.venv
PYEXEC=poetry run
OBJ_DIR=obj
# CPP
OS:=$(shell uname -s)
CC=gcc
FLAGS:=-lstdc++ -std=c++17 -Wall -Wextra -Werror -g
OBJ_DIR=lib/obj

ifeq ($(OS), Darwin)
	FLAGS_PLATFORM =-lgtest 
else
	FLAGS_PLATFORM =-lgtest -lrt -lm -lpthread 
endif

clean :
	rm -rf main $(OBJ_DIR)/*.o $(OBJ_DIR)/*.so

lib_cpp:
	g++ -c -fPIC lib/model.cc -Wextra -Wall -o $(OBJ_DIR)/model.o 
	g++ -shared -Wl,-soname,model.so -o $(OBJ_DIR)/model.so $(OBJ_DIR)/model.o 

# TODO: Убрать это говно
main: main.o lib_cpp
	$(CC) $(OBJ_DIR)/main.o $(OBJ_DIR)/model.so -o main $(FLAGS) $(FLAGS_PLATFORM)
	
# TODO: Убрать это говно
main.o: main.cc 
	$(CC) -c $^ -o $(OBJ_DIR)/$@ $(FLAGS) $(FLAGS_PLATFORM) 


# install:
# # TODO: Заменить на установку проекта в каталог ../build
# 	$(PYEXEC) python view.py

# uninstall:
# # TODO: Заменить на удаление проекта
# 	echo "Uninstalling..."

# clean:
# 	rm -rf build *cache* .*cache dist .coverage htmlcov

# fclean: clean
# 	rm -rf $(VENV)

# dvi:
# # TODO: Добавить документацию
# 	open README.md

# dist:
# # TODO: Проверить после добавления install
# 	mkdir -p dist
# 	cp -r build/* dist
# 	tar -czf dist.tar.gz dist

# format:
# 	$(PYEXEC) isort .
# 	$(PYEXEC) ruff format .

# check:
# 	$(PYEXEC) ruff check
# 	# $(PYEXEC) mypy view.py # --strict  --exclude ui/ui_form.py --exclude ui/form_ui.py

# tests:
# 	$(PYEXEC) pytest #-W ignore::DeprecationWarning

# cov:
# 	$(PYEXEC) pytest --cov --cov-report=html #-W ignore::DeprecationWarning
# 	open htmlcov/index.html


venv:
	poetry env use $(PYTHON)
	poetry config --local virtualenvs.in-project true
	poetry install
