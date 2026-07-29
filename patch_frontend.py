import re
import os

# -------- sorovnomalar.html --------
with open('sorovnomalar.html', 'r', encoding='utf-8') as f:
    s_list = f.read()

# Replace <title>
s_list = re.sub(r'<title>.*?</title>', '<title>So\'rovnomalar - Maktab-Internati</title>', s_list, count=1)

# Highlight active nav block, maybe replace the Hero text
hero_h1 = r'<h1 style="font-size: 56px; color: var\(--white\); font-family: \'Playfair Display\', serif; font-weight: 700; margin-bottom: 24px; line-height: 1.1;">.*?</h1>'
s_list = re.sub(hero_h1, '<h1 style="font-size: 56px; color: var(--white); font-family: \'Playfair Display\', serif; font-weight: 700; margin-bottom: 24px; line-height: 1.1;">Maktab so\'rovnomalari</h1>', s_list)

hero_p = r'<p style="font-size: 20px; color: rgba\(255, 255, 255, 0.9\);.*?</p>'
s_list = re.sub(hero_p, '<p style="font-size: 20px; color: rgba(255, 255, 255, 0.9); margin-bottom: 32px; max-width: 600px;">Maktabimiz hayoti bo\'yicha ochiq so\'rovnomalarda qatnashing.</p>', s_list)

main_container_regex = re.compile(r'<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(350px, 1fr\)\); gap: 32px;" id="newsGrid">.*?</div>\n    </div>', re.DOTALL)

replacement_list = """<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 32px;" id="surveysGrid">
        <div style="text-align:center; padding: 40px; color: var(--text-muted); width: 100%;">Yuklanmoqda...</div>
      </div>
    </div>"""
s_list = main_container_regex.sub(replacement_list, s_list)

# JS for loading list
js_regex = re.compile(r'async function loadNewsFront\(\).*?loadNewsFront\(\);', re.DOTALL)
js_replacement = """async function loadSurveysFront() {
      if (!window.supabaseClient) return;
      const { data, error } = await supabaseClient.from('surveys').select('*').order('created_at', { ascending: false });
      const grid = document.getElementById('surveysGrid');
      
      if (error || !data || data.length === 0) {
        grid.innerHTML = '<div style="text-align:center; padding: 40px; width: 100%;">Hozircha so\\'rovnomalar yo\\'q.</div>';
        return;
      }

      grid.innerHTML = '';
      data.forEach(item => {
          const statusHtml = item.is_open 
            ? '<span style="color: green; font-weight: bold; font-size: 14px;">Qabul ochiq</span>' 
            : '<span style="color: red; font-size: 14px;">Yakunlangan (Natija)</span>';
            
          grid.innerHTML += `
            <div style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid var(--border); display: flex; flex-direction: column;">
              <div style="padding: 24px; flex: 1; display:flex; flex-direction:column;">
                <div style="display:flex; justify-content:space-between; margin-bottom: 12px;">
                  <span style="font-size: 14px; font-weight: 600; color: var(--gold); text-transform: uppercase;">FIKR BIZ UCHUN MUHIM</span>
                  ${statusHtml}
                </div>
                <h3 style="font-size: 22px; color: var(--navy); font-family: 'Playfair Display', serif; margin-bottom: 16px; line-height: 1.4;">${item.title}</h3>
                <p style="color: var(--text-dark); line-height: 1.6; margin-bottom: 24px; flex: 1;">${item.description || ''}</p>
                <div style="display: flex; align-items: center; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 20px;">
                  <span style="font-size: 14px; color: var(--text-muted);">${new Date(item.created_at).toLocaleDateString()}</span>
                  <a href="sorovnoma.html?id=${item.id}" style="color: var(--navy); font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 8px;">
                    ${item.is_open ? 'Qatnashish' : 'Natijani ko\\'rish'} &rarr;
                  </a>
                </div>
              </div>
            </div>
          `;
      });
    }
    loadSurveysFront();"""
s_list = js_regex.sub(js_replacement, s_list)
with open('sorovnomalar.html', 'w', encoding='utf-8') as f:
    f.write(s_list)


# -------- sorovnoma.html --------
with open('sorovnoma.html', 'r', encoding='utf-8') as f:
    s_det = f.read()

