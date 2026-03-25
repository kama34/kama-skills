---
theme: default
title: "MLOps: от ноутбука до продакшена за 1 день"
colorSchema: light
fonts:
  sans: Outfit
  serif: DM Sans
  mono: JetBrains Mono
transition: fade
aspectRatio: "16/9"
layout: none
---

<!-- Slide 1: Обложка — cover-hero, bg-accent -->
<!-- eyebrow: 0/4 — cover exempt -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-a">
  <div class="cover-circle-accent"></div>
  <!-- large decorative circle behind content -->
  <div style="position:absolute;bottom:-120px;left:-80px;width:480px;height:480px;border-radius:50%;border:1.5px solid rgba(255,255,255,0.12);pointer-events:none;"></div>
  <div style="position:absolute;top:20px;left:-40px;width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.09),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">Воркшоп · ML Engineering</span>
  <h1 style="font-size:3.2rem;font-weight:800;color:#ffffff;margin:0 0 14px;font-family:var(--font-heading);line-height:1.08;max-width:820px;">MLOps: от ноутбука до продакшена за 1 день</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Практический воркшоп для ML-инженеров</p>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.68);font-size:1.1rem;font-family:var(--font-body);">
    <span>Алексей Козлов</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Lead ML Engineer</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>2026</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 2: 87% ML-моделей не доходят — stat-hero centered, bg-base -->
<!-- eyebrow: 1/4 -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots">
  <!-- bottom glow supporting element -->
  <div style="position:absolute;bottom:-80px;left:50%;transform:translateX(-50%);width:600px;height:300px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.08),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:20px;font-family:var(--font-heading);">Реальность ML-индустрии · Gartner, 2025</span>
  <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:12px;">
    <span style="font-size:6.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">87%</span>
  </div>
  <p style="font-size:1.55rem;font-weight:600;color:var(--color-text);margin:0 0 8px;font-family:var(--font-heading);line-height:1.3;">ML-моделей никогда не доходят до продакшена</p>
  <p style="font-size:1.25rem;color:var(--color-muted);margin:0 0 36px;font-family:var(--font-body);">Главная причина — отсутствие инфраструктуры для деплоя</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">4,5 месяца от прототипа до деплоя</span>
    <span class="label-pill">$500К+ потери в год на команду</span>
  </div>
</div>
<!-- Footer anchor -->
<div class="stat-footer-band">
  <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Источник: Gartner «AI in Production» Report, 2025</span>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 3: Секция — VARIANT A: centered heading + radial glow, bg-accent -->
<!-- eyebrow: 1/4 — section exempt, no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- centered atmospheric glow -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:640px;height:520px;background:radial-gradient(ellipse,rgba(255,255,255,0.10),transparent 65%);pointer-events:none;"></div>
  <!-- large circle decorative -->
  <div style="position:absolute;top:-100px;right:-100px;width:420px;height:420px;border-radius:50%;border:2px solid rgba(255,255,255,0.15);pointer-events:none;"></div>
  <!-- section count pills row -->
  <div style="position:absolute;bottom:36px;left:50%;transform:translateX(-50%);display:flex;gap:10px;align-items:center;">
    <span style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.25);border:1.5px solid rgba(255,255,255,0.45);border-radius:20px;padding:5px 14px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-heading);">Раздел 1 · Основы</span>
    <span style="display:flex;gap:6px;align-items:center;">
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.90);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
    </span>
  </div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px 80px;">
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.08;">Что такое MLOps<br>и зачем он нужен?</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:760px;line-height:1.55;font-family:var(--font-body);">Дисциплина, которая превращает эксперименты в работающие продукты</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 4: MLOps = DevOps + Data + ML — icon-trio, bg-base -->
<!-- eyebrow: 2/4 -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc">
  <div style="position:absolute;top:-80px;right:80px;width:320px;height:320px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.08),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Три составляющих</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 8px;font-family:var(--font-heading);">MLOps = DevOps + Data Engineering + ML</h1>
  <p style="font-size:1.25rem;color:var(--color-muted);margin:0 0 20px;font-family:var(--font-body);">Дисциплина автоматизации полного жизненного цикла модели</p>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:52px;">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:180px;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="automation" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Автоматизация</span>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Обучение и деплой без ручного вмешательства</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:180px;">
      <div style="width:72px;height:72px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="monitor" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Мониторинг</span>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Дрейф данных и деградация качества в реальном времени</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:180px;">
      <div style="width:72px;height:72px;border-radius:50%;background:rgba(var(--accent-rgb),0.15);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="version" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Версионирование</span>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Модели, данные и эксперименты — всё под контролем</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:180px;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="experiment" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Воспроизводимость</span>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Любой результат можно повторить точно</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 5: Уровни зрелости MLOps — timeline-horizontal (4×1 linear grid), bg-alt -->
