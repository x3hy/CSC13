PY     := python3
PIP    := pip
PYARGS :=
ARGS   := -dpi=2.0
DEPS   := .requirements

run: init.py
	$(PY) $(PYARGS) $^ $(ARGS)
