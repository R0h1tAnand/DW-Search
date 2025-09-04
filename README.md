# DW-Search

[![PyPI Version](https://img.shields.io/pypi/v/dw-search)](https://pypi.org/project/dw-search/)
[![Downloads](https://static.pepy.tech/badge/dw-search)](https://pepy.tech/project/dw-search)
[![License](https://img.shields.io/pypi/l/dw-search)](https://github.com/R0h1tAnand/DW-Search/blob/main/LICENSE)
[![CI](https://github.com/R0h1tAnand/DW-Search/actions/workflows/ci.yml/badge.svg)](https://github.com/R0h1tAnand/DW-Search/actions)

A powerful Python tool for discovering and scraping URLs from various Tor (.onion) search engines. Built for researchers, security professionals, and developers exploring the dark web safely and efficiently.

## ✨ Features

- 🔍 **Multi-Engine Scraping**: Supports 16+ different .onion search engines
- ⚡ **High Performance**: Utilizes multiprocessing for faster results
- 📊 **Flexible Output**: CSV format with customizable fields
- 🛡️ **Tor Integration**: Seamless proxy configuration for .onion access
- 📈 **Progress Tracking**: Real-time progress bars and statistics
- 🎯 **Selective Scraping**: Choose specific engines or exclude unwanted ones
- 🔧 **Command-Line Interface**: Easy-to-use CLI with extensive options

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Tor Browser or Tor daemon running
- Internet connection

### Installation

#### From PyPI (Recommended)

```bash
pip install dw-search
```

#### From Source

```bash
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
pip install -r requirements.txt
pip install -e .
```

### Basic Usage

```bash
# Simple search
dw-search "python programming"

# Search with custom output
dw-search "machine learning" --output results.csv

# Use specific search engines
dw-search "security research" --engines ahmia tor66 phobos
```

## 📖 Usage Guide

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `search` | Search query (required) | - |
| `--proxy` | Tor proxy address | `127.0.0.1:9050` |
| `--output` | Output file path | `output_$SEARCH_$DATE.txt` |
| `--limit` | Max pages per engine | `0` (unlimited) |
| `--engines` | Specific engines to use | All available |
| `--exclude` | Engines to exclude | None |
| `--fields` | CSV fields to output | `engine name link` |
| `--mp_units` | Number of processes | `cpu_count - 1` |

### Advanced Examples

```bash
# Limit results and use specific engines
dw-search "blockchain" --engines ahmia darksearchio --limit 5

# Custom output fields
dw-search "privacy" --fields engine domain link --field_delimiter ";"

# Exclude certain engines
dw-search "anonymity" --exclude notevil torgle

# Continuous writing for large searches
dw-search "big data" --continuous_write True
```

### Tor Configuration

1. Install and start Tor Browser
2. Ensure Tor is listening on port 9050 (default)
3. DW-Search will automatically route requests through Tor

## 🔧 Supported Search Engines

| Engine | Status | Description |
|--------|--------|-------------|
| ahmia | ✅ Active | Popular clearnet .onion search |
| darksearchio | ✅ Active | Dark web search engine |
| onionland | ✅ Active | Comprehensive .onion directory |
| phobos | ✅ Active | Advanced dark web search |
| tor66 | ✅ Active | Fast .onion search results |
| haystack | ✅ Active | Curated .onion links |
| onionsearchserver | ✅ Active | Dedicated .onion search |
| darksearchenginer | ✅ Active | Specialized search engine |
| torgle | ⚠️ Variable | Alternative search option |
| notevil | ❌ Offline | Currently unavailable |
| onionsearchengine | ❌ Offline | Currently unavailable |
| tordex | ❌ Offline | Currently unavailable |
| tor66 | ✅ Active | Fast .onion search results |
| tormax | ❌ Offline | Currently unavailable |
| multivac | ❌ Offline | Currently unavailable |
| evosearch | ❌ Offline | Currently unavailable |
| deeplink | ❌ Offline | Currently unavailable |

*Engine availability may change over time. Some engines may be temporarily offline.*

## 🏗️ Development

### Setup Development Environment

```bash
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### Running Tests

```bash
python -m unittest discover tests
```

### Building Documentation

Documentation is available in the `docs/` directory. View the full documentation at [docs/index.md](docs/index.md).

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run the test suite: `python -m unittest discover tests`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add unit tests for new features
- Update documentation for API changes
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

DW-Search is intended for educational and research purposes only. Users are responsible for complying with all applicable laws and regulations when using this tool. The authors are not responsible for any misuse or illegal activities.

## 📞 Contact

For questions, issues, or contributions:

- 📧 Email: [Your Email Here]
- 🐛 Issues: [GitHub Issues](https://github.com/R0h1tAnand/DW-Search/issues)
- 📖 Documentation: [Full Docs](docs/index.md)

---

**Made with ❤️ for the research community**

*If you find this tool useful, please consider starring the repository!* ⭐
