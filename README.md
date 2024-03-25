# SearchPyPI

SearchPyPI is a Python script designed to quickly search and open multiple PyPI (Python Package Index) search results in your default web browser.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Efficiently retrieves top search results from PyPI.
- Opens multiple search result links in separate browser tabs.
- Customizable: Set the number of search results to open in tabs.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/benrandom/searchpypi.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Execute the script in your terminal or command prompt, passing the desired search term as an argument:

```bash
python3 searchpypi.py <search term>
```

Replace `<search term>` with the keyword you want to search for on PyPI.

## Example

To search for packages related to "web scraping":

```bash
python3 searchpypi.py web scraping
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.