test:
    pytest tests/ -v

precommit:
    pre-commit run --all-files

ruff:
    pre-commit run ruff --all-files

mypy:
    pre-commit run mypy --all-files

lint: ruff mypy

list:
    just --list

bandit:
    bandit -r app/

safety:
    safety scan

secure: bandit safety
