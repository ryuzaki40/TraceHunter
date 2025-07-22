import os
import re 
import json 

def extract_artifacts_from_logs(log_dir):
    regrex_patterns = {
        "emails": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "ips": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "phones": r"\+?\d[\d\- ]{9,14}\d",
        "urls": r"https?://[^\s]+"
    }

    results = {key: set() for key in regrex_patterns}

    for root, _, files in os.walk(log_dir): 
        for file in files: 
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding= 'utf-8', errors='ignore') as f:
                content = f.read()
                for key , pattern in regrex_patterns.items():
                    matches= re.findall(pattern, content)
                    results[key].update(matches)

    for key in results:
        results[key] = list(results[key])

    os.makedirs("output", exist_ok= True)
    with open("output/artifacts.json", "w") as outfile:
        json.dump(results, outfile, indent=1)

    return results 
