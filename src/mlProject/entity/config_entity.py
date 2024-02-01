from dataclasses import dataclass
from pathlib import Path

# instead of self.variable we can direclty define variables using this decorator, path, str are data types
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


