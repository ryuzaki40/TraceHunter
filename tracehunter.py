from core.parse_browser import extract_browser_history
from core.parse_deleted import extract_deleted_files
from core.parse_users import extract_user_accounts
from core.osint_enrich import enrich_browser_history
from core.visualize import plot_browser_activity

OUTPUT_DIR = "output"
BROWSER_HISTORY_PATH = f"{OUTPUT_DIR}/browser_history.json"
DELETED_FILES_PATH = f"{OUTPUT_DIR}/deleted_files.json"
USER_ACCOUNTS_PATH = f"{OUTPUT_DIR}/user_accounts.json"
VISUALIZATION_PATH = f"{OUTPUT_DIR}/visuals/browser_timeline.html"

def main():
    print("🚀 TraceHunter Initiated...\n")

    # Phase 1: Artifact Parsing
    print("[PHASE 1] Parsing Artifacts...")
    extract_browser_history(output_path=BROWSER_HISTORY_PATH)
    extract_deleted_files(output_path=DELETED_FILES_PATH)
    extract_user_accounts(output_path=USER_ACCOUNTS_PATH)

    # Phase 2: OSINT Enrichment
    print("\n[PHASE 2] Enriching Browser History with OSINT...")
    enrich_browser_history(input_path=BROWSER_HISTORY_PATH)

    # Phase 3: Visualization
    print("\n[PHASE 3] Visualizing Browser Activity Timeline...")
    plot_browser_activity(
        json_path=BROWSER_HISTORY_PATH,
        output_path=VISUALIZATION_PATH
    )

    print("\n✅ All phases complete. Check the output folder!")

if __name__ == "__main__":
    main()
