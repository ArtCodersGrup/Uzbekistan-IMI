import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add "So'rovnomalar" nav link
nav_target = """<a href="#" onclick="showTab('teachersTab')">O'qituvchilar</a>"""
nav_replacement = nav_target + """\n                <a href="#" onclick="showTab('surveysTab')">So'rovnomalar</a>"""
html = html.replace(nav_target, nav_replacement)

# 2. Add surveysTab HTML
teachers_tab_end_target = """                </div>\n\n                <!-- SETTINGS TAB -->"""
surveys_tab_html = """                <!-- SURVEYS TAB -->
                <div id="surveysTab" class="hidden">
                    <div class="dash-title">
                        <span>So'rovnomalar</span>
                        <button onclick="openSurveyModal()">+ Qo'shish</button>
                    </div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Noms</th>
                                <th>Holati</th>
                                <th>Sana</th>
                                <th>Amallar</th>
                            </tr>
                        </thead>
                        <tbody id="surveysTbody">
                            <tr><td colspan="4">Yuklanmoqda...</td></tr>
                        </tbody>
                    </table>
                </div>

                <!-- SETTINGS TAB -->"""
html = html.replace(teachers_tab_end_target, surveys_tab_html)

# 3. Add modal HTML
modals_target = """    <script>"""
modals_html = """    <!-- SURVEY MODAL -->
    <div id="surveyModal" class="modal-overlay hidden">
        <div class="modal" style="max-width:600px;">
            <h3 id="surveyModalTitle">So'rovnoma Qo'shish</h3>
            <form id="surveyForm">
                <input type="hidden" id="surveyId">
                <div class="form-group">
                    <label>Sarlavha</label>
                    <input type="text" id="surveyTitle" class="form-control" required>
                </div>
                <div class="form-group">
                    <label>Tasnifi (Qisqacha)</label>
                    <textarea id="surveyDesc" class="form-control" rows="2"></textarea>
                </div>
                <div class="form-group" style="display:flex; gap:16px; align-items:center;">
                    <label style="margin:0; display:flex; align-items:center; gap:8px;">
                        <input type="checkbox" id="surveyAnon"> Anonim ruxsat etiladi
                    </label>
                    <label style="margin:0; display:flex; align-items:center; gap:8px;">
                        <input type="checkbox" id="surveyOpen" checked> Faol (Ochiq)
                    </label>
                </div>
                
                <h4 style="margin:16px 0 8px 0; border-bottom:1px solid var(--border); padding-bottom:8px;">Savollar</h4>
                <div id="surveyQuestionsBox" style="display:flex; flex-direction:column; gap:16px; margin-bottom:16px;">
                </div>
                <button type="button" class="btn-outline" style="font-size:12px; padding:6px 12px;" onclick="addSurveyQuestion()">+ Savol qo'shish</button>

                <div class="modal-actions">
                    <button type="button" class="btn-outline" onclick="closeModal('surveyModal')">Bekor qilish</button>
                    <button type="submit" class="btn" id="surveySubmitBtn" style="width:auto;">Saqlash</button>
                </div>
            </form>
        </div>
    </div>

    <!-- SURVEY STATS MODAL -->
    <div id="surveyStatsModal" class="modal-overlay hidden">
        <div class="modal" style="max-width:800px; max-height:90vh; overflow-y:auto;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
                <h3 id="surveyStatsTitle">Statistika</h3>
                <button type="button" class="btn-outline" onclick="closeModal('surveyStatsModal')">Yopish</button>
            </div>
            <div id="surveyStatsContent">Yuklanmoqda...</div>
        </div>
    </div>

    <script>"""
html = html.replace(modals_target, modals_html)

# 4. Integrate to showTab
showtab_target = "document.getElementById('settingsTab').classList.add('hidden');"
showtab_replacement = showtab_target + "\n            document.getElementById('surveysTab').classList.add('hidden');"
html = html.replace(showtab_target, showtab_replacement)

# 5. Inject survey_admin.js
script_target = "</body>"
script_replacement = '    <script src="survey_admin.js"></script>\n</body>'
html = html.replace(script_target, script_replacement)

# 6. Add loadSurveys() to showDashboard
showdash_target = "loadTeachers();"
showdash_replacement = "loadTeachers();\n            if(typeof loadSurveys === 'function') loadSurveys();"
html = html.replace(showdash_target, showdash_replacement)


with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("admin.html patched.")
