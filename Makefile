PY     := python3
PIP    := pip
PYARGS :=
DEPS   := .requirements

run: init.py
	$(PY) $(PYARGS) $^ $(ARGS)

backend: init.py
	$(PY) $(PYARGS) $^ --backend-only

frontend: init.py
	$(PY) $(PYARGS) $^ --frontend-only
