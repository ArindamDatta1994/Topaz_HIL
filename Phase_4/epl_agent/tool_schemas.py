TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "browse_website",
            "description": "Browse a URL and return its text content. Use this to fetch EPL news, standings, or scores.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The full URL to browse (e.g., https://www.premierleague.com)"
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_to_file",
            "description": "Save the final extracted EPL information to a text file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The formatted EPL information to save."
                    },
                    "filename": {
                        "type": "string",
                        "description": "The filename to save to (default: epl_report.txt)"
                    }
                },
                "required": ["content"]
            }
        }
    }
]