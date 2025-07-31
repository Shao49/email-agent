# E-Posta Özetleyici ve Cevaplayan Agent

Bu uygulama, kullanıcıdan aldığı e-posta metnini OpenAI GPT modeli ile analiz ederek:
- E-postanın genel konusunu tahmin eder,
- E-postayı 2-3 cümleyle özetler,
- E-postaya uygun, kısa ve kibar bir yanıt taslağı oluşturur.

## 🔧 Kurulum

1. Python 3.10+ kurulu olmalıdır.
2. Terminal üzerinden aşağıdaki adımları izleyin:

```bash
git clone [repo-url]  # opsiyonel
cd email-agent
python -m venv venv
venv\Scripts\activate      # (Windows)
# veya
source venv/bin/activate   # (Mac/Linux)
pip install -r requirements.txt
