import json
from typing import List, Dict

def extract_user_accounts(file_path: str) -> List[Dict]:
    """
    Parses user accounts from the provided JSON log file.

    Args:
        file_path (str): Path to the JSON file containing user account data.

    Returns:
        List[Dict]: A list of parsed user account artifacts.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        artifacts = []
        for entry in data:
            artifact = {
                "type": "user_account",
                "username": entry.get("username"),
                "user_id": entry.get("user_id"),
                "creation_date": entry.get("creation_date"),
                "home_directory": entry.get("home_directory"),
                "source": file_path
            }
            artifacts.append(artifact)

        return artifacts

    except Exception as e:
        print(f"[!] Failed to parse user accounts: {e}")
        return []
