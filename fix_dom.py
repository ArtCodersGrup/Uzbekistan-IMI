import re

# FIX sorovnomalar.html
with open('sorovnomalar.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire yangiliklar section
target = r'<section id="yangiliklar".*?</section>'
replacement = """<section id="surveys" class="section" style="min-height: 70vh; padding-top: 120px;">
    <div class="section-inner">
      <div class="section-head">
        <span class="section-label">Fikr bildiring</span>
        <h2 class="section-title">So'rovnomalar</h2>
        <p class="section-desc">Maktabimiz hayoti bo'yicha ochiq so'rovnomalarda qatnashing.</p>
      </div>
      <div id="surveysGrid"
        style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px;">
        <div style="padding: 40px; color: var(--text-muted); grid-column: 1 / -1; text-align: center;">Yuklanmoqda...
        </div>
      </div>
    </div>
  </section>"""
text = re.sub(target, replacement, text, flags=re.DOTALL)
with open('sorovnomalar.html', 'w', encoding='utf-8') as f:
    f.write(text)

# FIX sorovnoma.html
with open('sorovnoma.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

replacement2 = """<section id="survey-detail" class="section" style="min-height: 70vh; padding-top: 120px;">
    <div class="section-inner" id="surveyContainer" style="max-width: 800px; margin: 0 auto; background: var(--white); padding: 40px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid var(--border);">
       <div style="text-align:center; padding: 40px; color:var(--text-muted);">Yuklanmoqda...</div>
    </div>
  </section>"""
text2 = re.sub(target, replacement2, text2, flags=re.DOTALL)
with open('sorovnoma.html', 'w', encoding='utf-8') as f:
    f.write(text2)

print("HTML DOM fixed")
