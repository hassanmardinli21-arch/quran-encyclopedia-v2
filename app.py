<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الموسوعة القرآنية - التفاسير</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HF0JEW40GY"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-HF0JEW40GY');
    </script>
    <style>
        :root {
            --parchment-1: #F5E6C8; --parchment-2: #EFDCB8; --parchment-3: #E8D5A8;
            --parchment-dark: #C9B282; --ink-primary: #4A3728; --ink-secondary: #6B5540;
            --gold: #B8860B; --gold-light: #D4AF37; --border-color: #A68B5B;
            --shadow: rgba(74, 55, 40, 0.2); --highlight-bg: #FFE9A8; --highlight-border: #E6C34A;
            --bookmark-color: #8B4513; --bookmark-dark: #5C2E0E;
            --special-color: #7c3aed; --special-dark: #4c1d95;
            --card-bg-1: #FFFCF2; --card-bg-2: #FAF0D7;
            --container-bg-1: #FBF0D8; --container-bg-2: #F5E6C8;
            --input-bg: #FFFCF2;
        }
        body.dark-mode {
            --parchment-1: #1a1a1a; --parchment-2: #222222; --parchment-3: #2a2a2a;
            --parchment-dark: #3a3a3a; --ink-primary: #E8DFC8; --ink-secondary: #B0A88C;
            --gold: #D4AF37; --gold-light: #E8C766; --border-color: #4A3F2E;
            --shadow: rgba(0, 0, 0, 0.5); --highlight-bg: #5C4A1E; --highlight-border: #B8860B;
            --card-bg-1: #2a2620; --card-bg-2: #211e18;
            --container-bg-1: #1f1c17; --container-bg-2: #2a2519; --input-bg: #2a2620;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Cairo', sans-serif; background: radial-gradient(circle at 20% 30%, rgba(212, 175, 55, 0.08) 0%, transparent 50%), radial-gradient(circle at 80% 70%, rgba(184, 134, 11, 0.06) 0%, transparent 50%), linear-gradient(135deg, var(--parchment-1) 0%, var(--parchment-2) 50%, var(--parchment-3) 100%); background-attachment: fixed; color: var(--ink-primary); min-height: 100vh; padding: 20px; line-height: 1.8; transition: background 0.4s, color 0.4s; }
        body::before { content: ''; position: fixed; inset: 0; background-image: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(139, 109, 66, 0.03) 2px, rgba(139, 109, 66, 0.03) 4px), repeating-linear-gradient(90deg, transparent, transparent 2px, rgba(139, 109, 66, 0.03) 2px, rgba(139, 109, 66, 0.03) 4px); pointer-events: none; z-index: 0; }
        body.dark-mode::before { opacity: 0.3; }
        .container { position: relative; z-index: 1; max-width: 950px; margin: 0 auto; background: linear-gradient(180deg, var(--container-bg-1) 0%, var(--container-bg-2) 100%); border: 3px double var(--border-color); border-radius: 12px; padding: 30px 28px; box-shadow: 0 0 0 1px rgba(184, 134, 11, 0.2), 0 10px 40px var(--shadow); }
        h1 { font-family: 'Amiri', serif; font-size: 2.4rem; text-align: center; color: var(--ink-primary); margin-bottom: 8px; text-shadow: 1px 1px 0 var(--parchment-dark); }
        h1::before, h1::after { content: '❁'; color: var(--gold); margin: 0 12px; font-size: 1.6rem; vertical-align: middle; }
        .subtitle { text-align: center; color: var(--ink-secondary); font-size: 1rem; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid var(--border-color); font-style: italic; }
        .top-buttons { display: flex; gap: 8px; justify-content: center; margin-bottom: 20px; flex-wrap: wrap; }
        .about-btn { padding: 8px 16px; background: linear-gradient(180deg, var(--gold-light) 0%, var(--gold) 100%); color: #FFF8DC; border: 1px solid #8B6508; border-radius: 20px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.9rem; cursor: pointer; text-shadow: 1px 1px 0 rgba(0,0,0,0.2); transition: 0.2s; box-shadow: 0 2px 6px rgba(184, 134, 11, 0.3); }
        .about-btn:hover { transform: translateY(-1px); box-shadow: 0 4px 10px rgba(184, 134, 11, 0.4); }
        .about-btn.sync { background: linear-gradient(180deg,#38bdf8,#0284c7); border-color:#075985; }
        .about-btn.dark { background: linear-gradient(180deg,#6b7280,#374151); border-color:#1f2937; }
        .about-btn.nav { background: linear-gradient(180deg,#a78bfa,#7c3aed); border-color:#5b21b6; }
        .about-btn.bm-color { background: linear-gradient(180deg,#f59e0b,#b45309); border-color:#78350f; }
        .about-btn.my-bm { background: linear-gradient(180deg,#a78bfa,#7c3aed); border-color:#5b21b6; }
        .about-btn.help { background: linear-gradient(180deg,#10b981,#047857); border-color:#065f46; }
        .about-btn.wake { background: linear-gradient(180deg,#fbbf24,#d97706); border-color:#92400e; }
        .about-btn.wake.active { background: linear-gradient(180deg,#f59e0b,#b45309); border-color:#78350f; box-shadow: 0 0 0 2px rgba(251,191,36,0.5); }
        .about-btn.lock { background: linear-gradient(180deg,#ef4444,#b91c1c); border-color:#7f1d1d; }
        .about-btn.lock.active { background: linear-gradient(180deg,#dc2626,#991b1b); }
        .about-btn.prayer { background: linear-gradient(180deg,#8b5cf6,#6d28d9); border-color:#5b21b6; }

        .reading-timer { display: flex; align-items: center; justify-content: center; gap: 8px; padding: 8px 16px; background: linear-gradient(180deg, rgba(59,130,246,0.1), rgba(37,99,235,0.05)); border: 1px dashed #3b82f6; border-radius: 10px; margin-bottom: 15px; font-weight: 700; font-size: 0.9rem; color: #1e40af; }
        body.dark-mode .reading-timer { color: #60a5fa; }
        .reading-timer .timer-value { font-family: 'Courier New', monospace; font-size: 1.05rem; background: rgba(255,255,255,0.5); padding: 2px 10px; border-radius: 6px; border: 1px solid rgba(59,130,246,0.3); color: #1d4ed8; }
        body.dark-mode .reading-timer .timer-value { background: rgba(0,0,0,0.3); color: #93c5fd; }

        .screen-lock-overlay { display: none; position: fixed; inset: 0; background: rgba(220, 38, 38, 0.02); z-index: 9996; pointer-events: none; }
        .screen-lock-overlay.active { display: block; }
        body.screen-locked .ayah-card, body.screen-locked .bookmark-btn, body.screen-locked .special-btn, body.screen-locked .show-context-btn, body.screen-locked .bookmark-jump-btn, body.screen-locked .bookmark-clear-btn, body.screen-locked .pagination a, body.screen-locked .surah-suggestion button, body.screen-locked .top-buttons button, body.screen-locked .search-box button, body.screen-locked .search-box input, body.screen-locked .search-box select { pointer-events: none !important; }
        body.screen-locked .lock-fab, body.screen-locked .screen-lock-float { pointer-events: auto !important; }
        .screen-lock-float { display: none; position: fixed; top: 15px; right: 15px; z-index: 10001; padding: 10px 16px; background: linear-gradient(180deg, #dc2626, #991b1b); color: white; border: 2px solid white; border-radius: 30px; font-weight: 700; font-size: 0.85rem; cursor: pointer; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.5); white-space: nowrap; }
        .screen-lock-float.active { display: flex; align-items: center; gap: 6px; }
        .lock-fab { position: fixed; bottom: 25px; right: 20px; width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(180deg, #ef4444, #b91c1c); color: white; border: 3px solid white; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.5); cursor: pointer; display: none; align-items: center; justify-content: center; font-size: 1.6rem; z-index: 10000; padding: 0; line-height: 1; }
        .lock-fab.visible { display: flex; }
        .lock-fab.locked { background: linear-gradient(180deg, #10b981, #047857); }

        .toast-container { position: fixed; top: 80px; left: 50%; transform: translateX(-50%); z-index: 10000; display: flex; flex-direction: column; gap: 10px; pointer-events: none; max-width: 90vw; }
        .toast { background: linear-gradient(180deg, #10b981, #047857); color: white; padding: 14px 22px; border-radius: 12px; font-weight: 700; font-size: 1rem; box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5); display: flex; align-items: center; gap: 10px; border: 2px solid rgba(255,255,255,0.3); pointer-events: auto; max-width: 100%; }
        .toast.toast-bookmark { background: linear-gradient(180deg, var(--bookmark-color), var(--bookmark-dark)); }
        .toast.toast-special { background: linear-gradient(180deg, #7c3aed, #4c1d95); }
        .toast.toast-info { background: linear-gradient(180deg, #3b82f6, #1d4ed8); }
        .toast.toast-warning { background: linear-gradient(180deg, #f59e0b, #b45309); }

        .progress-wrap { background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 20px; padding: 12px 18px 36px 18px; margin-bottom: 20px; display: flex; align-items: flex-start; gap: 12px; position: relative; }
        .progress-label { font-size: 0.85rem; font-weight: 700; color: var(--ink-primary); white-space: nowrap; padding-top: 12px; }
        .progress-bar { flex: 1; height: 18px; background: rgba(0,0,0,0.08); border-radius: 10px; border: 1px solid var(--border-color); position: relative; direction: ltr; margin-top: 10px; }
        body.dark-mode .progress-bar { background: rgba(255,255,255,0.08); }
        .progress-fill { height: 100%; background: linear-gradient(90deg, var(--bookmark-color) 0%, var(--gold) 100%); width: 0%; transition: width 0.5s ease; border-radius: 10px; }
        .progress-percent { font-size: 0.9rem; font-weight: 700; color: var(--bookmark-dark); min-width: 50px; text-align: left; padding-top: 12px; }
        body.dark-mode .progress-percent { color: var(--gold-light); }
        .milestone { position: absolute; top: -3px; bottom: -3px; width: 2px; background: var(--ink-secondary); border-radius: 2px; z-index: 3; transform: translateX(-50%); opacity: 0.5; }
        .milestone.reached { background: #16a34a; width: 3px; opacity: 1; }
        .milestone[data-pct="100"] { background: var(--gold); width: 3px; opacity: 0.8; }
        .milestone-label { position: absolute; top: 24px; transform: translateX(-50%); font-size: 0.7rem; font-weight: 700; color: var(--ink-secondary); white-space: nowrap; z-index: 4; padding: 2px 6px; background: var(--input-bg); border-radius: 6px; opacity: 0.7; }
        .milestone-label.reached { color: #16a34a; opacity: 1; }
        .milestone-label[data-pct="100"] { color: var(--gold); }

        .bookmark-bar { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 12px 18px; background: linear-gradient(180deg, var(--bookmark-color) 0%, var(--bookmark-dark) 100%); border: 2px solid #3D1F08; border-radius: 10px; margin-bottom: 15px; flex-wrap: wrap; }
        .bookmark-info { display: flex; align-items: center; gap: 8px; font-size: 0.95rem; color: #FFFFFF; flex: 1; min-width: 200px; flex-wrap: wrap; }
        .bookmark-info strong { color: #FFD98A; }
        .bookmark-info #hereMsg { display: none; background: #16a34a; color: white; padding: 2px 10px; border-radius: 10px; font-size: 0.75rem; font-weight: 700; }
        .bookmark-actions { display: flex; gap: 8px; flex-wrap: wrap; }
        .bookmark-jump-btn, .bookmark-clear-btn { padding: 8px 14px; border-radius: 8px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.85rem; cursor: pointer; border: none; }
        .bookmark-jump-btn { background: linear-gradient(180deg, #E8A317 0%, #B8860B 100%); color: white; }
        .bookmark-jump-btn.at-location { background: linear-gradient(180deg, #16a34a 0%, #15803d 100%) !important; }
        .bookmark-clear-btn { background: rgba(220, 38, 38, 0.85); color: white; }

        .search-box { display: flex; flex-wrap: wrap; gap: 10px; background: var(--input-bg); padding: 15px; border: 1px solid var(--border-color); border-radius: 10px; margin-bottom: 15px; }
        .search-box input, .search-box select { flex: 1; min-width: 120px; padding: 12px 16px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--input-bg); color: var(--ink-primary); font-family: 'Cairo', sans-serif; font-size: 1rem; outline: none; }
        .search-box button { padding: 12px 28px; background: linear-gradient(180deg, var(--gold-light) 0%, var(--gold) 100%); color: #FFF8DC; border: 1px solid #8B6508; border-radius: 8px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 1rem; cursor: pointer; }

        .tafsir-toggle-bar { display: flex; align-items: center; justify-content: center; gap: 12px; padding: 12px 18px; background: var(--input-bg); border: 1px dashed var(--border-color); border-radius: 10px; margin-bottom: 20px; flex-wrap: wrap; }
        .tafsir-toggle-bar label { display: flex; align-items: center; gap: 8px; cursor: pointer; font-weight: 600; color: var(--ink-primary); font-size: 0.95rem; }
        .tafsir-toggle-bar input[type="checkbox"] { width: 20px; height: 20px; cursor: pointer; accent-color: var(--gold); }
        .toggle-hint { font-size: 0.85rem; color: var(--ink-secondary); font-style: italic; }

        .results-info { text-align: center; color: var(--ink-secondary); font-size: 0.95rem; margin-bottom: 20px; padding: 8px; background: var(--input-bg); border-radius: 6px; border: 1px dashed var(--border-color); }
        .surah-suggestion { background: linear-gradient(180deg, #10b981 0%, #047857 100%); color: white; border-radius: 12px; padding: 16px 20px; margin-bottom: 20px; display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
        .surah-suggestion button { padding: 10px 20px; background: white; color: #047857; border: none; border-radius: 8px; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer; }

        .show-context-btn { background: linear-gradient(180deg, #3b82f6 0%, #1d4ed8 100%); color: white; border: none; border-radius: 20px; padding: 4px 12px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.75rem; cursor: pointer; }
        .ayah-card { background: linear-gradient(180deg, var(--card-bg-1) 0%, var(--card-bg-2) 100%); border: 1px solid var(--border-color); border-right: 5px solid var(--gold); border-radius: 10px; padding: 20px 22px; margin-bottom: 18px; box-shadow: 0 2px 8px rgba(74, 55, 40, 0.08); position: relative; }
        .ayah-card::before { content: '۞'; position: absolute; top: 8px; left: 12px; color: var(--gold); font-size: 1.4rem; opacity: 0.5; }
        .ayah-card.bookmarked { background: var(--highlight-bg); border-right-color: var(--bookmark-color); }
        .ayah-card.focused { box-shadow: 0 0 0 5px #f59e0b !important; }
        .bookmark-ribbon { position: absolute; top: -12px; left: 20px; background: linear-gradient(180deg, var(--bookmark-color) 0%, var(--bookmark-dark) 100%); color: white; padding: 4px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; z-index: 2; }
        .special-ribbon { position: absolute; top: -12px; right: 20px; background: linear-gradient(180deg, var(--special-color) 0%, var(--special-dark) 100%); color: white; padding: 4px 12px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; z-index: 2; max-width: 200px; overflow: hidden; text-overflow: ellipsis; }
        .ayah-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px dashed var(--parchment-dark); flex-wrap: wrap; gap: 8px; }
        .ayah-header-right { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
        .ayah-ref { background: linear-gradient(180deg, var(--gold-light) 0%, var(--gold) 100%); color: #FFF8DC; padding: 4px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; }
        .ayah-type { font-size: 0.8rem; color: var(--ink-secondary); background: rgba(201, 178, 130, 0.3); padding: 3px 12px; border-radius: 12px; }
        .ayah-btns { display: flex; gap: 6px; align-items: center; }
        .bookmark-btn, .special-btn { background: rgba(255, 248, 220, 0.7); border: 1px solid var(--border-color); color: var(--ink-secondary); width: 36px; height: 36px; border-radius: 50%; cursor: pointer; font-size: 1.1rem; display: flex; align-items: center; justify-content: center; padding: 0; line-height: 1; }
        .bookmark-btn.active { background: linear-gradient(180deg, var(--bookmark-color) 0%, var(--bookmark-dark) 100%); color: white; }
        .special-btn.has-special { background: linear-gradient(180deg, var(--special-color) 0%, var(--special-dark) 100%); color: white; }
        .ayah-text { font-family: 'Amiri', serif; font-size: 1.5rem; line-height: 2.4; color: var(--ink-primary); text-align: justify; margin-bottom: 12px; }
        .tafsir-block { background: var(--highlight-bg); border-right: 3px solid var(--gold); border-radius: 6px; padding: 12px 16px; margin-top: 10px; }
        .tafsir-block h4 { font-size: 0.9rem; font-weight: 700; color: var(--gold); margin-bottom: 6px; }
        .tafsir-text { font-size: 1rem; color: var(--ink-secondary); line-height: 2; }
        mark { background: var(--highlight-bg); color: var(--bookmark-color); padding: 0 4px; border-radius: 3px; }
        .empty-msg { text-align: center; padding: 50px 20px; color: var(--ink-secondary); font-size: 1.1rem; background: var(--input-bg); border: 2px dashed var(--border-color); border-radius: 10px; }
        .pagination { display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 30px; padding-top: 20px; border-top: 1px solid var(--border-color); flex-wrap: wrap; }
        .pagination a, .pagination span { padding: 8px 16px; background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 6px; color: var(--ink-primary); text-decoration: none; font-weight: 600; cursor: pointer; }
        .pagination .current { background: var(--gold); color: #FFF8DC; }
        .footer-ornament { text-align: center; margin-top: 30px; color: var(--gold); font-size: 1.4rem; letter-spacing: 8px; opacity: 0.6; }
        .tafsir-count { display: inline-block; background: rgba(184, 134, 11, 0.15); color: var(--gold); padding: 2px 10px; border-radius: 12px; font-size: 0.8rem; font-weight: 700; }
        .loading-msg { text-align: center; padding: 30px; color: var(--ink-secondary); font-size: 1rem; }

        .about-overlay { display: none; position: fixed; inset: 0; background: rgba(74, 55, 40, 0.6); z-index: 9999; justify-content: center; align-items: center; padding: 20px; }
        .about-overlay.active { display: flex; }
        .about-modal { position: relative; max-width: 620px; width: 100%; max-height: 85vh; overflow-y: auto; background: linear-gradient(180deg, var(--container-bg-1) 0%, var(--container-bg-2) 100%); border: 3px double var(--border-color); border-radius: 12px; padding: 30px 28px; }
        .about-modal h2 { font-family: 'Amiri', serif; font-size: 2rem; text-align: center; color: var(--ink-primary); margin-bottom: 6px; }
        .about-intro { text-align: center; color: var(--gold); font-family: 'Amiri', serif; font-size: 1.1rem; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid var(--border-color); }
        .about-modal h3 { font-family: 'Cairo', sans-serif; font-size: 1.15rem; color: var(--gold); margin: 20px 0 10px 0; padding-right: 10px; border-right: 4px solid var(--gold); }
        .about-modal p { color: var(--ink-secondary); line-height: 1.9; margin-bottom: 10px; }
        .about-modal ul { list-style: none; padding: 0; margin-bottom: 10px; }
        .about-modal ul li { padding: 6px 12px; margin-bottom: 4px; color: var(--ink-secondary); background: var(--input-bg); border-radius: 6px; border-right: 3px solid var(--gold-light); font-size: 0.95rem; }
        .about-dua { background: var(--highlight-bg); border: 1px dashed var(--gold); border-radius: 8px; padding: 14px 18px; font-family: 'Amiri', serif; font-size: 1.05rem; text-align: center; line-height: 2; }
        .about-footer { text-align: center; margin-top: 20px; padding-top: 15px; border-top: 1px solid var(--border-color); color: var(--ink-secondary); font-size: 0.9rem; }
        .about-close { position: absolute; top: 12px; left: 12px; width: 34px; height: 34px; border-radius: 50%; background: rgba(184, 134, 11, 0.15); border: 1px solid var(--border-color); cursor: pointer; z-index: 5; }

        .help-step { display: flex; gap: 14px; padding: 14px 16px; background: var(--input-bg); border-radius: 10px; margin-bottom: 12px; border-right: 4px solid var(--gold); }
        .help-step-icon { width: 50px; height: 50px; border-radius: 50%; background: linear-gradient(180deg, var(--gold-light), var(--gold)); color: white; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; }
        .help-step-content { flex: 1; }
        .help-step-title { font-weight: 700; color: var(--ink-primary); font-size: 1rem; margin-bottom: 4px; }
        .help-step-desc { color: var(--ink-secondary); font-size: 0.9rem; line-height: 1.7; }
        .help-step-desc code { background: var(--highlight-bg); padding: 1px 6px; border-radius: 4px; color: var(--bookmark-color); font-weight: 700; }
        .help-section-title { font-family: 'Amiri', serif; font-size: 1.3rem; color: var(--gold); margin: 20px 0 12px 0; padding: 8px 14px; background: var(--highlight-bg); border-radius: 8px; text-align: center; }
        .help-tip { background: rgba(16, 185, 129, 0.1); border: 1px dashed #10b981; border-radius: 8px; padding: 12px 16px; margin: 12px 0; color: #065f46; font-size: 0.9rem; line-height: 1.8; }
        body.dark-mode .help-tip { color: #34d399; }

        .sidebar-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 9998; }
        .sidebar-overlay.active { display: block; }
        .sidebar { position: fixed; top: 0; right: -320px; width: 300px; height: 100vh; background: linear-gradient(180deg, var(--container-bg-1) 0%, var(--container-bg-2) 100%); border-left: 3px double var(--border-color); padding: 20px 15px; overflow-y: auto; z-index: 9999; transition: right 0.3s ease; }
        .sidebar.active { right: 0; }
        .sidebar h3 { text-align: center; font-family: 'Amiri', serif; color: var(--ink-primary); font-size: 1.3rem; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid var(--gold); }
        .sidebar-close { position: absolute; top: 10px; left: 10px; width: 30px; height: 30px; border-radius: 50%; background: rgba(220,38,38,0.15); border: 1px solid #fca5a5; color: #b91c1c; cursor: pointer; }
        .surah-nav-item { display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 6px; margin-bottom: 5px; cursor: pointer; color: var(--ink-primary); font-weight: 600; font-size: 0.9rem; }
        .surah-nav-item .num { background: var(--gold); color: #FFF8DC; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0; }

        .color-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 15px 0; }
        .color-option { width: 100%; aspect-ratio: 1; border-radius: 10px; cursor: pointer; border: 3px solid transparent; position: relative; }
        .color-option.selected { border-color: var(--gold); }
        .color-option.selected::after { content: '✓'; position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 1.5rem; text-shadow: 1px 1px 3px rgba(0,0,0,0.7); }

        .bm-item { display: flex; justify-content: space-between; align-items: center; gap: 8px; padding: 10px 12px; background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 8px; border-right: 4px solid var(--special-color); }
        .bm-item-info { flex: 1; color: var(--ink-primary); font-size: 0.9rem; }
        .bm-item-label { font-weight: 700; color: var(--special-color); font-size: 0.9rem; }
        .bm-item-actions { display: flex; gap: 4px; }
        .bm-item-actions button { padding: 6px 10px; border: none; border-radius: 6px; cursor: pointer; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.8rem; }
        .bm-jump { background: var(--gold); color: white; }
        .bm-edit { background: #2563eb; color: white; }
        .bm-del { background: rgba(220,38,38,0.85); color: white; }

        .label-input-wrap { padding: 15px; background: var(--input-bg); border: 2px solid var(--special-color); border-radius: 10px; margin-bottom: 15px; }
        .label-input-wrap input { width: 100%; padding: 10px 14px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--input-bg); color: var(--ink-primary); font-family: 'Cairo', sans-serif; font-size: 1rem; margin-bottom: 10px; }
        .label-buttons { display: flex; gap: 8px; }
        .label-buttons button { flex: 1; padding: 10px; border: none; border-radius: 8px; cursor: pointer; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.9rem; }
        .label-save { background: var(--special-color); color: white; }
        .label-cancel { background: rgba(107,114,128,0.3); color: var(--ink-primary); }
        .quick-labels { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
        .quick-labels button { padding: 5px 12px; background: rgba(124, 58, 237, 0.1); border: 1px solid var(--special-color); color: var(--special-color); border-radius: 20px; font-family: 'Cairo', sans-serif; font-weight: 600; font-size: 0.8rem; cursor: pointer; }

        .prayer-modal { max-width: 750px !important; }
        .prayer-tabs { display: flex; gap: 4px; margin-bottom: 20px; background: var(--input-bg); border-radius: 10px; padding: 5px; flex-wrap: wrap; }
        .prayer-tab { flex: 1; padding: 10px 12px; background: transparent; border: none; border-radius: 8px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 0.85rem; color: var(--ink-secondary); cursor: pointer; min-width: 80px; }
        .prayer-tab.active { background: linear-gradient(180deg, var(--gold-light), var(--gold)); color: white; }
        .prayer-content { display: none; }
        .prayer-content.active { display: block; }
        .prayer-date-info { text-align: center; padding: 12px; background: var(--highlight-bg); border: 1px dashed var(--gold); border-radius: 10px; margin-bottom: 15px; font-family: 'Amiri', serif; }
        .prayer-date-info .hijri { font-size: 1.2rem; color: var(--gold); font-weight: 700; }
        .prayer-date-info .gregorian { font-size: 0.85rem; color: var(--ink-secondary); }
        .prayer-next { background: linear-gradient(180deg, #10b981, #047857); color: white; padding: 16px 20px; border-radius: 12px; text-align: center; margin-bottom: 20px; }
        .prayer-next .label { font-size: 0.85rem; opacity: 0.9; }
        .prayer-next .name { font-size: 1.5rem; font-weight: 700; margin: 4px 0; }
        .prayer-next .time { font-size: 1.8rem; font-family: 'Courier New', monospace; font-weight: 700; }
        .prayer-next .countdown { font-size: 0.85rem; margin-top: 6px; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; display: inline-block; }
        .prayer-list { display: grid; gap: 8px; }
        .prayer-item { display: flex; justify-content: space-between; align-items: center; padding: 14px 18px; background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 10px; }
        .prayer-item.next-prayer { background: linear-gradient(180deg, rgba(16,185,129,0.15), rgba(5,150,105,0.08)); border-color: #10b981; border-right: 4px solid #10b981; }
        .prayer-item.passed { opacity: 0.6; }
        .prayer-item-name { font-weight: 700; color: var(--ink-primary); font-size: 1rem; }
        .prayer-item-time { font-family: 'Courier New', monospace; font-size: 1.15rem; font-weight: 700; color: var(--gold); }
        .prayer-location-info { text-align: center; padding: 10px; font-size: 0.85rem; color: var(--ink-secondary); margin-top: 15px; background: var(--input-bg); border-radius: 8px; border: 1px dashed var(--border-color); }
        .prayer-location-btn { padding: 10px 20px; background: linear-gradient(180deg, #3b82f6, #1d4ed8); color: white; border: none; border-radius: 8px; font-family: 'Cairo', sans-serif; font-weight: 700; cursor: pointer; margin-top: 10px; font-size: 0.9rem; }
        .rakah-section { margin-bottom: 20px; }
        .rakah-section-title { font-family: 'Amiri', serif; font-size: 1.2rem; color: var(--gold); margin-bottom: 12px; padding: 8px 14px; background: var(--highlight-bg); border-radius: 8px; border-right: 4px solid var(--gold); }
        .rakah-table { width: 100%; border-collapse: collapse; background: var(--input-bg); border-radius: 10px; overflow: hidden; }
        .rakah-table th { background: linear-gradient(180deg, var(--gold-light), var(--gold)); color: white; padding: 10px; font-size: 0.85rem; text-align: center; }
        .rakah-table td { padding: 10px 12px; text-align: center; border-bottom: 1px solid var(--border-color); color: var(--ink-primary); font-size: 0.9rem; }
        .rakah-num { font-weight: 700; color: var(--gold); font-size: 1.1rem; }
        .rakah-note { background: rgba(59,130,246,0.1); border-right: 3px solid #3b82f6; padding: 10px 14px; border-radius: 6px; margin-top: 10px; font-size: 0.85rem; color: var(--ink-secondary); }
        .qibla-container { text-align: center; padding: 10px; }
        .qibla-compass { position: relative; width: 260px; height: 260px; margin: 15px auto; border-radius: 50%; background: radial-gradient(circle, var(--input-bg) 0%, var(--highlight-bg) 100%); border: 4px solid var(--gold); }
        .qibla-arrow { position: absolute; top: 50%; left: 50%; width: 4px; height: 105px; background: linear-gradient(180deg, #10b981, #047857); transform-origin: bottom center; transform: translate(-50%, -100%) rotate(0deg); border-radius: 2px; }
        .qibla-arrow::after { content: '🕋'; position: absolute; top: -30px; left: 50%; transform: translateX(-50%); font-size: 2rem; }
        .qibla-north { position: absolute; top: 10px; left: 50%; transform: translateX(-50%); font-weight: 700; color: var(--gold); font-size: 1.2rem; }
        .qibla-south { position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%); font-weight: 700; color: var(--ink-secondary); font-size: 0.9rem; }
        .qibla-east { position: absolute; top: 50%; right: 10px; transform: translateY(-50%); font-weight: 700; color: var(--ink-secondary); font-size: 0.9rem; }
        .qibla-west { position: absolute; top: 50%; left: 10px; transform: translateY(-50%); font-weight: 700; color: var(--ink-secondary); font-size: 0.9rem; }
        .qibla-center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 20px; height: 20px; background: var(--gold); border-radius: 50%; }
        .qibla-degree { font-size: 1.3rem; font-weight: 700; color: var(--gold); font-family: 'Courier New', monospace; margin-top: 10px; }
        .qibla-instruction { background: var(--highlight-bg); border: 1px dashed var(--gold); border-radius: 10px; padding: 14px; margin-top: 20px; font-size: 0.9rem; color: var(--ink-primary); text-align: right; line-height: 1.8; }
        .prayer-guide-section { margin-bottom: 20px; background: var(--input-bg); border-radius: 10px; padding: 16px; border-right: 4px solid var(--gold); }
        .prayer-guide-title { font-family: 'Amiri', serif; font-size: 1.3rem; color: var(--gold); margin-bottom: 10px; }
        .prayer-guide-desc { color: var(--ink-secondary); font-size: 0.9rem; line-height: 1.9; margin-bottom: 10px; }
        .prayer-guide-steps { list-style: none; padding: 0; }
        .prayer-guide-steps li { padding: 10px 14px; margin-bottom: 6px; background: var(--highlight-bg); border-radius: 8px; border-right: 3px solid var(--gold-light); font-size: 0.9rem; color: var(--ink-primary); line-height: 1.7; }
        .prayer-guide-steps li strong { color: var(--gold); }
        .prayer-guide-note { background: rgba(16,185,129,0.1); border: 1px dashed #10b981; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 0.85rem; color: #065f46; }

        .welcome-modal { max-width: 680px !important; }
        .welcome-header { text-align: center; margin-bottom: 20px; }
        .welcome-icon { font-size: 4rem; display: block; margin-bottom: 10px; }
        .welcome-title { font-family: 'Amiri', serif; font-size: 2.2rem; color: var(--ink-primary); margin-bottom: 8px; }
        .welcome-version { display: inline-block; background: linear-gradient(180deg, #10b981 0%, #047857 100%); color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; margin-bottom: 15px; }
        .welcome-message { background: var(--highlight-bg); border: 1px dashed var(--gold); border-radius: 10px; padding: 16px 20px; margin: 15px 0 20px 0; font-family: 'Amiri', serif; font-size: 1.05rem; text-align: center; line-height: 2; }
        .welcome-features-title { font-size: 1.15rem; color: var(--gold); margin: 20px 0 12px 0; padding-right: 10px; border-right: 4px solid var(--gold); }
        .feature-item { display: flex; gap: 12px; padding: 12px 14px; background: var(--input-bg); border-radius: 10px; margin-bottom: 10px; border-right: 4px solid var(--gold); }
        .feature-icon { width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(180deg, var(--gold-light), var(--gold)); color: white; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; flex-shrink: 0; }
        .feature-content { flex: 1; }
        .feature-title { font-weight: 700; color: var(--ink-primary); font-size: 0.95rem; margin-bottom: 3px; }
        .feature-desc { color: var(--ink-secondary); font-size: 0.85rem; line-height: 1.6; }
        .feature-badge { display: inline-block; background: linear-gradient(180deg, #ef4444, #b91c1c); color: white; padding: 1px 8px; border-radius: 8px; font-size: 0.65rem; font-weight: 700; margin-right: 6px; }
        .welcome-footer-btn { width: 100%; padding: 14px; background: linear-gradient(180deg, #10b981, #047857); color: white; border: none; border-radius: 10px; font-family: 'Cairo', sans-serif; font-weight: 700; font-size: 1.05rem; cursor: pointer; margin-top: 20px; }
        .welcome-dua { text-align: center; font-family: 'Amiri', serif; font-size: 0.95rem; color: var(--gold); margin-top: 18px; padding-top: 15px; border-top: 1px dashed var(--border-color); line-height: 1.9; }

        .sync-badge { display: inline-block; background: rgba(34,197,94,0.15); color: #16a34a; padding: 2px 8px; border-radius: 10px; font-size: 0.7rem; font-weight: 700; margin-right: 6px; }

        @media (max-width: 600px) {
            h1 { font-size: 1.7rem; }
            .ayah-text { font-size: 1.25rem; line-height: 2.1; }
            .container { padding: 20px 14px; }
            .search-box { flex-direction: column; }
            .search-box input, .search-box select, .search-box button { width: 100%; }
            .about-btn { font-size: 0.8rem; padding: 7px 12px; }
            .qibla-compass { width: 220px; height: 220px; }
            .qibla-arrow { height: 85px; }
            .prayer-tab { font-size: 0.75rem; padding: 8px 6px; }
            .lock-fab { width: 55px; height: 55px; font-size: 1.4rem; bottom: 20px; right: 15px; }
        }
    </style>
</head>
<body>
    <div class="toast-container" id="toastContainer"></div>
    <div class="screen-lock-overlay" id="screenLockOverlay"></div>
    <button class="lock-fab" id="lockFab" onclick="toggleScreenLock()">🔒</button>

    <div class="container">
        <h1>الموسوعة القرآنية</h1>
        <p class="subtitle">﴿ وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ ﴾</p>

        <div class="top-buttons">
            <button class="about-btn help" onclick="openHelp()">📖 طريقة الاستخدام</button>
            <button class="about-btn prayer" onclick="openPrayer()">🕌 الصلاة</button>
            <button class="about-btn" onclick="openAbout()">ℹ️ حول</button>
            <button class="about-btn sync" onclick="openSync()">🔄 مزامنة</button>
            <button class="about-btn nav" onclick="openSidebar()">⚡ السور</button>
            <button class="about-btn my-bm" onclick="openBookmarksList()">📌 علاماتي <span id="bmCount" style="background:rgba(255,255,255,0.3); padding:1px 8px; border-radius:10px; font-size:0.75rem;">0</span></button>
            <button class="about-btn bm-color" onclick="openColorPicker()">🎨 لون</button>
            <button class="about-btn wake" onclick="toggleWakeLock()" id="wakeBtn">☀️ إبقاء الشاشة</button>
            <button class="about-btn lock" onclick="toggleScreenLock()" id="lockBtn">🔒 قفل الشاشة</button>
            <button class="about-btn dark" onclick="toggleDarkMode()" id="darkModeBtn">🌙 ليلي</button>
        </div>

        <div class="reading-timer">
            <span>⏱️</span>
            <span>مدة القراءة:</span>
            <span class="timer-value" id="readingTimer">00:00:00</span>
        </div>

        <div class="progress-wrap">
            <span class="progress-label">📊 تقدم القراءة:</span>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
                <div class="milestone" style="left: 25%;" data-pct="25"></div>
                <div class="milestone" style="left: 50%;" data-pct="50"></div>
                <div class="milestone" style="left: 75%;" data-pct="75"></div>
                <div class="milestone" style="left: 100%;" data-pct="100"></div>
                <div class="milestone-label" style="left: 25%;" data-pct="25">📖 ربع</div>
                <div class="milestone-label" style="left: 50%;" data-pct="50">📖 نصف</div>
                <div class="milestone-label" style="left: 75%;" data-pct="75">📖 ٣/٤</div>
                <div class="milestone-label" style="left: 100%;" data-pct="100">🏁 ختم</div>
            </div>
            <span class="progress-percent" id="progressPercent">0%</span>
        </div>

        <div class="bookmark-bar" id="bookmarkBar" style="display: none;">
            <div class="bookmark-info">
                <span>🔖</span>
                <strong>آخر قراءة:</strong>
                <span id="bookmarkLocation">—</span>
                <span id="hereMsg">✅ أنت هنا</span>
            </div>
            <div class="bookmark-actions">
                <button class="bookmark-jump-btn" id="jumpBtn" onclick="jumpToBookmark()">📖 العلامة المحفوظة</button>
                <button class="bookmark-clear-btn" onclick="clearBookmark()">✖ حذف</button>
            </div>
        </div>

        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 ابحث...">
            <select id="sourceSelect">
                <option value="quran">📖 القرآن</option>
                <option value="all_tafsirs">📚 جميع التفاسير</option>
                <option value="tafsir_saadi">📗 السعدي</option>
                <option value="tafsir_ibn_kathir">📘 ابن كثير</option>
            </select>
            <select id="surahSelect"><option value="all">جميع السور</option></select>
            <select id="ayahSelect"><option value="all">كل الآيات</option></select>
            <button id="searchBtn">بحث</button>
        </div>

        <div class="tafsir-toggle-bar" id="tafsirToggleBar">
            <label><input type="checkbox" id="showTafsirToggle"> 📚 إظهار التفاسير</label>
            <span class="toggle-hint" id="toggleHint">(مخفية)</span>
        </div>

        <div class="results-info" id="resultsInfo">⏳ جاري تحميل البيانات...</div>
        <div id="surahSuggestionContainer"></div>
        <div id="resultsContainer"><div class="loading-msg">⏳ جاري تحميل البيانات...</div></div>
        <div class="pagination" id="pagination"></div>
        <div class="footer-ornament">❁ ❁ ❁</div>
    </div>

    <div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>
    <div class="sidebar" id="sidebar">
        <button class="sidebar-close" onclick="closeSidebar()">✖</button>
        <h3>⚡ الانتقال السريع</h3>
        <div id="sidebarList"></div>
    </div>

    <div class="about-overlay" id="welcomeOverlay" onclick="closeWelcomeOutside(event)">
        <div class="about-modal welcome-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeWelcome()">✖</button>
            <div class="welcome-header">
                <span class="welcome-icon">🌟</span>
                <h2 class="welcome-title">مرحباً بك</h2>
                <div class="welcome-version">الإصدار الجديد v2.1</div>
            </div>
            <div class="welcome-message">
                ﴿ وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ ﴾
                <br>
                <span style="font-size:0.85rem; color:var(--ink-secondary);">أهلاً بك في الموسوعة القرآنية</span>
            </div>
            <h3 class="welcome-features-title">✨ ما الجديد في هذا التحديث</h3>
            <div class="feature-item"><div class="feature-icon">📊</div><div class="feature-content"><div class="feature-title"><span class="feature-badge">جديد</span> Google Analytics</div><div class="feature-desc">ربط التطبيق بـ Google Analytics لمعرفة عدد الزوار وإحصائيات الاستخدام.</div></div></div>
            <div class="feature-item"><div class="feature-icon">🔖</div><div class="feature-content"><div class="feature-title"><span class="feature-badge">إصلاح</span> ثبات البوك مارك</div><div class="feature-desc">البوك مارك لا يختفي الآن عند فتح التطبيق مرة أخرى.</div></div></div>
            <div class="feature-item"><div class="feature-icon">🕌</div><div class="feature-content"><div class="feature-title">قسم الصلاة الكامل</div><div class="feature-desc">مواقيت الصلاة + القبلة + جدول الركعات + كيفية الصلاة.</div></div></div>
            <button class="welcome-footer-btn" onclick="closeWelcome()">✅ فهمت، لنبدأ القراءة</button>
            <div class="welcome-dua">اللهم اجعل هذا العمل خالصاً لوجهك الكريم 🤲</div>
        </div>
    </div>

    <div class="about-overlay" id="helpOverlay" onclick="closeHelpOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()" style="max-width:720px;">
            <button class="about-close" onclick="closeHelp()">✖</button>
            <h2>📖 طريقة الاستخدام</h2>
            <p class="about-intro">دليل شامل لاستخدام جميع ميزات التطبيق</p>
            <h3 class="help-section-title">🕌 قسم الصلاة</h3>
            <div class="help-step"><div class="help-step-icon">🕌</div><div class="help-step-content"><div class="help-step-title">مواقيت الصلاة والقبلة</div><div class="help-step-desc">اضغط زر <strong>🕌 الصلاة</strong> → فعّل الموقع → ستظهر مواقيت الصلاة + التاريخ الهجري + العد التنازلي.</div></div></div>
            <div class="help-step"><div class="help-step-icon">📖</div><div class="help-step-content"><div class="help-step-title">كيفية الصلاة</div><div class="help-step-desc">تبويب <strong>📖 التعليمات</strong> يحتوي: العيد، الجمعة، الجنازة، التراويح، قيام الليل.</div></div></div>
            <h3 class="help-section-title">🔒 قفل الشاشة</h3>
            <div class="help-step"><div class="help-step-icon">🔒</div><div class="help-step-content"><div class="help-step-title">قفل الشاشة الذكي</div><div class="help-step-desc">اضغط <strong>🔒 قفل الشاشة</strong>. يمكنك التنقل بين الصفحات! زر الفتح في الزاوية العلوية اليمنى.</div></div></div>
            <h3 class="help-section-title">⏱️ الميزات</h3>
            <div class="help-step"><div class="help-step-icon">⏱️</div><div class="help-step-content"><div class="help-step-title">مؤقت القراءة</div><div class="help-step-desc">يعرض مدة قراءتك منذ فتح التطبيق.</div></div></div>
            <div class="help-step"><div class="help-step-icon">☀️</div><div class="help-step-content"><div class="help-step-title">إبقاء الشاشة مضيئة</div><div class="help-step-desc">لمنع انطفاء الشاشة أثناء القراءة.</div></div></div>
            <h3 class="help-section-title">🌟 الاستخدام الأساسي</h3>
            <div class="help-step"><div class="help-step-icon">📖</div><div class="help-step-content"><div class="help-step-title">قراءة القرآن</div><div class="help-step-desc">اختر السورة واضغط <code>بحث</code>.</div></div></div>
            <div class="help-step"><div class="help-step-icon">🔖</div><div class="help-step-content"><div class="help-step-title">حفظ موضع القراءة</div><div class="help-step-desc">اضغط <code>🔖</code> على أي آية.</div></div></div>
            <div class="help-step"><div class="help-step-icon">📌</div><div class="help-step-content"><div class="help-step-title">علامة خاصة</div><div class="help-step-desc">اضغط <code>📌</code> وأدخل اسماً.</div></div></div>
            <h3 class="help-section-title">☁️ المزامنة</h3>
            <div class="help-step"><div class="help-step-icon">🔄</div><div class="help-step-content"><div class="help-step-title">مزامنة الأجهزة</div><div class="help-step-desc">انسخ الرمز من <code>🔄 مزامنة</code> وضعه في أجهزتك.</div></div></div>
            <h3 class="help-section-title">🎨 التخصيص</h3>
            <div class="help-step"><div class="help-step-icon">🎨</div><div class="help-step-content"><div class="help-step-title">لون العلامة</div><div class="help-step-desc"><code>🎨 لون</code> لاختيار من 8 ألوان.</div></div></div>
            <div class="help-step"><div class="help-step-icon">🌙</div><div class="help-step-content"><div class="help-step-title">الوضع الليلي</div><div class="help-step-desc"><code>🌙 ليلي</code> للتبديل.</div></div></div>
            <h3 class="help-section-title">🤲 دعاء</h3>
            <p class="about-dua">اللهم اجعل هذا العمل خالصاً لوجهك الكريم،<br>وانفع به المسلمين.</p>
        </div>
    </div>

    <div class="about-overlay" id="aboutOverlay" onclick="closeAboutOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeAbout()">✖</button>
            <h2>📖 حول التطبيق</h2>
            <p class="about-intro">بسم الله الرحمن الرحيم</p>
            <p><strong>الموسوعة القرآنية</strong> تطبيق إسلامي مجاني لقراءة القرآن والتفاسير.</p>
            <h3>✨ المميزات</h3>
            <ul>
                <li>📖 القرآن الكريم كاملاً (6236 آية)</li>
                <li>📗 تفسير السعدي + 📘 تفسير ابن كثير</li>
                <li>🔍 بحث ذكي يتجاهل التشكيل</li>
                <li>🕌 قسم صلاة كامل (مواقيت + قبلة + تعليمات)</li>
                <li>⏱️ مؤقت مدة القراءة</li>
                <li>🔒 قفل الشاشة الذكي</li>
                <li>☀️ إبقاء الشاشة مضيئة</li>
                <li>☁️ مزامنة تلقائية بين الأجهزة</li>
                <li>📊 إحصائيات Google Analytics</li>
                <li>🌙 وضع ليلي + 🎨 لون العلامة</li>
            </ul>
            <h3>🤲 دعاء</h3>
            <p class="about-dua">اللهم اجعل هذا العمل خالصاً لوجهك الكريم،<br>وانفع به المسلمين،<br>واجعله صدقة جارية عن روح والدينا ووالديكم.</p>
            <p class="about-footer"><strong>إعداد:</strong> حسان مارديني<br><strong>السنة:</strong> 1447 هـ / 2026 م</p>
        </div>
    </div>

    <div class="about-overlay" id="prayerOverlay" onclick="closePrayerOutside(event)">
        <div class="about-modal prayer-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closePrayer()">✖</button>
            <h2>🕌 قسم الصلاة</h2>
            <p class="about-intro">مواقيت الصلاة، الركعات، القبلة، وكيفية الصلاة</p>
            <div class="prayer-tabs">
                <button class="prayer-tab active" onclick="showPrayerTab('times')" id="tab-times">🕌 المواقيت</button>
                <button class="prayer-tab" onclick="showPrayerTab('rakah')" id="tab-rakah">🔢 الركعات</button>
                <button class="prayer-tab" onclick="showPrayerTab('qibla')" id="tab-qibla">🧭 القبلة</button>
                <button class="prayer-tab" onclick="showPrayerTab('guide')" id="tab-guide">📖 التعليمات</button>
            </div>
            <div class="prayer-content active" id="content-times">
                <div id="prayerTimesContainer">
                    <div style="text-align:center; padding:30px;">
                        <div style="font-size:3rem; margin-bottom:10px;">📍</div>
                        <p style="margin-bottom:15px; color:var(--ink-secondary);">لتحديد مواقيت الصلاة، نحتاج إذن الوصول إلى موقعك</p>
                        <button class="prayer-location-btn" onclick="requestLocation()">📍 تفعيل الموقع</button>
                    </div>
                </div>
            </div>
            <div class="prayer-content" id="content-rakah">
                <div class="rakah-section">
                    <div class="rakah-section-title">🕌 الصلوات المفروضة</div>
                    <table class="rakah-table">
                        <thead><tr><th>الصلاة</th><th>عدد الركعات</th><th>الوقت</th></tr></thead>
                        <tbody>
                            <tr><td>الفجر</td><td class="rakah-num">2</td><td>من الفجر حتى طلوع الشمس</td></tr>
                            <tr><td>الظهر</td><td class="rakah-num">4</td><td>من الزوال حتى العصر</td></tr>
                            <tr><td>العصر</td><td class="rakah-num">4</td><td>من العصر حتى الغروب</td></tr>
                            <tr><td>المغرب</td><td class="rakah-num">3</td><td>بعد الغروب</td></tr>
                            <tr><td>العشاء</td><td class="rakah-num">4</td><td>من العشاء حتى الفجر</td></tr>
                        </tbody>
                    </table>
                </div>
                <div class="rakah-section">
                    <div class="rakah-section-title">⭐ السنن الرواتب المؤكدة</div>
                    <table class="rakah-table">
                        <thead><tr><th>الصلاة</th><th>قبل الفرض</th><th>بعد الفرض</th></tr></thead>
                        <tbody>
                            <tr><td>الفجر</td><td class="rakah-num">2</td><td>—</td></tr>
                            <tr><td>الظهر</td><td class="rakah-num">2</td><td class="rakah-num">2</td></tr>
                            <tr><td>المغرب</td><td>—</td><td class="rakah-num">2</td></tr>
                            <tr><td>العشاء</td><td>—</td><td class="rakah-num">2</td></tr>
                            <tr><td>العصر</td><td colspan="2">لا سنة راتبة</td></tr>
                        </tbody>
                    </table>
                    <div class="rakah-note">💡 السنن الرواتب المؤكدة 12 ركعة يومياً.</div>
                </div>
                <div class="rakah-section">
                    <div class="rakah-section-title">🌙 قيام الليل والوتر</div>
                    <table class="rakah-table">
                        <thead><tr><th>الصلاة</th><th>الركعات</th></tr></thead>
                        <tbody>
                            <tr><td>قيام الليل (تهجد)</td><td>مثنى مثنى</td></tr>
                            <tr><td>الوتر</td><td>1 (آخر الليل)</td></tr>
                            <tr><td>صلاة التراويح</td><td>مثنى مثنى (11 أو 23)</td></tr>
                            <tr><td>صلاة الضحى</td><td>2 إلى 12</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="prayer-content" id="content-qibla">
                <div class="qibla-container">
                    <div id="qiblaStatus" style="padding:15px; background:var(--input-bg); border-radius:10px; margin-bottom:15px; text-align:center;">⏳ جاري تحديد موقعك...</div>
                    <div class="qibla-compass" id="qiblaCompass" style="display:none;">
                        <div class="qibla-north">ش</div>
                        <div class="qibla-south">ج</div>
                        <div class="qibla-east">ق</div>
                        <div class="qibla-west">غ</div>
                        <div class="qibla-center"></div>
                        <div class="qibla-arrow" id="qiblaArrow"></div>
                    </div>
                    <div class="qibla-degree" id="qiblaDegree"></div>
                    <button class="prayer-location-btn" onclick="requestLocation()" style="margin-top:15px;">📍 تحديث الموقع</button>
                    <div class="qibla-instruction" id="qiblaInstruction">
                        📱 <strong>كيف تستخدم القبلة؟</strong><br>
                        1. ضع الهاتف مسطحاً<br>
                        2. حرّك الهاتف حتى يشير السهم الأخضر 🕋 للقبلة<br>
                        3. السهم يدور تلقائياً<br><br>
                        💡 إذا لم يتحرك السهم، جهازك لا يحتوي بوصلة إلكترونية.
                    </div>
                </div>
            </div>
            <div class="prayer-content" id="content-guide">
                <div class="prayer-guide-section">
                    <div class="prayer-guide-title">🎉 كيفية صلاة العيد</div>
                    <div class="prayer-guide-desc">صلاة العيدين سنة مؤكدة، تُصلى جماعة.</div>
                    <ol class="prayer-guide-steps">
                        <li><strong>1.</strong> تكبيرة الإحرام ثم 7 تكبيرات في الركعة الأولى.</li>
                        <li><strong>2.</strong> الفاتحة وسورة (الأعلى).</li>
                        <li><strong>3.</strong> الركعة الثانية: 5 تكبيرات، الفاتحة، والغاشية.</li>
                        <li><strong>4.</strong> التشهد والسلام.</li>
                        <li><strong>5.</strong> خطبتان بعد الصلاة.</li>
                    </ol>
                    <div class="prayer-guide-note">⏰ بعد طلوع الشمس بمقدار رمح حتى الزوال.</div>
                </div>
                <div class="prayer-guide-section">
                    <div class="prayer-guide-title">🕌 كيفية صلاة الجمعة</div>
                    <div class="prayer-guide-desc">فرض عين على كل مسلم ذكر بالغ عاقل مقيم.</div>
                    <ol class="prayer-guide-steps">
                        <li><strong>1. الاستعداد:</strong> الاغتسال، التطيب، لبس أحسن الثياب.</li>
                        <li><strong>2. السنن القبلية:</strong> نافلة حتى يخرج الإمام.</li>
                        <li><strong>3. الاستماع للخطبة:</strong> خطبتان مع الإنصات.</li>
                        <li><strong>4. الصلاة:</strong> ركعتان جهريتان بعد الخطبة.</li>
                        <li><strong>5. السنن البعدية:</strong> أربع أو ركعتين بعد الجمعة.</li>
                    </ol>
                    <div class="prayer-guide-note">⚠️ من فاتته الجمعة، يُصلي الظهر أربع ركعات.</div>
                </div>
                <div class="prayer-guide-section">
                    <div class="prayer-guide-title">🕊️ كيفية صلاة الجنازة</div>
                    <div class="prayer-guide-desc">فرض كفاية، بدون ركوع ولا سجود، 4 تكبيرات.</div>
                    <ol class="prayer-guide-steps">
                        <li><strong>التكبيرة الأولى:</strong> الإحرام + الفاتحة.</li>
                        <li><strong>التكبيرة الثانية:</strong> الصلاة على النبي ﷺ.</li>
                        <li><strong>التكبيرة الثالثة:</strong> الدعاء للميت.</li>
                        <li><strong>التكبيرة الرابعة:</strong> الدعاء للمسلمين.</li>
                        <li><strong>التسليم:</strong> تسليمتان.</li>
                    </ol>
                    <div class="prayer-guide-note">📌 تُصلى جماعة أو فرادى.</div>
                </div>
                <div class="prayer-guide-section">
                    <div class="prayer-guide-title">🌙 كيفية صلاة التراويح وقيام الليل</div>
                    <div class="prayer-guide-desc">سنة مؤكدة في رمضان وفي كل ليلة.</div>
                    <ol class="prayer-guide-steps">
                        <li><strong>1. النية:</strong> للتراويح أو القيام.</li>
                        <li><strong>2. الصلاة:</strong> مثنى مثنى.</li>
                        <li><strong>3. القراءة:</strong> جهراً.</li>
                        <li><strong>4. الراحة:</strong> بعد كل 4 ركعات.</li>
                        <li><strong>5. الوتر:</strong> يُختم بثلاث ركعات وتر.</li>
                    </ol>
                    <div class="prayer-guide-note">⭐ العدد: 11 أو 23 ركعة.<br>⏰ الوقت: بعد العشاء حتى الفجر.</div>
                </div>
                <div class="prayer-guide-section">
                    <div class="prayer-guide-title">🌟 أوقات الصلاة وفضلها</div>
                    <div class="prayer-guide-desc">الصلاة على وقتها من أحب الأعمال إلى الله.</div>
                    <ol class="prayer-guide-steps">
                        <li><strong>الفجر:</strong> طلوع الفجر حتى طلوع الشمس.</li>
                        <li><strong>الظهر:</strong> الزوال حتى يصير الظل مثله.</li>
                        <li><strong>العصر:</strong> حتى غروب الشمس.</li>
                        <li><strong>المغرب:</strong> من الغروب حتى ذهاب الحمرة.</li>
                        <li><strong>العشاء:</strong> حتى نصف الليل.</li>
                    </ol>
                </div>
            </div>
        </div>
    </div>

    <div class="about-overlay" id="syncOverlay" onclick="closeSyncOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeSync()">✖</button>
            <h2>🔄 مزامنة الأجهزة</h2>
            <p class="about-intro">اربط أجهزتك</p>
            <div style="text-align:center; padding:12px; background:rgba(34,197,94,0.15); border:2px solid #16a34a; border-radius:8px; margin-bottom:15px; font-weight:700; color:#15803d;">✅ المزامنة مُفعّلة</div>
            <h3>🔑 رمزك الخاص</h3>
            <div style="display:flex; gap:8px; margin:10px 0;">
                <input type="text" id="syncCodeDisplay" readonly style="flex:1; padding:12px; font-size:1.2rem; font-weight:700; text-align:center; letter-spacing:3px; border:2px solid var(--gold); border-radius:8px; background:var(--input-bg); color:var(--ink-primary); direction:ltr;">
                <button onclick="copySyncCode()" type="button" style="padding:12px 20px; background:linear-gradient(180deg,#D4AF37,#B8860B); color:white; border:none; border-radius:8px; font-weight:700; cursor:pointer;">📋 نسخ</button>
            </div>
            <hr style="border:none; border-top:1px dashed var(--border-color); margin:20px 0;">
            <h3>🔗 ربط بجهاز آخر</h3>
            <input type="text" id="syncCodeInput" placeholder="الصق رمز الجهاز الآخر" style="width:100%; padding:12px; font-size:1rem; text-align:center; letter-spacing:2px; border:2px solid var(--gold); border-radius:8px; background:var(--input-bg); color:var(--ink-primary); direction:ltr; margin-bottom:10px;">
            <button onclick="linkToSyncCode()" type="button" style="width:100%; padding:12px; background:linear-gradient(180deg,#38bdf8,#0284c7); color:white; border:none; border-radius:8px; font-weight:700; cursor:pointer;">✅ ربط ومزامنة</button>
        </div>
    </div>

    <div class="about-overlay" id="colorOverlay" onclick="closeColorOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeColorPicker()">✖</button>
            <h2>🎨 لون العلامة</h2>
            <p class="about-intro">اختر اللون المفضل</p>
            <div class="color-grid" id="colorGrid"></div>
        </div>
    </div>

    <div class="about-overlay" id="bookmarksOverlay" onclick="closeBookmarksOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeBookmarksList()">✖</button>
            <h2>📌 علاماتي الخاصة</h2>
            <p class="about-intro"><span class="sync-badge">☁️ مُزامنة</span> جميع العلامات الخاصة بك</p>
            <div id="bookmarksListContainer"></div>
        </div>
    </div>

    <div class="about-overlay" id="labelOverlay" onclick="closeLabelOutside(event)">
        <div class="about-modal" onclick="event.stopPropagation()">
            <button class="about-close" onclick="closeLabelDialog()">✖</button>
            <h2>📌 إضافة علامة خاصة</h2>
            <p class="about-intro" id="labelDialogRef">سورة — آية —</p>
            <div class="label-input-wrap">
                <label style="display:block; font-weight:700; margin-bottom:8px; color:var(--ink-primary);">✏️ اسم العلامة:</label>
                <input type="text" id="labelInput" placeholder="مثلاً: وردي اليومي - يس" maxlength="60">
                <div class="quick-labels" id="quickLabels"></div>
            </div>
            <div class="label-buttons">
                <button class="label-save" onclick="saveLabelBookmark()">✅ حفظ العلامة</button>
                <button class="label-cancel" onclick="closeLabelDialog()">إلغاء</button>
            </div>
        </div>
    </div>

    <script>
        const APP_VERSION = 'v2.1';
        const SURAH_NAMES = ["الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس","هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه","الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجدة","الأحزاب","سبأ","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة","الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج","نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبأ","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات","القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الإخلاص","الفلق","الناس"];
        const SURAH_AYAH_COUNTS = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6];
        const TOTAL_QURAN_AYAHS = 6236;
        const TAFSIR_FILES = [{ key: 'saadi', file: 'tafsir_saadi.json', label: 'تفسير السعدي', icon: '📗' }, { key: 'ibn_kathir', file: 'tafsir_ibn_kathir.json', label: 'تفسير ابن كثير', icon: '📘' }];
        const BOOKMARK_COLORS = [{ name: 'بني محروق', light: '#8B4513', dark: '#5C2E0E' }, { name: 'ذهبي', light: '#D4AF37', dark: '#8B6508' }, { name: 'أخضر زمردي', light: '#059669', dark: '#064e3b' }, { name: 'أزرق نيلي', light: '#2563eb', dark: '#1e3a8a' }, { name: 'أحمر قرمزي', light: '#dc2626', dark: '#7f1d1d' }, { name: 'بنفسجي', light: '#7c3aed', dark: '#4c1d95' }, { name: 'برتقالي', light: '#ea580c', dark: '#7c2d12' }, { name: 'أسود فاحم', light: '#374151', dark: '#111827' }];
        const QUICK_LABELS = ['📌 وردي اليومي', '💭 للتدبر', '⭐ مهمة', '📖 حفظ', '🤲 دعاء', '🔍 للبحث'];

        let quranData = [], allTafsirs = {};
        let currentSource = 'quran', currentKeyword = '', currentSurah = 'all', currentAyah = 'all';
        let currentPage = 1, showTafsir = false;
        let bookmark = null, allBookmarks = [], bookmarkColorIndex = 0;
        let pendingSurah = null, pendingAyah = null;
        let focusAyah = null;
        let serverSyncEnabled = true, isSyncingToServer = false, lastAddTime = 0;
        let wakeLock = null, wakeLockWanted = false;
        let screenLocked = false;
        let readingStartTime = Date.now();
        let userLocation = null;
        let prayerTimes = null;
        let prayerInterval = null;
        let prayerMethod = 13;
        const perPage = 10;

        try {
            if (localStorage.getItem('showTafsir') === 'true') showTafsir = true;
            if (localStorage.getItem('darkMode') === 'true') document.body.classList.add('dark-mode');
            const bc = localStorage.getItem('bookmarkColor'); if (bc) bookmarkColorIndex = parseInt(bc);
            const bms = localStorage.getItem('allBookmarks'); if (bms) allBookmarks = JSON.parse(bms);
            if (localStorage.getItem('wakeLockWanted') === 'true') wakeLockWanted = true;
            const sl = localStorage.getItem('userLocation'); if (sl) userLocation = JSON.parse(sl);
            const sm = localStorage.getItem('prayerMethod'); if (sm) prayerMethod = parseInt(sm);
        } catch (e) {}

        function showToast(message, type = 'default', duration = 3000) {
            const container = document.getElementById('toastContainer');
            if (!container) return;
            const toast = document.createElement('div');
            toast.className = 'toast';
            if (type === 'bookmark') toast.classList.add('toast-bookmark');
            else if (type === 'special') toast.classList.add('toast-special');
            else if (type === 'info') toast.classList.add('toast-info');
            else if (type === 'warning') toast.classList.add('toast-warning');
            let icon = '✅';
            if (type === 'bookmark') icon = '🔖';
            else if (type === 'special') icon = '📌';
            else if (type === 'info') icon = 'ℹ️';
            else if (type === 'warning') icon = '⚠️';
            toast.innerHTML = `<span style="font-size:1.3rem;">${icon}</span><span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => { if (toast.parentNode) toast.parentNode.removeChild(toast); }, duration);
        }

        function updateReadingTimer() {
            const elapsed = Math.floor((Date.now() - readingStartTime) / 1000);
            const h = Math.floor(elapsed / 3600), m = Math.floor((elapsed % 3600) / 60), s = elapsed % 60;
            const pad = (n) => String(n).padStart(2, '0');
            const el = document.getElementById('readingTimer');
            if (el) el.textContent = `${pad(h)}:${pad(m)}:${pad(s)}`;
        }
        setInterval(updateReadingTimer, 1000);

        function toggleScreenLock() {
            if (screenLocked) { unlockScreen(); }
            else {
                screenLocked = true;
                document.body.classList.add('screen-locked');
                document.getElementById('screenLockOverlay').classList.add('active');
                const lb = document.getElementById('lockBtn');
                if (lb) { lb.textContent = '🔓 فتح الشاشة'; lb.classList.add('active'); }
                const fab = document.getElementById('lockFab');
                if (fab) { fab.textContent = '🔓'; fab.classList.add('locked', 'visible'); }
                const floatBtn = document.createElement('div');
                floatBtn.className = 'screen-lock-float active';
                floatBtn.id = 'screenLockFloat';
                floatBtn.innerHTML = '<span>🔓</span><span>فتح الشاشة</span>';
                floatBtn.onclick = unlockScreen;
                document.body.appendChild(floatBtn);
                showToast('تم قفل الشاشة 🔒', 'info', 2000);
            }
        }
        function unlockScreen() {
            if (!screenLocked) return;
            screenLocked = false;
            document.body.classList.remove('screen-locked');
            document.getElementById('screenLockOverlay').classList.remove('active');
            const lb = document.getElementById('lockBtn');
            if (lb) { lb.textContent = '🔒 قفل الشاشة'; lb.classList.remove('active'); }
            const fab = document.getElementById('lockFab');
            if (fab) { fab.textContent = '🔒'; fab.classList.remove('locked'); }
            const fb = document.getElementById('screenLockFloat'); if (fb) fb.remove();
            showToast('تم فتح الشاشة 🔓', 'info', 1500);
        }
        window.addEventListener('scroll', function() {
            const fab = document.getElementById('lockFab');
            if (!fab) return;
            if (window.scrollY > 200 || screenLocked) fab.classList.add('visible');
            else fab.classList.remove('visible');
        });

        function checkForUpdate() {
            let lv = '';
            try { lv = localStorage.getItem('appVersion') || ''; } catch (e) {}
            if (lv !== APP_VERSION) { setTimeout(() => { openWelcome(); }, 800); return true; }
            return false;
        }
        function openWelcome() { document.getElementById('welcomeOverlay').classList.add('active'); document.body.style.overflow = 'hidden'; }
        function closeWelcome() { document.getElementById('welcomeOverlay').classList.remove('active'); document.body.style.overflow = ''; try { localStorage.setItem('appVersion', APP_VERSION); } catch (e) {} }
        function closeWelcomeOutside(e) { if (e.target.id === 'welcomeOverlay') closeWelcome(); }

        async function requestWakeLock() {
            if (!('wakeLock' in navigator)) return false;
            try { wakeLock = await navigator.wakeLock.request('screen'); return true; } catch (err) { return false; }
        }
        async function toggleWakeLock() {
            if (!('wakeLock' in navigator)) { alert('⚠️ الميزة غير مدعومة.'); return; }
            const btn = document.getElementById('wakeBtn');
            if (wakeLockWanted) {
                wakeLockWanted = false;
                try { localStorage.setItem('wakeLockWanted', 'false'); } catch (e) {}
                if (wakeLock) { try { await wakeLock.release(); } catch (e) {} wakeLock = null; }
                if (btn) { btn.textContent = '☀️ إبقاء الشاشة'; btn.classList.remove('active'); }
                showToast('تم إيقاف إبقاء الشاشة', 'info', 2000);
            } else {
                wakeLockWanted = true;
                try { localStorage.setItem('wakeLockWanted', 'true'); } catch (e) {}
                const ok = await requestWakeLock();
                if (ok) { if (btn) { btn.textContent = '💡 الشاشة مضيئة'; btn.classList.add('active'); } showToast('تم تفعيل إبقاء الشاشة ☀️', 'info', 2000); }
                else { wakeLockWanted = false; try { localStorage.setItem('wakeLockWanted', 'false'); } catch (e) {} alert('❌ تعذّر التفعيل.'); }
            }
        }
        document.addEventListener('visibilitychange', async () => {
            if (document.visibilityState === 'visible' && wakeLockWanted) {
                await requestWakeLock();
                const btn = document.getElementById('wakeBtn');
                if (btn && wakeLock) { btn.textContent = '💡 الشاشة مضيئة'; btn.classList.add('active'); }
            }
        });
        async function initWakeLock() {
            const btn = document.getElementById('wakeBtn');
            if (!('wakeLock' in navigator)) { if (btn) { btn.style.opacity = '0.5'; } return; }
            if (wakeLockWanted) { const ok = await requestWakeLock(); if (ok && btn) { btn.textContent = '💡 الشاشة مضيئة'; btn.classList.add('active'); } }
        }

        function applyBookmarkColor() {
            const c = BOOKMARK_COLORS[bookmarkColorIndex] || BOOKMARK_COLORS[0];
            document.documentElement.style.setProperty('--bookmark-color', c.light);
            document.documentElement.style.setProperty('--bookmark-dark', c.dark);
            try { localStorage.setItem('bookmarkColor', bookmarkColorIndex); } catch (e) {}
        }
        function openColorPicker() {
            const grid = document.getElementById('colorGrid');
            grid.innerHTML = BOOKMARK_COLORS.map((c, i) => `<div class="color-option ${i === bookmarkColorIndex ? 'selected' : ''}" style="background: linear-gradient(180deg, ${c.light}, ${c.dark});" onclick="selectColor(${i})" title="${c.name}"></div>`).join('');
            document.getElementById('colorOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
        }
        function selectColor(i) { bookmarkColorIndex = i; applyBookmarkColor(); closeColorPicker(); }
        function closeColorPicker() { document.getElementById('colorOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function closeColorOutside(e) { if (e.target.id === 'colorOverlay') closeColorPicker(); }
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            const isDark = document.body.classList.contains('dark-mode');
            try { localStorage.setItem('darkMode', isDark); } catch (e) {}
            const btn = document.getElementById('darkModeBtn');
            if (btn) btn.textContent = isDark ? '☀️ نهاري' : '🌙 ليلي';
        }
        function openHelp() { document.getElementById('helpOverlay').classList.add('active'); document.body.style.overflow = 'hidden'; }
        function closeHelp() { document.getElementById('helpOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function closeHelpOutside(e) { if (e.target.id === 'helpOverlay') closeHelp(); }
        function loadBookmark() { try { const s = localStorage.getItem('quranBookmark'); if (s) bookmark = JSON.parse(s); } catch (e) { bookmark = null; } }
        function saveAllBookmarksLocal() { try { localStorage.setItem('allBookmarks', JSON.stringify(allBookmarks)); } catch (e) {} updateBmCount(); }
        function saveAllBookmarks() { saveAllBookmarksLocal(); lastAddTime = Date.now(); syncSpecialBookmarksToServer(); }
        function updateBmCount() { const el = document.getElementById('bmCount'); if (el) el.textContent = allBookmarks.length; }

        function renderResultsPreservingScroll(anchorSurah, anchorAyah) {
            let anchorTop = null;
            if (anchorSurah && anchorAyah) {
                const ae = document.getElementById(`ayah-${anchorSurah}-${anchorAyah}`);
                if (ae) anchorTop = ae.getBoundingClientRect().top;
            }
            const scrollY = window.scrollY;
            focusAyah = null;
            renderResults();
            requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                    if (anchorTop !== null) {
                        const ne = document.getElementById(`ayah-${anchorSurah}-${anchorAyah}`);
                        if (ne) window.scrollBy(0, ne.getBoundingClientRect().top - anchorTop);
                    } else window.scrollTo(0, scrollY);
                });
            });
        }
        function clearBookmark() {
            if (!confirm('حذف علامة آخر قراءة؟')) return;
            bookmark = null;
            try { localStorage.removeItem('quranBookmark'); } catch (e) {}
            try { localStorage.setItem('pendingBookmarkSync', 'true'); } catch (e) {}
            syncDeleteToServer();
            updateBookmarkBar();
            focusAyah = null;
            renderResultsPreservingScroll();
            showToast('تم حذف العلامة', 'warning', 2000);
        }
        // ✅ إصلاح البوك مارك - دالة الحفظ/الحذف
        function toggleBookmark(surah, ayah) {
            const sName = SURAH_NAMES[surah - 1] || '؟';
            if (bookmark && bookmark.surah == surah && bookmark.ayah == ayah) {
                bookmark = null;
                try { localStorage.removeItem('quranBookmark'); } catch (e) {}
                try { localStorage.setItem('pendingBookmarkSync', 'true'); } catch (e) {}
                syncDeleteToServer();
                showToast(`تم إزالة العلامة من سورة ${sName}`, 'warning', 2500);
            } else {
                bookmark = { surah: parseInt(surah), ayah: parseInt(ayah), timestamp: Date.now() };
                try { localStorage.setItem('quranBookmark', JSON.stringify(bookmark)); } catch (e) {}
                try { localStorage.setItem('pendingBookmarkSync', 'true'); } catch (e) {}
                syncBookmarkToServer(parseInt(surah), parseInt(ayah));
                showToast(`تم حفظ آخر قراءة: ${sName} - آية ${ayah}`, 'bookmark', 3000);
            }
            updateBookmarkBar();
            updateProgress();
            renderResultsPreservingScroll(surah, ayah);
        }
        function openLabelDialog(surah, ayah) {
            pendingSurah = surah; pendingAyah = ayah;
            const sName = SURAH_NAMES[surah - 1] || '؟';
            document.getElementById('labelDialogRef').textContent = `📍 سورة ${sName} - آية ${ayah}`;
            document.getElementById('labelInput').value = '';
            const ql = document.getElementById('quickLabels');
            ql.innerHTML = QUICK_LABELS.map(l => `<button onclick="setQuickLabel('${l.replace(/'/g, "\\'")}')">${l}</button>`).join('');
            document.getElementById('labelOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
            setTimeout(() => document.getElementById('labelInput').focus(), 100);
        }
        function setQuickLabel(text) { document.getElementById('labelInput').value = text; }
        function saveLabelBookmark() {
            const label = document.getElementById('labelInput').value.trim();
            if (!label) { alert('❌ أدخل اسماً للعلامة'); return; }
            if (pendingSurah === null || pendingAyah === null) return;
            const aS = pendingSurah, aA = pendingAyah;
            const sName = SURAH_NAMES[aS - 1] || '؟';
            if (allBookmarks.find(b => b.surah === aS && b.ayah === aA && b.label === label)) { if (!confirm('موجودة بالفعل، إضافتها مرة أخرى؟')) return; }
            allBookmarks.push({ id: String(Date.now()) + '_' + Math.random().toString(36).substring(2, 8), label, surah: aS, ayah: aA, created: Date.now() });
            saveAllBookmarks();
            updateProgress();
            closeLabelDialog();
            renderResultsPreservingScroll(aS, aA);
            showToast(`تمت إضافة "${label}" على ${sName}`, 'special', 3500);
        }
        function closeLabelDialog() { document.getElementById('labelOverlay').classList.remove('active'); document.body.style.overflow = ''; pendingSurah = null; pendingAyah = null; }
        function closeLabelOutside(e) { if (e.target.id === 'labelOverlay') closeLabelDialog(); }
        function hasSpecialBookmark(surah, ayah) { return allBookmarks.some(b => b.surah == surah && b.ayah == ayah); }
        function getSpecialLabels(surah, ayah) { return allBookmarks.filter(b => b.surah == surah && b.ayah == ayah).map(b => b.label); }
        function jumpToSpecificBookmark(id) {
            const b = allBookmarks.find(x => String(x.id) === String(id));
            if (!b) return;
            bookmark = { surah: b.surah, ayah: b.ayah, timestamp: Date.now() };
            try { localStorage.setItem('quranBookmark', JSON.stringify(bookmark)); } catch (e) {}
            closeBookmarksList();
            jumpToBookmark();
        }
        function deleteMyBookmark(id) {
            if (!confirm('حذف هذه العلامة؟')) return;
            allBookmarks = allBookmarks.filter(x => String(x.id) !== String(id));
            saveAllBookmarks(); updateProgress(); openBookmarksList();
            showToast('تم حذف العلامة', 'warning', 2000);
        }
        function editMyBookmark(id) {
            const b = allBookmarks.find(x => String(x.id) === String(id));
            if (!b) return;
            const nl = prompt('تعديل اسم العلامة:', b.label);
            if (nl === null || !nl.trim()) return;
            b.label = nl.trim();
            saveAllBookmarks(); openBookmarksList();
            renderResultsPreservingScroll();
        }
        function openBookmarksList() {
            const c = document.getElementById('bookmarksListContainer');
            if (allBookmarks.length === 0) {
                c.innerHTML = `<div style="text-align:center; padding:30px; color:var(--ink-secondary);">📭 لا توجد علامات بعد.<br><br><strong>كيف تضيف؟</strong><br>1. اذهب لأي آية<br>2. اضغط <strong>📌</strong><br>3. اكتب اسماً → حفظ</div>`;
            } else {
                const s = [...allBookmarks].sort((a, b) => a.surah - b.surah || a.ayah - b.ayah);
                c.innerHTML = s.map(b => {
                    const sn = SURAH_NAMES[b.surah - 1] || '؟';
                    return `<div class="bm-item"><div class="bm-item-info"><div class="bm-item-label">📌 ${b.label}</div><div style="font-size:0.8rem; color:var(--ink-secondary);">سورة ${sn} - آية ${b.ayah}</div></div><div class="bm-item-actions"><button class="bm-jump" onclick="jumpToSpecificBookmark('${b.id}')">📖</button><button class="bm-edit" onclick="editMyBookmark('${b.id}')">✏️</button><button class="bm-del" onclick="deleteMyBookmark('${b.id}')">🗑️</button></div></div>`;
                }).join('');
            }
            document.getElementById('bookmarksOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
        }
        function closeBookmarksList() { document.getElementById('bookmarksOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function closeBookmarksOutside(e) { if (e.target.id === 'bookmarksOverlay') closeBookmarksList(); }
        function updateProgress() {
            const u = new Set(allBookmarks.map(b => b.surah));
            if (bookmark) u.add(bookmark.surah);
            let ta = 0;
            u.forEach(sn => { const i = sn - 1; if (i >= 0 && i < SURAH_AYAH_COUNTS.length) ta += SURAH_AYAH_COUNTS[i]; });
            const p = Math.min(100, Math.round((ta / TOTAL_QURAN_AYAHS) * 100));
            const pf = document.getElementById('progressFill'); if (pf) pf.style.width = p + '%';
            const pe = document.getElementById('progressPercent');
            if (!pe) return;
            document.querySelectorAll('.milestone').forEach(m => { const pc = parseInt(m.dataset.pct); if (p >= pc) m.classList.add('reached'); else m.classList.remove('reached'); });
            document.querySelectorAll('.milestone-label').forEach(l => { const pc = parseInt(l.dataset.pct); if (p >= pc) l.classList.add('reached'); else l.classList.remove('reached'); });
            pe.title = `قرأت ${ta} آية من ${TOTAL_QURAN_AYAHS}`;
            if (p >= 100) { pe.textContent = '🏁 ختم'; pe.style.color = '#d4a100'; }
            else if (p >= 75) { pe.textContent = p + '%'; pe.style.color = '#16a34a'; }
            else if (p >= 50) { pe.textContent = p + '%'; pe.style.color = '#0ea5e9'; }
            else if (p >= 25) { pe.textContent = p + '%'; pe.style.color = '#f59e0b'; }
            else { pe.textContent = p + '%'; pe.style.color = ''; }
        }
        function updateBookmarkBar() {
            const bar = document.getElementById('bookmarkBar');
            if (!bar) return;
            if (!bookmark) { bar.style.display = 'none'; return; }
            bar.style.display = 'flex';
            const sn = SURAH_NAMES[bookmark.surah - 1] || 'غير معروفة';
            document.getElementById('bookmarkLocation').textContent = `سورة ${sn} - آية ${bookmark.ayah}`;
        }
        function updateJumpBtnText() {
            const btn = document.getElementById('jumpBtn');
            const hm = document.getElementById('hereMsg');
            if (!btn || !bookmark) { if (hm) hm.style.display = 'none'; return; }
            const el = document.getElementById(`ayah-${bookmark.surah}-${bookmark.ayah}`);
            if (!el) { btn.textContent = '📖 العلامة المحفوظة'; btn.classList.remove('at-location'); if (hm) hm.style.display = 'none'; return; }
            const r = el.getBoundingClientRect();
            const inView = r.top < (window.innerHeight * 0.85) && r.bottom > (window.innerHeight * 0.15);
            if (inView) { btn.textContent = '📖 العودة'; btn.classList.add('at-location'); if (hm) hm.style.display = 'inline-block'; }
            else { btn.textContent = '📖 العلامة المحفوظة'; btn.classList.remove('at-location'); if (hm) hm.style.display = 'none'; }
        }
        function jumpToBookmark() {
            if (!bookmark) return;
            document.getElementById('sourceSelect').value = 'quran';
            document.getElementById('surahSelect').value = bookmark.surah;
            updateAyahDropdown(bookmark.surah, 'all');
            document.getElementById('ayahSelect').value = 'all';
            document.getElementById('searchInput').value = '';
            currentSource = 'quran'; currentSurah = String(bookmark.surah); currentAyah = 'all'; currentKeyword = '';
            focusAyah = bookmark.ayah;
            let source = quranData.filter(a => a.surah == bookmark.surah);
            const index = source.findIndex(a => a.ayah == bookmark.ayah);
            currentPage = index >= 0 ? Math.floor(index / perPage) + 1 : 1;
            renderResults();
        }
        function isBookmarked(surah, ayah) { return bookmark && bookmark.surah == surah && bookmark.ayah == ayah; }
        function removeTashkeel(text) {
            if (!text) return '';
            return text.replace(/[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D3-\u08E1\u08E3-\u08FF]/g, '').replace(/\u0640/g, '').replace(/[\u0622\u0623\u0625\u0671]/g, '\u0627').replace(/\u0649/g, '\u064A').replace(/\u0624/g, '\u0648').replace(/\u0629/g, '\u0647').replace(/[﴿﴾۝۞۩]/g, '');
        }
        function normalizeSearch(text) { return text ? removeTashkeel(text).replace(/\s+/g, ' ').trim() : ''; }
        function isArabicLetter(c) { if (!c) return false; return /[\u0621-\u063A\u0641-\u064A]/.test(c); }
        function findKeywordPosition(text, keyword) {
            if (!keyword || !text) return null;
            const ck = removeTashkeel(keyword);
            if (!ck) return null;
            const positions = [];
            let ct = '';
            for (let i = 0; i < text.length; i++) {
                const c = removeTashkeel(text[i]);
                if (c.length > 0) for (let j = 0; j < c.length; j++) { positions.push(i); ct += c[j]; }
            }
            const isShort = ck.length <= 3;
            let idx = ct.indexOf(ck);
            while (idx !== -1) {
                if (isShort) {
                    const before = idx === 0 ? '' : ct[idx - 1];
                    const after = (idx + ck.length) >= ct.length ? '' : ct[idx + ck.length];
                    if (!isArabicLetter(before) && !isArabicLetter(after)) return { start: positions[idx], end: positions[idx + ck.length - 1] + 1 };
                } else return { start: positions[idx], end: positions[idx + ck.length - 1] + 1 };
                idx = ct.indexOf(ck, idx + 1);
            }
            return null;
        }
        function searchMatch(text, keyword) { if (!keyword) return true; return findKeywordPosition(text, keyword) !== null; }
        function highlight(text, keyword) {
            if (!keyword || !text) return text;
            const m = findKeywordPosition(text, keyword);
            if (!m) return text;
            return text.substring(0, m.start) + '<mark>' + text.substring(m.start, m.end) + '</mark>' + text.substring(m.end);
        }
        function findSurahByName(kw) {
            if (!kw) return null;
            const ck = normalizeSearch(kw);
            if (!ck || ck.length < 2) return null;
            for (let i = 0; i < SURAH_NAMES.length; i++) if (normalizeSearch(SURAH_NAMES[i]) === ck) return i + 1;
            if (ck.length >= 3) for (let i = 0; i < SURAH_NAMES.length; i++) if (normalizeSearch(SURAH_NAMES[i]).includes(ck)) return i + 1;
            return null;
        }
        function populateSurahSelect() {
            const sel = document.getElementById('surahSelect');
            SURAH_NAMES.forEach((n, i) => { const o = document.createElement('option'); o.value = i + 1; o.textContent = `${i + 1}. ${n}`; sel.appendChild(o); });
        }
        function updateAyahDropdown(sn, ka) {
            const as = document.getElementById('ayahSelect');
            as.innerHTML = '<option value="all">كل الآيات</option>';
            if (!sn || sn === 'all') return;
            const s = parseInt(sn);
            quranData.filter(a => a.surah === s).forEach(a => { const o = document.createElement('option'); o.value = a.ayah; o.textContent = `آية ${a.ayah}`; as.appendChild(o); });
            if (ka) as.value = ka;
        }
        function populateSidebar() {
            document.getElementById('sidebarList').innerHTML = SURAH_NAMES.map((n, i) => `<div class="surah-nav-item" onclick="jumpToSurah(${i + 1})"><span class="num">${i + 1}</span><span>${n}</span></div>`).join('');
        }
        function jumpToSurah(num) {
            closeSidebar();
            document.getElementById('sourceSelect').value = 'quran';
            document.getElementById('surahSelect').value = num;
            document.getElementById('searchInput').value = '';
            updateAyahDropdown(num, 'all');
            currentSource = 'quran'; currentSurah = String(num); currentAyah = 'all'; currentKeyword = ''; currentPage = 1;
            focusAyah = null;
            renderResults();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        function showFullSurah(surah, ayah) {
            focusAyah = ayah;
            currentSource = 'quran'; currentSurah = String(surah); currentAyah = 'all'; currentKeyword = '';
            document.getElementById('searchInput').value = '';
            document.getElementById('sourceSelect').value = 'quran';
            document.getElementById('surahSelect').value = surah;
            updateAyahDropdown(surah, 'all');
            document.getElementById('ayahSelect').value = 'all';
            let source = quranData.filter(a => a.surah == surah);
            const index = source.findIndex(a => a.ayah === ayah);
            currentPage = index >= 0 ? Math.floor(index / perPage) + 1 : 1;
            renderResults();
        }
        function openSidebar() { document.getElementById('sidebar').classList.add('active'); document.getElementById('sidebarOverlay').classList.add('active'); document.body.style.overflow = 'hidden'; }
        function closeSidebar() { document.getElementById('sidebar').classList.remove('active'); document.getElementById('sidebarOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function initTafsirToggle() {
            const t = document.getElementById('showTafsirToggle');
            const h = document.getElementById('toggleHint');
            t.checked = showTafsir;
            uh();
            t.addEventListener('change', () => { showTafsir = t.checked; try { localStorage.setItem('showTafsir', showTafsir); } catch (e) {} uh(); renderResultsPreservingScroll(); });
            function uh() { h.textContent = showTafsir ? '(ظاهرة)' : '(مخفية)'; h.style.color = showTafsir ? '#16a34a' : 'var(--gold)'; }
        }
        async function loadTafsirFile(config) {
            try {
                const res = await fetch(config.file);
                if (!res.ok) { allTafsirs[config.key] = { label: config.label, icon: config.icon, ayahs: [] }; return; }
                const text = await res.text();
                if (text.startsWith('SQLite') || text.startsWith('<!DOCTYPE') || text.startsWith('<html')) { allTafsirs[config.key] = { label: config.label, icon: config.icon, ayahs: [] }; return; }
                let raw;
                try { raw = JSON.parse(text); } catch (e) { allTafsirs[config.key] = { label: config.label, icon: config.icon, ayahs: [] }; return; }
                let ayahs = [];
                if (Array.isArray(raw)) ayahs = raw.map(a => ({ surah: parseInt(a.surah || a.sura || 1), number: parseInt(a.number || a.ayah || a.numberInSurah || a.id || 1), text: a.text || a.tafsir || a.content || '' }));
                else if (raw && raw.ayahs && Array.isArray(raw.ayahs)) ayahs = raw.ayahs.map(a => ({ surah: parseInt(a.surah || a.sura || 1), number: parseInt(a.number || a.ayah || 1), text: a.text || a.tafsir || a.content || '' }));
                else if (raw && typeof raw === 'object') ayahs = Object.keys(raw).map(key => {
                    if (!key.includes(':')) return null;
                    const p = key.split(':'); if (p.length !== 2) return null;
                    const s = parseInt(p[0]), n = parseInt(p[1]);
                    if (isNaN(s) || isNaN(n)) return null;
                    const item = raw[key]; let t = '';
                    if (typeof item === 'string') t = item;
                    else if (item && typeof item === 'object') t = item.text || item.tafsir || item.content || '';
                    t = t.replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/\s+/g, ' ').trim();
                    return { surah: s, number: n, text: t };
                }).filter(a => a && a.text && a.text.length > 0);
                allTafsirs[config.key] = { label: config.label, icon: config.icon, ayahs };
            } catch (e) { allTafsirs[config.key] = { label: config.label, icon: config.icon, ayahs: [] }; }
        }
        async function loadData() {
            try {
                const r = await fetch('quran.json');
                const raw = await r.json();
                if (Array.isArray(raw) && raw.length > 0 && raw[0].verses) { quranData = []; raw.forEach(s => (s.verses || []).forEach(v => quranData.push({ surah: s.id, ayah: v.id, text: v.text }))); }
                else if (Array.isArray(raw)) quranData = raw.map(a => ({ surah: parseInt(a.surah || 1), ayah: parseInt(a.ayah || a.number || 1), text: a.text || '' }));
                await Promise.all(TAFSIR_FILES.map(loadTafsirFile));
                const tt = Object.values(allTafsirs).reduce((s, t) => s + t.ayahs.length, 0);
                document.getElementById('resultsInfo').textContent = `📖 ${quranData.length} آية | 📚 ${tt} مدخل تفسيري`;
                updateBookmarkBar(); updateProgress(); updateBmCount(); renderResults();
            } catch (err) { document.getElementById('resultsInfo').innerHTML = '❌ <span style="color:#8B4513">تعذر تحميل البيانات: ' + err.message + '</span>'; }
        }
        function searchInSingleTafsir(k, kw, surah) {
            const res = [];
            const t = allTafsirs[k];
            if (!t || t.ayahs.length === 0) return res;
            t.ayahs.forEach(a => { if (surah !== 'all' && a.surah != surah) return; if (kw && !searchMatch(a.text, kw)) return; res.push({ tafsirKey: k, tafsirLabel: t.label, tafsirIcon: t.icon, surah: a.surah, number: a.number, text: a.text }); });
            return res;
        }
        function searchInAllTafsirs(kw, s) { const r = []; Object.keys(allTafsirs).forEach(k => r.push(...searchInSingleTafsir(k, kw, s))); return r; }
        function performSearch() {
            currentKeyword = document.getElementById('searchInput').value.trim();
            currentSource = document.getElementById('sourceSelect').value;
            currentSurah = document.getElementById('surahSelect').value;
            const sa = document.getElementById('ayahSelect').value;
            if (currentSource === 'quran' && currentSurah !== 'all' && sa !== 'all') {
                focusAyah = parseInt(sa); currentAyah = 'all';
                let source = quranData.filter(a => a.surah == parseInt(currentSurah));
                const index = source.findIndex(a => a.ayah === focusAyah);
                currentPage = index >= 0 ? Math.floor(index / perPage) + 1 : 1;
            } else { focusAyah = null; currentAyah = sa; currentPage = 1; }
            renderResults();
        }
        function renderSurahSuggestion() {
            const c = document.getElementById('surahSuggestionContainer');
            c.innerHTML = '';
            if (currentSource !== 'quran' || !currentKeyword || currentSurah !== 'all') return;
            const sn = findSurahByName(currentKeyword);
            if (!sn) return;
            const s = SURAH_NAMES[sn - 1];
            c.innerHTML = `<div class="surah-suggestion"><span style="font-size:1rem; font-weight:700;">📖 عرض <strong>سورة ${s}</strong> كاملة؟</span><button onclick="jumpToSurah(${sn})">⚡ عرض السورة</button></div>`;
        }
        function attachTapHighlight() {
            document.querySelectorAll('.ayah-card').forEach(card => {
                card.addEventListener('click', function(e) {
                    if (e.target.tagName === 'BUTTON' || e.target.closest('button')) return;
                    if (screenLocked) return;
                    this.classList.add('temp-highlight');
                    setTimeout(() => this.classList.remove('temp-highlight'), 1500);
                });
            });
        }
        function renderResults() {
            const c = document.getElementById('resultsContainer');
            const pe = document.getElementById('pagination');
            const ie = document.getElementById('resultsInfo');
            const tb = document.getElementById('tafsirToggleBar');
            let items = [], isTafsir = false;
            const isSearchMode = (currentKeyword && currentKeyword.length > 0) || (currentAyah !== 'all');
            if (currentSource === 'quran') {
                let s = quranData;
                if (currentSurah !== 'all') { const x = parseInt(currentSurah); s = s.filter(a => a.surah == x); }
                if (currentAyah !== 'all') { const x = parseInt(currentAyah); s = s.filter(a => a.ayah == x); }
                if (currentKeyword) s = s.filter(a => searchMatch(a.text, currentKeyword));
                items = s;
            } else if (currentSource === 'all_tafsirs') { isTafsir = true; items = searchInAllTafsirs(currentKeyword, currentSurah); }
            else { isTafsir = true; const k = currentSource.replace('tafsir_', ''); items = searchInSingleTafsir(k, currentKeyword, currentSurah); }
            tb.style.display = currentSource === 'quran' ? 'flex' : 'none';
            const tp = Math.max(1, Math.ceil(items.length / perPage));
            if (currentPage > tp) currentPage = tp;
            const paginated = items.slice((currentPage - 1) * perPage, currentPage * perPage);
            ie.textContent = `📊 ${items.length} نتيجة | صفحة ${currentPage}/${tp}`;
            renderSurahSuggestion();
            if (paginated.length === 0) { c.innerHTML = '<div class="empty-msg">📭 لا توجد نتائج مطابقة</div>'; pe.innerHTML = ''; setTimeout(updateJumpBtnText, 100); return; }
            if (isTafsir) {
                c.innerHTML = paginated.map(i => { const sn = SURAH_NAMES[i.surah - 1] || '؟'; return `<div class="ayah-card"><div class="ayah-header"><span class="ayah-ref">${i.tafsirIcon} ${i.tafsirLabel} - ${sn} - آية ${i.number}</span><span class="ayah-type">تفسير</span></div><div class="tafsir-text">${highlight(i.text, currentKeyword)}</div></div>`; }).join('');
            } else {
                c.innerHTML = paginated.map(item => {
                    const sn = SURAH_NAMES[item.surah - 1] || '؟';
                    const at = highlight(item.text, currentKeyword);
                    const marked = isBookmarked(item.surah, item.ayah);
                    const hs = hasSpecialBookmark(item.surah, item.ayah);
                    const sl = getSpecialLabels(item.surah, item.ayah);
                    let tB = '', cB = '';
                    if (showTafsir) {
                        let cf = 0;
                        TAFSIR_FILES.forEach(cfg => { const t = allTafsirs[cfg.key]; if (!t || t.ayahs.length === 0) return; const m = t.ayahs.find(x => x.surah == item.surah && x.number == item.ayah); if (m && m.text) { cf++; tB += `<div class="tafsir-block"><h4>${t.icon} ${t.label}</h4><div class="tafsir-text">${highlight(m.text, currentKeyword)}</div></div>`; } });
                        if (cf > 0) cB = `<span class="tafsir-count">📚 ${cf}</span>`;
                    }
                    const bR = marked ? `<div class="bookmark-ribbon">🔖 آخر قراءة</div>` : '';
                    const sR = hs ? `<div class="special-ribbon">📌 ${sl.join(' · ')}</div>` : '';
                    const scB = isSearchMode ? `<button class="show-context-btn" onclick="showFullSurah(${item.surah}, ${item.ayah})">📖 عرض</button>` : '';
                    return `<div class="ayah-card ${marked ? 'bookmarked' : ''}" id="ayah-${item.surah}-${item.ayah}">${bR}${sR}<div class="ayah-header"><span class="ayah-ref">سورة ${sn} - آية ${item.ayah}</span><div class="ayah-header-right">${cB}${scB}<span class="ayah-type">آية</span><div class="ayah-btns"><button class="special-btn ${hs ? 'has-special' : ''}" onclick="openLabelDialog(${item.surah}, ${item.ayah})">📌</button><button class="bookmark-btn ${marked ? 'active' : ''}" onclick="toggleBookmark(${item.surah}, ${item.ayah})">🔖</button></div></div></div><div class="ayah-text">${at}</div>${tB}</div>`;
                }).join('');
            }
            let ph = '';
            if (tp > 1) {
                if (currentPage > 1) ph += `<a data-page="${currentPage - 1}">⬅ السابق</a>`;
                for (let i = Math.max(1, currentPage - 2); i <= Math.min(tp, currentPage + 2); i++) ph += (i === currentPage) ? `<span class="current">${i}</span>` : `<a data-page="${i}">${i}</a>`;
                if (currentPage < tp) ph += `<a data-page="${currentPage + 1}">التالي ➡</a>`;
            }
            pe.innerHTML = ph;
            pe.querySelectorAll('a[data-page]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); currentPage = parseInt(a.dataset.page); focusAyah = null; renderResults(); window.scrollTo({ top: 0, behavior: 'smooth' }); }));
            if (focusAyah && currentSurah !== 'all') { setTimeout(() => { const el = document.getElementById(`ayah-${currentSurah}-${focusAyah}`); if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'center' }); el.classList.add('focused'); setTimeout(() => el.classList.remove('focused'), 3000); } }, 400); }
            setTimeout(() => { updateJumpBtnText(); attachTapHighlight(); }, 100);
        }
        function openAbout() { document.getElementById('aboutOverlay').classList.add('active'); document.body.style.overflow = 'hidden'; }
        function closeAbout() { document.getElementById('aboutOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function closeAboutOutside(e) { if (e.target.id === 'aboutOverlay') closeAbout(); }
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { closeAbout(); closeSync(); closeColorPicker(); closeBookmarksList(); closeSidebar(); closeLabelDialog(); closeHelp(); closeWelcome(); closePrayer(); } });

        function generateSyncCode() { const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; let c = ''; const arr = new Uint32Array(12); crypto.getRandomValues(arr); for (let i = 0; i < 12; i++) c += chars[arr[i] % chars.length]; return c; }
        function getSyncCode() { let c = ''; try { c = localStorage.getItem('syncCode') || ''; } catch (e) {} if (!c || c.length < 8) { c = generateSyncCode(); try { localStorage.setItem('syncCode', c); } catch (e) {} } return c; }

        // ✅ إصلاح البوك مارك - حفظ مع علامة "pending"
        async function syncBookmarkToServer(surah, ayah) {
            const code = getSyncCode(); if (!code) return;
            try {
                const res = await fetch('/api/sync_bookmark', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ sync_code: code, surah, ayah })
                });
                if (res.ok) {
                    try { localStorage.removeItem('pendingBookmarkSync'); } catch (e) {}
                }
            } catch (e) {}
        }
        // ✅ إصلاح البوك مارك - الحذف
        async function syncDeleteToServer() {
            const code = getSyncCode(); if (!code) return;
            try {
                const res = await fetch('/api/delete_bookmark', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ sync_code: code })
                });
                if (res.ok) {
                    try { localStorage.removeItem('pendingBookmarkSync'); } catch (e) {}
                }
            } catch (e) {}
        }
        // ✅ إصلاح البوك مارك - لا يستبدل المحلي إذا كان هناك pending
        async function loadBookmarkFromServer(silent) {
            const code = getSyncCode(); if (!code) return;

            let hasPending = false;
            try { hasPending = localStorage.getItem('pendingBookmarkSync') === 'true'; } catch (e) {}

            if (hasPending && bookmark) {
                await syncBookmarkToServer(bookmark.surah, bookmark.ayah);
                return;
            }

            try {
                const res = await fetch(`/api/get_bookmark/${code}`);
                const data = await res.json();
                if (data.status === 'success') {
                    if (!bookmark || bookmark.surah != data.surah || bookmark.ayah != data.ayah) {
                        bookmark = { surah: data.surah, ayah: data.ayah, timestamp: Date.now() };
                        try { localStorage.setItem('quranBookmark', JSON.stringify(bookmark)); } catch (e) {}
                        updateBookmarkBar(); updateProgress();
                        if (!silent) renderResultsPreservingScroll();
                    }
                } else if (data.status === 'empty' && bookmark) {
                    syncBookmarkToServer(bookmark.surah, bookmark.ayah);
                }
            } catch (e) {}
        }
        async function syncSpecialBookmarksToServer() {
            if (!serverSyncEnabled || isSyncingToServer) return;
            const code = getSyncCode(); if (!code) return;
            isSyncingToServer = true;
            try { await fetch('/api/special_bookmarks', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ sync_code: code, bookmarks: allBookmarks }) }); } catch (e) {} finally { isSyncingToServer = false; }
        }
        async function loadSpecialBookmarksFromServer(silent) {
            const code = getSyncCode(); if (!code) return;
            if (Date.now() - lastAddTime < 8000) return;
            if (isSyncingToServer) return;
            try {
                const res = await fetch(`/api/special_bookmarks/${code}`);
                const data = await res.json();
                if (data.status !== 'success') return;
                const sb = (data.bookmarks || []).map(b => ({ id: String(b.id), label: b.label, surah: parseInt(b.surah), ayah: parseInt(b.ayah) }));
                if (allBookmarks.length === 0 && sb.length > 0) { allBookmarks = sb; saveAllBookmarksLocal(); updateProgress(); if (!silent) renderResultsPreservingScroll(); return; }
                if (sb.length === 0 && allBookmarks.length > 0) { await syncSpecialBookmarksToServer(); return; }
                const li = new Set(allBookmarks.map(b => String(b.id)));
                const nf = sb.filter(b => !li.has(String(b.id)));
                if (nf.length > 0) { allBookmarks = [...allBookmarks, ...nf]; saveAllBookmarksLocal(); updateProgress(); if (!silent) renderResultsPreservingScroll(); }
            } catch (e) {}
        }
        function startSync() { getSyncCode(); loadBookmarkFromServer(true); loadSpecialBookmarksFromServer(true); setInterval(() => { loadBookmarkFromServer(false); loadSpecialBookmarksFromServer(false); }, 15000); }
        function openSync() { document.getElementById('syncOverlay').classList.add('active'); document.body.style.overflow = 'hidden'; document.getElementById('syncCodeDisplay').value = getSyncCode(); document.getElementById('syncCodeInput').value = ''; }
        function closeSync() { document.getElementById('syncOverlay').classList.remove('active'); document.body.style.overflow = ''; }
        function closeSyncOutside(e) { if (e.target.id === 'syncOverlay') closeSync(); }
        function copySyncCode() { const c = getSyncCode(); navigator.clipboard.writeText(c).then(() => alert('✅ تم النسخ:\n' + c)).catch(() => { document.getElementById('syncCodeDisplay').select(); document.execCommand('copy'); alert('✅ تم النسخ: ' + c); }); }
        async function linkToSyncCode() {
            const input = document.getElementById('syncCodeInput');
            const code = (input.value || '').trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
            if (!code || code.length < 8) { alert('❌ الرمز قصير'); return; }
            try { localStorage.setItem('syncCode', code); } catch (e) {}
            document.getElementById('syncCodeDisplay').value = code;
            input.value = '';
            alert('✅ تم الربط: ' + code);
            await loadBookmarkFromServer(false);
            try {
                const res = await fetch(`/api/special_bookmarks/${code}`);
                const data = await res.json();
                if (data.status === 'success' && data.bookmarks && data.bookmarks.length > 0) {
                    const sb = data.bookmarks.map(b => ({ id: String(b.id), label: b.label, surah: parseInt(b.surah), ayah: parseInt(b.ayah) }));
                    const li = new Set(allBookmarks.map(b => String(b.id)));
                    const no = sb.filter(b => !li.has(String(b.id)));
                    if (no.length > 0) { allBookmarks = [...allBookmarks, ...no]; saveAllBookmarksLocal(); updateProgress(); renderResultsPreservingScroll(); }
                }
            } catch (e) {}
        }

        function openPrayer() {
            document.getElementById('prayerOverlay').classList.add('active');
            document.body.style.overflow = 'hidden';
            if (userLocation) {
                if (document.getElementById('content-times').classList.contains('active')) loadPrayerTimes();
                if (document.getElementById('content-qibla').classList.contains('active')) calcQibla();
            }
        }
        function closePrayer() { document.getElementById('prayerOverlay').classList.remove('active'); document.body.style.overflow = ''; if (prayerInterval) { clearInterval(prayerInterval); prayerInterval = null; } }
        function closePrayerOutside(e) { if (e.target.id === 'prayerOverlay') closePrayer(); }
        function showPrayerTab(tab) {
            document.querySelectorAll('.prayer-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.prayer-content').forEach(c => c.classList.remove('active'));
            document.getElementById('tab-' + tab).classList.add('active');
            document.getElementById('content-' + tab).classList.add('active');
            if (tab === 'qibla') { if (!userLocation) requestLocation(); else calcQibla(); }
            if (tab === 'times') { if (!userLocation) requestLocation(); else loadPrayerTimes(); }
        }
        function requestLocation() {
            const c = document.getElementById('prayerTimesContainer');
            const s = document.getElementById('qiblaStatus');
            if (!navigator.geolocation) { alert('⚠️ متصفحك لا يدعم الموقع.'); return; }
            if (c) c.innerHTML = '<div style="text-align:center; padding:30px;"><div style="font-size:2rem;">⏳</div><p>جاري تحديد موقعك...</p></div>';
            if (s) s.textContent = '⏳ جاري تحديد موقعك...';
            navigator.geolocation.getCurrentPosition(
                function(p) { userLocation = { lat: p.coords.latitude, lng: p.coords.longitude }; try { localStorage.setItem('userLocation', JSON.stringify(userLocation)); } catch (e) {} loadPrayerTimes(); calcQibla(); },
                function(err) {
                    let m = '⚠️ تعذّر تحديد موقعك.';
                    if (err.code === 1) m = '⚠️ رفضت إذن الموقع.';
                    else if (err.code === 2) m = '⚠️ الموقع غير متاح.';
                    else if (err.code === 3) m = '⚠️ انتهت المدة.';
                    if (c) c.innerHTML = `<div style="text-align:center; padding:30px;"><div style="font-size:2rem;">❌</div><p>${m}</p><button class="prayer-location-btn" onclick="requestLocation()" style="margin-top:15px;">🔄 إعادة المحاولة</button></div>`;
                    if (s)
