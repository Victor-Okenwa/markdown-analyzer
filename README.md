# Markdown Directory Analyzer

This project is a Python-based tool that analyzes a directory (and its subdirectories) of Markdown (`.md`) files and generates a comprehensive summary report. The goal is to provide insight into documentation quality and content metrics for codebases, technical blogs, knowledge bases, or any project using Markdown files.

---

## Features

- **Recursive Scanning:** Analyzes all Markdown files within the specified root directory and subfolders.
- **Per-File Metrics:** Reports for each file:
  - File path
  - Word count
  - Header (e.g., `#`/`##`) count
  - Code block count
  - Estimated reading time (minutes, at 200 wpm)
- **Aggregated Directory Metrics:** 
  - Total number of Markdown files
  - Combined word and code block counts
  - Average reading time across files
- **Generates a Markdown Summary:** Output includes a table breakdown of each file for easy reporting and sharing.
- **CLI or Interactive Use:** Accepts directory as a command-line argument or prompts for user input.
- **Saves Output:** Automatically saves analysis to `summary_report.md` in the current working directory.

---

## Getting Started

### 1. **Install Requirements**

Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 2. **Usage**

**From the command line:**
```bash
python main.py /path/to/your/markdown-directory
```

**Or run and enter directory interactively:**
```bash
python main.py
# When prompted, type the target folder path (or press Enter for current directory)
```

After running, view or share your `summary_report.md`!

---

## Example Output

```
# Markdown Directory Analysis Summary

- **Total Files Analyzed:** 5
- **Total Word Count:** 12,500 words
- **Total Code Blocks:** 16
- **Avg Reading Time:** 10.32 minutes

---

### Individual File Breakdown
| File Path           | Words | Headers | Code Blocks | Est. Read Time |
| :---                | :---  | :---    | :---        | :---           |
| docs/intro.md       | 1200  | 12      | 2           | 6.0 min        |
| guide/howto.md      | 3000  | 25      | 5           | 15.0 min       |
| ...                 | ...   | ...     | ...         | ...            |
```

---

## Project Structure

- `main.py` &mdash; Entry point, CLI, report formatting and saving.
- `analyzer.py` &mdash; Analyzes the entire directory and aggregates results.
- `parser.py` &mdash; Parses individual Markdown files and calculates metrics.
- `models.py` &mdash; Data models (using Pydantic) for structured report and file metrics.
- `requirements.txt` &mdash; List of Python dependencies.

---

## Extending / Customization

- Add new metrics (e.g. link integrity, image stats) in `parser.py` and update models for richer reports.
- Adjust reading speed estimation by changing the calculation logic.
- Customize output format by editing the Markdown rendering in `main.py`.

---

## License

MIT License

---