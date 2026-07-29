let qCount = 0;

function addSurveyQuestion(qId = '', qText = '', qType = 'text', options = []) {
    qCount++;
    const id = qCount;
    const box = document.createElement('div');
    box.className = 'q-row';
    box.style.border = '1px solid var(--border)';
    box.style.padding = '12px';
    box.style.borderRadius = '8px';
    box.innerHTML = `
        <input type="hidden" class="q-id" value="${qId}">
        <div style="display:flex; gap:12px; margin-bottom:8px;">
            <input type="text" class="form-control q-text" style="flex:1;" placeholder="Savol matni" value="${qText}" required>
            <select class="form-control q-type" style="width:150px;" onchange="toggleOptions(this)">
                <option value="text" ${qType === 'text' ? 'selected' : ''}>Yozma javob</option>
                <option value="choice" ${qType === 'choice' ? 'selected' : ''}>Variantli</option>
            </select>
            <button type="button" class="btn-outline" style="color:red; border-color:red;" onclick="this.parentElement.parentElement.remove()">-</button>
        </div>
        <div class="q-options" style="display: ${qType === 'choice' ? 'block' : 'none'}; padding-left:16px;">
            <button type="button" class="btn-outline" style="font-size:12px; padding:4px 8px; margin-bottom:8px;" onclick="addOptionRow(this)">+ Variant qo'shish</button>
            <div class="options-container" style="display:flex; flex-direction:column; gap:4px;"></div>
        </div>
    `;

    document.getElementById('surveyQuestionsBox').appendChild(box);

    if (qType === 'choice' && options.length > 0) {
        const cont = box.querySelector('.options-container');
        options.forEach(opt => {
            const orow = createOptionRow(opt.id, opt.option_text);
            cont.appendChild(orow);
        });
    }
}

function toggleOptions(select) {
    const opts = select.parentElement.parentElement.querySelector('.q-options');
    opts.style.display = select.value === 'choice' ? 'block' : 'none';
}

function addOptionRow(btn) {
    const cont = btn.parentElement.querySelector('.options-container');
    cont.appendChild(createOptionRow('', ''));
}

function createOptionRow(id, text) {
    const div = document.createElement('div');
    div.className = 'opt-row';
    div.style.display = 'flex';
    div.style.gap = '8px';
    div.innerHTML = `
        <input type="hidden" class="opt-id" value="${id}">
        <input type="text" class="form-control opt-text" placeholder="Variant matni" value="${text}" style="flex:1; padding:4px; font-size:14px;" required>
        <button type="button" style="color:red; background:transparent; border:none; cursor:pointer;" onclick="this.parentElement.remove()">x</button>
    `;
    return div;
}

function openSurveyModal() {
    document.getElementById('surveyForm').reset();
    document.getElementById('surveyId').value = '';
    document.getElementById('surveyQuestionsBox').innerHTML = '';
    document.getElementById('surveyModalTitle').innerText = "So'rovnoma Qo'shish";
    document.getElementById('surveyModal').classList.remove('hidden');
    addSurveyQuestion(); // add one empty question
}