<!-- eyebrow: 2/4 — no eyebrow on this slide -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-arc-alt">
  <div style="position:absolute;top:0;right:0;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.12),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 6px;font-family:var(--font-heading);">Четыре уровня зрелости MLOps</h1>
  <p style="font-size:1.25rem;color:var(--color-muted);margin:0 0 20px;font-family:var(--font-body);">От ручного процесса до полной автоматизации</p>
  <!-- 4 cards in a single horizontal row with progression arrows -->
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px;align-items:stretch;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 18px;display:flex;flex-direction:column;position:relative;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:rgba(var(--text-rgb),0.08);font-size:0.8rem;font-weight:800;color:var(--color-muted);font-family:var(--font-heading);flex-shrink:0;">0</span>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Ручной</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Jupyter Notebooks, деплой вручную, нет версионирования</span>
      <span style="margin-top:auto;padding-top:12px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-muted);font-weight:600;">Level 0</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 18px;display:flex;flex-direction:column;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);font-size:0.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">1</span>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Автопайплайн</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Автоматизация обучения, базовое версионирование</span>
      <span style="margin-top:auto;padding-top:12px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:600;">Level 1</span>
    </div>
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:20px 18px;display:flex;flex-direction:column;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:var(--color-accent);font-size:0.8rem;font-weight:800;color:#fff;font-family:var(--font-heading);flex-shrink:0;">2</span>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">CI/CD для ML</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);">Автоматический ретрейнинг, тестирование моделей</span>
      <span style="margin-top:auto;padding-top:12px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:700;">Level 2 · Цель воркшопа</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 18px;display:flex;flex-direction:column;opacity:0.75;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:rgba(var(--text-rgb),0.06);font-size:0.8rem;font-weight:800;color:var(--color-muted);font-family:var(--font-heading);flex-shrink:0;">3</span>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-muted);font-family:var(--font-heading);">Полная авто</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">A/B тестирование, self-healing ML pipelines</span>
      <span style="margin-top:auto;padding-top:12px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-muted);font-weight:600;">Level 3 · Roadmap</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 6: Секция — VARIANT B: left-aligned heading + large ghost number "06", bg-accent -->
<!-- eyebrow: 2/4 — section exempt, no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- large ghost number as decorative element -->
  <div style="position:absolute;right:60px;top:50%;transform:translateY(-50%);font-size:14rem;font-weight:900;color:rgba(255,255,255,0.12);font-family:var(--font-heading);line-height:1;user-select:none;pointer-events:none;letter-spacing:-0.04em;">06</div>
  <!-- horizontal rule accent -->
  <div style="position:absolute;bottom:80px;left:72px;right:72px;height:1px;background:rgba(255,255,255,0.20);pointer-events:none;"></div>
  <!-- navigation pills bottom-left -->
  <div style="position:absolute;bottom:36px;left:72px;display:flex;gap:10px;align-items:center;">
    <span style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.22);border:1.5px solid rgba(255,255,255,0.40);border-radius:20px;padding:5px 14px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-heading);">Раздел 2 · Инструменты</span>
    <span style="display:flex;gap:6px;align-items:center;">
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.90);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
    </span>
  </div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:60px 72px 100px;">
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.08;max-width:560px;">Стек<br>инструментов</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:500px;line-height:1.5;font-family:var(--font-body);">Минимальный стек для старта и продвинутый — для масштаба</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 7: Минимальный стек — bento-grid (featured-left), bg-base -->
<!-- eyebrow: 3/4 -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow">
  <div style="position:absolute;top:0;left:0;width:300px;height:300px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.07),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Стартовый набор</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Минимальный стек для первого шага</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- Featured card: MLflow (spans 2 rows) -->
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.12),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="width:56px;height:56px;border-radius:50%;background:rgba(var(--accent-rgb),0.15);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="experiment" :size="26" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.55rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Эксперименты</span>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;margin-bottom:16px;font-family:var(--font-body);">Отслеживание метрик, параметров и артефактов каждого запуска</span>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <span class="label-pill">MLflow</span>
        <span class="label-pill">Weights & Biases</span>
      </div>
    </div>
    <!-- Item 2: Airflow -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="pipeline" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;font-family:var(--font-heading);">Оркестрация</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Airflow / Prefect</span>
      </div>
    </div>
    <!-- Item 3: Seldon / BentoML -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="deploy" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;font-family:var(--font-heading);">Деплой + Реестр</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Seldon Core / BentoML + MLflow Registry</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 8: Продвинутый стек — card-mosaic with hierarchy (featured top-left), bg-base -->
