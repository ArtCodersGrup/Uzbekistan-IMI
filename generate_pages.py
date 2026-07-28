import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

header_end = content.find('<section id="hero">')
footer_start = content.find('<footer>')

header = content[:header_end]
footer = content[footer_start:]

teachers_content = """
<section id="oqituvchilar" class="section" style="min-height: 70vh; padding-top: 120px;">
  <div class="section-inner">
    <div class="section-head">
      <span class="section-label">Bizning faxrimiz</span>
      <h2 class="section-title">Maktab O'qituvchilari</h2>
      <p class="section-desc">O'quvchilarimizga bilim va tarbiya beruvchi fidoiy ustozlarimiz</p>
    </div>
    <div class="leader-list">
      <div class="leader-row">
        <div class="leader-photo"><img src="img/direktor.jpg" alt="Toshmatov Eshmat" style="object-fit:cover; width:100%; height:100%;"></div>
        <div class="leader-info">
          <div>
            <div class="leader-name">Toshmatov Eshmat</div>
            <div class="leader-role" style="margin-top:6px">Matematika fani o'qituvchisi</div>
          </div>
          <p class="leader-desc">Oliy toifali o'qituvchi, 15 yillik ish tajribasi. Ko'plab olimpiada g'oliblari ustozi.</p>
        </div>
      </div>
      <div class="leader-divider"></div>
      <div class="leader-row reverse">
        <div class="leader-photo"><img src="img/maslahatchi.jpg" alt="Eshmatova Toshmatxon" style="object-fit:cover; width:100%; height:100%;"></div>
        <div class="leader-info">
          <div>
            <div class="leader-name">Eshmatova Toshmatxon</div>
            <div class="leader-role" style="margin-top:6px">Informatika fani o'qituvchisi</div>
          </div>
          <p class="leader-desc">Zamonaviy texnologiyalar va dasturlash tillari bo'yicha mutaxassis.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
with open('teachers.html', 'w', encoding='utf-8') as f:
    f.write(header + teachers_content + footer)

news_content = """
<section id="yangiliklar" class="section" style="min-height: 70vh; padding-top: 120px;">
  <div class="section-inner">
    <div class="section-head">
      <span class="section-label">So'nggi voqealar</span>
      <h2 class="section-title">Yangiliklar</h2>
      <p class="section-desc">Maktabimiz hayotidagi eng muhim xabarlar va tadbirlar</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px;">
      <a href="news-detail.html" style="display:block; border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: #fff;">
        <img src="img/hero-1.jpg" alt="Yangilik" style="width:100%; height: 200px; object-fit: cover;">
        <div style="padding: 20px;">
          <h3 style="font-size: 18px; color: var(--navy); margin-bottom: 8px;">Maktabimizda Navro'z sayli o'tkazildi</h3>
          <p style="font-size: 14px; color: var(--text-muted);">Barcha o'quvchilar ishtirokida katta bayram bo'lib o'tdi...</p>
        </div>
      </a>
      <a href="news-detail.html" style="display:block; border: 1px solid var(--border); border-radius: 12px; overflow: hidden; background: #fff;">
        <img src="img/hero-2.jpg" alt="Yangilik" style="width:100%; height: 200px; object-fit: cover;">
        <div style="padding: 20px;">
          <h3 style="font-size: 18px; color: var(--navy); margin-bottom: 8px;">Matematika bo'yicha ochiq darslar</h3>
          <p style="font-size: 14px; color: var(--text-muted);">Viloyat mutaxassislari tashrif buyurdi...</p>
        </div>
      </a>
    </div>
  </div>
</section>
"""
with open('news.html', 'w', encoding='utf-8') as f:
    f.write(header + news_content + footer)

news_detail = """
<section id="yangilik-detail" class="section" style="min-height: 70vh; padding-top: 120px;">
  <div class="section-inner" style="max-width: 800px; margin: 0 auto;">
    <h1 style="font-size: 32px; color: var(--navy); margin-bottom: 16px; font-family: 'Playfair Display', serif;">Maktabimizda Navro'z sayli o'tkazildi</h1>
    <p style="color: var(--text-muted); margin-bottom: 24px; font-size: 14px;">Chop etildi: 21 Mart, 2026</p>
    <img src="img/hero-1.jpg" alt="Navroz" style="width: 100%; border-radius: 12px; margin-bottom: 32px;">
    <div style="color: var(--text-dark); line-height: 1.8; font-size: 16px;">
      <p style="margin-bottom: 16px;">Kuni kecha maktab-internatimiz hovlisida bahor ayyomi — Navro'z umumxalq bayrami keng nishonlandi.</p>
      <p style="margin-bottom: 16px;">Bayram dasturida milliy kuy va qo'shiqlar, raqslar, sport musobaqalari o'rin oldi.</p>
      <a href="news.html" style="display: inline-block; margin-top: 24px; color: var(--gold); font-weight: 600;">&larr; Yangiliklarga qaytish</a>
    </div>
  </div>
</section>
"""
with open('news-detail.html', 'w', encoding='utf-8') as f:
    f.write(header + news_detail + footer)
