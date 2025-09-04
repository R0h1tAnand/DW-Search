# DW-Search Documentation

## Overview

DW-Search is a powerful Python-based command-line tool designed for scraping URLs from various Tor (.onion) search engines. It provides a comprehensive solution for researchers, security professionals, and developers who need to collect data from the dark web efficiently and safely.

### Key Features

- **Multi-Engine Support**: Scrapes from 16+ different .onion search engines
- **Multiprocessing**: Utilizes multiple CPU cores for faster scraping
- **Flexible Output**: CSV format with customizable fields and delimiters
- **Tor Integration**: Built-in support for Tor proxy configuration
- **Progress Tracking**: Real-time progress bars with tqdm
- **Error Handling**: Robust error handling and retry mechanisms
- **Customizable**: Extensive command-line options for fine-tuning

### Architecture

The project follows a modular structure:

```
DW-Search/
├── src/dw_search/
│   ├── __init__.py
│   └── core.py          # Main scraping logic
├── tests/
├── docs/
├── requirements.txt
└── setup.py
```

## Installation

### Prerequisites

- Python 3.6+
- Tor (for .onion access)
- Internet connection

### From PyPI

```bash
pip install dw-search
```

### From Source

```bash
git clone https://github.com/R0h1tAnand/DW-Search.git
cd DW-Search
pip install -r requirements.txt
pip install -e .
```

### Dependencies

- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `tqdm` - Progress bars
- `termcolor` - Colored terminal output
- `PySocks` - SOCKS proxy support
- `html5lib` - HTML parsing
- `argparse` - Command-line argument parsing

## Quick Start

### Basic Usage

```bash
# Search for "python" on all engines
dw-search "python"

# Search with custom output file
dw-search "machine learning" --output results.csv

# Use specific engines only
dw-search "security" --engines ahmia tor66 phobos
```

### Tor Setup

1. Install Tor Browser or Tor daemon
2. Ensure Tor is running on default port (9050)
3. Run DW-Search (it will automatically use Tor proxy)

## Configuration

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `search` | Search query (required) | - |
| `--proxy` | Tor proxy address | `127.0.0.1:9050` |
| `--output` | Output file path | `output_$SEARCH_$DATE.txt` |
| `--continuous_write` | Write results progressively | `False` |
| `--limit` | Max pages per engine | `0` (unlimited) |
| `--engines` | Specific engines to use | All available |
| `--exclude` | Engines to exclude | None |
| `--fields` | CSV fields to output | `engine name link` |
| `--field_delimiter` | CSV delimiter | `,` |
| `--mp_units` | Number of processes | `cpu_count - 1` |

### Output Fields

Available CSV fields:
- `engine` - Search engine name
- `name` - Link title/description
- `link` - URL
- `domain` - Domain name

### Examples

```bash
# Basic search
dw-search "dark web research"

# Advanced search with custom fields
dw-search "bitcoin" --fields engine domain link --field_delimiter ";"

# Limited search on specific engines
dw-search "privacy" --engines ahmia darksearchio --limit 5

# Exclude certain engines
dw-search "security" --exclude notevil torgle
```

## API Reference

### Core Functions

#### `scrape()`

Main scraping function that orchestrates the entire search process.

**Parameters:**
- Uses global `args` from command-line parsing

**Process:**
1. Parses search query and builds filename
2. Initializes multiprocessing pool
3. Distributes work across engines
4. Collects and processes results
5. Writes output to CSV

#### Engine-Specific Functions

Each search engine has its own scraping function:

- `ahmia_search(searchstr)`
- `darksearchio_search(searchstr)`
- `onionland_search(searchstr)`
- etc.

**Parameters:**
- `searchstr` (str): Search query

**Returns:**
- List of result dictionaries

### Data Structures

#### Result Dictionary

```python
{
    'engine': 'ahmia',
    'name': 'Example Title',
    'link': 'http://example.onion/page',
    'domain': 'example.onion'
}
```

#### Engine Configuration

```python
ENGINES = {
    "ahmia": "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion",
    "darksearchio": "http://darksearch.io",
    # ... more engines
}
```

## Supported Engines

| Engine | Status | URL |
|--------|--------|-----|
| ahmia | Active | juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion |
| darksearchio | Active | darksearch.io |
| onionland | Active | 3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion |
| notevil | Offline | hss3uro2hsxfogfq.onion |
| darksearchenginer | Active | l4rsciqnpzdndt2llgjx3luvnxip7vbyj6k6nmdy4xs77tx6gkd24ead.onion |
| phobos | Active | phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion |
| onionsearchserver | Active | 3fzh7yuupdfyjhwt3ugzqqof6ulbcl27ecev33knxe3u7goi3vfn2qqd.onion |
| torgle | Active | no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion |
| tor66 | Active | tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion |
| haystack | Active | haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion |
| deeplink | Offline | deeplinkdeatbml7.onion |

*Note: Engine status may change over time. Some engines may be temporarily offline.*

## Troubleshooting

### Common Issues

#### Tor Connection Issues

**Problem:** `Connection refused` or proxy errors

**Solution:**
1. Ensure Tor is running: `sudo systemctl start tor`
2. Check Tor port: `netstat -tlnp | grep 9050`
3. Verify proxy settings: `--proxy 127.0.0.1:9050`

#### No Results Found

**Problem:** Empty output file

**Solutions:**
- Check internet connectivity
- Verify Tor configuration
- Try different search engines: `--engines ahmia tor66`
- Increase page limit: `--limit 10`

#### Multiprocessing Errors

**Problem:** Issues with parallel processing

**Solution:**
- Reduce processes: `--mp_units 1`
- Check system resources
- Use sequential mode for debugging

#### CSV Encoding Issues

**Problem:** Special characters in output

**Solution:**
- Use UTF-8 encoding
- Change delimiter: `--field_delimiter "|"`

### Debug Mode

Enable verbose output by modifying the logging level in the source code.

### Performance Tips

1. Use specific engines instead of all
2. Limit pages per engine
3. Adjust multiprocessing units based on system
4. Use continuous write for large searches

## Development

### Project Structure

```
src/dw_search/
├── __init__.py      # Package initialization
└── core.py          # Main application logic

tests/
├── __init__.py
└── test_core.py     # Unit tests

docs/
└── index.md         # This documentation

.github/workflows/
└── ci.yml           # CI/CD pipeline
```

### Adding New Engines

1. Add engine URL to `ENGINES` dictionary
2. Implement scraping function following the pattern:
   ```python
   def new_engine_search(searchstr):
       # Implementation
       return results
   ```
3. Add function call in main scraping loop
4. Update documentation

### Testing

```bash
# Run all tests
python -m unittest discover tests

# Run specific test
python -m unittest tests.test_core.TestDWSearch.test_example
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Handle exceptions appropriately

## Security Considerations

- **Legal Compliance**: Ensure usage complies with local laws
- **Ethical Use**: Respect privacy and avoid harmful activities
- **Tor Usage**: Always use Tor for .onion access
- **Data Handling**: Be cautious with scraped data

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](../LICENSE) file for details.

## Support

For support and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the README for examples

## Changelog

### Version 1.3
- Updated package structure
- Added comprehensive documentation
- Improved error handling
- Enhanced multiprocessing support

---

*This documentation is for DW-Search v1.3. For the latest updates, check the GitHub repository.*
