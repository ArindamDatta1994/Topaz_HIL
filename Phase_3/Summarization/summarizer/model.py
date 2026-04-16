# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text, max_len = 150, min_len = 50):
#     result = summarizer(
#         text,
#         max_length= max_len,
#         min_length= min_len,
#         do_sample=False
#     )

#     return result[0]['summary_text']

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(**inputs, max_length=150, min_length=50)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)