<!-- eyebrow: 4/4 — LAST allowed eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots">
  <div style="position:absolute;bottom:0;left:0;width:420px;height:420px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.06),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Продвинутый уровень</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Стек для масштаба: Feature Store до DVC</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <!-- Card 1 featured (accent) — Feature Store -->
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.15);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="feature-store" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.4rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Feature Store</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;margin-bottom:12px;font-family:var(--font-body);">Переиспользование признаков, консистентность между обучением и инфером</span>
      <div style="display:flex;gap:8px;">
        <span class="label-pill">Feast</span>
        <span class="label-pill">Tecton</span>
      </div>
    </div>
    <!-- Card 2 — Monitoring -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:44px;height:44px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="monitor" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.4rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Мониторинг дрейфа</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;margin-bottom:12px;font-family:var(--font-body);">Статистические тесты на data drift и performance degradation</span>
      <div style="display:flex;gap:8px;">
        <span class="label-pill">Evidently AI</span>
        <span class="label-pill">WhyLabs</span>
      </div>
    </div>
    <!-- Card 3 — Kubernetes -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="kubernetes" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.4rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Инфраструктура</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;margin-bottom:12px;font-family:var(--font-body);">Контейнеризация и оркестрация на продакшн-уровне</span>
      <div style="display:flex;gap:8px;">
        <span class="label-pill">Kubernetes</span>
        <span class="label-pill">Kubeflow</span>
      </div>
    </div>
    <!-- Card 4 — Data (solid) -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:44px;height:44px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="data" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.4rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Данные</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;margin-bottom:12px;font-family:var(--font-body);">Версионирование датасетов и управление большими таблицами</span>
      <div style="display:flex;gap:8px;">
        <span class="label-pill">DVC</span>
        <span class="label-pill">Delta Lake</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 9: Секция — VARIANT C: full-width heading + horizontal rule below, bg-accent -->
<!-- eyebrow: 4/4 — section exempt, no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- large translucent circle decorative element (Rule: must have 1 prominent decorative) -->
  <div style="position:absolute;left:-80px;bottom:-80px;width:520px;height:520px;border-radius:50%;border:2px solid rgba(255,255,255,0.16);pointer-events:none;"></div>
  <div style="position:absolute;left:-30px;bottom:-30px;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.08),transparent 65%);pointer-events:none;"></div>
  <!-- navigation pills bottom-right -->
  <div style="position:absolute;bottom:36px;right:72px;display:flex;gap:10px;align-items:center;">
    <span style="display:flex;gap:6px;align-items:center;">
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.90);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
    </span>
    <span style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.22);border:1.5px solid rgba(255,255,255,0.40);border-radius:20px;padding:5px 14px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-heading);">Раздел 3 · Практика</span>
  </div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px 80px;">
  <h1 style="font-size:4rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.05;">Практика: деплоим модель</h1>
  <!-- thick horizontal rule -->
  <div style="width:80%;height:3px;background:rgba(255,255,255,0.35);margin-bottom:20px;border-radius:2px;"></div>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:600px;line-height:1.5;font-family:var(--font-body);">4 шага от обученной модели до живого API в продакшене</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 10: Пайплайн 4 шага — timeline-horizontal variant 2 (vertical list with step connectors), bg-alt -->
