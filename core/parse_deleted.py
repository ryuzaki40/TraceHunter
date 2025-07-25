import os
import datetime

def extract_deleted_files(directory):
    """
    Simulate extraction of deleted files by checking Recycle Bin-like names.

    Args:
        directory (str): Path to the directory to scan.

    Returns:
        List[Dict]: List of suspected deleted files with metadata.
    """
    deleted_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Simulate: Files with ~$ or .tmp or in Recycle Bin
            if file.startswith("~$") or file.endswith(".tmp") or "Recycle.Bin" in root or "$Recycle.Bin" in root:
                try:
                    stat = os.stat(file_path)
                    deleted_files.append({
                        "file_name": file,
                        "file_path": file_path,
                        "size": stat.st_size,
                        "last_modified": datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return deleted_files
