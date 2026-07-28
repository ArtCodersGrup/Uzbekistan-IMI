import io

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
      <p class="section-desc">O'quvchilarimizga bilim va tarbiya beruvchi fidoiy ustozlarimiz. (Batafsil ma'lumot uchun ustoz profiliga bosing)</p>
    </div>
    
    <div class="leader-list">
      <!-- Oqituvchi 1 -->
      <a href="teacher-detail.html" class="teacher-card-link" style="display:block; text-decoration:none; color:inherit; transition:transform 0.2s; border-radius: 16px; padding: 16px; cursor: pointer;">
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
      </a>
      <div class="leader-divider"></div>

      <!-- Oqituvchi 2 -->
      <a href="teacher-detail.html" class="teacher-card-link" style="display:block; text-decoration:none; color:inherit; transition:transform 0.2s; border-radius: 16px; padding: 16px; cursor: pointer;">
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
      </a>
    </div>
  </div>
</section>
<style>
.teacher-card-link:hover {
  background: var(--bg);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(27,58,107,0.05);
}
</style>
"""
with open('teachers.html', 'w', encoding='utf-8') as f:
    f.write(header + teachers_content + footer)

teacher_detail = """
<section id="teacher-detail" class="section" style="min-height: 70vh; padding-top: 120px;">
  <div class="section-inner" style="max-width: 900px; margin: 0 auto;">
    <a href="teachers.html" style="display: inline-block; margin-bottom: 24px; color: var(--text-muted); font-weight: 500;">&larr; Barcha o'qituvcilarga qaytish</a>
    
    <div style="display: flex; gap: 40px; margin-bottom: 48px; flex-wrap: wrap;">
      <!-- Rasm -->
      <div style="width: 280px; height: 320px; border-radius: 16px; overflow: hidden; flex-shrink: 0; box-shadow: 0 12px 24px rgba(0,0,0,0.06);">
        <img src="img/direktor.jpg" alt="Toshmatov Eshmat" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      
      <!-- Asosiy Info -->
      <div style="flex: 1; min-width: 300px;">
        <h1 style="font-size: 32px; color: var(--navy); font-family: 'Playfair Display', serif; margin-bottom: 8px;">Toshmatov Eshmat</h1>
        <div style="font-size: 16px; font-weight: 600; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 24px;">Matematika fani o'qituvchisi</div>
        
        <!-- Kontaktlar / Ijtimoiy -->
        <div style="display: flex; gap: 16px; margin-bottom: 24px;">
          <!-- Telefon (Conditionally displayed, demo data) -->
          <a href="tel:+998901234567" style="display: flex; align-items: center; gap: 8px; background: var(--bg); padding: 8px 16px; border-radius: 8px; color: var(--navy); font-weight: 600; text-decoration: none;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            +998 90 123 45 67
          </a>
          <!-- Telegram (Conditionally displayed, demo data) -->
          <a href="https://t.me/eshmatov" target="_blank" style="display: flex; align-items: center; gap: 8px; background: #E8F4F8; padding: 8px 16px; border-radius: 8px; color: #0088cc; font-weight: 600; text-decoration: none;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69.01-.03.01-.14-.07-.19-.08-.05-.19-.02-.27 0-.11.03-1.84 1.18-5.22 3.47-.49.34-.94.5-1.35.49-.45-.01-1.32-.26-1.96-.47-.79-.26-1.42-.4-1.36-.84.03-.23.34-.48.91-.74 3.56-1.55 5.94-2.58 7.14-3.08 3.39-1.41 4.1-1.65 4.56-1.66.1 0 .32.02.46.12.11.08.14.19.16.27.02.05.02.18.01.27z"/></svg>
            @eshmatov
          </a>
        </div>
        
        <!-- Bio -->
        <h3 style="font-size: 18px; color: var(--navy); margin-bottom: 12px;">O'qituvchi haqida (Bio)</h3>
        <p style="color: var(--text-dark); line-height: 1.8; font-size: 16px; margin-bottom: 16px;">
          Ushbu o'qituvchi uzoq yillar davomida xalq ta'limi sohasida mehnat qilib keladi. Oliy toifali mutaxassis bo'lib, hozirgacha 100 dan ortiq Respublika va xalqaro olimpiada g'oliblarini yetishtirib chiqargan. O'quvchilarda nafaqat matematik fikrlash, balki muammolarni tizimli hal etish ko'nikmalarini shakllantiradi. Maktab-internatimizda 2023-yildan buyon faoliyat olib bormoqda.
        </p>
      </div>
    </div>
    
    <!-- Sertifikatlar Bloki -->
    <div style="border-top: 1px solid var(--border); padding-top: 40px;">
      <h3 style="font-size: 24px; color: var(--navy); font-family: 'Playfair Display', serif; margin-bottom: 24px;">Sertifikatlar va Yutuqlar</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 24px;">
        <!-- Sertifikat 1 -->
        <div style="border: 1px solid var(--border); border-radius: 12px; padding: 12px; background: var(--white); text-align: center;">
          <div style="width: 100%; height: 180px; background: var(--bg); border-radius: 8px; margin-bottom: 12px; display: flex; align-items:center; justify-content:center;">
             <span style="color:var(--text-muted); font-size:14px;">Sertifikat Rasmi (Namuna)</span>
          </div>
          <span style="font-weight: 600; font-size: 14px; color: var(--navy);">Xalq Ta'limi a'lochisi</span>
        </div>
        
        <!-- Sertifikat 2 -->
        <div style="border: 1px solid var(--border); border-radius: 12px; padding: 12px; background: var(--white); text-align: center;">
           <div style="width: 100%; height: 180px; background: var(--bg); border-radius: 8px; margin-bottom: 12px; display: flex; align-items:center; justify-content:center;">
             <span style="color:var(--text-muted); font-size:14px;">Sertifikat Rasmi (Namuna)</span>
          </div>
          <span style="font-weight: 600; font-size: 14px; color: var(--navy);">Xalqaro TOFEL Level</span>
        </div>
      </div>
    </div>

  </div>
</section>
"""
with open('teacher-detail.html', 'w', encoding='utf-8') as f:
    f.write(header + teacher_detail + footer)
