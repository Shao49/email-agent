# agent/email_processor.py

import openai
import os
from dotenv import load_dotenv
from .prompt_builder import build_email_prompt
from .email_analysis import (
    summarize_email,
    classify_email_topic,
    generate_reply,
    suggest_action,
    get_priority_score,
    extract_datetime
)

# .env dosyasını yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_email_with_gpt(email_text: str) -> dict:
    """
    E-posta metnini GPT API ile işler ve analiz sonuçlarını döndürür.

    :param email_text: Kullanıcıdan alınan e-posta içeriği
    :return: Tüm analizlerin bulunduğu sözlük
    """
    try:
        result = {
            "summary": summarize_email(email_text),
            "topic": classify_email_topic(email_text),
            "reply_draft": generate_reply(email_text),
            "suggested_action": suggest_action(email_text),
            "priority_score": get_priority_score(email_text),
            "datetime_info": extract_datetime(email_text)
        }
        return result
    except Exception as e:
        return {"error": str(e)}
