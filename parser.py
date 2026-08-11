# Single file parsing Logic

from models import DirectoryReport, FileMetrics


def analyze_file(file_path: str) -> FileMetrics:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        word_count: int = len(content.split())
        reading_time: float = word_count/200.0

        lines = content.splitlines()
        header_count: int = len([line for line in lines if line.strip().startswith("#")])
        code_block_count: int = len([line for line in lines if line.strip().startswith("```")])//2

        return FileMetrics(
            file_path=file_path,
            word_count=word_count,
            reading_time_minutes=reading_time,
            header_count=header_count,
            code_block_count=code_block_count,
        )


def analyze_directory(directory_path: str) -> DirectoryReport:
    
