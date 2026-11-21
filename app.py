<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>الموسوعة القرآنية</title>
<!-- [تعديل 1] إضافة خط Amiri Quran لوضوح التنوين -->
<!-- [إصلاح 1] إضافة خط Amiri Quran لوضوح التنوين -->
<link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri:wght@400;700&family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
@@ -97,7 +97,7 @@
.btn-icon{background:rgba(255,248,220,.7);border:1px solid var(--bd);color:var(--ink2);width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:1.1rem;display:flex;align-items:center;justify-content:center;padding:0;line-height:1}
.bm-btn.active{background:linear-gradient(180deg,var(--bm),var(--bmD));color:#fff}
.sp-btn.has{background:linear-gradient(180deg,var(--sp),var(--spD));color:#fff}
/* [تعديل 2] وضوح التنوين وخط الآيات */
/* [إصلاح 2] وضوح التنوين وخط الآيات */
.ayah-text{font-family:'Amiri Quran', 'Amiri', serif;font-size:1.8rem;line-height:2.8;text-align:justify;margin-bottom:12px;letter-spacing:0.5px}
.tafsir-block{background:var(--hl);border-right:3px solid var(--gold);border-radius:6px;padding:12px 16px;margin-top:10px}
.tafsir-block h4{font-size:.9rem;font-weight:700;color:var(--gold);margin-bottom:6px}
@@ -210,160 +210,7 @@
.guide ol{list-style:none;padding:0}
.guide ol li{padding:10px 14px;margin-bottom:6px;background:var(--hl);border-radius:8px;border-right:3px solid var(--goldL);font-size:.9rem;line-height:1.7}
.guide ol li strong{color:var(--gold)}
.guide-note{background:rgba(16,185,129,.1);border:1px dashed #10b981;padding:10px 14px;border-radius:8px;margin-top:10px;font-size:.85rem;color:#065f46}
.help-step{display:flex;gap:14px;padding:14px 16px;background:var(--in);border-radius:10px;margin-bottom:12px;border-right:4px solid var(--gold)}
.help-ic{width:50px;height:50px;border-radius:50%;background:linear-gradient(180deg,var(--goldL),var(--gold));color:#fff;display:flex;align-items:center;justify-content:center;font-size:1.5rem;flex-shrink:0}
.help-t{font-weight:700;font-size:1rem;margin-bottom:4px}
.help-d{color:var(--ink2);font-size:.9rem;line-height:1.7}
.help-d code{background:var(--hl);padding:1px 6px;border-radius:4px;color:var(--bm);font-weight:700}
.help-sec{font-family:'Amiri',serif;font-size:1.3rem;color:var(--gold);margin:20px 0 12px;padding:8px 14px;background:var(--hl);border-radius:8px;text-align:center}
.about-new{background:linear-gradient(180deg,#2d3a2d 0%,#1e2a1e 100%)!important;border:3px solid #D4AF37!important;color:#fff!important;max-width:500px!important;border-radius:24px!important;padding:30px 25px!important}
.about-new .about-close-red{position:absolute;top:15px;left:15px;width:44px;height:44px;border-radius:50%;background:#dc2626;color:#fff;border:3px solid #fff;cursor:pointer;font-size:1.4rem;font-weight:700;display:flex;align-items:center;justify-content:center;z-index:10;box-shadow:0 3px 10px rgba(220,38,38,.5)}
.about-new .about-close-red:hover{background:#b91c1c;transform:scale(1.05)}
.about-new .about-title{text-align:center;font-family:'Amiri',serif;font-size:1.8rem;color:#D4AF37;margin:10px 0 20px;padding-bottom:20px;border-bottom:2px solid #D4AF37}
.about-new .info-box{background:linear-gradient(180deg,#3a5236 0%,#2d4229 100%);border-radius:16px;padding:20px 18px;margin-bottom:20px;box-shadow:inset 0 2px 8px rgba(0,0,0,.3)}
.about-new .info-name{text-align:center;font-family:'Amiri',serif;font-size:1.5rem;color:#D4AF37;font-weight:700;margin-bottom:18px;padding-bottom:15px;border-bottom:1px dashed rgba(212,175,55,.4)}
.about-new .info-row{display:flex;align-items:center;justify-content:space-between;background:rgba(255,255,255,.06);padding:12px 18px;border-radius:12px;margin-bottom:10px;color:#E8DFC8;font-size:1.05rem;text-decoration:none;transition:.2s;border:1px solid rgba(212,175,55,.2)}
.about-new .info-row:hover{background:rgba(255,255,255,.12);transform:translateX(-3px)}
.about-new .info-row .icon{font-size:1.3rem;margin-right:8px}
.about-new .info-row .value{font-family:'Courier New',monospace;direction:ltr;flex:1;text-align:center;letter-spacing:.5px}
.about-new .whatsapp-row{background:linear-gradient(180deg,#25D366,#128C7E)!important;color:#fff!important;border:none!important;font-weight:700;justify-content:center}
.about-new .whatsapp-row:hover{background:linear-gradient(180deg,#128C7E,#075E54)!important;transform:scale(1.02)}
.about-new .share-box{background:linear-gradient(180deg,#d4e8d0 0%,#b8d4b4 100%);border-radius:16px;padding:18px;text-align:center;border:2px solid #D4AF37}
.about-new .share-title{font-family:'Amiri',serif;font-size:1.2rem;color:#1e2a1e;font-weight:700;margin-bottom:6px}
.about-new .share-subtitle{font-size:.9rem;color:#3a5236;font-family:'Amiri',serif}
.about-new .share-buttons{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:15px 0}
.about-new .share-btn{padding:12px 8px;border-radius:10px;border:none;color:#fff;font-family:'Cairo',sans-serif;font-weight:700;font-size:.8rem;cursor:pointer;text-align:center;display:flex;flex-direction:column;align-items:center;gap:4px;transition:.2s;text-decoration:none}
.about-new .share-btn:hover{transform:translateY(-2px);box-shadow:0 4px 10px rgba(0,0,0,.3)}
.about-new .share-btn .ico{font-size:1.4rem}
.about-new .sb-whatsapp{background:linear-gradient(180deg,#25D366,#128C7E)}
.about-new .sb-telegram{background:linear-gradient(180deg,#2AABEE,#229ED9)}
.about-new .sb-facebook{background:linear-gradient(180deg,#1877F2,#0C5DC7)}
.about-new .sb-twitter{background:linear-gradient(180deg,#1DA1F2,#0C85D0)}
.about-new .sb-email{background:linear-gradient(180deg,#EA4335,#C5221F)}
.about-new .sb-copy{background:linear-gradient(180deg,#6B7280,#374151)}
.about-new .share-url{background:#fff;border-radius:8px;padding:10px 14px;font-family:'Courier New',monospace;font-size:.85rem;color:#1e2a1e;text-align:center;direction:ltr;margin-top:10px;border:2px solid #D4AF37;word-break:break-all}
.about-new .share-note{text-align:center;font-family:'Amiri',serif;font-size:.9rem;color:#3a5236;margin-top:10px}
.note-item{display:flex;justify-content:space-between;align-items:flex-start;gap:8px;padding:12px 14px;background:var(--in);border:1px solid var(--bd);border-radius:10px;margin-bottom:8px;border-right:4px solid #f472b6}
.note-item .txt{flex:1;font-size:.95rem;line-height:1.7;white-space:pre-wrap;word-break:break-word}
.note-item .date{font-size:.75rem;color:var(--ink2);margin-top:4px}
.note-item .del{background:rgba(220,38,38,.85);color:#fff;border:none;padding:6px 10px;border-radius:6px;cursor:pointer;font-weight:700}
.time-display{background:var(--hl);border:2px dashed var(--gold);border-radius:15px;padding:20px;margin-bottom:15px}
.time-big{font-size:3rem;font-family:'Courier New',monospace;font-weight:700;color:var(--gold);margin:10px 0}
.time-sec{font-size:2rem;color:var(--ink2)}
.date-box{background:var(--in);border-radius:10px;padding:15px;margin-top:12px;border-right:4px solid var(--gold)}
.date-box .lbl{font-size:.85rem;color:var(--ink2);font-weight:700;margin-bottom:6px}
.date-box .val{font-size:1.1rem;font-weight:700;color:var(--gold);font-family:'Amiri',serif}
.date-box .num{font-size:.9rem;color:var(--ink2);margin-top:4px}
.tasbih-body{text-align:center;padding:20px 10px}
.tasbih-dhikr{font-family:'Amiri',serif;font-size:2rem;color:var(--gold);margin-bottom:8px;line-height:1.6}
.tasbih-fadl{font-size:.85rem;color:var(--ink2);font-style:italic;margin-bottom:20px}
.tasbih-counter{position:relative;width:220px;height:220px;margin:20px auto;border-radius:50%;background:radial-gradient(circle,var(--hl),var(--in));border:5px solid var(--gold);display:flex;align-items:center;justify-content:center;cursor:pointer;user-select:none;box-shadow:0 8px 30px rgba(184,134,11,.3);transition:.15s}
.tasbih-counter:active{transform:scale(.96)}
.tasbih-counter.pulse{animation:tasbihPulse .3s}
@keyframes tasbihPulse{0%{transform:scale(1)}50%{transform:scale(1.05)}100%{transform:scale(1)}}
.tasbih-num{font-family:'Amiri',serif;font-size:4.5rem;font-weight:700;color:var(--gold);line-height:1}
.tasbih-target{font-size:.85rem;color:var(--ink2);margin-top:5px}
.tasbih-progress{width:200px;height:8px;background:rgba(0,0,0,.1);border-radius:10px;margin:15px auto;overflow:hidden;border:1px solid var(--bd)}
.tasbih-fill{height:100%;background:linear-gradient(90deg,var(--goldL),var(--gold));width:0;transition:width .3s;border-radius:10px}
.tasbih-actions{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:15px}
.tasbih-actions button{padding:10px 18px;border:none;border-radius:20px;font-family:'Cairo',sans-serif;font-weight:700;font-size:.9rem;cursor:pointer}
.tasbih-reset{background:linear-gradient(180deg,#ef4444,#b91c1c);color:#fff}
.tasbih-switch{background:linear-gradient(180deg,#3b82f6,#1d4ed8);color:#fff}
.tasbih-dhikr-tabs{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-bottom:15px}
.tasbih-tab{padding:8px 14px;background:var(--in);border:1px solid var(--bd);border-radius:20px;font-family:'Cairo',sans-serif;font-weight:700;font-size:.8rem;cursor:pointer;color:var(--ink2);transition:.2s}
.tasbih-tab.active{background:linear-gradient(180deg,var(--goldL),var(--gold));color:#fff;border-color:#8B6508}
.tasbih-total{text-align:center;padding:12px;background:var(--in);border:1px dashed var(--gold);border-radius:10px;margin-top:15px;font-size:.85rem;color:var(--ink2)}
.tasbih-total strong{color:var(--gold);font-size:1.1rem}
@media(max-width:600px){h1{font-size:1.7rem}.ayah-text{font-size:1.4rem;line-height:2.4}.container{padding:20px 14px}.search{flex-direction:column}.search input,.search select,.search button{width:100%}.btn{font-size:.8rem;padding:7px 12px}.compass{width:220px;height:220px}.arrow{height:85px}.tab{font-size:.75rem;padding:8px 6px}.fab{width:55px;height:55px;font-size:1.4rem;bottom:20px;right:15px}.about-new .share-buttons{grid-template-columns:repeat(2,1fr)}.top-buttons{gap:5px}.btn-icon{width:34px;height:34px;font-size:1rem}.tasbih-counter{width:180px;height:180px}.tasbih-num{font-size:3.5rem}}
</style>
</head>
<body>
<div class="toast-c" id="toastC"></div>
<div class="lock-overlay" id="lockOv"></div>
<button class="fab" id="fab" onclick="toggleLock()">🔒</button>

<div class="container">
<h1>الموسوعة القرآنية</h1>
<p class="subtitle">﴿ وَنُنَزِّلُ مِنَ الْقُرْآنِ مَا هُوَ شِفَاءٌ وَرَحْمَةٌ لِّلْمُؤْمِنِينَ ﴾</p>

<div class="top-buttons">
<button class="btn help" onclick="openModal('helpOv')">📖 الاستخدام</button>
<button class="btn prayer" onclick="openPrayer()">🕌 الصلاة</button>
<button class="btn notes" onclick="openNotes()">📝 ملاحظات</button>
<button class="btn tasbih" onclick="openTasbih()">📿 المسبحة</button>
<button class="btn" onclick="openModal('aboutOv')">ℹ️ حول</button>
<button class="btn sync" onclick="openSync()">🔄 مزامنة</button>
<button class="btn nav" onclick="openSidebar()">⚡ السور</button>
<button class="btn mybm" onclick="openBookmarks()">📌 علاماتي <span id="bmCount" style="background:rgba(255,255,255,.3);padding:1px 8px;border-radius:10px;font-size:.75rem">0</span></button>
<button class="btn bmc" onclick="openColorPicker()">🎨 لون</button>
<button class="btn time" onclick="openTimeDisplay()">🕐 التوقيت</button>
<button class="btn wake" onclick="toggleWake()" id="wakeBtn">☀️ إبقاء</button>
<button class="btn lock" onclick="toggleLock()" id="lockBtn">🔒 قفل</button>
<button class="btn dark" onclick="toggleDark()" id="darkBtn">🌙 ليلي</button>
</div>

<div class="timer"><span>⏱️</span><span>مدة القراءة:</span><span class="val" id="timer">00:00:00</span></div>

<div id="syncBar" style="display:flex;align-items:center;justify-content:center;gap:8px;padding:8px 14px;background:linear-gradient(180deg,rgba(59,130,246,.08),rgba(37,99,235,.04));border:1px dashed #3b82f6;border-radius:10px;margin-bottom:15px;font-size:.85rem;color:#1e40af;flex-wrap:wrap">
<span id="syncStatusIcon">☁️</span>
<span id="syncStatusText" style="font-weight:700">جاري الاتصال...</span>
<span style="opacity:.6">|</span>
<span>الرمز:</span>
<span id="syncBarCode" style="font-family:'Courier New',monospace;font-weight:700;letter-spacing:2px;background:rgba(255,255,255,.6);padding:2px 10px;border-radius:6px;border:1px solid rgba(59,130,246,.3);direction:ltr;cursor:pointer" onclick="copyCode()" title="اضغط للنسخ"></span>
<button onclick="copyCode()" style="padding:4px 12px;background:linear-gradient(180deg,#38bdf8,#0284c7);color:#fff;border:none;border-radius:6px;font-family:'Cairo',sans-serif;font-weight:700;font-size:.75rem;cursor:pointer">📋 نسخ</button>
</div>

<div class="progress">
<span class="lbl">📊 تقدم القراءة:</span>
<div class="bar">
<div class="fill" id="pfill"></div>
<div class="ms" style="left:25%" data-pct="25"></div>
<div class="ms" style="left:50%" data-pct="50"></div>
<div class="ms" style="left:75%" data-pct="75"></div>
<div class="ms" style="left:100%" data-pct="100"></div>
<div class="ms-l" style="left:25%" data-pct="25">📖 ربع</div>
<div class="ms-l" style="left:50%" data-pct="50">📖 نصف</div>
<div class="ms-l" style="left:75%" data-pct="75">📖 ٣/٤</div>
<div class="ms-l" style="left:100%" data-pct="100">🏁 ختم</div>
</div>
<span class="pct" id="pct">0%</span>
</div>

<div class="bm-bar" id="bmBar" style="display:none">
<div class="info"><span>🔖</span><strong>آخر قراءة:</strong><span id="bmLoc">—</span><span id="hereMsg">✅ أنت هنا</span></div>
<div style="display:flex;gap:8px;flex-wrap:wrap">
<button class="bm-jump" id="jumpBtn" onclick="jumpToBm()">📖 العلامة</button>
<button class="bm-clear" onclick="clearBm()">✖ حذف</button>
</div>
</div>

<div class="search">
<input type="text" id="q" placeholder="🔍 ابحث...">
<select id="src">
<option value="quran">📖 القرآن</option>
<option value="all_tafsirs">📚 جميع التفاسير</option>
<option value="tafsir_saadi">📗 السعدي</option>
<option value="tafsir_ibn_kathir">📘 ابن كثير</option>
</select>
<select id="surah"><option value="all">جميع السور</option></select>
<select id="ayah"><option value="all">كل الآيات</option></select>
<button id="searchBtn">بحث</button>
</div>

<div class="toggle-bar" id="tbar">
<label><input type="checkbox" id="showTafsir"> 📚 إظهار التفاسير</label>
<span class="hint" id="hint">(مخفية)</span>
</div>

<div class="res-info" id="resInfo">⏳ جاري التحميل...</div>
<div id="sugg"></div>
<div id="results"><div class="loading">⏳ جاري تحميل البيانات...</div></div>
<div class="pagination" id="pages"></div>
<div class="ornament">❁ ❁ ❁</div>
</div>

<div class="sidebar-ov" id="sbOv" onclick="closeSidebar()"></div>
  <div class="sidebar-ov" id="sbOv" onclick="closeSidebar()"></div>
<div class="sidebar" id="sb">
<button class="close" onclick="closeSidebar()">✖</button>
<h3>⚡ الانتقال السريع</h3>
@@ -498,104 +345,7 @@ <h2>🕌 قسم الصلاة</h2>
<li><strong>التسليم:</strong> تسليمتان.</li>
</ol></div>
<div class="guide"><div class="guide-title">🌙 التراويح وقيام الليل</div><div class="guide-desc">سنة مؤكدة في رمضان وفي كل ليلة.</div><ol>
<li><strong>1.</strong> النية للتراويح أو القيام.</li>
<li><strong>2.</strong> الصلاة مثنى مثنى.</li>
<li><strong>3.</strong> القراءة جهراً.</li>
<li><strong>4.</strong> الراحة بعد كل 4 ركعات.</li>
<li><strong>5.</strong> الوتر بثلاث ركعات.</li>
</ol><div class="guide-note">⭐ العدد: 11 أو 23 ركعة.</div></div>
</div>
</div>
</div>

<div class="overlay" id="timeOv" onclick="closeModalOutside(event,'timeOv')">
<div class="modal" style="max-width:500px" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('timeOv')">✖</button>
<h2>🕐 التوقيت والتاريخ</h2>
<p class="intro">الساعة المباشرة + التاريخ الهجري والميلادي</p>
<div id="timeDisplay" style="text-align:center"></div>
</div>
</div>

<div class="overlay" id="notesOv" onclick="closeModalOutside(event,'notesOv')">
<div class="modal" style="max-width:600px" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('notesOv')">✖</button>
<h2>📝 ملاحظاتي</h2>
<p class="intro">ملاحظات شخصية محفوظة سحابياً</p>
<div class="label-wrap">
<textarea id="noteIn" placeholder="اكتب ملاحظتك هنا..." style="width:100%;min-height:100px;padding:12px;border:1px solid var(--bd);border-radius:8px;background:var(--in);color:var(--ink);font-family:'Cairo',sans-serif;font-size:1rem;resize:vertical" maxlength="500"></textarea>
<button class="lbl-save" onclick="saveNote()" style="width:100%;padding:12px;margin-top:10px;background:var(--gold);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer">➕ إضافة ملاحظة</button>
</div>
<div id="notesList" style="max-height:400px;overflow-y:auto"></div>
</div>
</div>

<div class="overlay" id="syncOv" onclick="closeModalOutside(event,'syncOv')">
<div class="modal" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('syncOv')">✖</button>
<h2>🔄 المزامنة السحابية</h2>
<p class="intro">بياناتك تتزامن تلقائياً بين أجهزتك</p>
<div style="text-align:center;padding:15px;background:var(--hl);border-radius:10px;margin-bottom:15px">
<div style="font-size:2rem">☁️</div>
<div style="font-weight:700;color:var(--gold)">مزامنة تلقائية نشطة</div>
</div>
<h3>🔑 رمز المزامنة (احتفظ به)</h3>
<div style="display:flex;gap:8px;margin:10px 0">
<input type="text" id="syncCode" readonly style="flex:1;padding:12px;font-size:1.2rem;font-weight:700;text-align:center;letter-spacing:3px;border:2px solid var(--gold);border-radius:8px;background:var(--in);color:var(--ink);direction:ltr">
<button onclick="copyCode()" style="padding:12px 20px;background:linear-gradient(180deg,#D4AF37,#B8860B);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer">📋 نسخ</button>
</div>
<p style="font-size:.85rem;color:var(--ink2);text-align:center;margin-top:10px">⚠️ استخدم هذا الرمز على أي جهاز آخر لربط بياناتك</p>
<hr style="border:none;border-top:1px dashed var(--bd);margin:20px 0">
<h3>🔗 ربط جهاز آخر</h3>
<input type="text" id="syncIn" placeholder="الصق رمز المزامنة من الجهاز الآخر" style="width:100%;padding:12px;font-size:1rem;text-align:center;letter-spacing:2px;border:2px solid var(--gold);border-radius:8px;background:var(--in);color:var(--ink);direction:ltr;margin-bottom:10px">
<button onclick="linkCode()" style="width:100%;padding:12px;background:linear-gradient(180deg,#38bdf8,#0284c7);color:#fff;border:none;border-radius:8px;font-weight:700;cursor:pointer">✅ ربط الجهاز</button>
</div>
</div>

<div class="overlay" id="colorOv" onclick="closeModalOutside(event,'colorOv')">
<div class="modal" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('colorOv')">✖</button>
<h2>🎨 لون العلامة</h2>
<p class="intro">اختر اللون المفضل</p>
<div class="color-grid" id="colorGrid"></div>
</div>
</div>

<div class="overlay" id="bmsOv" onclick="closeModalOutside(event,'bmsOv')">
<div class="modal" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('bmsOv')">✖</button>
<h2>📌 علاماتي</h2>
<p class="intro">📖 انتقال • 🔖 تعيين كآخر قراءة • ✏️ تعديل • 🗑️ حذف</p>
<div id="bmsList"></div>
</div>
</div>

<div class="overlay" id="tasbihOv" onclick="closeModalOutside(event,'tasbihOv')">
<div class="modal" style="max-width:520px" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('tasbihOv')">✖</button>
<h2>📿 المسبحة</h2>
<p class="intro">ذكر الله يطمئن القلب</p>
<div id="tasbihContent"></div>
</div>
</div>

<div class="overlay" id="labelOv" onclick="closeModalOutside(event,'labelOv')">
<div class="modal" onclick="event.stopPropagation()">
<button class="close" onclick="closeModal('labelOv')">✖</button>
<h2>📌 إضافة علامة</h2>
<p class="intro" id="labelRef">سورة — آية —</p>
<div class="label-wrap">
<label style="display:block;font-weight:700;margin-bottom:8px">✏️ اسم العلامة:</label>
<input type="text" id="labelIn" placeholder="مثلاً: وردي اليومي" maxlength="60">
<div class="qlabels" id="qlabels"></div>
</div>
<div class="lbl-btns">
<button class="lbl-save" onclick="saveLabel()">✅ حفظ</button>
<button class="lbl-cancel" onclick="closeModal('labelOv')">إلغاء</button>
</div>
</div>
</div>
<script>
  <script>
const APP_VERSION='v3.0';
const SURAHS=["الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس","هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه","الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجدة","الأحزاب","سبأ","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة","الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج","نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبأ","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات","القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الإخلاص","الفلق","الناس"];
const AYAH_COUNTS=[7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6];
@@ -680,6 +430,7 @@ <h2>📌 إضافة علامة</h2>
}
}

// [إصلاح 3] المزامنة باستخدام await لمنع تأخر الحفظ
async function syncToCloud(){
if(!window.fbReady||isSyncing)return;
isSyncing=true;
@@ -968,71 +719,1353 @@ <h2>📌 إضافة علامة</h2>
saveBms();updateProgress();closeModal('labelOv');render();
requestAnimationFrame(()=>window.scrollTo(0,_y));
setTimeout(()=>window.scrollTo(0,_y),180);
toast('تمت إضافة "'+l+'"','special',3000);
pendSur=null;pendAyah=null;
toast('تمت
      <script>
const APP_VERSION='v3.0';
const SURAHS=["الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس","هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه","الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجدة","الأحزاب","سبأ","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة","الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج","نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبأ","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات","القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الإخلاص","الفلق","الناس"];
const AYAH_COUNTS=[7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6];
const TOTAL=6236;
const TAFSIRS=[{k:'saadi',f:'tafsir_saadi.json',l:'تفسير السعدي',i:'📗'},{k:'ibn_kathir',f:'tafsir_ibn_kathir.json',l:'تفسير ابن كثير',i:'📘'}];
const COLORS=[{n:'بني',l:'#8B4513',d:'#5C2E0E'},{n:'ذهبي',l:'#D4AF37',d:'#8B6508'},{n:'أخضر',l:'#059669',d:'#064e3b'},{n:'أزرق',l:'#2563eb',d:'#1e3a8a'},{n:'أحمر',l:'#dc2626',d:'#7f1d1d'},{n:'بنفسجي',l:'#7c3aed',d:'#4c1d95'},{n:'برتقالي',l:'#ea580c',d:'#7c2d12'},{n:'أسود',l:'#374151',d:'#111827'}];
const QLABELS=['📌 وردي اليومي','💭 للتدبر','⭐ مهمة','📖 حفظ','🤲 دعاء','🔍 للبحث'];
const SAMPLE=[{surah:1,ayah:1,text:"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"},{surah:1,ayah:2,text:"الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"},{surah:103,ayah:1,text:"وَالْعَصْرِ"},{surah:112,ayah:1,text:"قُلْ هُوَ اللَّهُ أَحَدٌ"}];
const SHAMI_MONTHS=['كانون الثاني','شباط','آذار','نيسان','أيار','حزيران','تموز','آب','أيلول','تشرين الأول','تشرين الثاني','كانون الأول'];
const HIJRI_MONTHS=['محرم','صفر','ربيع الأول','ربيع الآخر','جمادى الأولى','جمادى الآخرة','رجب','شعبان','رمضان','شوال','ذو القعدة','ذو الحجة'];
const ADHKAR=[
{d:'سُبْحَانَ اللَّهِ',n:'سبحان الله',t:33,f:'من قالها 100 مرة حُطّت خطاياه'},
{d:'الْحَمْدُ لِلَّهِ',n:'الحمد لله',t:33,f:'الحمد لله تملأ الميزان'},
{d:'اللَّهُ أَكْبَرُ',n:'الله أكبر',t:33,f:'الله أكبر كبيراً'},
{d:'لَا إِلَٰهَ إِلَّا اللَّهُ',n:'لا إله إلا الله',t:100,f:'خير ما قاله النبيون'},
{d:'أَسْتَغْفِرُ اللَّهَ',n:'أستغفر الله',t:100,f:'من لزم الاستغفار جعل الله له من كل هم فرجاً'},
{d:'سُبْحَانَ اللَّهِ وَبِحَمْدِهِ',n:'سبحان الله وبحمده',t:100,f:'من قالها 100 مرة حُطّت خطاياه ولو كانت مثل زبد البحر'},
{d:'لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ',n:'لا حول ولا قوة إلا بالله',t:100,f:'كنز من كنوز الجنة'},
{d:'سُبْحَانَ اللَّهِ وَالْحَمْدُ لِلَّهِ وَلَا إِلَٰهَ إِلَّا اللَّهُ وَاللَّهُ أَكْبَرُ',n:'الباقيات الصالحات',t:100,f:'أفضل الكلام بعد القرآن'}
];

let quran=[],tafsirs={};
let curSrc='quran',curKW='',curSur='all',curAyah='all';
let page=1,showTafsir=false;
let bm=null,allBms=[],bmColorIdx=0,allNotes=[];
let pendSur=null,pendAyah=null,focusAyah=null;
let wakeLock=null,wakeWanted=false;
let locked=false,startTime=Date.now(),_savedScroll=0;
let userLoc=null,devHeading=null;
let syncUserId=null,isSyncing=false,timeInterval=null;
let tasbihState={dhikrIdx:0,count:0,target:33,total:0};
const perPage=10;

try{
if(localStorage.getItem('showTafsir')==='true')showTafsir=true;
if(localStorage.getItem('darkMode')==='true')document.body.classList.add('dark');
const bc=localStorage.getItem('bookmarkColor');if(bc)bmColorIdx=parseInt(bc);
const bms=localStorage.getItem('allBookmarks');if(bms)allBms=JSON.parse(bms);
const nt=localStorage.getItem('quranNotes');if(nt)allNotes=JSON.parse(nt);
if(localStorage.getItem('wakeLockWanted')==='true')wakeWanted=true;
const sl=localStorage.getItem('userLocation');if(sl)userLoc=JSON.parse(sl);
const ts=localStorage.getItem('tasbihState');
if(ts){
const p=JSON.parse(ts);
if(typeof p.dhikrIdx==='number')tasbihState.dhikrIdx=p.dhikrIdx;
if(typeof p.count==='number')tasbihState.count=p.count;
if(typeof p.target==='number')tasbihState.target=p.target;
if(typeof p.total==='number')tasbihState.total=p.total;
}
function hasSP(s,a){return allBms.some(b=>b.surah==s&&b.ayah==a)}
function getSP(s,a){return allBms.filter(b=>b.surah==s&&b.ayah==a).map(b=>b.label)}
}catch(e){}

function jumpToBmItem(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
closeModal('bmsOv');
document.getElementById('src').value='quran';
document.getElementById('surah').value=b.surah;
updateAyahDD(b.surah,'all');
document.getElementById('ayah').value='all';
document.getElementById('q').value='';
curSrc='quran';curSur=String(b.surah);curAyah='all';curKW='';
focusAyah=b.ayah;
const src=quran.filter(a=>a.surah==b.surah);
const i=src.findIndex(a=>a.ayah==b.ayah);
page=i>=0?Math.floor(i/perPage)+1:1;
render();
// ============ المزامنة السحابية ============
function getUserId(){
let id=localStorage.getItem('syncUserId');
if(!id||id.length<8){
const chars='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';let n='';
for(let i=0;i<12;i++)n+=chars[Math.floor(Math.random()*chars.length)];
localStorage.setItem('syncUserId',n);id=n;
}
return id;
}
syncUserId=getUserId();

function setAsBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
bm={surah:b.surah,ayah:b.ayah,timestamp:Date.now()};
localStorage.setItem('quranBookmark',JSON.stringify(bm));
updateBmBar();updateProgress();
toast('تم تعيين "'+b.label+'" كآخر قراءة 🔖','bookmark',2000);
syncToCloud();
closeModal('bmsOv');
jumpToBm();
function setSyncStatus(state,text){
const icon=document.getElementById('syncStatusIcon');
const txt=document.getElementById('syncStatusText');
if(!icon||!txt)return;
const states={
ok:{i:'☁️',c:'#16a34a',bg:'rgba(22,163,74,.1)',bd:'#16a34a',t:text||'متزامن'},
syncing:{i:'⏳',c:'#2563eb',bg:'rgba(37,99,235,.1)',bd:'#3b82f6',t:text||'جاري المزامنة...'},
error:{i:'⚠️',c:'#dc2626',bg:'rgba(220,38,38,.1)',bd:'#dc2626',t:text||'خطأ في المزامنة'},
waiting:{i:'⏸️',c:'#f59e0b',bg:'rgba(245,158,11,.1)',bd:'#f59e0b',t:text||'بانتظار الاتصال'}
};
const s=states[state]||states.ok;
icon.textContent=s.i;
txt.textContent=s.t;
txt.style.color=s.c;
const bar=document.getElementById('syncBar');
if(bar){
bar.style.background=s.bg;
bar.style.borderColor=s.bd;
}
}

function delBm(id){
if(!confirm('حذف؟'))return;
const _y=window.scrollY||0;
allBms=allBms.filter(x=>String(x.id)!==String(id));
saveBms();updateProgress();openBookmarks();
requestAnimationFrame(()=>window.scrollTo(0,_y));
toast('تم الحذف','warn',2000);
// [إصلاح 3] المزامنة باستخدام await لمنع تأخر الحفظ
async function syncToCloud(){
if(!window.fbReady||isSyncing)return;
isSyncing=true;
setSyncStatus('syncing');
try{
await window.fbSet(window.fbDoc(window.fbDB,'sync',syncUserId),{
bms:allBms,bm:bm,color:bmColorIdx,notes:allNotes,
dark:document.body.classList.contains('dark'),
tafsir:showTafsir,
tasbih:tasbihState,
updatedAt:Date.now()
});
console.log("☁️ Synced");
setSyncStatus('ok','متزامن ✓');
setTimeout(()=>{const t=document.getElementById('syncStatusText');if(t&&t.textContent==='متزامن ✓')setSyncStatus('ok','متزامن');},2000);
}catch(e){
console.error("Sync error:",e);
setSyncStatus('error');
}
function editBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
const nl=prompt('تعديل الاسم:',b.label);
if(!nl||!nl.trim())return;
b.label=nl.trim();saveBms();openBookmarks();render();
isSyncing=false;
}
function openBookmarks(){
_savedScroll=window.scrollY||0;
const c=document.getElementById('bmsList');
if(allBms.length===0){c.innerHTML='<div style="text-align:center;padding:30px;color:var(--ink2)">📭 لا توجد علامات.<br><br>اذهب لأي آية، اضغط 📌، واكتب اسماً.</div>';}
else{
const s=[...allBms].sort((a,b)=>a.surah-b.surah||a.ayah-b.ayah);
c.innerHTML=s.map(b=>{
const sn=SURAHS[b.surah-1]||'؟';
const isCurrentBm=bm&&bm.surah==b.surah&&bm.ayah==b.ayah;
return `<div class="bm-item"><div class="info"><div class="lbl">📌 ${b.label}${isCurrentBm?' <span style="background:#16a34a;color:#fff;padding:1px 6px;border-radius:8px;font-size:.65rem">🔖 الحالية</span>':''}</div><div style="font-size:.8rem;color:var(--ink2)">سورة ${sn} - آية ${b.ayah}</div></div><div class="act"><button class="jump" onclick="jumpToBmItem('${b.id}')" title="انتقال فقط">📖</button><button class="setbm" onclick="setAsBm('${b.id}')" title="تعيين كآخر قراءة">🔖</button><button class="edit" onclick="editBm('${b.id}')" title="تعديل">✏️</button><button class="del" onclick="delBm('${b.id}')" title="حذف">🗑️</button></div></div>`;
}).join('');

async function loadFromCloud(){
if(!window.fbReady){
setSyncStatus('waiting','جاري تهيئة Firebase...');
setTimeout(loadFromCloud,500);
return;
}
openModal('bmsOv');
setSyncStatus('syncing','جاري التحميل من السحابة...');
try{
const snap=await window.fbGet(window.fbDoc(window.fbDB,'sync',syncUserId));
if(snap.exists()){
const data=snap.data();
if(data.bms)allBms=data.bms;
if(data.bm)bm=data.bm;
if(data.color!==undefined){bmColorIdx=data.color;applyColor();}
if(data.notes&&Array.isArray(data.notes))allNotes=data.notes;
if(data.tafsir!==undefined){showTafsir=data.tafsir;const cb=document.getElementById('showTafsir');if(cb)cb.checked=showTafsir;const h=document.getElementById('hint');if(h)h.textContent=showTafsir?'(ظاهرة)':'(مخفية)';}
if(data.dark!==undefined){if(data.dark)document.body.classList.add('dark');else document.body.classList.remove('dark');const btn=document.getElementById('darkBtn');if(btn)btn.textContent=data.dark?'☀️ نهاري':'🌙 ليلي';}
if(data.tasbih&&typeof data.tasbih==='object'){
tasbihState={...tasbihState,...data.tasbih};
localStorage.setItem('tasbihState',JSON.stringify(tasbihState));
}
localStorage.setItem('allBookmarks',JSON.stringify(allBms));
localStorage.setItem('quranNotes',JSON.stringify(allNotes));
if(bm)localStorage.setItem('quranBookmark',JSON.stringify(bm));
localStorage.setItem('bookmarkColor',bmColorIdx);
localStorage.setItem('showTafsir',showTafsir);
updateBmBar();updateProgress();updateBmCount();render();
console.log("☁️ Loaded from cloud");
setSyncStatus('ok','تم التحميل ✓');
setTimeout(()=>{const t=document.getElementById('syncStatusText');if(t&&t.textContent==='تم التحميل ✓')setSyncStatus('ok','متزامن');},2000);
}else{
console.log("🆕 New sync code — creating empty document");
setSyncStatus('syncing','إنشاء مستند جديد...');
await syncToCloud();
if(allBms.length>0||allNotes.length>0||bm){
setTimeout(()=>{
if(confirm('⚠️ هذا الجهاز يستخدم رمز مزامنة جديد.\n\nهل تريد نسخ الرمز الآن للاحتفاظ به؟\n\n(إذا كان لديك رمز قديم من جهاز آخر، استخدم "🔗 ربط جهاز آخر" في نافذة المزامنة)')){
openSync();
}
},2500);
}
}
}catch(e){
console.error("Load error:",e);
setSyncStatus('error','فشل التحميل');
}
}

function openSync(){
_savedScroll=window.scrollY||0;
document.getElementById('syncCode').value=syncUserId;
document.getElementById('syncIn').value='';
const bar=document.getElementById('syncBarCode');
if(bar)bar.textContent=syncUserId;
openModal('syncOv');
}
// [تعديل 3] حساب نسبة الختمة بدقة
function copyCode(){
const code=syncUserId;
if(navigator.clipboard){
navigator.clipboard.writeText(code).then(()=>toast('✅ تم نسخ: '+code,'info',2500)).catch(()=>{
const el=document.getElementById('syncCode');
if(el){el.select();try{document.execCommand('copy');toast('✅ تم النسخ','info',2000);}catch(e){alert('الرمز: '+code);}}
});
}else{
const el=document.getElementById('syncCode');
if(el){el.select();try{document.execCommand('copy');toast('✅ تم النسخ','info',2000);}catch(e){alert('الرمز: '+code);}}
else alert('الرمز: '+code);
}
}
async function linkCode(){
const inp=document.getElementById('syncIn');
const newCode=(inp.value||'').trim().toUpperCase().replace(/[^A-Z0-9]/g,'');
if(!newCode||newCode.length<8){alert('❌ رمز غير صالح');return;}
localStorage.setItem('syncUserId',newCode);syncUserId=newCode;
const bar=document.getElementById('syncBarCode');
if(bar)bar.textContent=syncUserId;
alert('✅ تم الربط! جاري تحميل بياناتك...');
closeModal('syncOv');
await loadFromCloud();
}

function toast(msg,type='',dur=3000){
const c=document.getElementById('toastC');
const t=document.createElement('div');
t.className='toast '+(type||'');
let icon='✅';
if(type==='bookmark')icon='🔖';else if(type==='special')icon='📌';else if(type==='info')icon='☁️';else if(type==='warn')icon='⚠️';
t.innerHTML=`<span style="font-size:1.3rem">${icon}</span><span>${msg}</span>`;
c.appendChild(t);
setTimeout(()=>{if(t.parentNode)t.parentNode.removeChild(t)},dur);
}

setInterval(()=>{
const e=Math.floor((Date.now()-startTime)/1000);
const h=Math.floor(e/3600),m=Math.floor((e%3600)/60),s=e%60;
const p=n=>String(n).padStart(2,'0');
const el=document.getElementById('timer');
if(el)el.textContent=`${p(h)}:${p(m)}:${p(s)}`;
},1000);

// ============ قفل الشاشة ============
function toggleLock(){
if(locked){unlock();return}
locked=true;
document.body.classList.add('locked');
document.getElementById('lockOv').classList.add('active');
const lb=document.getElementById('lockBtn');if(lb){lb.textContent='🔓 فتح';lb.classList.add('active')}
const fab=document.getElementById('fab');if(fab){fab.textContent='🔓';fab.classList.add('locked','visible')}
const f=document.createElement('div');f.className='lock-float active';f.id='lockFloat';
f.innerHTML='<span>🔓</span><span>فتح الشاشة</span>';f.onclick=unlock;
document.body.appendChild(f);
toast('تم قفل الشاشة 🔒','info',2000);
}
function unlock(){
if(!locked)return;
locked=false;
document.body.classList.remove('locked');
document.getElementById('lockOv').classList.remove('active');
const lb=document.getElementById('lockBtn');if(lb){lb.textContent='🔒 قفل';lb.classList.remove('active')}
const fab=document.getElementById('fab');if(fab){fab.textContent='🔒';fab.classList.remove('locked')}
const f=document.getElementById('lockFloat');if(f)f.remove();
toast('تم فتح الشاشة 🔓','info',1500);
}
window.addEventListener('scroll',()=>{
const fab=document.getElementById('fab');if(!fab)return;
if(window.scrollY>200||locked)fab.classList.add('visible');else fab.classList.remove('visible');
});

// ============ إبقاء الشاشة مضيئة ============
async function reqWake(){
if(!('wakeLock' in navigator))return false;
try{wakeLock=await navigator.wakeLock.request('screen');return true}catch(e){return false}
}
async function toggleWake(){
if(!('wakeLock' in navigator)){alert('⚠️ غير مدعوم في هذا المتصفح');return}
const btn=document.getElementById('wakeBtn');
if(wakeWanted){
wakeWanted=false;localStorage.setItem('wakeLockWanted','false');
if(wakeLock){try{await wakeLock.release()}catch(e){}wakeLock=null}
if(btn){btn.textContent='☀️ إبقاء';btn.classList.remove('active')}
toast('تم الإيقاف','info',2000);
}else{
wakeWanted=true;localStorage.setItem('wakeLockWanted','true');
const ok=await reqWake();
if(ok){if(btn){btn.textContent='💡 مضيئة';btn.classList.add('active')}toast('تم التفعيل ☀️','info',2000)}
else{wakeWanted=false;localStorage.setItem('wakeLockWanted','false');alert('❌ تعذّر تفعيل الإبقاء')}
}
}
document.addEventListener('visibilitychange',async()=>{
if(document.visibilityState==='visible'&&wakeWanted)await reqWake();
});
if(wakeWanted){const btn=document.getElementById('wakeBtn');if(btn){btn.textContent='💡 مضيئة';btn.classList.add('active')}reqWake();}

// ============ النوافذ ============
function openModal(id){
_savedScroll=window.scrollY||0;
document.getElementById(id).classList.add('active');
document.body.style.overflow='hidden';
if(id==='aboutOv'){const el=document.getElementById('shareUrl');if(el)el.textContent=window.location.origin;}
}
function closeModal(id){
document.getElementById(id).classList.remove('active');
document.body.style.overflow='';
if(id==='timeOv'&&timeInterval){clearInterval(timeInterval);timeInterval=null;}
requestAnimationFrame(()=>{window.scrollTo(0,_savedScroll);});
setTimeout(()=>{window.scrollTo(0,_savedScroll);},30);
}
function closeModalOutside(e,id){if(e.target.id===id){closeModal(id);if(id==='welcomeOv')localStorage.setItem('appVersion',APP_VERSION);}}
document.addEventListener('keydown',e=>{
if(e.key==='Escape'){
['welcomeOv','helpOv','aboutOv','prayerOv','syncOv','colorOv','bmsOv','labelOv','timeOv','notesOv','tasbihOv'].forEach(id=>{closeModal(id);if(id==='welcomeOv')localStorage.setItem('appVersion',APP_VERSION);});
closeSidebar();
}
});
function closeWelcome(){closeModal('welcomeOv');localStorage.setItem('appVersion',APP_VERSION);}
setTimeout(()=>{const v=localStorage.getItem('appVersion')||'';if(v!==APP_VERSION){openModal('welcomeOv');}},800);

function toggleDark(){
document.body.classList.toggle('dark');
const d=document.body.classList.contains('dark');
localStorage.setItem('darkMode',d);
document.getElementById('darkBtn').textContent=d?'☀️ نهاري':'🌙 ليلي';
syncToCloud();
}
if(document.body.classList.contains('dark'))document.getElementById('darkBtn').textContent='☀️ نهاري';

function applyColor(){
const c=COLORS[bmColorIdx]||COLORS[0];
document.documentElement.style.setProperty('--bm',c.l);
document.documentElement.style.setProperty('--bmD',c.d);
localStorage.setItem('bookmarkColor',bmColorIdx);
}
function openColorPicker(){
_savedScroll=window.scrollY||0;
const g=document.getElementById('colorGrid');
g.innerHTML=COLORS.map((c,i)=>`<div class="color-opt ${i===bmColorIdx?'selected':''}" style="background:linear-gradient(180deg,${c.l},${c.d})" onclick="selectColor(${i})" title="${c.n}"></div>`).join('');
openModal('colorOv');
}
function selectColor(i){bmColorIdx=i;applyColor();closeModal('colorOv');syncToCloud();}

function shareTo(platform){
const url=window.location.origin;
const title='الموسوعة القرآنية';
const text='تطبيق رائع لقراءة القرآن مع التفاسير ومواقيت الصلاة';
switch(platform){
case 'whatsapp':window.open('https://wa.me/?text='+encodeURIComponent(text+'\n'+url),'_blank');break;
case 'telegram':window.open('https://t.me/share/url?url='+encodeURIComponent(url)+'&text='+encodeURIComponent(text),'_blank');break;
case 'facebook':window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(url),'_blank');break;
case 'twitter':window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent(text)+'&url='+encodeURIComponent(url),'_blank');break;
case 'email':window.location.href='mailto:?subject='+encodeURIComponent(title)+'&body='+encodeURIComponent(text+'\n\n'+url);break;
case 'copy':
if(navigator.clipboard){navigator.clipboard.writeText(url).then(()=>toast('✅ تم نسخ الرابط','info',2000)).catch(()=>fallbackCopy(url));}
else fallbackCopy(url);
break;
}
}
function fallbackCopy(text){
const inp=document.createElement('input');inp.value=text;document.body.appendChild(inp);inp.select();
try{document.execCommand('copy');toast('✅ تم نسخ الرابط','info',2000);}catch(e){alert('انسخ يدوياً: '+text);}
inp.remove();
}

// ============ العلامات ============
function loadBm(){try{const s=localStorage.getItem('quranBookmark');if(s)bm=JSON.parse(s)}catch(e){bm=null}}
function saveBms(){localStorage.setItem('allBookmarks',JSON.stringify(allBms));updateBmCount();syncToCloud();}
function updateBmCount(){const e=document.getElementById('bmCount');if(e)e.textContent=allBms.length}
function clearBm(){
if(!confirm('حذف علامة آخر قراءة؟'))return;
const _y=window.scrollY||0;
bm=null;localStorage.removeItem('quranBookmark');
updateBmBar();focusAyah=null;render();
requestAnimationFrame(()=>window.scrollTo(0,_y));
toast('تم حذف العلامة','warn',2000);syncToCloud();
}
function toggleBm(s,a){
const oldBm=bm;
const isCurrentlyBm=bm&&bm.surah==s&&bm.ayah==a;
if(isCurrentlyBm){bm=null;localStorage.removeItem('quranBookmark');toast('تم إزالة العلامة','warn',2000);}
else{bm={surah:parseInt(s),ayah:parseInt(a),timestamp:Date.now()};localStorage.setItem('quranBookmark',JSON.stringify(bm));toast('تم الحفظ 🔖','bookmark',2000);}
updateBmBar();updateProgress();
if(oldBm){const oc=document.getElementById(`ayah-${oldBm.surah}-${oldBm.ayah}`);if(oc){oc.classList.remove('bookmarked');const r=oc.querySelector('.ribbon-bm');if(r)r.remove();const b=oc.querySelector('.bm-btn');if(b)b.classList.remove('active');}}
const card=document.getElementById(`ayah-${s}-${a}`);
if(card){if(bm){card.classList.add('bookmarked');if(!card.querySelector('.ribbon-bm')){const r=document.createElement('div');r.className='ribbon-bm';r.textContent='🔖 آخر قراءة';card.insertBefore(r,card.firstChild);}const b=card.querySelector('.bm-btn');if(b)b.classList.add('active');}else{card.classList.remove('bookmarked');const r=card.querySelector('.ribbon-bm');if(r)r.remove();const b=card.querySelector('.bm-btn');if(b)b.classList.remove('active');}}
else{render();}
syncToCloud();
}
function openLabel(s,a){
_savedScroll=window.scrollY||0;
pendSur=s;pendAyah=a;
const n=SURAHS[s-1]||'؟';
document.getElementById('labelRef').textContent='📍 سورة '+n+' - آية '+a;
document.getElementById('labelIn').value='';
document.getElementById('qlabels').innerHTML=QLABELS.map(l=>`<button onclick="document.getElementById('labelIn').value='${l}'">${l}</button>`).join('');
openModal('labelOv');
setTimeout(()=>document.getElementById('labelIn').focus(),100);
}
function saveLabel(){
const l=document.getElementById('labelIn').value.trim();
if(!l){alert('❌ أدخل اسماً');return}
if(pendSur===null||pendAyah===null)return;
const s=pendSur,a=pendAyah;
const _y=_savedScroll||window.scrollY||0;
allBms.push({id:String(Date.now())+'_'+Math.random().toString(36).slice(2,8),label:l,surah:s,ayah:a,created:Date.now()});
saveBms();updateProgress();closeModal('labelOv');render();
requestAnimationFrame(()=>window.scrollTo(0,_y));
setTimeout(()=>window.scrollTo(0,_y),180);
toast('تمت إضافة "'+l+'"','special',3000);
pendSur=null;pendAyah=null;
}
function hasSP(s,a){return allBms.some(b=>b.surah==s&&b.ayah==a)}
function getSP(s,a){return allBms.filter(b=>b.surah==s&&b.ayah==a).map(b=>b.label)}

function jumpToBmItem(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
closeModal('bmsOv');
document.getElementById('src').value='quran';
document.getElementById('surah').value=b.surah;
updateAyahDD(b.surah,'all');
document.getElementById('ayah').value='all';
document.getElementById('q').value='';
curSrc='quran';curSur=String(b.surah);curAyah='all';curKW='';
focusAyah=b.ayah;
const src=quran.filter(a=>a.surah==b.surah);
const i=src.findIndex(a=>a.ayah==b.ayah);
page=i>=0?Math.floor(i/perPage)+1:1;
render();
}

function setAsBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
bm={surah:b.surah,ayah:b.ayah,timestamp:Date.now()};
localStorage.setItem('quranBookmark',JSON.stringify(bm));
updateBmBar();updateProgress();
toast('تم تعيين "'+b.label+'" كآخر قراءة 🔖','bookmark',2000);
syncToCloud();
closeModal('bmsOv');
jumpToBm();
}

function delBm(id){
if(!confirm('حذف؟'))return;
const _y=window.scrollY||0;
allBms=allBms.filter(x=>String(x.id)!==String(id));
saveBms();updateProgress();openBookmarks();
requestAnimationFrame(()=>window.scrollTo(0,_y));
toast('تم الحذف','warn',2000);
}
function editBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
const nl=prompt('تعديل الاسم:',b.label);
if(!nl||!nl.trim())return;
b.label=nl.trim();saveBms();openBookmarks();render();
}
function openBookmarks(){
_savedScroll=window.scrollY||0;
const c=document.getElementById('bmsList');
if(allBms.length===0){c.innerHTML='<div style="text-align:center;padding:30px;color:var(--ink2)">📭 لا توجد علامات.<br><br>اذهب لأي آية، اضغط 📌، واكتب اسماً.</div>';}
else{
const s=[...allBms].sort((a,b)=>a.surah-b.surah||a.ayah-b.ayah);
c.innerHTML=s.map(b=>{
const sn=SURAHS[b.surah-1]||'؟';
const isCurrentBm=bm&&bm.surah==b.surah&&bm.ayah==b.ayah;
return `<div class="bm-item"><div class="info"><div class="lbl">📌 ${b.label}${isCurrentBm?' <span style="background:#16a34a;color:#fff;padding:1px 6px;border-radius:8px;font-size:.65rem">🔖 الحالية</span>':''}</div><div style="font-size:.8rem;color:var(--ink2)">سورة ${sn} - آية ${b.ayah}</div></div><div class="act"><button class="jump" onclick="jumpToBmItem('${b.id}')" title="انتقال فقط">📖</button><button class="setbm" onclick="setAsBm('${b.id}')" title="تعيين كآخر قراءة">🔖</button><button class="edit" onclick="editBm('${b.id}')" title="تعديل">✏️</button><button class="del" onclick="delBm('${b.id}')" title="حذف">🗑️</button></div></div>`;
}).join('');
}
openModal('bmsOv');
}

// [إصلاح 2] حساب نسبة الختمة بدقة
function updateProgress(){
    // نعتمد على علامة "آخر قراءة" (bm) لحساب أين وصل المستخدم
    let currentSurah = bm ? bm.surah : 1;
    let currentAyah = bm ? bm.ayah : 0;

    // جمع آيات السور السابقة
    let ayahsReadBefore = 0;
    for (let i = 0; i < currentSurah - 1; i++) {
        ayahsReadBefore += AYAH_COUNTS[i];
    }

    let totalAyahsRead = ayahsReadBefore + currentAyah;
    let p = (totalAyahsRead / TOTAL) * 100;
    
    if (currentSurah === 114 && currentAyah === 6) p = 100; // ختم المصحف
    p = Math.min(100, Math.max(0, Math.round(p)));

    const pf = document.getElementById('pfill');
    if(pf) pf.style.width = p + '%';
    
    const pe = document.getElementById('pct');
    if(!pe) return;
    
    document.querySelectorAll('.ms').forEach(m => {
        const pc = parseInt(m.dataset.pct);
        if (p >= pc) m.classList.add('r');
        else m.classList.remove('r');
    });
    
    document.querySelectorAll('.ms-l').forEach(l => {
        const pc = parseInt(l.dataset.pct);
        if (p >= pc) l.classList.add('r');
        else l.classList.remove('r');
    });
    
    pe.title = `قرأت ${totalAyahsRead} آية من ${TOTAL}`;
    if (p >= 100) {
        pe.textContent = '🏁 ختم';
        pe.style.color = '#d4a100';
    } else {
        pe.textContent = p + '%';
        pe.style.color = '';
    }
}
function updateBmBar(){
const bar=document.getElementById('bmBar');if(!bar)return;
if(!bm){bar.style.display='none';return}
bar.style.display='flex';
document.getElementById('bmLoc').textContent=`سورة ${SURAHS[bm.surah-1]||'؟'} - آية ${bm.ayah}`;
}
function jumpToBm(){
if(!bm)return;
document.getElementById('src').value='quran';
document.getElementById('surah').value=bm.surah;
updateAyahDD(bm.surah,'all');
document.getElementById('ayah').value='all';
document.getElementById('q').value='';
curSrc='quran';curSur=String(bm.surah);curAyah='all';curKW='';
focusAyah=bm.ayah;
const src=quran.filter(a=>a.surah==bm.surah);
const i=src.findIndex(a=>a.ayah==bm.ayah);
page=i>=0?Math.floor(i/perPage)+1:1;
render();
}
function isBm(s,a){return bm&&bm.surah==s&&bm.ayah==a}
function rmTashkeel(t){if(!t)return'';return t.replace(/[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]/g,'').replace(/[\u0622\u0623\u0625\u0671]/g,'ا').replace(/\u0649/g,'ي').replace(/\u0624/g,'و').replace(/\u0629/g,'ه');}
function match(t,kw){if(!kw)return true;return rmTashkeel(t).includes(rmTashkeel(kw));}
function hl(t,kw){if(!kw||!t)return t;const n=rmTashkeel(t);const k=rmTashkeel(kw);const i=n.indexOf(k);if(i<0)return t;return t.substring(0,i)+'<mark>'+t.substring(i,i+kw.length)+'</mark>'+t.substring(i+kw.length);}

function populateSurah(){const s=document.getElementById('surah');SURAHS.forEach((n,i)=>{const o=document.createElement('option');o.value=i+1;o.textContent=`${i+1}. ${n}`;s.appendChild(o)});}
function updateAyahDD(sn,ka){
const a=document.getElementById('ayah');
a.innerHTML='<option value="all">كل الآيات</option>';
if(!sn||sn==='all')return;
const s=parseInt(sn);
quran.filter(x=>x.surah===s).forEach(x=>{const o=document.createElement('option');o.value=x.ayah;o.textContent='آية '+x.ayah;a.appendChild(o)});
if(ka)a.value=ka;
}
function populateSidebar(){document.getElementById('sbList').innerHTML=SURAHS.map((n,i)=>`<div class="surah-item" onclick="jumpSurah(${i+1})"><span class="n">${i+1}</span><span>${n}</span></div>`).join('');}
function jumpSurah(n){
closeSidebar();
document.getElementById('src').value='quran';
document.getElementById('surah').value=n;
document.getElementById('q').value='';
updateAyahDD(n,'all');
curSrc='quran';curSur=String(n);curAyah='all';curKW='';page=1;focusAyah=null;
render();
window.scrollTo({top:0,behavior:'smooth'});
}
function showFullSurah(s,a){
focusAyah=a;curSrc='quran';curSur=String(s);curAyah='all';curKW='';
document.getElementById('q').value='';
document.getElementById('src').value='quran';
document.getElementById('surah').value=s;
updateAyahDD(s,'all');
document.getElementById('ayah').value='all';
const src=quran.filter(x=>x.surah==s);
const i=src.findIndex(x=>x.ayah===a);
page=i>=0?Math.floor(i/perPage)+1:1;
render();
}
function openSidebar(){_savedScroll=window.scrollY||0;document.getElementById('sb').classList.add('active');document.getElementById('sbOv').classList.add('active');document.body.style.overflow='hidden';}
function closeSidebar(){document.getElementById('sb').classList.remove('active');document.getElementById('sbOv').classList.remove('active');document.body.style.overflow='';requestAnimationFrame(()=>window.scrollTo(0,_savedScroll));}

function initTafsir(){
const t=document.getElementById('showTafsir');
const h=document.getElementById('hint');
t.checked=showTafsir;
const u=()=>{h.textContent=showTafsir?'(ظاهرة)':'(مخفية)';h.style.color=showTafsir?'#16a34a':'var(--gold)'};
u();
t.addEventListener('change',()=>{showTafsir=t.checked;localStorage.setItem('showTafsir',showTafsir);u();render();syncToCloud();});
}

async function loadTafsirFile(cfg){
try{
const r=await fetch(cfg.f);
if(!r.ok){tafsirs[cfg.k]={l:cfg.l,i:cfg.i,ayahs:[]};return}
const text=await r.text();
if(text.startsWith('SQLite')||text.startsWith('<!DOCTYPE')||text.startsWith('<html')){tafsirs[cfg.k]={l:cfg.l,i:cfg.i,ayahs:[]};return}
let raw;
try{raw=JSON.parse(text)}catch(e){tafsirs[cfg.k]={l:cfg.l,i:cfg.i,ayahs:[]};return}
let ayahs=[];
if(Array.isArray(raw)){ayahs=raw.map(a=>({surah:parseInt(a.surah||a.sura||1),number:parseInt(a.number||a.ayah||a.numberInSurah||a.id||1),text:a.text||a.tafsir||a.content||''}));}
else if(raw&&raw.ayahs&&Array.isArray(raw.ayahs)){ayahs=raw.ayahs.map(a=>({surah:parseInt(a.surah||a.sura||1),number:parseInt(a.number||a.ayah||1),text:a.text||a.tafsir||a.content||''}));}
else if(raw&&typeof raw==='object'){
ayahs=Object.keys(raw).map(k=>{
if(k.indexOf(':')===-1)return null;
const p=k.split(':');if(p.length!==2)return null;
const s=parseInt(p[0]),n=parseInt(p[1]);
if(isNaN(s)||isNaN(n))return null;
const item=raw[k];let t='';
if(typeof item==='string')t=item;
else if(item&&typeof item==='object')t=item.text||item.tafsir||item.content||'';
t=t.replace(/<[^>]+>/g,'').replace(/&nbsp;/g,' ').replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/\s+/g,' ').trim();
return{surah:s,number:n,text:t};
}).filter(a=>a&&a.text&&a.text.length>0);
}
tafsirs[cfg.k]={l:cfg.l,i:cfg.i,ayahs:ayahs};
}catch(e){tafsirs[cfg.k]={l:cfg.l,i:cfg.i,ayahs:[]};}
}

async function loadData(){
const info=document.getElementById('resInfo');
try{
const r=await fetch('quran.json');
if(!r.ok)throw new Error('HTTP '+r.status);
const raw=await r.json();
if(Array.isArray(raw)&&raw.length>0&&raw[0].verses){quran=[];raw.forEach(s=>{(s.verses||[]).forEach(v=>{quran.push({surah:s.id,ayah:v.id,text:v.text})})});}
else if(Array.isArray(raw)){quran=raw.map(a=>({surah:parseInt(a.surah||1),ayah:parseInt(a.ayah||a.number||1),text:a.text||''}));}
if(!quran.length)throw new Error('ملف فارغ');
}catch(e){console.warn('⚠️ استخدام بيانات تجريبية:',e.message);quran=SAMPLE.slice();}
await Promise.all(TAFSIRS.map(loadTafsirFile));
const tt=Object.values(tafsirs).reduce((s,t)=>s+t.ayahs.length,0);
info.innerHTML=`📖 ${quran.length} آية | 📚 ${tt} مدخل تفسيري`;
updateBmBar();updateProgress();updateBmCount();render();
await loadFromCloud();
}

function searchTafsir(k,kw,sur){
const res=[];const t=tafsirs[k];
if(!t||t.ayahs.length===0)return res;
t.ayahs.forEach(a=>{
if(sur!=='all'&&a.surah!=sur)return;
if(kw&&!match(a.text,kw))return;
res.push({tk:k,tl:t.l,ti:t.i,surah:a.surah,number:a.number,text:a.text});
});
return res;
}
function doSearch(){
curKW=document.getElementById('q').value.trim();
curSrc=document.getElementById('src').value;
curSur=document.getElementById('surah').value;
const sa=document.getElementById('ayah').value;
if(curSrc==='quran'&&curSur!=='all'&&sa!=='all'){
focusAyah=parseInt(sa);curAyah='all';
const src=quran.filter(a=>a.surah==parseInt(curSur));
const i=src.findIndex(a=>a.ayah===focusAyah);
page=i>=0?Math.floor(i/perPage)+1:1;
}else{focusAyah=null;curAyah=sa;page=1}
render();
}
function attachTap(){document.querySelectorAll('.card').forEach(c=>{c.addEventListener('click',function(e){if(e.target.tagName==='BUTTON'||e.target.closest('button'))return;if(locked)return;this.classList.add('temp-hl');const self=this;setTimeout(()=>self.classList.remove('temp-hl'),1500);});});}
function render(){
const c=document.getElementById('results');
const pe=document.getElementById('pages');
const ie=document.getElementById('resInfo');
const tb=document.getElementById('tbar');
let items=[],isT=false;
const searchMode=(curKW&&curKW.length>0)||(curAyah!=='all');
if(curSrc==='quran'){
let s=quran;
if(curSur!=='all'){const x=parseInt(curSur);s=s.filter(a=>a.surah==x)}
if(curAyah!=='all'){const x=parseInt(curAyah);s=s.filter(a=>a.ayah==x)}
if(curKW)s=s.filter(a=>match(a.text,curKW));
items=s;
}else if(curSrc==='all_tafsirs'){isT=true;Object.keys(tafsirs).forEach(k=>items.push(...searchTafsir(k,curKW,curSur)));}
else{isT=true;items=searchTafsir(curSrc.replace('tafsir_',''),curKW,curSur);}
tb.style.display=curSrc==='quran'?'flex':'none';
const tp=Math.max(1,Math.ceil(items.length/perPage));
if(page>tp)page=tp;
const paged=items.slice((page-1)*perPage,page*perPage);
ie.textContent=`📊 ${items.length} نتيجة | صفحة ${page}/${tp}`;
if(paged.length===0){c.innerHTML='<div class="empty">📭 لا توجد نتائج</div>';pe.innerHTML='';return;}
if(isT){
c.innerHTML=paged.map(i=>{const sn=SURAHS[i.surah-1]||'؟';return `<div class="card"><div class="card-head"><span class="ref">${i.ti} ${i.tl} - ${sn} - آية ${i.number}</span><span class="type">تفسير</span></div><div class="tafsir-text">${hl(i.text,curKW)}</div></div>`;}).join('');
}else{
c.innerHTML=paged.map(item=>{
const sn=SURAHS[item.surah-1]||'؟';
const at=hl(item.text,curKW);
const marked=isBm(item.surah,item.ayah);
const hs=hasSP(item.surah,item.ayah);
const sl=getSP(item.surah,item.ayah);
let tB='',cB='';
if(showTafsir){let cf=0;TAFSIRS.forEach(cfg=>{const t=tafsirs[cfg.k];if(!t||t.ayahs.length===0)return;const m=t.ayahs.find(x=>x.surah==item.surah&&x.number==item.ayah);if(m&&m.text){cf++;tB+=`<div class="tafsir-block"><h4>${t.i} ${t.l}</h4><div class="tafsir-text">${hl(m.text,curKW)}</div></div>`}});if(cf>0)cB=`<span class="tc">📚 ${cf}</span>`;}
const bR=marked?'<div class="ribbon-bm">🔖 آخر قراءة</div>':'';
const sR=hs?`<div class="ribbon-sp">📌 ${sl.join(' · ')}</div>`:'';
const scB=searchMode?`<button class="show-ctx" onclick="showFullSurah(${item.surah},${item.ayah})">📖 عرض</button>`:'';
return `<div class="card ${marked?'bookmarked':''}" id="ayah-${item.surah}-${item.ayah}">${bR}${sR}<div class="card-head"><span class="ref">سورة ${sn} - آية ${item.ayah}</span><div class="head-right">${cB}${scB}<span class="type">آية</span><button class="btn-icon sp-btn ${hs?'has':''}" onclick="openLabel(${item.surah},${item.ayah})">📌</button><button class="btn-icon bm-btn ${marked?'active':''}" onclick="toggleBm(${item.surah},${item.ayah})">🔖</button></div></div><div class="ayah-text">${at}</div>${tB}</div>`;
}).join('');
}
let ph='';
if(tp>1){
if(page>1)ph+=`<a data-page="${page-1}">⬅ السابق</a>`;
for(let i=Math.max(1,page-2);i<=Math.min(tp,page+2);i++)ph+=i===page?`<span class="current">${i}</span>`:`<a data-page="${i}">${i}</a>`;
if(page<tp)ph+=`<a data-page="${page+1}">التالي ➡</a>`;
}
pe.innerHTML=ph;
pe.querySelectorAll('a[data-page]').forEach(a=>{a.addEventListener('click',e=>{e.preventDefault();page=parseInt(a.dataset.page);focusAyah=null;render();window.scrollTo({top:0,behavior:'smooth'});});});
if(focusAyah&&curSur!=='all'){setTimeout(()=>{const el=document.getElementById('ayah-'+curSur+'-'+focusAyah);if(el){el.scrollIntoView({behavior:'smooth',block:'center'});el.classList.add('focused');setTimeout(()=>el.classList.remove('focused'),3000)}},400);}
setTimeout(attachTap,100);
}

// ============ الملاحظات ============
function saveNotesToStorage(){localStorage.setItem('quranNotes',JSON.stringify(allNotes));syncToCloud();}
function openNotes(){_savedScroll=window.scrollY||0;renderNotes();openModal('notesOv');}
function renderNotes(){
const c=document.getElementById('notesList');
if(allNotes.length===0){c.innerHTML='<div style="text-align:center;padding:30px;color:var(--ink2)">📭 لا توجد ملاحظات<br><br>اكتب ملاحظتك أعلاه واضغط إضافة</div>';return;}
const sorted=[...allNotes].sort((a,b)=>b.created-a.created);
c.innerHTML=sorted.map(n=>{const d=new Date(n.created);const dateStr=`${d.getDate()} ${SHAMI_MONTHS[d.getMonth()]} ${d.getFullYear()} - ${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;return `<div class="note-item"><div style="flex:1"><div class="txt">${escapeHtml(n.text)}</div><div class="date">🕐 ${dateStr}</div></div><button class="del" onclick="delNote('${n.id}')">🗑️</button></div>`;}).join('');
}
function escapeHtml(text){const div=document.createElement('div');div.textContent=text;return div.innerHTML;}
function saveNote(){
const txt=document.getElementById('noteIn').value.trim();
if(!txt){alert('❌ اكتب ملاحظة أولاً');return;}
allNotes.push({id:String(Date.now())+'_'+Math.random().toString(36).slice(2,8),text:txt,created:Date.now()});
saveNotesToStorage();
document.getElementById('noteIn').value='';
renderNotes();
toast('تمت إضافة الملاحظة 📝','info',2000);
}
function delNote(id){
if(!confirm('حذف هذه الملاحظة؟'))return;
allNotes=allNotes.filter(n=>n.id!==id);
saveNotesToStorage();renderNotes();toast('تم الحذف','warn',2000);
}

// ============ التوقيت والتاريخ ============
function openTimeDisplay(){
_savedScroll=window.scrollY||0;
updateTimeDisplay();
openModal('timeOv');
if(timeInterval)clearInterval(timeInterval);
timeInterval=setInterval(updateTimeDisplay,1000);
}
function updateTimeDisplay(){
const el=document.getElementById('timeDisplay');if(!el)return;
const now=new Date();
const hours=String(now.getHours()).padStart(2,'0');
const minutes=String(now.getMinutes()).padStart(2,'0');
const seconds=String(now.getSeconds()).padStart(2,'0');
const gregDay=now.getDate();
const gregMonth=now.getMonth();
const gregYear=now.getFullYear();
const shamiMonth=SHAMI_MONTHS[gregMonth];
const gregMonthNum=gregMonth+1;
const weekDays=['الأحد','الإثنين','الثلاثاء','الأربعاء','الخميس','الجمعة','السبت'];
const weekDay=weekDays[now.getDay()];

let hijriDay='—',hijriMonth='—',hijriYear='—',hijriMonthNum='—',hijriWeekDay=weekDay;
try{
const parts=new Intl.DateTimeFormat('en-US-u-ca-islamic-umalqura',{
day:'numeric',month:'numeric',year:'numeric'
}).formatToParts(now);
parts.forEach(p=>{
if(p.type==='day')hijriDay=p.value;
if(p.type==='month')hijriMonthNum=p.value;
if(p.type==='year')hijriYear=p.value.replace(/[^\d]/g,'');
});
hijriDay=String(hijriDay).replace(/[٠-٩]/g,d=>'٠١٢٣٤٥٦٧٨٩'.indexOf(d));
hijriMonthNum=String(hijriMonthNum).replace(/[٠-٩]/g,d=>'٠١٢٣٤٥٦٧٨٩'.indexOf(d));
hijriYear=String(hijriYear).replace(/[٠-٩]/g,d=>'٠١٢٣٤٥٦٧٨٩'.indexOf(d));
const mNum=parseInt(hijriMonthNum);
if(!isNaN(mNum)&&mNum>=1&&mNum<=12){
hijriMonth=HIJRI_MONTHS[mNum-1];
}else{
try{
const arMonth=new Intl.DateTimeFormat('ar-SA-u-ca-islamic-umalqura',{month:'long'}).format(now);
const clean=arMonth.replace(/[^\u0600-\u06FF\s]/g,'').trim();
const idx=HIJRI_MONTHS.findIndex(m=>clean.includes(m)||m.includes(clean));
if(idx>=0){hijriMonth=HIJRI_MONTHS[idx];hijriMonthNum=String(idx+1);}
else{hijriMonth=clean||'—';hijriMonthNum='—';}
}catch(e2){hijriMonth='—';hijriMonthNum='—';}
}
}catch(e){
hijriDay='—';hijriMonth='—';hijriYear='—';
}

el.innerHTML=`
<div class="time-display">
<div style="font-size:.85rem;color:var(--ink2);font-weight:700">⏰ الساعة الآن</div>
<div class="time-big">${hours}<span class="time-sec">:${minutes}:${seconds}</span></div>
</div>
<div class="date-box">
<div class="lbl">📅 التاريخ الهجري</div>
<div class="val">${hijriWeekDay} ${hijriDay} ${hijriMonth} ${hijriYear} هـ</div>
<div class="num">(${hijriDay}/${hijriMonthNum}/${hijriYear})</div>
</div>
<div class="date-box">
<div class="lbl">📅 التاريخ الميلادي (الشامي)</div>
<div class="val">${weekDay} ${gregDay} ${shamiMonth} ${gregYear} م</div>
<div class="num">(${gregDay}/${gregMonthNum}/${gregYear})</div>
</div>
`;
}

// ============ المسبحة ============
function saveTasbihToStorage(){localStorage.setItem('tasbihState',JSON.stringify(tasbihState));syncToCloud();}
function openTasbih(){
_savedScroll=window.scrollY||0;
renderTasbih();
openModal('tasbihOv');
}
function renderTasbih(){
const c=document.getElementById('tasbihContent');
if(!c)return;
const cur=ADHKAR[tasbihState.dhikrIdx]||ADHKAR[0];
const prog=tasbihState.target>0?Math.min(100,(tasbihState.count/tasbihState.target)*100):0;
c.innerHTML=`
<div class="tasbih-body">
<div class="tasbih-dhikr">${cur.d}</div>
<div class="tasbih-fadl">${cur.f}</div>
<div class="tasbih-dhikr-tabs">
${ADHKAR.map((a,i)=>`<button class="tasbih-tab ${i===tasbihState.dhikrIdx?'active':''}" onclick="switchDhikr(${i})">${a.n}</button>`).join('')}
</div>
<div class="tasbih-counter" id="tasbihCounter" onclick="tasbihCount()">
<div>
<div class="tasbih-num" id="tasbihNum">${tasbihState.count}</div>
<div class="tasbih-target">الهدف: ${tasbihState.target}</div>
</div>
</div>
<div class="tasbih-progress">
<div class="tasbih-fill" style="width:${prog}%"></div>
</div>
<div class="tasbih-actions">
<button class="tasbih-reset" onclick="resetTasbih()">🔄 تصفير</button>
<button class="tasbih-switch" onclick="changeTarget()">🎯 تغيير الهدف</button>
</div>
<div class="tasbih-total">المجموع الكلي: <strong>${tasbihState.total}</strong></div>
</div>
`;
}
function tasbihCount(){
tasbihState.count++;tasbihState.total++;
const cur=ADHKAR[tasbihState.dhikrIdx]||ADHKAR[0];
if(tasbihState.count===cur.t){
toast('🎉 أكملت '+cur.t+' مرة من '+cur.n,'info',3000);
}
saveTasbihToStorage();
renderTasbih();
const el=document.getElementById('tasbihCounter');
if(el){el.classList.add('pulse');setTimeout(()=>el.classList.remove('pulse'),300);}
if(navigator.vibrate)navigator.vibrate(20);
}
function resetTasbih(){
if(!confirm('تصفير العدّاد الحالي؟'))return;
tasbihState.count=0;saveTasbihToStorage();renderTasbih();toast('تم التصفير','warn',1500);
}
function switchDhikr(i){
tasbihState.dhikrIdx=i;
tasbihState.target=ADHKAR[i].t;
tasbihState.count=0;
saveTasbihToStorage();renderTasbih();
}
function changeTarget(){
const t=prompt('أدخل الهدف الجديد:',tasbihState.target);
if(t&&!isNaN(t)&&parseInt(t)>0){
tasbihState.target=parseInt(t);saveTasbihToStorage();renderTasbih();
}
}

// ============ مواقيت الصلاة ============
let prayerTimesData=null;
function openPrayer(){_savedScroll=window.scrollY||0;openModal('prayerOv');if(userLoc){fetchPrayerTimes(userLoc.lat,userLoc.lng);}}
function showTab(name){
document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
const tab=document.getElementById('tab-'+name);
const content=document.getElementById('c-'+name);
if(tab)tab.classList.add('active');
if(content)content.classList.add('active');
if(name==='qibla'&&userLoc){updateCompassUI();}
}
function requestLocation(){
if(!navigator.geolocation){alert('⚠️ المتصفح لا يدعم تحديد الموقع');return;}
const p=document.getElementById('prayerC');
if(p)p.innerHTML='<div style="text-align:center;padding:30px"><div style="font-size:3rem">⏳</div><p>جاري تحديد موقعك...</p></div>';
navigator.geolocation.getCurrentPosition(
pos=>{
userLoc={lat:pos.coords.latitude,lng:pos.coords.longitude};
localStorage.setItem('userLocation',JSON.stringify(userLoc));
const qs=document.getElementById('qStatus');
if(qs)qs.textContent='✅ تم تحديد الموقع';
fetchPrayerTimes(userLoc.lat,userLoc.lng);
updateCompassUI();
},
err=>{
const p=document.getElementById('prayerC');
if(p)p.innerHTML='<div style="text-align:center;padding:30px"><div style="font-size:3rem">❌</div><p>تعذر الحصول على الموقع</p><button class="pbtn" onclick="requestLocation()">🔄 إعادة المحاولة</button></div>';
},
{enableHighAccuracy:true,timeout:10000}
);
}
async function fetchPrayerTimes(lat,lng){
try{
const now=new Date();
const dateStr=`${now.getDate()}-${now.getMonth()+1}-${now.getFullYear()}`;
const r=await fetch(`https://api.aladhan.com/v1/timings/${dateStr}?latitude=${lat}&longitude=${lng}&method=3`);
const data=await r.json();
if(data.code===200){
prayerTimesData=data.data.timings;
renderPrayerTimes(prayerTimesData);
}
}catch(e){
const p=document.getElementById('prayerC');
if(p)p.innerHTML='<div style="text-align:center;padding:30px"><div style="font-size:3rem">⚠️</div><p>فشل جلب المواقيت</p><button class="pbtn" onclick="fetchPrayerTimes('+lat+','+lng+')">🔄 إعادة</button></div>';
}
}
function renderPrayerTimes(t){
const c=document.getElementById('prayerC');
if(!c)return;
const prayers=[
{k:'Fajr',n:'الفجر',i:'🌅'},
{k:'Dhuhr',n:'الظهر',i:'☀️'},
{k:'Asr',n:'العصر',i:'🌤️'},
{k:'Maghrib',n:'المغرب',i:'🌇'},
{k:'Isha',n:'العشاء',i:'🌙'}
];
const now=new Date();
const nowMin=now.getHours()*60+now.getMinutes();
let nextP=null;
let rows=prayers.map(p=>{
const time=t[p.k];
const [h,m]=time.split(':').map(Number);
const pMin=h*60+m;
const passed=nowMin>pMin;
if(!passed&&!nextP)nextP={...p,time};
return `<tr style="${passed?'opacity:.5':''}"><td>${p.i} ${p.n}</td><td style="font-family:'Courier New',monospace;font-weight:700;color:var(--gold)">${time}</td><td>${passed?'✅ فات':'⏳'}</td></tr>`;
}).join('');
c.innerHTML=`
<div class="pdate">
<div class="h">🕌 مواقيت الصلاة</div>
<div class="g">${new Date().toLocaleDateString('ar-SA')}</div>
</div>
<table style="margin-bottom:15px">
<thead><tr><th>الصلاة</th><th>الوقت</th><th>الحالة</th></tr></
  <script>
const APP_VERSION='v3.0';
const SURAHS=["الفاتحة","البقرة","آل عمران","النساء","المائدة","الأنعام","الأعراف","الأنفال","التوبة","يونس","هود","يوسف","الرعد","إبراهيم","الحجر","النحل","الإسراء","الكهف","مريم","طه","الأنبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجدة","الأحزاب","سبأ","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثية","الأحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعة","الحديد","المجادلة","الحشر","الممتحنة","الصف","الجمعة","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقة","المعارج","نوح","الجن","المزمل","المدثر","القيامة","الإنسان","المرسلات","النبأ","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الأعلى","الغاشية","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينة","الزلزلة","العاديات","القارعة","التكاثر","العصر","الهمزة","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الإخلاص","الفلق","الناس"];
const AYAH_COUNTS=[7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6];
const TOTAL=6236;
const TAFSIRS=[{k:'saadi',f:'tafsir_saadi.json',l:'تفسير السعدي',i:'📗'},{k:'ibn_kathir',f:'tafsir_ibn_kathir.json',l:'تفسير ابن كثير',i:'📘'}];
const COLORS=[{n:'بني',l:'#8B4513',d:'#5C2E0E'},{n:'ذهبي',l:'#D4AF37',d:'#8B6508'},{n:'أخضر',l:'#059669',d:'#064e3b'},{n:'أزرق',l:'#2563eb',d:'#1e3a8a'},{n:'أحمر',l:'#dc2626',d:'#7f1d1d'},{n:'بنفسجي',l:'#7c3aed',d:'#4c1d95'},{n:'برتقالي',l:'#ea580c',d:'#7c2d12'},{n:'أسود',l:'#374151',d:'#111827'}];
const QLABELS=['📌 وردي اليومي','💭 للتدبر','⭐ مهمة','📖 حفظ','🤲 دعاء','🔍 للبحث'];
const SAMPLE=[{surah:1,ayah:1,text:"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"},{surah:1,ayah:2,text:"الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"},{surah:103,ayah:1,text:"وَالْعَصْرِ"},{surah:112,ayah:1,text:"قُلْ هُوَ اللَّهُ أَحَدٌ"}];
const SHAMI_MONTHS=['كانون الثاني','شباط','آذار','نيسان','أيار','حزيران','تموز','آب','أيلول','تشرين الأول','تشرين الثاني','كانون الأول'];
const HIJRI_MONTHS=['محرم','صفر','ربيع الأول','ربيع الآخر','جمادى الأولى','جمادى الآخرة','رجب','شعبان','رمضان','شوال','ذو القعدة','ذو الحجة'];
const ADHKAR=[
{d:'سُبْحَانَ اللَّهِ',n:'سبحان الله',t:33,f:'من قالها 100 مرة حُطّت خطاياه'},
{d:'الْحَمْدُ لِلَّهِ',n:'الحمد لله',t:33,f:'الحمد لله تملأ الميزان'},
{d:'اللَّهُ أَكْبَرُ',n:'الله أكبر',t:33,f:'الله أكبر كبيراً'},
{d:'لَا إِلَٰهَ إِلَّا اللَّهُ',n:'لا إله إلا الله',t:100,f:'خير ما قاله النبيون'},
{d:'أَسْتَغْفِرُ اللَّهَ',n:'أستغفر الله',t:100,f:'من لزم الاستغفار جعل الله له من كل هم فرجاً'},
{d:'سُبْحَانَ اللَّهِ وَبِحَمْدِهِ',n:'سبحان الله وبحمده',t:100,f:'من قالها 100 مرة حُطّت خطاياه ولو كانت مثل زبد البحر'},
{d:'لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ',n:'لا حول ولا قوة إلا بالله',t:100,f:'كنز من كنوز الجنة'},
{d:'سُبْحَانَ اللَّهِ وَالْحَمْدُ لِلَّهِ وَلَا إِلَٰهَ إِلَّا اللَّهُ وَاللَّهُ أَكْبَرُ',n:'الباقيات الصالحات',t:100,f:'أفضل الكلام بعد القرآن'}
];

let quran=[],tafsirs={};
let curSrc='quran',curKW='',curSur='all',curAyah='all';
let page=1,showTafsir=false;
let bm=null,allBms=[],bmColorIdx=0,allNotes=[];
let pendSur=null,pendAyah=null,focusAyah=null;
let wakeLock=null,wakeWanted=false;
let locked=false,startTime=Date.now(),_savedScroll=0;
let userLoc=null,devHeading=null;
let syncUserId=null,isSyncing=false,timeInterval=null;
let tasbihState={dhikrIdx:0,count:0,target:33,total:0};
const perPage=10;

try{
if(localStorage.getItem('showTafsir')==='true')showTafsir=true;
if(localStorage.getItem('darkMode')==='true')document.body.classList.add('dark');
const bc=localStorage.getItem('bookmarkColor');if(bc)bmColorIdx=parseInt(bc);
const bms=localStorage.getItem('allBookmarks');if(bms)allBms=JSON.parse(bms);
const nt=localStorage.getItem('quranNotes');if(nt)allNotes=JSON.parse(nt);
if(localStorage.getItem('wakeLockWanted')==='true')wakeWanted=true;
const sl=localStorage.getItem('userLocation');if(sl)userLoc=JSON.parse(sl);
const ts=localStorage.getItem('tasbihState');
if(ts){
const p=JSON.parse(ts);
if(typeof p.dhikrIdx==='number')tasbihState.dhikrIdx=p.dhikrIdx;
if(typeof p.count==='number')tasbihState.count=p.count;
if(typeof p.target==='number')tasbihState.target=p.target;
if(typeof p.total==='number')tasbihState.total=p.total;
}
}catch(e){}

// ============ المزامنة السحابية ============
function getUserId(){
let id=localStorage.getItem('syncUserId');
if(!id||id.length<8){
const chars='ABCDEFGHJKLMNPQRSTUVWXYZ23456789';let n='';
for(let i=0;i<12;i++)n+=chars[Math.floor(Math.random()*chars.length)];
localStorage.setItem('syncUserId',n);id=n;
}
return id;
}
syncUserId=getUserId();

function setSyncStatus(state,text){
const icon=document.getElementById('syncStatusIcon');
const txt=document.getElementById('syncStatusText');
if(!icon||!txt)return;
const states={
ok:{i:'☁️',c:'#16a34a',bg:'rgba(22,163,74,.1)',bd:'#16a34a',t:text||'متزامن'},
syncing:{i:'⏳',c:'#2563eb',bg:'rgba(37,99,235,.1)',bd:'#3b82f6',t:text||'جاري المزامنة...'},
error:{i:'⚠️',c:'#dc2626',bg:'rgba(220,38,38,.1)',bd:'#dc2626',t:text||'خطأ في المزامنة'},
waiting:{i:'⏸️',c:'#f59e0b',bg:'rgba(245,158,11,.1)',bd:'#f59e0b',t:text||'بانتظار الاتصال'}
};
const s=states[state]||states.ok;
icon.textContent=s.i;
txt.textContent=s.t;
txt.style.color=s.c;
const bar=document.getElementById('syncBar');
if(bar){
bar.style.background=s.bg;
bar.style.borderColor=s.bd;
}
}

// [إصلاح 3] المزامنة باستخدام await لمنع تأخر الحفظ
async function syncToCloud(){
if(!window.fbReady||isSyncing)return;
isSyncing=true;
setSyncStatus('syncing');
try{
await window.fbSet(window.fbDoc(window.fbDB,'sync',syncUserId),{
bms:allBms,bm:bm,color:bmColorIdx,notes:allNotes,
dark:document.body.classList.contains('dark'),
tafsir:showTafsir,
tasbih:tasbihState,
updatedAt:Date.now()
});
console.log("☁️ Synced");
setSyncStatus('ok','متزامن ✓');
setTimeout(()=>{const t=document.getElementById('syncStatusText');if(t&&t.textContent==='متزامن ✓')setSyncStatus('ok','متزامن');},2000);
}catch(e){
console.error("Sync error:",e);
setSyncStatus('error');
}
isSyncing=false;
}

async function loadFromCloud(){
if(!window.fbReady){
setSyncStatus('waiting','جاري تهيئة Firebase...');
setTimeout(loadFromCloud,500);
return;
}
setSyncStatus('syncing','جاري التحميل من السحابة...');
try{
const snap=await window.fbGet(window.fbDoc(window.fbDB,'sync',syncUserId));
if(snap.exists()){
const data=snap.data();
if(data.bms)allBms=data.bms;
if(data.bm)bm=data.bm;
if(data.color!==undefined){bmColorIdx=data.color;applyColor();}
if(data.notes&&Array.isArray(data.notes))allNotes=data.notes;
if(data.tafsir!==undefined){showTafsir=data.tafsir;const cb=document.getElementById('showTafsir');if(cb)cb.checked=showTafsir;const h=document.getElementById('hint');if(h)h.textContent=showTafsir?'(ظاهرة)':'(مخفية)';}
if(data.dark!==undefined){if(data.dark)document.body.classList.add('dark');else document.body.classList.remove('dark');const btn=document.getElementById('darkBtn');if(btn)btn.textContent=data.dark?'☀️ نهاري':'🌙 ليلي';}
if(data.tasbih&&typeof data.tasbih==='object'){
tasbihState={...tasbihState,...data.tasbih};
localStorage.setItem('tasbihState',JSON.stringify(tasbihState));
}
localStorage.setItem('allBookmarks',JSON.stringify(allBms));
localStorage.setItem('quranNotes',JSON.stringify(allNotes));
if(bm)localStorage.setItem('quranBookmark',JSON.stringify(bm));
localStorage.setItem('bookmarkColor',bmColorIdx);
localStorage.setItem('showTafsir',showTafsir);
updateBmBar();updateProgress();updateBmCount();render();
console.log("☁️ Loaded from cloud");
setSyncStatus('ok','تم التحميل ✓');
setTimeout(()=>{const t=document.getElementById('syncStatusText');if(t&&t.textContent==='تم التحميل ✓')setSyncStatus('ok','متزامن');},2000);
}else{
console.log("🆕 New sync code — creating empty document");
setSyncStatus('syncing','إنشاء مستند جديد...');
await syncToCloud();
if(allBms.length>0||allNotes.length>0||bm){
setTimeout(()=>{
if(confirm('⚠️ هذا الجهاز يستخدم رمز مزامنة جديد.\n\nهل تريد نسخ الرمز الآن للاحتفاظ به؟\n\n(إذا كان لديك رمز قديم من جهاز آخر، استخدم "🔗 ربط جهاز آخر" في نافذة المزامنة)')){
openSync();
}
},2500);
}
}
}catch(e){
console.error("Load error:",e);
setSyncStatus('error','فشل التحميل');
}
}

function openSync(){
_savedScroll=window.scrollY||0;
document.getElementById('syncCode').value=syncUserId;
document.getElementById('syncIn').value='';
const bar=document.getElementById('syncBarCode');
if(bar)bar.textContent=syncUserId;
openModal('syncOv');
}
function copyCode(){
const code=syncUserId;
if(navigator.clipboard){
navigator.clipboard.writeText(code).then(()=>toast('✅ تم نسخ: '+code,'info',2500)).catch(()=>{
const el=document.getElementById('syncCode');
if(el){el.select();try{document.execCommand('copy');toast('✅ تم النسخ','info',2000);}catch(e){alert('الرمز: '+code);}}
});
}else{
const el=document.getElementById('syncCode');
if(el){el.select();try{document.execCommand('copy');toast('✅ تم النسخ','info',2000);}catch(e){alert('الرمز: '+code);}}
else alert('الرمز: '+code);
}
}
async function linkCode(){
const inp=document.getElementById('syncIn');
const newCode=(inp.value||'').trim().toUpperCase().replace(/[^A-Z0-9]/g,'');
if(!newCode||newCode.length<8){alert('❌ رمز غير صالح');return;}
localStorage.setItem('syncUserId',newCode);syncUserId=newCode;
const bar=document.getElementById('syncBarCode');
if(bar)bar.textContent=syncUserId;
alert('✅ تم الربط! جاري تحميل بياناتك...');
closeModal('syncOv');
await loadFromCloud();
}

function toast(msg,type='',dur=3000){
const c=document.getElementById('toastC');
const t=document.createElement('div');
t.className='toast '+(type||'');
let icon='✅';
if(type==='bookmark')icon='🔖';else if(type==='special')icon='📌';else if(type==='info')icon='☁️';else if(type==='warn')icon='⚠️';
t.innerHTML=`<span style="font-size:1.3rem">${icon}</span><span>${msg}</span>`;
c.appendChild(t);
setTimeout(()=>{if(t.parentNode)t.parentNode.removeChild(t)},dur);
}

setInterval(()=>{
const e=Math.floor((Date.now()-startTime)/1000);
const h=Math.floor(e/3600),m=Math.floor((e%3600)/60),s=e%60;
const p=n=>String(n).padStart(2,'0');
const el=document.getElementById('timer');
if(el)el.textContent=`${p(h)}:${p(m)}:${p(s)}`;
},1000);

// ============ قفل الشاشة ============
function toggleLock(){
if(locked){unlock();return}
locked=true;
document.body.classList.add('locked');
document.getElementById('lockOv').classList.add('active');
const lb=document.getElementById('lockBtn');if(lb){lb.textContent='🔓 فتح';lb.classList.add('active')}
const fab=document.getElementById('fab');if(fab){fab.textContent='🔓';fab.classList.add('locked','visible')}
const f=document.createElement('div');f.className='lock-float active';f.id='lockFloat';
f.innerHTML='<span>🔓</span><span>فتح الشاشة</span>';f.onclick=unlock;
document.body.appendChild(f);
toast('تم قفل الشاشة 🔒','info',2000);
}
function unlock(){
if(!locked)return;
locked=false;
document.body.classList.remove('locked');
document.getElementById('lockOv').classList.remove('active');
const lb=document.getElementById('lockBtn');if(lb){lb.textContent='🔒 قفل';lb.classList.remove('active')}
const fab=document.getElementById('fab');if(fab){fab.textContent='🔒';fab.classList.remove('locked')}
const f=document.getElementById('lockFloat');if(f)f.remove();
toast('تم فتح الشاشة 🔓','info',1500);
}
window.addEventListener('scroll',()=>{
const fab=document.getElementById('fab');if(!fab)return;
if(window.scrollY>200||locked)fab.classList.add('visible');else fab.classList.remove('visible');
});

// ============ إبقاء الشاشة مضيئة ============
async function reqWake(){
if(!('wakeLock' in navigator))return false;
try{wakeLock=await navigator.wakeLock.request('screen');return true}catch(e){return false}
}
async function toggleWake(){
if(!('wakeLock' in navigator)){alert('⚠️ غير مدعوم في هذا المتصفح');return}
const btn=document.getElementById('wakeBtn');
if(wakeWanted){
wakeWanted=false;localStorage.setItem('wakeLockWanted','false');
if(wakeLock){try{await wakeLock.release()}catch(e){}wakeLock=null}
if(btn){btn.textContent='☀️ إبقاء';btn.classList.remove('active')}
toast('تم الإيقاف','info',2000);
}else{
wakeWanted=true;localStorage.setItem('wakeLockWanted','true');
const ok=await reqWake();
if(ok){if(btn){btn.textContent='💡 مضيئة';btn.classList.add('active')}toast('تم التفعيل ☀️','info',2000)}
else{wakeWanted=false;localStorage.setItem('wakeLockWanted','false');alert('❌ تعذّر تفعيل الإبقاء')}
}
}
document.addEventListener('visibilitychange',async()=>{
if(document.visibilityState==='visible'&&wakeWanted)await reqWake();
});
if(wakeWanted){const btn=document.getElementById('wakeBtn');if(btn){btn.textContent='💡 مضيئة';btn.classList.add('active')}reqWake();}

// ============ النوافذ ============
function openModal(id){
_savedScroll=window.scrollY||0;
document.getElementById(id).classList.add('active');
document.body.style.overflow='hidden';
if(id==='aboutOv'){const el=document.getElementById('shareUrl');if(el)el.textContent=window.location.origin;}
}
function closeModal(id){
document.getElementById(id).classList.remove('active');
document.body.style.overflow='';
if(id==='timeOv'&&timeInterval){clearInterval(timeInterval);timeInterval=null;}
requestAnimationFrame(()=>{window.scrollTo(0,_savedScroll);});
setTimeout(()=>{window.scrollTo(0,_savedScroll);},30);
}
function closeModalOutside(e,id){if(e.target.id===id){closeModal(id);if(id==='welcomeOv')localStorage.setItem('appVersion',APP_VERSION);}}
document.addEventListener('keydown',e=>{
if(e.key==='Escape'){
['welcomeOv','helpOv','aboutOv','prayerOv','syncOv','colorOv','bmsOv','labelOv','timeOv','notesOv','tasbihOv'].forEach(id=>{closeModal(id);if(id==='welcomeOv')localStorage.setItem('appVersion',APP_VERSION);});
closeSidebar();
}
});
function closeWelcome(){closeModal('welcomeOv');localStorage.setItem('appVersion',APP_VERSION);}
setTimeout(()=>{const v=localStorage.getItem('appVersion')||'';if(v!==APP_VERSION){openModal('welcomeOv');}},800);

function toggleDark(){
document.body.classList.toggle('dark');
const d=document.body.classList.contains('dark');
localStorage.setItem('darkMode',d);
document.getElementById('darkBtn').textContent=d?'☀️ نهاري':'🌙 ليلي';
syncToCloud();
}
if(document.body.classList.contains('dark'))document.getElementById('darkBtn').textContent='☀️ نهاري';

function applyColor(){
const c=COLORS[bmColorIdx]||COLORS[0];
document.documentElement.style.setProperty('--bm',c.l);
document.documentElement.style.setProperty('--bmD',c.d);
localStorage.setItem('bookmarkColor',bmColorIdx);
}
function openColorPicker(){
_savedScroll=window.scrollY||0;
const g=document.getElementById('colorGrid');
g.innerHTML=COLORS.map((c,i)=>`<div class="color-opt ${i===bmColorIdx?'selected':''}" style="background:linear-gradient(180deg,${c.l},${c.d})" onclick="selectColor(${i})" title="${c.n}"></div>`).join('');
openModal('colorOv');
}
function selectColor(i){bmColorIdx=i;applyColor();closeModal('colorOv');syncToCloud();}

function shareTo(platform){
const url=window.location.origin;
const title='الموسوعة القرآنية';
const text='تطبيق رائع لقراءة القرآن مع التفاسير ومواقيت الصلاة';
switch(platform){
case 'whatsapp':window.open('https://wa.me/?text='+encodeURIComponent(text+'\n'+url),'_blank');break;
case 'telegram':window.open('https://t.me/share/url?url='+encodeURIComponent(url)+'&text='+encodeURIComponent(text),'_blank');break;
case 'facebook':window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(url),'_blank');break;
case 'twitter':window.open('https://twitter.com/intent/tweet?text='+encodeURIComponent(text)+'&url='+encodeURIComponent(url),'_blank');break;
case 'email':window.location.href='mailto:?subject='+encodeURIComponent(title)+'&body='+encodeURIComponent(text+'\n\n'+url);break;
case 'copy':
if(navigator.clipboard){navigator.clipboard.writeText(url).then(()=>toast('✅ تم نسخ الرابط','info',2000)).catch(()=>fallbackCopy(url));}
else fallbackCopy(url);
break;
}
}
function fallbackCopy(text){
const inp=document.createElement('input');inp.value=text;document.body.appendChild(inp);inp.select();
try{document.execCommand('copy');toast('✅ تم نسخ الرابط','info',2000);}catch(e){alert('انسخ يدوياً: '+text);}
inp.remove();
}

// ============ العلامات ============
function loadBm(){try{const s=localStorage.getItem('quranBookmark');if(s)bm=JSON.parse(s)}catch(e){bm=null}}
function saveBms(){localStorage.setItem('allBookmarks',JSON.stringify(allBms));updateBmCount();syncToCloud();}
function updateBmCount(){const e=document.getElementById('bmCount');if(e)e.textContent=allBms.length}
function clearBm(){
if(!confirm('حذف علامة آخر قراءة؟'))return;
const _y=window.scrollY||0;
bm=null;localStorage.removeItem('quranBookmark');
updateBmBar();focusAyah=null;render();
requestAnimationFrame(()=>window.scrollTo(0,_y));
toast('تم حذف العلامة','warn',2000);syncToCloud();
}
function toggleBm(s,a){
const oldBm=bm;
const isCurrentlyBm=bm&&bm.surah==s&&bm.ayah==a;
if(isCurrentlyBm){bm=null;localStorage.removeItem('quranBookmark');toast('تم إزالة العلامة','warn',2000);}
else{bm={surah:parseInt(s),ayah:parseInt(a),timestamp:Date.now()};localStorage.setItem('quranBookmark',JSON.stringify(bm));toast('تم الحفظ 🔖','bookmark',2000);}
updateBmBar();updateProgress();
if(oldBm){const oc=document.getElementById(`ayah-${oldBm.surah}-${oldBm.ayah}`);if(oc){oc.classList.remove('bookmarked');const r=oc.querySelector('.ribbon-bm');if(r)r.remove();const b=oc.querySelector('.bm-btn');if(b)b.classList.remove('active');}}
const card=document.getElementById(`ayah-${s}-${a}`);
if(card){if(bm){card.classList.add('bookmarked');if(!card.querySelector('.ribbon-bm')){const r=document.createElement('div');r.className='ribbon-bm';r.textContent='🔖 آخر قراءة';card.insertBefore(r,card.firstChild);}const b=card.querySelector('.bm-btn');if(b)b.classList.add('active');}else{card.classList.remove('bookmarked');const r=card.querySelector('.ribbon-bm');if(r)r.remove();const b=card.querySelector('.bm-btn');if(b)b.classList.remove('active');}}
else{render();}
syncToCloud();
}
function openLabel(s,a){
_savedScroll=window.scrollY||0;
pendSur=s;pendAyah=a;
const n=SURAHS[s-1]||'؟';
document.getElementById('labelRef').textContent='📍 سورة '+n+' - آية '+a;
document.getElementById('labelIn').value='';
document.getElementById('qlabels').innerHTML=QLABELS.map(l=>`<button onclick="document.getElementById('labelIn').value='${l}'">${l}</button>`).join('');
openModal('labelOv');
setTimeout(()=>document.getElementById('labelIn').focus(),100);
}
function saveLabel(){
const l=document.getElementById('labelIn').value.trim();
if(!l){alert('❌ أدخل اسماً');return}
if(pendSur===null||pendAyah===null)return;
const s=pendSur,a=pendAyah;
const _y=_savedScroll||window.scrollY||0;
allBms.push({id:String(Date.now())+'_'+Math.random().toString(36).slice(2,8),label:l,surah:s,ayah:a,created:Date.now()});
saveBms();updateProgress();closeModal('labelOv');render();
requestAnimationFrame(()=>window.scrollTo(0,_y));
setTimeout(()=>window.scrollTo(0,_y),180);
toast('تمت إضافة "'+l+'"','special',3000);
pendSur=null;pendAyah=null;
}
function hasSP(s,a){return allBms.some(b=>b.surah==s&&b.ayah==a)}
function getSP(s,a){return allBms.filter(b=>b.surah==s&&b.ayah==a).map(b=>b.label)}

function jumpToBmItem(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
closeModal('bmsOv');
document.getElementById('src').value='quran';
document.getElementById('surah').value=b.surah;
updateAyahDD(b.surah,'all');
document.getElementById('ayah').value='all';
document.getElementById('q').value='';
curSrc='quran';curSur=String(b.surah);curAyah='all';curKW='';
focusAyah=b.ayah;
const src=quran.filter(a=>a.surah==b.surah);
const i=src.findIndex(a=>a.ayah==b.ayah);
page=i>=0?Math.floor(i/perPage)+1:1;
render();
}

function setAsBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
bm={surah:b.surah,ayah:b.ayah,timestamp:Date.now()};
localStorage.setItem('quranBookmark',JSON.stringify(bm));
updateBmBar();updateProgress();
toast('تم تعيين "'+b.label+'" كآخر قراءة 🔖','bookmark',2000);
syncToCloud();
closeModal('bmsOv');
jumpToBm();
}

function delBm(id){
if(!confirm('حذف؟'))return;
const _y=window.scrollY||0;
allBms=allBms.filter(x=>String(x.id)!==String(id));
saveBms();updateProgress();openBookmarks();
requestAnimationFrame(()=>window.scrollTo(0,_y));
toast('تم الحذف','warn',2000);
}
function editBm(id){
const b=allBms.find(x=>String(x.id)===String(id));
if(!b)return;
const nl=prompt('تعديل الاسم:',b.label);
if(!nl||!nl.trim())return;
b.label=nl.trim();saveBms();openBookmarks();render();
}
function openBookmarks(){
_savedScroll=window.scrollY||0;
const c=document.getElementById('bmsList');
if(allBms.length===0){c.innerHTML='<div style="text-align:center;padding:30px;color:var(--ink2)">📭 لا توجد علامات.<br><br>اذهب لأي آية، اضغط 📌، واكتب اسماً.</div>';}
else{
const s=[...allBms].sort((a,b)=>a.surah-b.surah||a.ayah-b.ayah);
c.innerHTML=s.map(b=>{
const sn=SURAHS[b.surah-1]||'؟';
const isCurrentBm=bm&&bm.surah==b.surah&&bm.ayah==b.ayah;
return `<div class="bm-item"><div class="info"><div class="lbl">📌 ${b.label}${isCurrentBm?' <span style="background:#16a34a;color:#fff;padding:1px 6px;border-radius:8px;font-size:.65rem">🔖 الحالية</span>':''}</div><div style="font-size:.8rem;color:var(--ink2)">سورة ${sn} - آية ${b.ayah}</div></div><div class="act"><button class="jump" onclick="jumpToBmItem('${b.id}')" title="انتقال فقط">📖</button><button class="setbm" onclick="setAsBm('${b.id}')" title="تعيين كآخر قراءة">🔖</button><button class="edit" onclick="editBm('${b.id}')" title="تعديل">✏️</button><button class="del" onclick="delBm('${b.id}')" title="حذف">🗑️</button></div></div>`;
}).join('');
}
openModal('bmsOv');
}

// [إصلاح 2] حساب نسبة الختمة بدقة
function updateProgress(){
    // نعتمد على علامة "آخر قراءة" (bm) لحساب أين وصل المستخدم
    let currentSurah = bm ? bm.surah : 1;
@@ -1566,3 +2599,4 @@ <h2>📌 إضافة علامة</h2>
</script>
</body>
</html>
.guide-note{background:rgba(16,185,129,.1);border:1px dashed #10b981;padding:
