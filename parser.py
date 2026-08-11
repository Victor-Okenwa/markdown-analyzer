# Single file parsing Logic
from pydantic import BaseModel, Field

#This model represents the analyzed statistics of a single Markdown file.
class FileMetrics(BaseModel):
    file_path: str
    word_count: int = Field(default=0, ge=0)
    reading_time_minutes: float = Field(default=0.0)
    header_count: int = Field(default=0)
    code_block_count: int = Field(default=0)
    has_broken_links: bool = Field(default=False)

# This model represents the aggregated summary of an entire folder filled with Markdown files.
class DirectoryReport(BaseModel): 
    total_files: int
    total_words: int
    total_code_blocks: int
    avg_reading_time: float
    files: list[FileMetrics]

