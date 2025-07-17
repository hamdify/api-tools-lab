import openai
import os
from dotenv import load_dotenv

# API anahtarını yükleme
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI istemcisini oluşturma
client = openai.OpenAI(api_key=api_key)

# Kullanıcıdan bilgi alma
isim = input("Adınız: ")
meslek = input("Mesleğiniz: ")
hedef = input("Bu hafta başarmak istediğiniz şey nedir? ")
bos_vakit = input("Günde kaç saat boş vaktiniz var? ")

# Prompt oluşturma
prompt = f"""
Sen bir kişisel asistan AI’sın. Kullanıcının adı {isim}.
Mesleği: {meslek}.
Bu haftaki hedefi: {hedef}.
Günlük boş vakti: {bos_vakit} saat.

Bu kullanıcı için 7 günlük detaylı bir çalışma planı oluştur. Her güne özel öneri ver, kısa motivasyon cümlesi ekle. 
Yalnızca madde madde, açık ve sade yaz.
"""

# ChatGPT'ye isteği gönderme
try:
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen yapıcı ve disiplinli bir AI planlayıcısın."},
            {"role": "user", "content": prompt}
        ]
    )

    plan = chat_completion.choices[0].message.content
    print("\n📅 Haftalık Planın:\n")
    print(plan)

    # Dosyaya kaydetme
    with open("haftalik_plan.txt", "w", encoding="utf-8") as f:
        f.write(plan)
    print("\n✅ Plan başarıyla 'haftalik_plan.txt' dosyasına kaydedildi.")

except Exception as e:
    print("❌ Hata oluştu:", e)