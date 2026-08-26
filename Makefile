PY     := python3
PYARGS :=
ARGS   := -dpi=4.0

run: init.py
	$(PY) $(PYARGS) $^ $(ARGS)
