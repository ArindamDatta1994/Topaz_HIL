import os

os.makedirs("rag_dataset/hr", exist_ok=True)
os.makedirs("rag_dataset/finance", exist_ok=True)
os.makedirs("rag_dataset/operations", exist_ok=True)
os.makedirs("rag_dataset/support", exist_ok=True)

# HR file
with open("rag_dataset/hr/policy.txt", "w") as f:
    f.write("""Employee Leave Policy
Employees are entitled to 20 paid leaves annually.
Work From Home allowed 3 days per week.""")

# Finance file
with open("rag_dataset/finance/invoice.txt", "w") as f:
    f.write("""Invoice ID: INV-001
Total: 142500 INR
Status: Pending""")

# Logs JSON
with open("rag_dataset/operations/logs.json", "w") as f:
    f.write("""[
{"level": "ERROR", "message": "DB failed"},
{"level": "INFO", "message": "Recovered"}
]""")

# Support tickets
with open("rag_dataset/support/tickets.txt", "w") as f:
    f.write("""Ticket: Login issue resolved
Ticket: Payment failure fixed""")

print("Dataset created!")