async function loadSurveys() {
    if (!window.supabaseClient) return;
    const { data, error } = await window.supabaseClient.from('surveys').select('*').order('created_at', { ascending: false });
    const tb = document.getElementById('surveysTbody');
    tb.innerHTML = '';
    if (error) {
        tb.innerHTML = `<tr><td colspan="4">Xato: ${error.message}</td></tr>`;
        return;
    }
    if (data.length === 0) {
        tb.innerHTML = `<tr><td colspan="4">So'rovnomalar yo'q.</td></tr>`;
        return;
    }
    data.forEach(item => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${item.title}</td>
            <td>${item.is_open ? '<span style="color:green; font-weight:bold;">Faol</span>' : '<span style="color:red;">Yakunlangan</span>'}</td>
            <td>${new Date(item.created_at).toLocaleDateString()}</td>
            <td class="action-links">
                <a onclick="editSurvey(${item.id})">Tahrirlash</a>
                <a onclick="viewSurveyStats(${item.id})">Natijalar</a>
                <a onclick="deleteSurvey(${item.id})" class="del">O'chirish</a>
            </td>
        `;
        tb.appendChild(tr);
    });
}

async function editSurvey(id) {
    const { data: survey, error } = await supabaseClient
        .from('surveys')
        .select('*, survey_questions(*, survey_options(*))')
        .eq('id', id)
        .single();

    if (error) {
        alert("Xato: " + error.message);
        return;
    }

    document.getElementById('surveyId').value = survey.id;
    document.getElementById('surveyTitle').value = survey.title;
    document.getElementById('surveyDesc').value = survey.description || '';
    document.getElementById('surveyAnon').checked = survey.is_anonymous_allowed;
    document.getElementById('surveyOpen').checked = survey.is_open;
    document.getElementById('surveyQuestionsBox').innerHTML = '';

    // Sort questions by order_num
    if (survey.survey_questions) {
        const qs = survey.survey_questions.sort((a, b) => a.order_num - b.order_num);
        qs.forEach(q => {
            const opts = q.survey_options ? q.survey_options : [];
            addSurveyQuestion(q.id, q.question_text, q.question_type, opts);
        });
    }

    document.getElementById('surveyModalTitle').innerText = "So'rovnomani Tahrirlash";
    document.getElementById('surveyModal').classList.remove('hidden');
}

async function deleteSurvey(id) {
    if (confirm("Haqiqatan ham o'chirmoqchimisiz?")) {
        const { error } = await supabaseClient.from('surveys').delete().eq('id', id);
        if (error) {
            alert("O'chirishda xatolik: " + error.message);
            return;
        }
        loadSurveys();
    }
}

document.getElementById('surveyForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('surveyId').value;
    const submitBtn = document.getElementById('surveySubmitBtn');
    submitBtn.disabled = true;
    submitBtn.innerText = "Yuklanmoqda...";

    try {
        const payload = {
            title: document.getElementById('surveyTitle').value,
            description: document.getElementById('surveyDesc').value,
            is_anonymous_allowed: document.getElementById('surveyAnon').checked,
            is_open: document.getElementById('surveyOpen').checked
        };

        let finalSurveyId = id;
        if (id) {
            const { error } = await supabaseClient.from('surveys').update(payload).eq('id', id);
            if (error) throw error;
        } else {
            const { data, error } = await supabaseClient.from('surveys').insert([payload]).select();
            if (error) throw error;
            if (data && data.length > 0) finalSurveyId = data[0].id;
        }

        const qRows = document.querySelectorAll('.q-row');
        let orderTracker = 0;
        for (const qRow of qRows) {
            orderTracker++;
            const qId = qRow.querySelector('.q-id').value;
            const qText = qRow.querySelector('.q-text').value;
            const qType = qRow.querySelector('.q-type').value;

            let finalQId = qId;
            if (finalQId) {
                await supabaseClient.from('survey_questions').update({ question_text: qText, question_type: qType, order_num: orderTracker }).eq('id', finalQId);
            } else {
                const { data: qData } = await supabaseClient.from('survey_questions').insert([{ survey_id: finalSurveyId, question_text: qText, question_type: qType, order_num: orderTracker }]).select();
                if (qData && qData.length > 0) finalQId = qData[0].id;
            }

            if (qType === 'choice' && finalQId) {
                const optRows = qRow.querySelectorAll('.opt-row');
                for (const oRow of optRows) {
                    const oId = oRow.querySelector('.opt-id').value;
                    const oText = oRow.querySelector('.opt-text').value;
                    if (oId) {
                        await supabaseClient.from('survey_options').update({ option_text: oText }).eq('id', oId);
                    } else {
                        await supabaseClient.from('survey_options').insert([{ question_id: finalQId, option_text: oText }]);
                    }
                }
            }
        }

        closeModal('surveyModal');
        loadSurveys();
    } catch (err) {
        alert("Xato: " + err.message);
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = "Saqlash";
    }
});

async function viewSurveyStats(surveyId) {
    const modal = document.getElementById('surveyStatsModal');
    const content = document.getElementById('surveyStatsContent');
    content.innerHTML = "Yuklanmoqda...";
    modal.classList.remove('hidden');

    // 1. Fetch survey and questions
    const { data: surveyData, error: sErr } = await supabaseClient
        .from('surveys')
        .select('*, survey_questions(*, survey_options(*))')
        .eq('id', surveyId)
        .single();
    if (sErr) { content.innerHTML = "Xato: " + sErr.message; return; }

    // 2. Fetch responses
    const { data: responses, error: rErr } = await supabaseClient
        .from('survey_responses')
        .select('*, survey_answers(*)')
        .eq('survey_id', surveyId);

    if (rErr) { content.innerHTML = "Xato: " + rErr.message; return; }

    const questions = (surveyData.survey_questions || []).sort((a, b) => a.order_num - b.order_num);
    const totalResponses = responses.length;

    let html = `<div style="margin-bottom:24px;">Umumiy javob berganlar soni: <strong>${totalResponses}</strong></div>`;

    if (totalResponses === 0) {
        html += `<div>Hech kim qatnashmagan.</div>`;
        content.innerHTML = html;
        return;
    }

    questions.forEach(q => {
        html += `<div style="margin-bottom: 24px; padding: 16px; border: 1px solid var(--border); border-radius: 8px;">`;
        html += `<h4 style="margin-bottom:12px; color:var(--navy);">${q.question_text}</h4>`;

        const qAnswers = [];
        responses.forEach(r => {
            if (r.survey_answers) {
                r.survey_answers.forEach(a => {
                    if (a.question_id === q.id) qAnswers.push(a);
                });
            }
        });

        if (q.question_type === 'choice') {
            const counts = {};
            let answeredCount = 0;
            q.survey_options.forEach(opt => counts[opt.id] = { text: opt.option_text, count: 0 });
            qAnswers.forEach(a => {
                if (a.option_id && counts[a.option_id]) {
                    counts[a.option_id].count++;
                    answeredCount++;
                }
            });

            for (const key in counts) {
                const opt = counts[key];
                const pct = answeredCount > 0 ? ((opt.count / answeredCount) * 100).toFixed(1) : 0;
                html += `
                    <div style="margin-bottom:8px;">
                        <div style="display:flex; justify-content:space-between; font-size:14px; margin-bottom:4px;">
                            <span>${opt.text}</span>
                            <span>${pct}% (${opt.count})</span>
                        </div>
                        <div style="width:100%; height:8px; background:var(--bg); border-radius:4px; overflow:hidden;">
                            <div style="width:${pct}%; height:100%; background:var(--gold);"></div>
                        </div>
                    </div>
                `;
            }
        } else {
            // text type
            html += `<ul style="list-style-type:disc; padding-left:20px; font-size:14px; color:var(--text-dark);">`;
            let txtCount = 0;
            qAnswers.forEach(a => {
                if (a.answer_text && a.answer_text.trim()) {
                    html += `<li style="margin-bottom:4px;">${a.answer_text}</li>`;
                    txtCount++;
                }
            });
            if (txtCount === 0) html += `<li>Javoblar yo'q</li>`;
            html += `</ul>`;
        }

        html += `</div>`;
    });

    content.innerHTML = html;
}
