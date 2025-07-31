# agent/email_analysis.py

import openai

# Ortak GPT çağrısı fonksiyonu
def call_gpt(prompt: str, max_tokens: int = 200) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen bir e-posta asistanısın."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content'].strip()

# 1. Özet
def summarize_email(content: str) -> str:
    prompt = f"""Aşağıdaki e-posta içeriğini kısa ve sade şekilde özetle:

\"\"\"{content}\"\"\"

Özet:
"""
    return call_gpt(prompt, max_tokens=200)

# 2. Etiketleme
def classify_email_topic(content: str) -> str:
    prompt = f"""Aşağıdaki e-posta içeriğini şu kategorilerden biriyle etiketle:
- Fatura
- Toplantı
- Destek Talebi
- Şikayet
- İş Başvurusu
- Diğer

Yalnızca kategori adını döndür.
\"\"\"{content}\"\"\"
"""
    return call_gpt(prompt)

# 3. Cevap taslağı
def generate_reply(content: str) -> str:
    prompt = f"""Aşağıdaki e-postaya uygun, resmi ve nazik bir cevap taslağı hazırla.

\"\"\"{content}\"\"\"

Cevap taslağı:
"""
    return call_gpt(prompt, max_tokens=300)

# 4. Eylem önerisi
def suggest_action(content: str) -> str:
    prompt = f"""Aşağıdaki e-postaya göre kullanıcıya tek cümlelik kısa bir eylem öner:
\"\"\"{content}\"\"\"

Önerilen Eylem:
"""
    return call_gpt(prompt)

# 5. Öncelik skoru
def get_priority_score(content: str) -> int:
    prompt = f"""Aşağıdaki e-postanın aciliyet derecesini 0 ile 100 arasında bir tam sayı olarak belirt:
\"\"\"{content}\"\"\"

Sadece sayı ver:
"""
    result = call_gpt(prompt)
    try:
        return int(result)
    except:
        return 0

# 6. Tarih/Saat çıkarımı
def extract_datetime(content: str) -> str:
    prompt = f"""E-postada belirtilen toplantı veya randevu varsa, tarih ve saatini belirt. Eğer yoksa 'Belirtilmemiş' yaz.
\"\"\"{content}\"\"\"

Tespit edilen Tarih/Saat:
"""
    return call_gpt(prompt)
