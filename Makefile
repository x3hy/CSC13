PY     := python3
PIP    := pip
PYARGS :=
ARGS   := --port=2020 --backend-only
DEPS   := .requirements

run: init.py
	$(PY) $(PYARGS) $^ $(ARGS)