s_det = re.sub(r'<title>.*?</title>', '<title>So\'rovnoma - Maktab-Internati</title>', s_det, count=1)
s_det = re.sub(hero_h1, '<h1 style="font-size: 56px; color: var(--white); font-family: \'Playfair Display\', serif; font-weight: 700; margin-bottom: 24px; line-height: 1.1;">So\'rovnoma</h1>', s_det)
s_det = re.sub(hero_p, '<p style="font-size: 20px; color: rgba(255, 255, 255, 0.9); margin-bottom: 32px; max-width: 600px;">Ishtirokingiz maktabimiz rivojiga o\'zbek hissasini qo\'shadi.</p>', s_det)

s_det_container_regex = re.compile(r'<div style="display: grid; grid-template-columns: repeat\(auto-fill, minmax\(350px, 1fr\)\); gap: 32px;" id="newsGrid">.*?</div>\n    </div>', re.DOTALL)
replacement_det = """<div id="surveyContainer" style="max-width: 800px; margin: 0 auto; background: var(--white); padding: 40px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid var(--border);">
       <div style="text-align:center; padding: 40px; color:var(--text-muted);">Yuklanmoqda...</div>
    </div>
    </div>"""
s_det = s_det_container_regex.sub(replacement_det, s_det)

js_det_replacement = """async function loadSurvey() {
        const params = new URLSearchParams(window.location.search);
        const id = params.get('id');
        const container = document.getElementById('surveyContainer');
        if (!id || !window.supabaseClient) {
            container.innerHTML = '<div style="text-align:center;">So\\'rovnoma topilmadi</div>';
            return;
        }

        const { data: survey, error } = await supabaseClient.from('surveys').select('*, survey_questions(*, survey_options(*))').eq('id', id).single();
        if (error || !survey) {
            container.innerHTML = '<div style="text-align:center;">So\\'rovnoma topilmadi</div>';
            return;
        }

        const qs = (survey.survey_questions || []).sort((a,b) => a.order_num - b.order_num);

        if (!survey.is_open) {
            // SHOW STATS
            const { data: responses } = await supabaseClient.from('survey_responses').select('*, survey_answers(*)').eq('survey_id', id);
            
            let html = `
                <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: var(--navy); margin-bottom: 24px;">${survey.title} (Yakunlangan)</h2>
                <div style="margin-bottom:32px;">Umumiy javoblar: <strong>${responses ? responses.length : 0}</strong></div>
            `;
            
            if(!responses || responses.length === 0) {
                html += `<div>Hech kim qatnashmagan.</div>`;
            } else {
                qs.forEach(q => {
                    html += `<div style="margin-bottom: 32px;">`;
                    html += `<h4 style="font-size: 18px; margin-bottom: 16px;">${q.question_text}</h4>`;
                    const qAnswers = [];
                    responses.forEach(r => {
                        if(r.survey_answers) {
                            r.survey_answers.forEach(a => { if (a.question_id === q.id) qAnswers.push(a); });
                        }
                    });

                    if (q.question_type === 'choice') {
                        const counts = {};
                        let answeredCount = 0;
                        q.survey_options.forEach(opt => counts[opt.id] = {text: opt.option_text, count: 0});
                        qAnswers.forEach(a => { if (a.option_id && counts[a.option_id]) { counts[a.option_id].count++; answeredCount++; } });

                        for (const key in counts) {
                            const opt = counts[key];
                            const pct = answeredCount > 0 ? ((opt.count / answeredCount) * 100).toFixed(1) : 0;
                            html += `
                                <div style="margin-bottom: 12px; font-size: 15px;">
                                    <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                                        <span>${opt.text}</span>
                                        <strong>${pct}% (${opt.count})</strong>
                                    </div>
                                    <div style="width:100%; height:10px; background:var(--border); border-radius:5px;">
                                        <div style="width:${pct}%; height:100%; background:var(--gold); border-radius:5px;"></div>
                                    </div>
                                </div>
                            `;
                        }
                    } else {
                        html += `<ul style="list-style:disc inside; padding:0; margin:0; font-size: 15px;">`;
                        qAnswers.forEach(a => {
                            if (a.answer_text && a.answer_text.trim()) {
                                html += `<li style="padding: 6px 0; border-bottom: 1px solid var(--border);">${a.answer_text}</li>`;
                            }
                        });
                        html += `</ul>`;
                    }
                    html += `</div>`;
                });
            }
            container.innerHTML = html;
        } else {
            // SHOW THE FORM
            let html = `
                <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: var(--navy); margin-bottom: 16px;">${survey.title}</h2>
                <p style="margin-bottom: 32px; font-size: 16px; color: var(--text-dark);">${survey.description}</p>
                <form id="publicSurveyForm">
            `;

            if (survey.is_anonymous_allowed) {
                html += `
                    <div style="margin-bottom: 24px;">
                        <label style="display:block; font-weight:600; margin-bottom:8px;">Ism familiyangiz (Ixtiyoriy, aniq yozishingiz yoki anonim qolishingiz mumkin)</label>
                        <input type="text" id="respName" style="width:100%; padding:12px; border:1px solid var(--border); border-radius:8px;" placeholder="Anonim">
                    </div>
                `;
            } else {
                html += `
                    <div style="margin-bottom: 24px;">
                        <label style="display:block; font-weight:600; margin-bottom:8px;">Ism familiyangiz</label>
                        <input type="text" id="respName" style="width:100%; padding:12px; border:1px solid var(--border); border-radius:8px;" placeholder="To'liq yozing" required>
                    </div>
                `;
            }

            qs.forEach(q => {
                html += `<div style="margin-bottom: 32px; background: #fafafa; padding: 24px; border-radius: 12px; border: 1px solid var(--border);" class="q-block" data-qid="${q.id}" data-type="${q.question_type}">`;
                html += `<label style="display:block; font-weight:600; margin-bottom:12px; font-size: 18px;">${q.question_text}</label>`;
                
                if (q.question_type === 'choice') {
                    q.survey_options.forEach(opt => {
                        html += `
                            <label style="display:flex; align-items:center; gap: 12px; margin-bottom: 12px; cursor:pointer; font-size: 16px;">
                                <input type="radio" name="q_${q.id}" value="${opt.id}" required style="width:18px; height:18px;">
                                ${opt.option_text}
                            </label>
                        `;
                    });
                } else {
                    html += `
                        <textarea style="width:100%; padding:12px; border:1px solid var(--border); border-radius:8px; display:block;" rows="3" required placeholder="Javobingiz..."></textarea>
                    `;
                }
                html += `</div>`;
            });

            html += `
                <button type="submit" id="sSubmit" style="background:var(--navy); color:var(--white); padding:16px 32px; border:none; border-radius:8px; font-size:16px; font-weight:600; cursor:pointer;" onmouseover="this.style.background='var(--navy-dark)'" onmouseout="this.style.background='var(--navy)'">Yuborish</button>
                </form>
            `;
            
            container.innerHTML = html;

            document.getElementById('publicSurveyForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const sBtn = document.getElementById('sSubmit');
                sBtn.disabled = true;
                sBtn.innerText = "Yuborilmoqda...";

                const nameInput = document.getElementById('respName');
                const fullName = nameInput ? nameInput.value : 'Anonim';

                const { data: rData, error: rErr } = await supabaseClient.from('survey_responses')
                    .insert([{ survey_id: id, responder_name: fullName }]).select();
                
                if(rErr) { alert(rErr.message); return; }
                const respId = rData[0].id;

                const qBlocks = document.querySelectorAll('.q-block');
                const answersPayload = [];
                for (const b of qBlocks) {
                    const qId = b.getAttribute('data-qid');
                    const qType = b.getAttribute('data-type');
                    
                    if (qType === 'choice') {
                        const opt = b.querySelector('input[type="radio"]:checked');
                        if (opt) answersPayload.push({ response_id: respId, question_id: qId, option_id: opt.value });
                    } else {
                        const txt = b.querySelector('textarea').value;
                        answersPayload.push({ response_id: respId, question_id: qId, answer_text: txt });
                    }
                }

                if (answersPayload.length > 0) {
                    await supabaseClient.from('survey_answers').insert(answersPayload);
                }

                container.innerHTML = `
                    <div style="text-align:center; padding: 60px 20px;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="green" stroke-width="2" style="margin-bottom:24px;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        <h2 style="font-family: 'Playfair Display', serif; font-size: 32px; color: var(--navy); margin-bottom:16px;">Natija qabul qilindi</h2>
                        <p style="font-size: 18px; color: var(--text-muted); margin-bottom:32px;">So'rovdan o'tganingiz uchun rahmat!</p>
                        <a href="sorovnomalar.html" style="background:var(--navy); color:var(--white); padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:600;">Boshqa so'rovnomalar</a>
                    </div>
                `;
            });
        }
    }
    window.addEventListener('DOMContentLoaded', loadSurvey);"""
s_det = js_regex.sub(js_det_replacement, s_det)

with open('sorovnoma.html', 'w', encoding='utf-8') as f:
    f.write(s_det)

print("Patching frontend completed.")