<!-- eyebrow: 4/4 — no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-dots">
  <div style="position:absolute;bottom:0;right:0;width:380px;height:380px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.14),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Пайплайн за 4 шага: от модели к API</h1>
  <!-- 4 steps in 2×2 grid with step numbers — different from slide 5's 4×1 layout -->
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;align-items:stretch;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--color-accent);font-size:1.1rem;font-weight:800;color:#fff;font-family:var(--font-heading);flex-shrink:0;">1</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Обучение + Логирование</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Обучаем модель, логируем все параметры и метрики в <strong>MLflow</strong></span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--color-accent);font-size:1.1rem;font-weight:800;color:#fff;font-family:var(--font-heading);flex-shrink:0;">2</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Регистрация в Registry</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Регистрируем лучшую модель в <strong>Model Registry</strong> и ставим тег Production</span>
    </div>
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.08),rgba(var(--accent-rgb),0.03));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--color-accent);font-size:1.1rem;font-weight:800;color:#fff;font-family:var(--font-heading);flex-shrink:0;">3</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Docker-контейнер</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Упаковываем модель в <strong>Docker</strong>-образ с FastAPI-сервером</span>
    </div>
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.08),rgba(var(--accent-rgb),0.03));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--color-accent);font-size:1.1rem;font-weight:800;color:#fff;font-family:var(--font-heading);flex-shrink:0;">4</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Деплой в Kubernetes</span>
      </div>
      <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Деплоим через <strong>Seldon Core</strong> — canary, A/B, rollback из коробки</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 11: Мониторинг — asymmetric-split, bg-alt -->
<!-- eyebrow: 4/4 — no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow">
  <div style="position:absolute;top:-80px;left:80px;width:360px;height:360px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:44px;align-items:center;">
  <!-- Left: large visual metric -->
  <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:20px;">
    <div style="width:100px;height:100px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:2.5px solid var(--color-accent);display:flex;align-items:center;justify-content:center;">
      <Icon name="monitor" :size="44" color="var(--color-accent)" />
    </div>
    <div style="text-align:center;">
      <span style="display:block;font-size:4rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">5%</span>
      <span style="font-size:1.25rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;display:block;">порог деградации<br>для авто-алерта</span>
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center;">
      <span class="label-pill">Каждый час</span>
    </div>
  </div>
  <!-- Right: text content -->
  <div style="display:flex;flex-direction:column;justify-content:center;gap:14px;">
    <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0;font-family:var(--font-heading);line-height:1.15;">Мониторинг — страховка от деградации</h1>
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div style="width:32px;height:32px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <Icon name="data" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);"><strong>Data drift:</strong> статистические тесты (KS, PSI) каждый час</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div style="width:32px;height:32px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <Icon name="alert" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);"><strong>Алерты:</strong> PagerDuty при падении accuracy более 5%</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.08),rgba(var(--accent-rgb),0.03));border:1.5px solid var(--color-accent-dim);border-radius:10px;padding:14px 18px;">
        <div style="width:32px;height:32px;border-radius:50%;background:rgba(var(--accent-rgb),0.15);border:1.5px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <Icon name="rollback" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);"><strong>Автоматический rollback</strong> при критических падениях</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 12: Секция — VARIANT D: asymmetric layout + warning tone, bg-accent -->
