import requests
from bs4 import BeautifulSoup
from datetime import datetime

def browse_website(url : str) -> str:
    """Fetch raw text content from url"""
    headers = {"User-Agent" : "Mozila/5.0"}

    try:
        response = requests.get(url, headers = headers, timeout= 10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # removes scripts/styles for clean text
        for tag in soup(["script", "style", "nav", "floater"]):
            tag.decompose()
        return soup.get_text(separator = "\n", strip = True)[:2000]
    
    except Exception as e:
        return f"Error could not fetch {url}. Reason: {e}"
    
def save_to_file(content: str, filename: str ="epl_report.txt") -> str:
    """Save extracted content to a .txt file"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_content = f"EPL Agent Report\nGenerated: {timestamp}\n{"=" * 50}\n\n{content}"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(full_content)
    
    return f"SUCCESS: Report saved to {filename}"