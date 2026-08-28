PY     := python3
PIP    := pip
PYARGS :=
ARGS   := --port=2020
DEPS   := .requirements

run: init.py
	$(PY) $(PYARGS) $^ $(ARGS)