<!-- eyebrow: 4/4 — section exempt, no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- warning diagonal stripe accent (right side) -->
  <div style="position:absolute;top:0;right:0;width:45%;height:100%;background:rgba(0,0,0,0.12);clip-path:polygon(20% 0%, 100% 0%, 100% 100%, 0% 100%);pointer-events:none;"></div>
  <!-- large alert icon decorative -->
  <div style="position:absolute;right:80px;top:50%;transform:translateY(-50%);opacity:0.18;pointer-events:none;">
    <svg width="200" height="200" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
      <line x1="12" y1="9" x2="12" y2="13"/>
      <line x1="12" y1="17" x2="12.01" y2="17"/>
    </svg>
  </div>
  <!-- navigation pills bottom-left -->
  <div style="position:absolute;bottom:36px;left:72px;display:flex;gap:10px;align-items:center;">
    <span style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.22);border:1.5px solid rgba(255,255,255,0.40);border-radius:20px;padding:5px 14px;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-heading);">Раздел 4 · Антипаттерны</span>
    <span style="display:flex;gap:6px;align-items:center;">
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.30);display:inline-block;"></span>
      <span style="width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,0.90);display:inline-block;"></span>
    </span>
  </div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:60px 72px 100px;max-width:60%;">
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.05;">Типичные<br>ошибки</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);line-height:1.5;font-family:var(--font-body);">Что мы потеряли, когда игнорировали MLOps</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 13: 5 ошибок — two-col-text (left: ошибки, right: последствия), bg-base -->
<!-- eyebrow: 4/4 — no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc">
  <div style="position:absolute;top:0;right:0;width:360px;height:360px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.07),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 12px;font-family:var(--font-heading);">5 ошибок, которые мы допустили</h1>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:flex-start;padding-top:8px;">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;">
    <!-- Left column: mistakes list -->
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:rgba(217,119,6,0.12);border:1.5px solid rgba(217,119,6,0.40);font-size:0.75rem;font-weight:800;color:var(--color-accent-warm);flex-shrink:0;margin-top:2px;">1</span>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);">Обучение на <strong>всех данных</strong> без версионирования датасетов</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:rgba(217,119,6,0.12);border:1.5px solid rgba(217,119,6,0.40);font-size:0.75rem;font-weight:800;color:var(--color-accent-warm);flex-shrink:0;margin-top:2px;">2</span>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);">Отсутствие <strong>staging-среды</strong> для тестирования моделей</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:rgba(217,119,6,0.12);border:1.5px solid rgba(217,119,6,0.40);font-size:0.75rem;font-weight:800;color:var(--color-accent-warm);flex-shrink:0;margin-top:2px;">3</span>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);">Игнорирование <strong>data drift</strong> первые 3 месяца работы</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:rgba(217,119,6,0.12);border:1.5px solid rgba(217,119,6,0.40);font-size:0.75rem;font-weight:800;color:var(--color-accent-warm);flex-shrink:0;margin-top:2px;">4</span>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;font-family:var(--font-body);">Ручной деплой «пока работает» — месяцами</span>
      </div>
    </div>
    <!-- Right column: consequences with accent separator -->
    <div style="border-left:3px solid var(--color-accent-dim);padding-left:32px;display:flex;flex-direction:column;gap:14px;justify-content:center;">
      <p style="font-size:1.25rem;font-weight:700;color:var(--color-text);margin:0 0 6px;font-family:var(--font-heading);">Чего это стоило команде</p>
      <div style="display:flex;align-items:flex-start;gap:10px;">
        <span style="width:6px;height:6px;border-radius:50%;background:var(--color-accent);flex-shrink:0;margin-top:8px;display:block;"></span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Невоспроизводимые результаты, которые нельзя проверить</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:10px;">
        <span style="width:6px;height:6px;border-radius:50%;background:var(--color-accent);flex-shrink:0;margin-top:8px;display:block;"></span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Инцидент в продакшене с просадкой выручки на 15%</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:10px;">
        <span style="width:6px;height:6px;border-radius:50%;background:var(--color-accent);flex-shrink:0;margin-top:8px;display:block;"></span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">5 часов ручного деплоя каждые 2 недели</span>
      </div>
    </div>
  </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 14: Без MLOps — рулетка — stat-hero TEXT-HERO variant, bg-base -->
<!-- eyebrow: 4/4 — no eyebrow (text-hero variant: heading as hero, no number) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow">
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:700px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.06),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 96px;">
  <h1 style="font-size:3.2rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;max-width:760px;">Без MLOps каждое обновление модели — рулетка</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;max-width:720px;width:100%;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:18px;text-align:center;">
      <span style="display:block;font-size:2.8rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">?</span>
      <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.3;margin-top:8px;display:block;">Непредсказуемое поведение в продакшене</span>
    </div>
    <div style="background:var(--color-surface);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:18px;text-align:center;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.08),rgba(var(--accent-rgb),0.02));">
      <span style="display:block;font-size:2.8rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">∞</span>
      <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.3;margin-top:8px;display:block;">Невозможно откатиться к предыдущей версии</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:18px;text-align:center;">
      <span style="display:block;font-size:2.8rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">4ч</span>
      <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.3;margin-top:8px;display:block;">Ручной деплой вместо 10 минут автоматизации</span>
    </div>
  </div>
