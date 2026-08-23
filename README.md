# KLM — Terminal AI Assistant

KLM is a lightweight terminal-based AI assistant written in Python. It provides a small interactive shell for simple utilities (date/time, coin toss, binary/text conversion, QR generation, YouTube downloads) and can forward free-text prompts to the Pollinations text generation API.

Key points:
- Small, single-file entrypoint: `klm.py` (also includes helper modules `kcli.py` and `stone.py`).
- Designed for interactive use in a terminal.
- Stores small local state under the `mem/` directory (API key, model, user name, and last response memory).

Features
- Terminal chat + command interface
- AI-powered responses (via Pollinations API)
- Small utilities: binary↔text conversion, QR code generator, YouTube download helper, simple games
- Lightweight — minimal third-party dependencies

Quick start

Prerequisites
- Python 3.8+ (3.8 or newer recommended)
- Git (to clone)
- FFmpeg (optional, recommended for yt-dlp video processing if you need post-processing)

Clone and install

```bash
git clone https://github.com/Kash-KLM-001/KLM-Assistant.git
cd KLM-Assistant
python -m pip install -r requirements.txt
```

Configuration
- On first run `klm.py` will create a `mem/` directory and prompt you for two values which it saves in files under `mem/`:
  - `mem/api_key.txt` — your Pollinations API key
  - `mem/ai_model.txt` — the model identifier to use with Pollinations
- You can edit those files manually if you prefer to preconfigure the assistant.

Run

```bash
python klm.py
```

The program prompts for your user name the first time and then starts an interactive prompt. Type `help` at the prompt to see available commands.

Available commands (extracted from code)
- /date — show today's date
- /time — show the current time
- /toss — coin toss
- /w_t_b — convert text to binary (writes binary string)
- /b_t_w — convert binary to text
- /cli — enter the bundled CLI (`K_CLI` from `kcli.py`)
- /install_deps — tries to install missing Python packages (runs pip)
- /gen_qr — generate a QR code image
- /sum — evaluate a numeric expression (uses `eval()` on user input)
- /calculate_death — playful (random years)
- /ytd — download YouTube video using `yt-dlp`
- games / lets play — plays rock-paper-scissors (uses `stone.py`)

Security & important notes
- The `/sum` command calls Python's `eval()` on user input. That's unsafe for untrusted environments — avoid running this in production or with untrusted users.
- The `/install_deps` command runs pip installs automatically. Review its behavior before using.
- The assistant stores your API key in plain text under `mem/api_key.txt`. Treat it like any secret and do not commit it to version control.

Dependencies
See `requirements.txt` for the external Python packages used by the project.

Contributing
Bug reports, suggestions and pull requests are welcome. Please open an issue for larger changes or to discuss features.

License
MIT — see the `LICENSE` file.

Author: Kash
