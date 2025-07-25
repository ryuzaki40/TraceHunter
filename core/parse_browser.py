import sqlite3
import os
import datetime

def extract_browser_history(file_path):
    """
    Extracts browsing history from a Chrome history SQLite file.

    Args:
        file_path (str): Path to the History file.

    Returns:
        List[Dict]: List of browsing history entries.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[ERROR] File not found: {file_path}")

    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()

        query = """
        SELECT url, title, visit_count, last_visit_time
        FROM urls
        ORDER BY last_visit_time DESC
        LIMIT 100
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        def convert_chrome_time(timestamp):
            """Chrome timestamps are in microseconds since Jan 1, 1601"""
            try:
                epoch_start = datetime.datetime(1601, 1, 1)
                return (epoch_start + datetime.timedelta(microseconds=timestamp)).strftime('%Y-%m-%d %H:%M:%S')
            except Exception:
                return "Invalid Time"

        history = []
        for url, title, visit_count, last_visit_time in rows:
            history.append({
                "url": url,
                "title": title,
                "visit_count": visit_count,
                "last_visit_time": convert_chrome_time(last_visit_time)
            })

        return history

    except sqlite3.DatabaseError as e:
        raise ValueError(f"[ERROR] SQLite error: {e}")

    finally:
        conn.close()
