# README.md

# Text Summarization Application

This project is a Python-based text summarization application that utilizes advanced algorithms to generate concise summaries from larger texts. It is designed to help users quickly understand the main points of lengthy documents.

## Features

- Summarization of text using various algorithms.
- Utility functions for text processing.
- Interactive Jupyter notebook for experimentation and visualization.
- Unit tests to ensure the reliability of the summarization logic.

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Ryanike1022/text-summarization.git
cd text-summarization
pip install -r requirements.txt
```

## Usage

To use the text summarization functionality, you can import the `Summarizer` class from the `src/summarizer.py` file:

```python
from src.summarizer import Summarizer

summarizer = Summarizer()
summary = summarizer.summarize("Your text here.")
print(summary)
```

## Jupyter Notebook

For an interactive experience, open the Jupyter notebook located in the `notebooks` directory:

```bash
jupyter notebook notebooks/text_summarization.ipynb
```

## Running Tests

To ensure everything is working correctly, you can run the unit tests provided in the `tests` directory:

```bash
pytest tests/test_summarizer.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.