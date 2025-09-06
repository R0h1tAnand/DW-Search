# DW-Search

[![PyPI Version](https://img.shields.io/pypi/v/dw-search)](https://pypi.org/project/dw-search/)
[![Downloads](https://static.pepy.tech/badge/dw-search)](https://pepy.tech/project/dw-search)
[![License](https://img.shields.io/pypi/l/dw-search)](LICENSE)

> Discover, collect, and export .onion links safely and efficiently via multiple Tor search engines.

DW-Search is a lightweight, CLI-first Python tool designed for security researchers, incident responders, and developers who need structured access to Tor (.onion) search results. It runs parallel queries against multiple onion search backends, normalizes results, and produces CSV output ready for analysis.

## Why DW-Search?

- Run many engines at once to increase coverage
- High-throughput collection using multiprocessing
- Clean, configurable CSV output for downstream tooling
- Works over Tor (SOCKS proxy) — keeps traffic on the Tor network
- CLI focused: scriptable, automatable, and easy to integrate

## Quick start

Prerequisites

- Python 3.6+
- Tor (Tor Browser or system tor) running and accepting SOCKS connections (default: 127.0.0.1:9050)

Install (recommended)

PowerShell / Bash:

```powershell
pip install dw-search
```

From source

```powershell
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
pip install -r requirements.txt
pip install -e .
```

Basic usage

```powershell
# Simple search
dw-search "privacy policies"

# Save to CSV with custom fields
dw-search "privacy" --output results.csv --fields engine domain link

# Use specific engines and limit pages
dw-search "blockchain" --engines ahmia phobos --limit 5
```

Tip: use `--continuous_write True` for long-running searches so results are flushed incrementally.

## Common options

- --proxy           Tor SOCKS proxy (default: 127.0.0.1:9050)
- --output          Output file path (CSV)
- --fields          Space-separated fields to include in output (e.g. "engine name link")
- --field_delimiter Field delimiter for CSV output (default: `,`)
- --engines         Comma/space-separated engines to use (default: all)
- --exclude         Engines to exclude
- --limit           Max pages per engine (0 = unlimited)
- --mp_units        Number of worker processes (default: cpu_count - 1)

Run `dw-search --help` for the complete list of flags and examples.

## Tor configuration

1. Install Tor (Tor Browser or tor daemon).
2. Start Tor and verify a SOCKS proxy (commonly 127.0.0.1:9050).
3. Use the default proxy or pass a custom address with `--proxy`.

Use Tor responsibly: respect site terms and rate limits.

## Supported search engines (representative)

Availability changes frequently; check `src/dw_search/core.py` for the current list.

| Engine | Status |
|--------|--------|
| ahmia | Active |
| darksearchio | Active |
| onionland | Active |
| phobos | Active |
| tor66 | Active |
| haystack | Active |
| torgle | Variable |
| notevil | Offline/variable |

## Development

Local development (PowerShell):

```powershell
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run tests

```powershell
python -m unittest discover tests
```

Docs

See `docs/index.md` for extended documentation and examples.

## Contributing

Contributions welcome. Suggested workflow:

1. Fork and create a feature branch
2. Add tests for changes
3. Run tests locally
4. Open a clear Pull Request

Follow PEP 8 and keep new dependencies minimal.

## License

This project is licensed under the GNU General Public License v3.0 — see `LICENSE`.

## Disclaimer

Intended for legitimate research and educational use. The authors are not responsible for misuse. Ensure compliance with local laws and target site policies.

## Contact

- Issues: https://github.com/R0h1tAnand/DW-Search/issues
- Maintainer email: (not provided in repository)

---

If you want, I can also:

- add a short quickstart doc in `docs/`
- add a `README-DEV.md` with dev notes and common troubleshooting

[![PyPI Version](https://img.shields.io/pypi/v/dw-search)](https://pypi.org/project/dw-search/)
[![Downloads](https://static.pepy.tech/badge/dw-search)](https://pepy.tech/project/dw-search)
[![License](https://img.shields.io/pypi/l/dw-search)](LICENSE)

# DW-Search

> Discover, collect, and export .onion links safely and efficiently via multiple Tor search engines.

DW-Search is a lightweight, CLI-first Python tool aimed at security researchers, digital forensics professionals, and developers who need to programmatically discover Tor (.onion) resources. It orchestrates parallel queries across several onion search engines, normalizes results, and writes structured output for analysis.

## Highlights

- Multi-engine scraping (many popular .onion search providers)
- Fast, parallel collection using multiprocessing
- Flexible CSV output with configurable fields and delimiters
- Built to run over Tor (SOCKS proxy support)
- Robust CLI with filtering, exclusion, and continuous write options

## Quick start

Prerequisites

- Python 3.6+
- Tor (Tor Browser or tor daemon) running locally and accepting SOCKS connections (default: 127.0.0.1:9050)

Install (recommended: PyPI)

PowerShell (Windows) / Bash (Linux/macOS):

```powershell
pip install dw-search
```

From source

```powershell
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
pip install -r requirements.txt
pip install -e .
```

Basic usage

```powershell
# Simple search
dw-search "privacy policies"

# Save to CSV with custom fields
dw-search "privacy" --output results.csv --fields engine domain link

# Use specific engines and limit pages
dw-search "blockchain" --engines ahmia phobos --limit 5
```

If you plan to run long or large searches, use `--continuous_write True` so results are flushed incrementally.

## Typical options

- --proxy           Tor SOCKS proxy (default: 127.0.0.1:9050)
- --output          Output file path (CSV)
- --fields          Space-separated fields to include in output (e.g. "engine name link")
- --field_delimiter Field delimiter for CSV output (default: `,`)
- --engines         Comma/space-separated engines to use (default: all)
- --exclude         Engines to exclude
- --limit           Max pages per engine (0 = unlimited)
- --mp_units        Number of worker processes (default: cpu_count - 1)

Run `dw-search --help` for the full list of flags and examples.

## Tor configuration

1. Install Tor (Tor Browser or system tor).
2. Start Tor and confirm a SOCKS proxy is available (commonly 127.0.0.1:9050).
3. Point the tool at that proxy (default is used automatically).

Note: using Tor responsibly is important — respect rate limits and terms of service of target sites.

## Supported search engines (sample)

The project integrates with many onion search endpoints. Availability fluctuates — this list is representative, not guaranteed up-to-date.

| Engine | Status |
|--------|--------|
| ahmia | Active |
| darksearchio | Active |
| onionland | Active |
| phobos | Active |
| tor66 | Active |
| haystack | Active |
| torgle | Variable |
| notevil | Offline/variable |

For the current engine list and status, see the `src/dw_search/core.py` implementation which enumerates supported backends.

## Development

Local development setup (PowerShell)

```powershell
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run tests

```powershell
python -m unittest discover tests
```

Docs

See `docs/index.md` for extended documentation and examples.

## Contributing

Contributions are welcome. Please follow these simple steps:

1. Fork the repo and create a feature branch
2. Add tests for any new behavior
3. Run the test suite and ensure it passes
4. Open a clear Pull Request with a description of your changes

Coding style: follow PEP 8 and keep new dependencies minimal.

## License

This project is licensed under the GNU General Public License v3.0 — see `LICENSE`.

## Disclaimer

DW-Search is provided for legitimate research, incident response, and educational use. The authors are not responsible for misuse. Ensure you comply with local laws and the terms of service of any sites you interact with.

## Contact & support

- Issues: https://github.com/R0h1tAnand/DW-Search/issues
- Email: (maintainer email not provided in repo)

---
