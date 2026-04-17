import os
import json
from pyexpat.errors import messages
from openai import OpenAI
from dotenv import load_dotenv
from tools import browse_website, save_to_file
from tool_schemas import TOOL_SCHEMAS

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """You are an EPL (English Premier League) research agent.

ONLY browse these verified URLs — do not guess or construct others:
- Standings  : https://www.bbc.com/sport/football/premier-league/table
- Top Scorers: https://www.bbc.com/sport/football/premier-league/top-scorers
- News       : https://www.bbc.com/sport/football/premier-league

Workflow (follow strictly):
1. Browse the standings URL
2. Browse the top scorers URL
3. Browse the news URL for recent results
4. Compile a clean, structured summary with headings
5. Call save_to_file ONCE at the end — never before step 4
"""

# Map tool names to actual Python functions
TOOL_MAP = {
    "browse_website": browse_website,
    "save_to_file": save_to_file
}

def run_agent(user_goal : str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_goal}
    ]

    print(f"\nAgent Started. Goal: {user_goal}\n{'='*60}")

    # Agent Loop
    while True:
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile", # "openai/gpt-oss-20b",
            messages = messages,
            tools= TOOL_SCHEMAS,
            tool_choice= "auto",
            max_tokens= 2000
        )

        message = response.choices[0].message
        messages.append(message)

        # --- If Groq wants to call a tool ---
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                print(f"\n🔧 Tool Called: {tool_name}")
                print(f"   Args: {tool_args}")

                # Execute the actual Python function
                result = TOOL_MAP[tool_name](**tool_args)
                print(f"   Result preview: {str(result)[:200]}...")

                # Feed the result back to Groq
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        # --- If Groq gives a final text response (no more tools needed) ---
        else:
            print(f"\n✅ Agent finished!\n")
            print(f"💬 Agent says: {message.content}")
            break

    return message.content

if __name__ == "__main__":
    run_agent(
        "Research the English Premier League. Get current standings, "
        "recent match results, and top scorers. Save a full report to epl_report.txt"
    )