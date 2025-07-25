import json
import requests
import tldextract
import time

URLSCAN_API = "https://urlscan.io/api/v1/search/?q=domain:{}"

def extract_domain(url):
    extracted = tldextract.extract(url)
    domain = ".".join(part for part in [extracted.domain, extracted.suffix] if part)
    return domain.lower()

def enrich_urlscan(domain):
    try:
        print(f"[+] Querying URLScan for: {domain}")
        resp = requests.get(URLSCAN_API.format(domain), timeout=10)
        if resp.status_code != 200:
            return {"error": f"Non-200 response: {resp.status_code}"}
        
        data = resp.json()
        if data.get("total", 0) == 0:
            return {"status": "unknown"}
        
        first_result = data["results"][0]
        return {
            "malicious": first_result.get("tags", []),
            "task": first_result.get("task", {}),
            "page": first_result.get("page", {})
        }
    except Exception as e:
        return {"error": str(e)}

def enrich_browser_history(input_path, output_path):
    with open(input_path, "r") as f:
        urls = json.load(f)

    enriched = []
    seen_domains = {}

    for entry in urls:
        url = entry.get("url")
        domain = extract_domain(url)

        if domain in seen_domains:
            result = seen_domains[domain]
        else:
            result = enrich_urlscan(domain)
            seen_domains[domain] = result
            time.sleep(1)  # Respect rate-limits

        entry["domain"] = domain
        entry["urlscan"] = result
        enriched.append(entry)

    with open(output_path, "w") as f:
        json.dump(enriched, f, indent=4)

    print(f"[✔] Enriched data written to {output_path}")
