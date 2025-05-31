# PayPy

**PayPy** — test loyihalarda sun'iy (simulyatsiya qilingan) to‘lov tizimidan foydalanish uchun bepul API xizmati.

---

## 🔧 Texnologiyalar

- **Python**
- **Django, drf**
- **HTML / CSS / SCSS**
- **Bootstrap**
- **JavaScript**
- **SQLite**


---

## 🚀 Maqsad

 Loyihalar qilishni endi boshlagan yangi dasturchilar ( Backendchilar ham Frontendchilar ham ) odatda Online Market loyihasini qilib ko'rishadi. 
 Ko'p hollarda bu loyihalarning o'z to'lov tizimi bo'lmaydi. Ya'ni online marketdagi mahsulotlarni tanlab sotib olishda to'lov tizimi ishlamaydi.
 Bu muammoga yechim berish maqsadida shu loyihani ishlab chiqdim.

---



## 📄 Foydalanish qo'llanmasi
🕒 Eslatma: Hozirda loyiha serverga joylanmagan.

 Loyihaning saytida ( hozircha serverga joylanman ) ro'yhatdan o'ting. Saytdagi Token bo'limida loyihangiz uchun token yaratib oling.
 Saytdagi Card bo'limida esa lohiyangizning to'lov qismida foydalanish uchun Kartalar yaratib olishingiz mumkin.
 Token va Kartalardan foydalanish uchun hozirda mavjud API to'plami:
 
- `GET /api/<token>/card/detail/<karta-raqami>/`  
  Kartaga oid ma'lumotlarni ko‘rish.

- `GET /api/<token>/card/free-money/<karta-raqami>/`  
  Karta balansiga test uchun 1 000 000 so‘m qo‘shadi.

- `POST /api/<token>/card/transaction/`  
  Bir kartadan boshqasiga pul o‘tkazish. 
  Body:
    - `from_card`: yuboruvchi karta raqami
    - `to_card`: qabul qiluvchi karta raqami
    - `amount`: yuboriladigan summa



> ⚠️ Diqqat: Ushbu API xizmatidagi karta raqamlari va pul mablag‘lari faqat test maqsadida yaratilgan bo‘lib, ular real to‘lov tizimlarida ishlamaydi.

 
## 🤝 Hissa qo‘shish

Agar siz ushbu loyihaga o‘z hissangizni qo‘shmoqchi bo‘lsangiz, pull request yuborishingiz mumkin. Taklif va savollar uchun [GitHub profilim](https://github.com/Inniyabdulloh) orqali bog‘lanishingiz mumkin.

