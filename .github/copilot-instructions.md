# KLM-Assistant Copilot Instructions

## Source-code protection

- Do NOT modify Python source-code files.
- Do NOT modify `klm.py`, `kcli.py`, `stone.py`, or any other `.py` source file.
- Do NOT add, remove, rename, or rewrite Python source files.
- If a Python code problem is found, report it instead of fixing it.

## Allowed files

Copilot may modify:
- `README.md`
- `requirements.txt`
- `.github/copilot-instructions.md`
- Documentation files

## README

- Keep `README.md` synchronized with the actual repository.
- Inspect the source code before documenting features.
- Do not document nonexistent features.
- Keep installation and usage instructions accurate.

## Requirements

- Keep `requirements.txt` synchronized with the project's actual Python dependencies.
- Add missing dependencies when the source code requires them.
- Remove dependencies that are clearly unused when appropriate.
- Do not add unnecessary packages.

## Git

- Create clear, descriptive commit messages.
- Create a Pull Request for changes.
- Keep source-code modifications out of the PR.

## Security

- Never commit API keys, tokens, passwords, or other secrets.
- Never put real credentials in `README.md` or `requirements.txt`.
