import imaplib
import os
from dotenv import load_dotenv
import email

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)

mail.select("inbox")

print("Connected Successfully!")

status, message = mail.search(None, "UNSEEN")

email_ids = message[0].split()

print(f"Unread emails: {len(email_ids)}")

# for e_ids in email_ids:
#     status, msg_data = mail.fetch(e_ids, "(RFC822)")

#     raw_email = msg_data[0][1]
#     msg = email.message_from_bytes(raw_email)

#     print("Subject:", msg["subject"])

download_folder = "attachments"
os.makedirs(download_folder, exist_ok=True)

for e_ids in email_ids:
    status, msg_data = mail.fetch(e_ids, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            file_name = part.get_filename()

            if file_name:
                file_path = os.path.join(download_folder, file_name)

                with open(file_path, "wb") as f:
                    f.write(part.get_payload(decode=True))

                print(f"Downloaded: {file_name}")