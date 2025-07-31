# agent/prompt_builder.py

def build_email_prompt(email_text: str) -> str:
    """
    GPT modeline gönderilecek prompt'u oluşturur.

    :param email_text: E-posta metni
    :return: Prompt formatında metin
    """
    prompt = f"""
Aşağıdaki e-posta mesajı için lütfen şu görevleri sırayla yerine getir:
1. E-postanın genel konusunu tahmin et (örneğin: iş, kişisel, fatura, etkinlik).
2. E-posta içeriğini 2-3 cümleyle özetle.
3. E-postaya uygun, kibar ve kısa bir yanıt taslağı oluştur.

E-posta içeriği:
\"\"\"
{email_text}
\"\"\"
"""
    return prompt
