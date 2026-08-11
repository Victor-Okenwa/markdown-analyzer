# Directory wide scanning

# Directory Scanner & Aggregator
from pathlib import Path
from models import DirectoryReport, FileMetrics
from parser import analyze_file


def analyze_directory(directory_path: str) -> DirectoryReport:
    path = Path(directory_path)

    mark_down_files = path.rglob("*.md") 
    
    metrics_list: list[FileMetrics] = [
        analyze_file(str(file_path)) for file_path in mark_down_files
    ]

    total_files: int = len(metrics_list)
    total_words: int = sum(file.word_count for file in metrics_list)
    total_code_blocks: int = sum(file.code_block_count for file in metrics_list)

    avg_reading_time= 0.0

    if total_files > 0:
        avg_reading_time: float = sum(file.reading_time_minutes for file in metrics_list) / total_files

    return DirectoryReport(
        total_files=total_files,
        total_words=total_words,
        total_code_blocks=total_code_blocks,
        avg_reading_time=round(avg_reading_time, 2),
        files=metrics_list
    )

