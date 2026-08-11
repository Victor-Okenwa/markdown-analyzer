from pathlib import Path
import sys
from analyzer import analyze_directory
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
    # Allow reading path from CLI argument OR interactive user input
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = (
            input("Input local directory path (press Enter for current folder '.'): ").strip()
            or "."
        )

    path = Path(target_path)
    
    if not path:
        print(f"Error: Path '{target_path}' does not exist.")
        return

    print(f"\n🔍 Analyzing Markdown files in: {path.resolve()} ...\n")

    # Run analysis & format output
    analysis = analyze_directory(str(path))
    formatted_report = format_markdown_report(analysis)

    print(formatted_report)

    # Save output to summary_report.md file
    output_file = Path("summary_report.md")
    output_file.write_text(formatted_report, encoding="utf-8")

    print(f"✅ Report saved to: {output_file.resolve()}")


if __name__ == "__main__":
    main()



