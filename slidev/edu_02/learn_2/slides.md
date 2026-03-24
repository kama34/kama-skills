---
theme: default
colorSchema: light
transition: fade
aspectRatio: "16/9"
fonts:
  heading: Outfit
  body: DM Sans
  mono: JetBrains Mono
css: styles/index.css
---

<!-- ============================================================ -->
<!-- SLIDE 1 — COVER (cover-hero, bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-b">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">Кафедра цифровых технологий · 2025</span>
  <h1 style="font-size:3.4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;">AI в образовании:<br>от хайпа к реальным результатам</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Лекция для преподавателей вузов</p>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.65);font-size:1rem;">
    <span>НИУ ВШЭ</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Лекция · 45 мин</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>2025</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 2 — STAT-HERO: 73% студентов (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 100px;">
  <div class="stat-hero" style="font-size:6rem;">73%</div>
  <p style="font-size:1.5rem;color:var(--color-text);margin:12px 0 8px;font-family:var(--font-body);font-weight:500;">студентов уже используют AI-инструменты</p>
  <p style="font-size:1.1rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);">ChatGPT, Claude, Perplexity — ТОП-3 инструментов по данным НИУ ВШЭ, 2025</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">НИУ ВШЭ, 2025</span>
    <span class="label-pill">+31% за год</span>
    <span class="label-pill">42% преп. не знают</span>
  </div>
</div>
<div class="stat-footer-band">
  <span style="font-size:0.85rem;color:var(--color-muted);">Источник: Центр социологии высшего образования НИУ ВШЭ · Всероссийский опрос студентов, n=4 200</span>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 3 — TWO-COL-TEXT: Старая модель vs новая (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);">Старая модель vs. новая реальность</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-content:center;">
    <div>
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:24px 28px;height:100%;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;">
          <div class="icon-ghost" style="width:36px;height:36px;border-color:rgba(var(--text-rgb),0.15);">
            <span style="font-size:1rem;">📋</span>
          </div>
          <span style="font-size:0.75rem;font-weight:700;color:var(--color-muted);text-transform:uppercase;letter-spacing:0.1em;">Традиционная модель</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:14px;">
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-muted);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">Лекция</span>
          </div>
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-muted);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">Конспект</span>
          </div>
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-muted);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">Экзамен</span>
          </div>
          <div style="margin-top:8px;padding:10px 14px;background:rgba(var(--text-rgb),0.04);border-radius:8px;">
            <span style="font-size:0.95rem;color:var(--color-muted);">Фокус: <strong style="color:var(--color-text);">запоминание</strong></span>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.07),rgba(var(--accent-rgb),0.02));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:24px 28px;height:100%;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px;">
          <div class="icon-circle" style="width:36px;height:36px;">
            <span style="font-size:1rem;">🚀</span>
          </div>
          <span style="font-size:0.75rem;font-weight:700;color:var(--color-accent);text-transform:uppercase;letter-spacing:0.1em;">Новая реальность</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:14px;">
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-accent);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">AI-ассистент</span>
          </div>
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-accent);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">Проект</span>
          </div>
          <div style="display:flex;align-items:center;gap:12px;">
            <span style="color:var(--color-accent);font-size:1.1rem;">→</span>
            <span style="font-size:1.05rem;color:var(--color-text);">Портфолио</span>
          </div>
          <div style="margin-top:8px;padding:10px 14px;background:rgba(var(--accent-rgb),0.08);border-radius:8px;">
            <span style="font-size:0.95rem;color:var(--color-text);">Фокус: <strong style="color:var(--color-accent);">применение</strong></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 4 — SECTION DIVIDER: Три модели интеграции (bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="section-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.70);font-weight:600;margin-bottom:16px;">Часть 1</span>
  <h1 style="font-size:3.5rem;font-weight:800;color:#ffffff;margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">3 модели<br>повышают успеваемость на 15%</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.80);max-width:700px;line-height:1.6;font-family:var(--font-body);">Интеграция AI в учебный процесс: от тьютора до предмета изучения</p>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 5 — BENTO-GRID: AI как тьютор (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Модель 1: AI как тьютор</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;min-height:280px;">
    <!-- Featured card -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <div class="icon-circle" style="width:48px;height:48px;">
          <span style="font-size:1.4rem;">🧑‍💻</span>
        </div>
        <span style="font-size:0.75rem;font-weight:700;color:var(--color-accent);text-transform:uppercase;letter-spacing:0.1em;">Персонализация</span>
      </div>
      <p style="font-size:1.1rem;color:var(--color-text);line-height:1.5;margin:0 0 16px;">Адаптивные траектории обучения под уровень каждого студента</p>
      <div style="display:flex;align-items:baseline;gap:8px;">
        <span style="font-size:2.2rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">+15%</span>
        <span class="stat-caption" style="font-size:1rem;">успеваемость по данным Carnegie Learning</span>
      </div>
    </div>
    <!-- Card 2 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded" style="width:40px;height:40px;flex-shrink:0;">
        <span style="font-size:1.1rem;">⚡</span>
      </div>
      <div>
        <span style="display:block;font-size:1rem;font-weight:600;color:var(--color-text);">Обратная связь 24/7</span>
        <span style="font-size:0.9rem;color:var(--color-muted);">Мгновенные ответы без ожидания</span>
      </div>
    </div>
    <!-- Card 3 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-ghost" style="width:40px;height:40px;flex-shrink:0;">
        <span style="font-size:1.1rem;">🎯</span>
      </div>
      <div>
        <span style="display:block;font-size:1rem;font-weight:600;color:var(--color-text);">Адаптивные задания</span>
        <span style="font-size:0.9rem;color:var(--color-muted);">Сложность под уровень студента</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 6 — ICON-TRIO: AI как соавтор (bg-alt) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Модель 2: AI как соавтор</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:48px;">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
      <div class="icon-circle" style="width:72px;height:72px;margin-bottom:16px;">
        <span style="font-size:2rem;">✍️</span>
      </div>
      <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Совместное письмо</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Написание текстов и кода вместе с AI</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
      <div class="icon-rounded" style="width:72px;height:72px;margin-bottom:16px;">
        <span style="font-size:2rem;">🔍</span>
      </div>
      <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Критический анализ</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Проверка и оценка AI-выводов</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
      <div class="icon-ghost" style="width:72px;height:72px;margin-bottom:16px;">
        <span style="font-size:2rem;">💬</span>
      </div>
      <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Промпт-инженерия</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Навык точного формулирования задач</span>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 7 — CARD-MOSAIC: AI как предмет (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Модель 3: AI как предмет изучения</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <!-- Card 1 solid -->
    <div class="card-solid" style="display:flex;align-items:flex-start;gap:14px;">
      <div class="icon-circle" style="width:44px;height:44px;flex-shrink:0;margin-top:2px;">
        <span style="font-size:1.2rem;">⚖️</span>
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:700;color:var(--color-text);margin-bottom:4px;">Этика AI</span>
        <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Курсы по ответственному использованию и социальным последствиям</span>
      </div>
    </div>
    <!-- Card 2 ghost -->
    <div class="card-ghost" style="display:flex;align-items:flex-start;gap:14px;">
      <div class="icon-rounded" style="width:44px;height:44px;flex-shrink:0;margin-top:2px;">
        <span style="font-size:1.2rem;">🛡️</span>
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:700;color:var(--color-text);margin-bottom:4px;">Ограничения моделей</span>
        <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Понимание того, как и почему AI ошибается</span>
      </div>
    </div>
    <!-- Card 3 solid -->
    <div class="card-solid" style="display:flex;align-items:flex-start;gap:14px;">
      <div class="icon-ghost" style="width:44px;height:44px;flex-shrink:0;margin-top:2px;">
        <span style="font-size:1.2rem;">🔎</span>
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:700;color:var(--color-text);margin-bottom:4px;">Распознавание галлюцинаций</span>
        <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Верификация AI-выводов через первичные источники</span>
      </div>
    </div>
    <!-- Card 4 accent -->
    <div class="card-accent" style="display:flex;align-items:flex-start;gap:14px;">
      <div class="icon-circle" style="width:44px;height:44px;flex-shrink:0;margin-top:2px;">
        <span style="font-size:1.2rem;">🌐</span>
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:700;color:var(--color-text);margin-bottom:4px;">Цифровое гражданство</span>
        <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Предвзятости алгоритмов и влияние на общество</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 8 — STAT-HERO: 87% работодателей (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 100px;">
  <div class="stat-hero" style="font-size:6rem;">87%</div>
  <p style="font-size:1.5rem;color:var(--color-text);margin:12px 0 8px;font-family:var(--font-body);font-weight:500;">работодателей ждут AI-навыки от выпускников</p>
  <p style="font-size:1.1rem;color:var(--color-muted);margin:0 0 20px;">Опрос HeadHunter, 2025 · 3 800 компаний-участников</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-bottom:8px;">
    <span class="label-pill">Промпт-инженерия</span>
    <span class="label-pill">Анализ данных</span>
    <span class="label-pill">Автоматизация</span>
  </div>
  <p style="font-size:1rem;color:var(--color-muted);margin-top:8px;">Только <strong style="color:var(--color-accent);">12%</strong> образовательных программ включают AI</p>
</div>
<div class="stat-footer-band">
  <span style="font-size:0.85rem;color:var(--color-muted);">Разрыв между спросом рынка и предложением вузов: <strong style="color:var(--color-text);">75 процентных пунктов</strong></span>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 9 — SECTION DIVIDER: Практические инструменты (bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="section-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.70);font-weight:600;margin-bottom:16px;">Часть 2</span>
  <h1 style="font-size:3.5rem;font-weight:800;color:#ffffff;margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Практические инструменты<br>уже доступны сегодня</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.80);max-width:700px;line-height:1.6;font-family:var(--font-body);">Что конкретно делать с понедельника</p>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 10 — BENTO-GRID: Набор инструментов (bg-alt) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Набор инструментов преподавателя</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;min-height:280px;">
    <!-- Featured: Генерация тестов -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <div class="icon-circle" style="width:48px;height:48px;">
          <span style="font-size:1.4rem;">🤖</span>
        </div>
        <span style="font-size:0.75rem;font-weight:700;color:var(--color-accent);text-transform:uppercase;letter-spacing:0.1em;">Генерация тестов</span>
      </div>
      <p style="font-size:1.05rem;color:var(--color-text);line-height:1.5;margin:0 0 12px;">Claude + структурированный промпт: создайте 20 вопросов за 3 минуты</p>
      <code style="font-size:0.85rem;color:var(--color-accent);background:rgba(var(--accent-rgb),0.08);padding:8px 12px;border-radius:8px;font-family:var(--font-body);">«Составь тест по теме X на уровень B2»</code>
    </div>
    <!-- Turnitin -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded" style="width:40px;height:40px;flex-shrink:0;">
        <span style="font-size:1.1rem;">🛡️</span>
      </div>
      <div>
        <span style="display:block;font-size:0.95rem;font-weight:600;color:var(--color-text);">Проверка работ</span>
        <span style="font-size:0.85rem;color:var(--color-muted);">Turnitin AI + ручной анализ</span>
      </div>
    </div>
    <!-- Аналитика -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-ghost" style="width:40px;height:40px;flex-shrink:0;">
        <span style="font-size:1.1rem;">📊</span>
      </div>
      <div>
        <span style="display:block;font-size:0.95rem;font-weight:600;color:var(--color-text);">Аналитика прогресса</span>
        <span style="font-size:0.85rem;color:var(--color-muted);">Дашборды LMS · Knewton Alta</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 11 — TIMELINE-HORIZONTAL: Пошаговый план (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Пошаговый план на семестр</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Нед. 1–2 · Старт</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">AI-грамотность для студентов</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Знакомство с инструментами, этика, базовый промптинг</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Нед. 3–8 · Практика</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">AI-ассистированные проекты</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Интеграция в реальные задания курса</span>
    </div>
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.07),rgba(var(--accent-rgb),0.02));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Нед. 9–12 · Анализ</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Критический анализ результатов</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Оценка качества AI-выводов, исправление ошибок</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Нед. 13–14 · Итог</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Защита проектов с AI-компонентом</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Публичная презентация + рефлексия</span>
    </div>
  </div>
  <div style="display:flex;justify-content:center;gap:32px;margin-top:12px;padding:10px 0;border-top:1px solid var(--color-surface-border);">
    <span style="font-size:0.8rem;color:var(--color-muted);">📅 14 недель</span>
    <span style="font-size:0.8rem;color:var(--color-muted);">·</span>
    <span style="font-size:0.8rem;color:var(--color-muted);">🎯 4 этапа</span>
    <span style="font-size:0.8rem;color:var(--color-muted);">·</span>
    <span style="font-size:0.8rem;color:var(--color-accent);font-weight:600;">Старт: 1 сентября</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 12 — TWO-COL-TEXT: Риски (bg-base) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);">Риски, которые нельзя игнорировать</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-content:start;">
    <!-- Left: Risks list -->
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:flex-start;gap:14px;background:rgba(220,53,69,0.05);border:1.5px solid rgba(220,53,69,0.20);border-radius:12px;padding:16px 18px;">
        <div style="width:36px;height:36px;border-radius:8px;background:rgba(220,53,69,0.10);border:1px solid rgba(220,53,69,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-size:1rem;">📋</span>
        </div>
        <div>
          <span style="display:block;font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:3px;">Плагиат и академическая честность</span>
          <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Размытые границы авторства требуют новых политик</span>
        </div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:14px;background:rgba(220,53,69,0.05);border:1.5px solid rgba(220,53,69,0.20);border-radius:12px;padding:16px 18px;">
        <div style="width:36px;height:36px;border-radius:8px;background:rgba(220,53,69,0.10);border:1px solid rgba(220,53,69,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-size:1rem;">🔗</span>
        </div>
        <div>
          <span style="display:block;font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:3px;">Зависимость без понимания основ</span>
          <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Студенты используют AI как костыль вместо инструмента</span>
        </div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:14px;background:rgba(220,53,69,0.05);border:1.5px solid rgba(220,53,69,0.20);border-radius:12px;padding:16px 18px;">
        <div style="width:36px;height:36px;border-radius:8px;background:rgba(220,53,69,0.10);border:1px solid rgba(220,53,69,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-size:1rem;">⚖️</span>
        </div>
        <div>
          <span style="display:block;font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:3px;">Неравный доступ к инструментам</span>
          <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.4;">Цифровое неравенство усиливает социальные разрывы</span>
        </div>
      </div>
    </div>
    <!-- Right: Mitigations -->
    <div style="display:flex;flex-direction:column;justify-content:center;gap:14px;">
      <div style="background:rgba(var(--accent-rgb),0.06);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:18px 20px;">
        <span style="display:block;font-size:0.7rem;font-weight:700;color:var(--color-accent);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:10px;">Как снизить риски</span>
        <div style="display:flex;flex-direction:column;gap:8px;">
          <div style="display:flex;align-items:center;gap:8px;">
            <span style="color:var(--color-accent);font-size:0.9rem;font-weight:700;">✓</span>
            <span style="font-size:0.95rem;color:var(--color-text);">Явная политика использования AI в слайлабусе</span>
          </div>
          <div style="display:flex;align-items:center;gap:8px;">
            <span style="color:var(--color-accent);font-size:0.9rem;font-weight:700;">✓</span>
            <span style="font-size:0.95rem;color:var(--color-text);">Задания с рефлексией и обоснованием выборов</span>
          </div>
          <div style="display:flex;align-items:center;gap:8px;">
            <span style="color:var(--color-accent);font-size:0.9rem;font-weight:700;">✓</span>
            <span style="font-size:0.95rem;color:var(--color-text);">Бесплатные университетские лицензии ChatGPT Edu</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 13 — STAT-HERO: Стоимость бездействия (bg-alt) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 100px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">Цена промедления</span>
  <p style="font-size:1.4rem;font-weight:600;color:var(--color-text);margin:0 0 4px;font-family:var(--font-heading);">Каждый месяц без AI-интеграции —</p>
  <div class="stat-hero" style="font-size:5rem;margin-bottom:4px;">потерянный семестр</div>
  <p style="font-size:1.1rem;color:var(--color-muted);max-width:640px;margin:8px auto 24px;line-height:1.5;">Студенты уже применяют AI бесконтрольно. Без методологии — хаотичное использование. Онлайн-школы уже внедрили.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">73% студентов уже внутри</span>
    <span class="label-pill">Конкуренты не ждут</span>
    <span class="label-pill">Разрыв растёт</span>
  </div>
</div>
<div class="stat-footer-band">
  <span style="font-size:0.85rem;color:var(--color-muted);">Стэнфорд, MIT, ВШЭ: программы AI-интеграции уже запущены · <strong style="color:var(--color-text);">Ваш вуз следующий?</strong></span>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 14 — CTA: Начните с одного курса (bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-c">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;" class="cta-variant-left">
  <span class="label-pill-cover" style="margin-bottom:24px;">Открытый пилот · Осенний семестр 2025</span>
  <h1 style="font-size:2.8rem;font-weight:800;color:#ffffff;margin:0 0 28px;font-family:var(--font-heading);line-height:1.15;">Начните с одного курса —<br>присоединяйтесь к пилоту</h1>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:540px;margin-bottom:32px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.20);border-radius:12px;padding:12px 16px;">
      <div class="icon-container-cover" style="width:36px;height:36px;flex-shrink:0;">
        <span style="font-size:1rem;">🎓</span>
      </div>
      <span style="font-size:1.05rem;color:#ffffff;">10 курсов в осеннем семестре · любые кафедры</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.20);border-radius:12px;padding:12px 16px;">
      <div class="icon-container-cover" style="width:36px;height:36px;flex-shrink:0;">
        <span style="font-size:1rem;">🛠️</span>
      </div>
      <span style="font-size:1.05rem;color:#ffffff;">Методическая поддержка + готовые шаблоны</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.20);border-radius:12px;padding:12px 16px;">
      <div class="icon-container-cover" style="width:36px;height:36px;flex-shrink:0;">
        <span style="font-size:1rem;">📊</span>
      </div>
      <span style="font-size:1.05rem;color:#ffffff;">Результаты через 1 семестр — измеримо</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.85);font-size:1.1rem;">
    <span>📧 ai-edu@university.ru</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Регистрация до 1 августа</span>
  </div>
</div>
