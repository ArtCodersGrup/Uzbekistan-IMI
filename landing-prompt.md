# PROMPT: Maktab-Internat Landing Sahifasi

## Loyiha haqida

O'zbekistondagi davlat maktab-internati uchun zamonaviy, formal/akademik uslubdagi **single-page landing** sahifa yarat. Sayt bitta `index.html` faylda bo'lsin (HTML + CSS + JS bitta faylda, framework ishlatilmasin). Til — faqat o'zbek tilida. Sayt to'liq **mobile-adaptive** (responsive) bo'lishi shart.

## Maktab ma'lumotlari

- **To'liq nomi:** Maktabgacha va maktab ta'lim vazirligi tasarrufidagi ixtisoslashtirilgan ta'lim muassasalari agentligi O'zbekiston tuman ixtisoslashtirilgan maktab-internati
- **Qisqa nomi (saytda ishlatiladi):** O'zbekiston tuman ixtisoslashtirilgan maktab-internati
- **Tashkil etilgan:** 2023-yil
- **Logo:** to'q ko'k (navy) fonda oq globus + kitob, sakkiz qirrali yulduz ichida (rasm beriladi)

## Dizayn talablari

- **Uslub:** formal, akademik, rasmiy davlat ta'lim muassasasiga mos. Zamonaviy va professional ko'rinish
- **Ranglar:** logo asosida — navy blue (#1B3A6B atrofida) asosiy rang, oq, gold/tilla (#C9A84C) accent sifatida, och kulrang fon (#F4F6F9)
- **Shriftlar:** sarlavhalar uchun serif (Playfair Display kabi), matn uchun zamonaviy sans-serif (Inter kabi)
- Kognitiv yuklama kam, minimalist, o'qish oson bo'lsin

## Sahifa tuzilishi (ketma-ketlik)

### 1. Header
- Sticky (yuqorida qotib turadi)
- Chapda: logo + maktab nomi
- O'ngda: menyu (bo'limlarga anchor linklar)
- Mobile'da hamburger menyu

### 2. Hero
- To'liq ekran balandligida
- Orqa fonda maktab binosining 3 ta katta rasmi avtomatik aylanib turadi (slider)
- Rasmlar ustida qoraytirilgan overlay — juda qorong'i emas, bino ko'rinib turadi, lekin oldidagi matn bemalol o'qiladi
- Ustida: maktab qisqa nomi (katta sarlavha) + qisqa slogan
- Hero ichida pastroqda: **"2023-yildan buyon o'z faoliyatini olib boradi"** yozuvi (maktab tarixi alohida bo'lim emas, shu yerda)
- Slider nuqtalari (dots) bilan boshqariladi

### 3. Statistika (animated counters)
- 300+ o'quvchilar soni
- 40+ o'qituvchilar soni
- 20+ tarbiyachilar soni
- 3 yillik faoliyat tajribasi
- Scroll qilib kelganda raqamlar 0 dan sanab chiqadi

### 4. Natijalarimiz (jadval)
Chiroyli styled jadval ko'rinishida:

| O'quv yili | Bitiruvchilar soni | Kirgan foiz | O'rtacha ball |
|-----------|-------------------|-------------|---------------|
| 2023–2024 | 60 | 100% | 175 ball |
| 2024–2025 | 58 | 100% | 181 ball |
| 2025–2026 | 93 | 100% | 183 ball |

Olimpiada natijalari KERAK EMAS.

### 5. Rahbariyat
**Alternating layout:** har bir rahbar ketma-ket joylashadi — birinchisida rasm chapda / matn o'ngda, keyingisida teskari (rasm o'ngda / matn chapda), va shunday almashinib boradi. Mobile'da rasm ustida, matn pastda.

Rahbarlar (rasmlari beriladi):
1. **Quziyeva Xafizaxon Abdullayevna** — Maktab-internat direktori
2. **Xalilov Dilshodbek Abduqahhor o'g'li** — Maktab-internat maslahatchisi
3. **Mirzayev Mirjalol Turg'unali o'g'li** — Ma'naviy-ma'rifiy ishlar bo'yicha direktor o'rinbosari
4. **Turonova Shahnozaxon** — O'quv ishlari bo'yicha direktor o'rinbosari

Har biriga qisqa tavsif matni (placeholder bo'lishi mumkin).

### 6. Fikrlar (testimonials)
- Horizontal scroll/carousel ko'rinishida kartalar
- Har kartada: fikr matni, ism, lavozim (masalan: "7-sinf o'quvchisining otasi", "Tuman hokimi")
- Oldinga/orqaga tugmalar bilan aylantiriladi
- 4-5 ta placeholder fikr

### 7. Biz bilan bog'lanish
- Telefon raqam (placeholder: +998 90 123-45-67)
- Telegram link (placeholder)
- Instagram link (placeholder)
- Manzil (placeholder)
- **Google Maps link** bo'lishi shart (xarita joylashuvi)
- Forma KERAK EMAS

### 8. FAQ
- Accordion ko'rinishida (bosganda ochiladi)
- 3-5 ta placeholder savol: qabul qanday, yotoqxona bormi, ta'lim yo'nalishlari, ota-onalar bilan aloqa, to'garaklar

### 9. Footer
- Logo + to'liq nom + qisqa ma'lumot
- Bo'limlar linklari
- Aloqa linklari
- Copyright

## KERAK EMAS bo'limlar
- Yangiliklar bo'limi — hozircha kerak emas
- Maktab tarixi alohida bo'lim — kerak emas (Hero ichida "2023-yildan" yozuvi yetarli)
- Bog'lanish formasi — kerak emas
- Olimpiada natijalari — kerak emas

## Texnik talablar

- Bitta `index.html` fayl — vanilla HTML/CSS/JS, framework yo'q
- Google Fonts CDN dan
- Rasmlar: berilgan rasmlarni ishlatish (yoki base64 embed)
- Smooth scroll, anchor navigatsiya (sticky header balandligini hisobga olib)
- Hero slider avtomatik (4-5 soniya) + qo'lda boshqarish
- FAQ accordion, testimonial carousel, animated counters — hammasi vanilla JS da
- Mobile breakpoints: 768px va 480px

## Kelajak rejasi (hozir qilinmaydi, arxitekturada hisobga olinadi)
- Keyinchalik admin panel / o'qituvchilar bo'limi qo'shilishi mumkin
- Natijalar ichiga kirib, eng faol o'quvchilarni ko'rish funksiyasi qo'shilishi mumkin
- Shuning uchun bo'limlar modular qilib yozilsin
