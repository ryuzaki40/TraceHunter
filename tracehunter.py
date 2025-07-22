from core.extract import extract_artifacts_from_logs

if __name__ == "__main__":
    log_dir = "data/sample_logs"
    artifacts = extract_artifacts_from_logs(log_dir)
    print("🧬 Extracted Artifacts:")
    for key, values in artifacts.items():
        print(f"{key.upper()}:")
        for val in values:
            print(f"  - {val}")
