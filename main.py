from pathlib import Path
from parser import analyze_directory
from models import DirectoryReport

# formats report into a beautiful Markdown string using multi-line f-strings
def format_markdown_report(report: DirectoryReport) -> str:
    # 1. Build table rows from report.files

    table_rows = "\n".join(
        f"| {f.file_path} | {f.word_count} | {f.header_count} | {f.code_block_count} | {f.reading_time_minutes} min |"
        for f in report.files
    )

    # 2. Construct the full report string
    report_md = f""" # Markdown Directory Analysis Summary

        - **Total Files Analyzed:** {report.total_files}
        - **Total Word Count:** {report.total_words:,} words
        - **Total Code Blocks:** {report.total_code_blocks}
        - **Avg Reading Time:** {report.avg_reading_time} minutes

        ---

        ### Individual File Breakdown
        | File Path | Words | Headers | Code Blocks | Est. Read Time |
        | :--- | :--- | :--- | :--- | :--- |
        {table_rows}
    """
    return report_md


def main():
    target_path = input(" Input local directory: \n")
    if Path(target_path).exists():
        analysis = analyze_directory(target_path)
        print(analysis)