</div>
<!-- Footer anchor -->
<div class="stat-footer-band">
  <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">MLOps превращает рулетку в управляемый процесс с предсказуемым результатом</span>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 15: Чеклист — card-mosaic CHECKLIST variant (4 checklist items), bg-alt -->
<!-- eyebrow: 4/4 — no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-arc-alt">
  <div style="position:absolute;top:0;right:0;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Чеклист MLOps-готовности</h1>
  <!-- 2x2 checklist cards — different visual from slides 7/8 card-mosaic: large single-item format -->
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="version" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Версионирование данных</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Каждый датасет — это тег в DVC или Delta Lake</span>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:14px;background:var(--color-accent-bg);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="experiment" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Воспроизводимость</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Любой эксперимент воспроизводим через MLflow run ID</span>
      </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:22px 24px;display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.15);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="monitor" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Мониторинг в продакшене</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Drift-алерты настроены и протестированы</span>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 24px;display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:14px;background:var(--color-accent-bg);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="pipeline" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Автоматизированный деплой</span>
        <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">CI/CD pipeline обновляет модель без ручного вмешательства</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 16: Ресурсы и CTA — cta-warm, bg-accent -->
<div style="position:absolute;inset:0;z-index:0;background:linear-gradient(145deg, var(--bg-accent, #0D9488) 0%, #0A7B70 100%);">
  <div style="position:absolute;inset:0;background-image:radial-gradient(circle, rgba(255,255,255,0.16) 1.5px, transparent 1.5px);background-size:28px 28px;pointer-events:none;"></div>
  <div class="cover-circle-accent" style="top:auto;right:auto;bottom:-100px;left:-100px;width:400px;height:400px;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:24px;">Следующие шаги</span>
  <h1 style="font-size:2.8rem;font-weight:800;color:#ffffff;margin:0 0 32px;font-family:var(--font-heading);line-height:1.12;max-width:680px;">Начните внедрять MLOps уже сегодня</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:680px;width:100%;margin-bottom:36px;">
    <div style="background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;text-align:left;">
      <div style="width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,0.25);border:2px solid rgba(255,255,255,0.55);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="github" :size="20" color="#ffffff" />
      </div>
      <div>
        <span style="display:block;font-size:1.1rem;font-weight:700;color:#ffffff;font-family:var(--font-heading);">GitHub репозиторий</span>
        <span style="font-size:1rem;color:rgba(255,255,255,0.75);font-family:var(--font-body);">github.com/mlops-workshop</span>
      </div>
    </div>
    <div style="background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;text-align:left;">
      <div style="width:40px;height:40px;border-radius:14px;background:rgba(255,255,255,0.25);border:2px solid rgba(255,255,255,0.55);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="book" :size="20" color="#ffffff" />
      </div>
      <div>
        <span style="display:block;font-size:1.1rem;font-weight:700;color:#ffffff;font-family:var(--font-heading);">Книга-база</span>
        <span style="font-size:1rem;color:rgba(255,255,255,0.75);font-family:var(--font-body);">Designing ML Systems — Chip Huyen</span>
      </div>
    </div>
    <div style="background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;text-align:left;">
      <div style="width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,0.25);border:2px solid rgba(255,255,255,0.55);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="community" :size="20" color="#ffffff" />
      </div>
      <div>
        <span style="display:block;font-size:1.1rem;font-weight:700;color:#ffffff;font-family:var(--font-heading);">Telegram-сообщество</span>
        <span style="font-size:1rem;color:rgba(255,255,255,0.75);font-family:var(--font-body);">t.me/mlops_ru</span>
      </div>
    </div>
    <div style="background:rgba(255,255,255,0.22);border:2px solid rgba(255,255,255,0.55);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:14px;text-align:left;">
      <div style="width:40px;height:40px;border-radius:14px;background:rgba(255,255,255,0.30);border:2px solid rgba(255,255,255,0.70);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="calendar" :size="20" color="#ffffff" />
      </div>
      <div>
        <span style="display:block;font-size:1.1rem;font-weight:700;color:#ffffff;font-family:var(--font-heading);">Следующий воркшоп</span>
        <span style="font-size:1rem;color:rgba(255,255,255,0.90);font-family:var(--font-body);font-weight:600;">20 апреля 2026</span>
      </div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.65);font-size:1rem;">
    <span>Алексей Козлов</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Lead ML Engineer</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Вопросы в чат</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
