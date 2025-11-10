.PHONY: init run test clean

init:
\tpython -m venv .venv
\tpip install --upgrade pip
\tpip install -r requirements.txt || true
\techo "✅ Environment ready."

run:
\tpython -m src.mlproject.core.test_settings

test:
\tpytest -q || echo "Add tests in /tests first."

clean:
\trm -rf __pycache__ .pytest_cache artifacts logs
