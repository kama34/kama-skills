---
theme: default
title: Рынок e-grocery в России
fonts:
  sans: Outfit
  serif: DM Sans
  mono: JetBrains Mono
colorSchema: light
transition: fade
aspectRatio: "16/9"
layout: none
---

<!-- Slide 1: Cover-hero | bg-accent | TIER 1 typography -->
<!-- eyebrow: cover slide — exempt from eyebrow counter -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-a">
  <div class="cover-circle-accent"></div>
  <!-- Dot pattern overlay -->
  <div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,0.14) 1.5px,transparent 1.5px);background-size:28px 28px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">Аналитический обзор · 2025</span>
  <h1 style="font-size:3.6rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.05;">E-grocery удвоится<br>к 2028 году</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Аналитический обзор рынка онлайн-продуктов в России</p>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.65);font-size:1.1rem;font-family:var(--font-body);">
    <span>DataInsight</span>
    <span style="width:4px;height:4px;background:rgba(255,255,255,0.40);border-radius:50%;flex-shrink:0;"></span>
    <span>Собственная аналитика</span>
    <span style="width:4px;height:4px;background:rgba(255,255,255,0.40);border-radius:50%;flex-shrink:0;"></span>
    <span>Март 2025</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 2: Stat-hero (centered standard) | bg-base | TIER 1 — 780 млрд ₽ -->
<!-- eyebrow: 0/2 used — using on this slide (1/2) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots">
  <!-- Decorative glow top-left -->
  <div style="position:absolute;top:-80px;left:-80px;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:20px;">Объём рынка · 2025</span>
  <h1 style="font-size:6rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);">780 млрд ₽</h1>
  <p style="font-size:1.5rem;color:var(--color-text);margin:12px 0 36px;font-family:var(--font-body);font-weight:500;">Рынок e-grocery — объём в 2025 году</p>
  <div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">+42% год к году</span>
    <span class="label-pill">Пенетрация 8,4%</span>
    <span class="label-pill">Прогноз 2028: 1,6 трлн ₽</span>
  </div>
  <div style="margin-top:32px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:16px 40px;display:inline-flex;gap:40px;align-items:center;">
    <div style="text-align:center;">
      <div style="font-size:2.5rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">8,4%</div>
      <div style="font-size:1.1rem;color:var(--color-muted);margin-top:4px;">от продуктового ритейла</div>
    </div>
    <div style="width:1px;height:56px;background:var(--color-surface-border);"></div>
    <div style="text-align:center;">
      <div style="font-size:2.5rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">1,6 трлн</div>
      <div style="font-size:1.1rem;color:var(--color-muted);margin-top:4px;">прогноз на 2028 год</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 3: Card-mosaic with hierarchy | bg-base | Самокат promoted -->
<!-- eyebrow: 1/2 used — using on this slide (2/2, LIMIT REACHED) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow">
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Конкурентный ландшафт</span>
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);line-height:1.1;">Топ-5 игроков контролируют 74% рынка</h1>
  <!-- Mosaic: promoted card (Самокат) spans rows 1+2, others fill 2x2 right -->
  <div style="flex:1;display:grid;grid-template-columns:1.3fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <!-- PROMOTED: Самокат — grid-row spans both rows -->
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.05));border:2px solid var(--color-accent-dim);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <span style="display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:var(--color-accent);color:#fff;font-size:0.8rem;font-weight:800;font-family:var(--font-heading);">1</span>
        <span style="font-size:1.5rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Самокат</span>
        <span style="font-size:0.7rem;color:var(--color-muted);font-weight:500;">Сбер</span>
      </div>
      <div style="font-size:4rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);margin-bottom:8px;">28%</div>
      <div style="font-size:1.25rem;color:var(--color-muted);margin-bottom:20px;">доля рынка</div>
      <div style="height:8px;border-radius:4px;background:var(--color-accent);width:90%;margin-bottom:16px;"></div>
      <span style="font-size:1.1rem;color:var(--color-text);line-height:1.4;">Лидер сегмента экспресс-доставки. Сеть дарксторов во всех городах-миллионниках.</span>
    </div>
    <!-- Яндекс Лавка -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);font-size:0.75rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">2</span>
      <div>
        <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Яндекс Лавка</div>
        <div style="font-size:2rem;font-weight:800;color:var(--color-text);line-height:1.1;font-family:var(--font-heading);">19%</div>
        <div style="height:6px;border-radius:3px;background:rgba(var(--accent-rgb),0.45);width:70%;margin-top:4px;"></div>
      </div>
    </div>
    <!-- ВкусВилл -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);font-size:0.75rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">3</span>
      <div>
        <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">ВкусВилл</div>
        <div style="font-size:2rem;font-weight:800;color:var(--color-text);line-height:1.1;font-family:var(--font-heading);">12%</div>
        <div style="height:6px;border-radius:3px;background:rgba(var(--accent-rgb),0.35);width:48%;margin-top:4px;"></div>
      </div>
    </div>
    <!-- Перекрёсток Впрок -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);font-size:0.75rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">4</span>
      <div>
        <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Перекрёсток Впрок</div>
        <div style="font-size:2rem;font-weight:800;color:var(--color-text);line-height:1.1;font-family:var(--font-heading);">9%</div>
        <div style="height:6px;border-radius:3px;background:rgba(var(--accent-rgb),0.30);width:36%;margin-top:4px;"></div>
      </div>
    </div>
    <!-- Ozon Fresh -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
      <span style="display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);font-size:0.75rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">5</span>
      <div>
        <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Ozon Fresh</div>
        <div style="font-size:2rem;font-weight:800;color:var(--color-text);line-height:1.1;font-family:var(--font-heading);">6%</div>
        <div style="height:6px;border-radius:3px;background:rgba(var(--accent-rgb),0.22);width:24%;margin-top:4px;"></div>
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

<!-- Slide 4: Section-divider VARIANT B — left-aligned + ghost "04" + lower anchor row -->
<!-- Section 1 of 2 — bg-accent — EYEBROW LIMIT REACHED, no eyebrow here -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- Atmospheric glow -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:480px;background:radial-gradient(ellipse,rgba(255,255,255,0.06),transparent 65%);pointer-events:none;"></div>
  <!-- Ghost number "04" — large decorative -->
  <div style="position:absolute;right:48px;top:50%;transform:translateY(-50%);font-size:10rem;font-weight:900;color:rgba(255,255,255,0.10);font-family:'Outfit',sans-serif;line-height:1;user-select:none;pointer-events:none;">04</div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:64px 80px;">
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.05;">Драйверы роста</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.75);max-width:580px;line-height:1.55;font-family:var(--font-body);">Два структурных фактора формируют новую норму рынка онлайн-продуктов</p>
  <!-- Lower anchor: section progress indicators -->
  <div style="position:absolute;bottom:40px;left:80px;display:flex;align-items:center;gap:12px;">
    <span style="font-size:0.7rem;color:rgba(255,255,255,0.55);text-transform:uppercase;letter-spacing:0.14em;font-weight:600;">Раздел 1 из 2</span>
    <span style="width:28px;height:4px;background:rgba(255,255,255,0.75);border-radius:2px;"></span>
    <span style="width:28px;height:4px;background:rgba(255,255,255,0.25);border-radius:2px;"></span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 5: Two-col-text | bg-base | Два драйвера -->
<!-- EYEBROW LIMIT REACHED — no eyebrow, heading speaks for itself -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc">
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Два драйвера ускоряют рынок</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-content:center;">
    <!-- Left: Speed delivery -->
    <div style="background:linear-gradient(145deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.03));border:1.5px solid var(--color-accent-dim);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;gap:16px;">
      <div style="display:flex;align-items:center;justify-content:center;margin-bottom:4px;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
          <Icon name="zap" :size="24" color="var(--color-accent)" />
        </div>
      </div>
      <div style="font-size:1.5rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);text-align:center;">Экспресс-доставка</div>
      <div style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;text-align:left;">15 минут стали стандартом. Аудитория ожидает мгновенного исполнения без компромисса по ассортименту.</div>
      <div style="text-align:center;margin-top:4px;">
        <span style="font-size:2.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">15 мин</span>
        <div style="font-size:1.1rem;color:var(--color-muted);margin-top:2px;">медианное время доставки</div>
      </div>
    </div>
    <!-- Right: Average ticket growth -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;gap:16px;">
      <div style="display:flex;align-items:center;justify-content:center;margin-bottom:4px;">
        <div style="width:56px;height:56px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
          <Icon name="trending-up" :size="24" color="var(--color-accent)" />
        </div>
      </div>
      <div style="font-size:1.5rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);text-align:center;">Рост среднего чека</div>
      <div style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;text-align:left;">Аудитория 35–55 лет перешла в онлайн, принося более высокий AOV и повторные заказы.</div>
      <div style="display:flex;align-items:center;justify-content:center;gap:12px;margin-top:4px;">
        <div style="text-align:center;">
          <div style="font-size:1.8rem;font-weight:800;color:var(--color-muted);font-family:var(--font-heading);line-height:1;">1 800 ₽</div>
          <div style="font-size:0.9rem;color:var(--color-muted);">2024</div>
        </div>
        <div style="font-size:1.5rem;color:var(--color-accent);font-weight:700;display:flex;align-items:center;justify-content:center;">
          <!-- SVG chevron-right arrow — no text arrow characters -->
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
        </div>
        <div style="text-align:center;">
          <div style="font-size:1.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">2 400 ₽</div>
          <div style="font-size:0.9rem;color:var(--color-muted);">2025 <span style="color:var(--color-accent);font-weight:600;">+33%</span></div>
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

<!-- Slide 6: Stat-hero ASYMMETRIC (variant B) | bg-alt | Дарксторы -->
<!-- EYEBROW LIMIT REACHED — no eyebrow. Visual-dominant: hero number left 40%, context right 60% -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow-alt">
  <!-- Arc decoration (dark color on bg-alt) -->
  <div style="position:absolute;top:-80px;right:-80px;width:420px;height:420px;border:6px solid rgba(var(--text-rgb),0.15);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:48px 64px;gap:40px;align-items:center;">
  <!-- LEFT: Hero number -->
  <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;">
    <div style="font-size:6.5rem;font-weight:900;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">4 200</div>
    <div style="font-size:1.3rem;color:var(--color-text);font-weight:600;margin-top:8px;font-family:var(--font-body);">дарксторов</div>
    <div style="font-size:1.1rem;color:var(--color-muted);margin-top:4px;">в России · 2025</div>
    <div style="margin-top:16px;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1rem;color:var(--color-muted);">vs 1 800 в 2023</span>
      <span style="background:rgba(var(--accent-rgb),0.15);border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:4px 12px;font-size:0.85rem;font-weight:700;color:var(--color-accent);">+133%</span>
    </div>
  </div>
  <!-- RIGHT: Context content -->
  <div style="display:flex;flex-direction:column;gap:16px;justify-content:center;">
    <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 8px;font-family:var(--font-heading);line-height:1.1;">Дарксторы — инфраструктура роста</h1>
    <!-- Three metric rows -->
    <div style="display:grid;grid-template-rows:1fr 1fr 1fr;gap:10px;flex:1;min-height:180px;">
      <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.65);border:1px solid rgba(var(--text-rgb),0.08);border-radius:12px;padding:0 20px;">
        <div style="width:40px;height:40px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="warehouse" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1.25rem;font-weight:600;color:var(--color-text);">Средняя площадь 250 м²</div>
          <div style="font-size:1.05rem;color:var(--color-muted);">Оптимально для 1 500–2 000 SKU</div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.65);border:1px solid rgba(var(--text-rgb),0.08);border-radius:12px;padding:0 20px;">
        <div style="width:40px;height:40px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="robot" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1.25rem;font-weight:600;color:var(--color-text);">60% заказов автоматизировано</div>
          <div style="font-size:1.05rem;color:var(--color-muted);">Роботизированная сборка снижает ошибки</div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
        <div style="width:40px;height:40px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="trending-up" :size="18" color="#ffffff" />
        </div>
        <div>
          <div style="font-size:1.25rem;font-weight:600;color:var(--color-text);">Рост сети: +133% за 2 года</div>
          <div style="font-size:1.05rem;color:var(--color-accent);font-weight:600;">1 800 → 4 200 точек (источник: DataInsight, 2025)</div>
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

<!-- Slide 7: Section-divider VARIANT C — centered + bold rule | bg-accent -->
<!-- Second section divider — must DIFFER from slide 4 (slide 4 = left-aligned + ghost number) -->
<!-- Variant C: centered heading + horizontal accent rule -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- dot pattern — different from slide 4's glow -->
  <div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,0.15) 1.5px,transparent 1.5px);background-size:32px 32px;pointer-events:none;"></div>
  <!-- Large decorative circle — visual weight on bg-accent (rule: 300px+) -->
  <div style="position:absolute;bottom:-100px;right:-100px;width:480px;height:480px;border-radius:50%;border:3px solid rgba(255,255,255,0.14);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-50px;right:-50px;width:320px;height:320px;border-radius:50%;background:rgba(255,255,255,0.05);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:64px 80px;">
  <!-- Bold horizontal rule above heading -->
  <div style="width:72px;height:4px;background:rgba(255,255,255,0.70);border-radius:2px;margin-bottom:28px;"></div>
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.05;">Вызовы и риски</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.75);max-width:580px;line-height:1.55;font-family:var(--font-body);">Рост рынка ограничен структурными барьерами, давлением на маржу и регуляторной неопределённостью</p>
  <!-- Lower anchor: section progress indicators — centered variant -->
  <div style="position:absolute;bottom:40px;display:flex;align-items:center;gap:12px;">
    <span style="width:28px;height:4px;background:rgba(255,255,255,0.30);border-radius:2px;"></span>
    <span style="width:28px;height:4px;background:rgba(255,255,255,0.75);border-radius:2px;"></span>
    <span style="font-size:0.7rem;color:rgba(255,255,255,0.55);text-transform:uppercase;letter-spacing:0.14em;font-weight:600;margin-left:4px;">Раздел 2 из 2</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 8: Bento-grid | bg-base | Юнит-экономика под давлением -->
<!-- EYEBROW LIMIT REACHED — no eyebrow. Heading speaks for itself. -->
<!-- Bento: featured cell = маржа 2-4% (spans rows), supporting = 2 smaller cells -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots">
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);line-height:1.1;">Юнит-экономика остаётся под давлением</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <!-- FEATURED: Маржа (spans both rows) — ≥3.5rem heading required -->
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.12),rgba(var(--accent-rgb),0.04));border:2px solid var(--color-accent-dim);border-radius:16px;padding:28px 24px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;justify-content:center;margin-bottom:16px;">
        <div style="width:60px;height:60px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;">
          <Icon name="chart-bar" :size="26" color="#ffffff" />
        </div>
      </div>
      <div style="text-align:center;">
        <div style="font-size:4rem;font-weight:900;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">2–4%</div>
        <div style="font-size:1.25rem;font-weight:600;color:var(--color-text);margin-top:6px;">Средняя маржа</div>
        <div style="font-size:1.1rem;color:var(--color-muted);margin-top:4px;line-height:1.4;">vs 8–12% у офлайн-ритейлеров</div>
      </div>
      <div style="margin-top:20px;padding:12px 16px;background:rgba(255,255,255,0.60);border-radius:10px;text-align:center;">
        <span style="font-size:1.1rem;color:var(--color-text);">Разрыв в марже — <strong>главный структурный вызов</strong> для рентабельности e-grocery</span>
      </div>
    </div>
    <!-- Supporting cell 1: Стоимость последней мили -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="truck" :size="18" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:600;color:var(--color-text);">Последняя миля</span>
      </div>
      <div style="font-size:2.5rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">180 ₽</div>
      <div style="font-size:1.1rem;color:var(--color-muted);">стоимость на заказ</div>
    </div>
    <!-- Supporting cell 2: Зарплаты курьеров -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-warm-rgb),0.10);border:1.5px solid rgba(var(--accent-warm-rgb),0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="users" :size="18" color="var(--color-accent-warm)" />
        </div>
        <span style="font-size:1.1rem;font-weight:600;color:var(--color-text);">Конкуренция за курьеров</span>
      </div>
      <div style="font-size:2.5rem;font-weight:800;color:var(--color-accent-warm);line-height:1;font-family:var(--font-heading);">+35%</div>
      <div style="font-size:1.1rem;color:var(--color-muted);">рост зарплат за год</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 9: Icon-trio | bg-base | Регуляторные риски -->
<!-- EYEBROW LIMIT REACHED — no eyebrow. Heading as action title. -->
<!-- icon-trio used only once in deck — OK -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow">
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Регуляторные риски нарастают</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:40px;">
    <!-- Risk 1: Закон о маркетплейсах -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;gap:14px;">
      <div style="width:80px;height:80px;border-radius:50%;background:rgba(var(--accent-warm-rgb),0.10);border:2px solid rgba(var(--accent-warm-rgb),0.35);display:flex;align-items:center;justify-content:center;">
        <Icon name="shield" :size="32" color="var(--color-accent-warm)" />
      </div>
      <div style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Закон о маркетплейсах</div>
      <div style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;text-align:left;max-width:180px;">Ограничения на скидки и акции затрагивают механику привлечения покупателей</div>
    </div>
    <!-- Vertical divider -->
    <div style="width:1px;height:160px;background:var(--color-surface-border);"></div>
    <!-- Risk 2: Маркировка -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;gap:14px;">
      <div style="width:80px;height:80px;border-radius:12px;background:var(--color-accent-bg);border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <Icon name="box" :size="32" color="var(--color-accent)" />
      </div>
      <div style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Маркировка продуктов</div>
      <div style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;text-align:left;max-width:180px;">Новые требования к маркировке увеличивают операционную нагрузку на 8–12%</div>
    </div>
    <!-- Vertical divider -->
    <div style="width:1px;height:160px;background:var(--color-surface-border);"></div>
    <!-- Risk 3: Трудовое законодательство -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;gap:14px;">
      <div style="width:80px;height:80px;border-radius:50%;background:var(--color-accent-bg);border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <Icon name="users" :size="32" color="var(--color-accent)" />
      </div>
      <div style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Статус курьеров</div>
      <div style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;text-align:left;max-width:180px;">Трудовое законодательство для самозанятых курьеров усложняет модели найма</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 10: Asymmetric-split (text-hero) | bg-alt | Прогноз консолидация -->
<!-- FINAL SLIDE — analytics report conclusion (NOT CTA) -->
<!-- Visual gravity: left-dominant (contrasts with right-dominant slide 6) -->
<!-- EYEBROW LIMIT REACHED — no eyebrow. Heading is the conclusion. -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-arc-alt">
  <!-- Top-left glow (complements bottom-left arc) -->
  <div style="position:absolute;top:0;left:0;width:500px;height:400px;background:radial-gradient(ellipse at 20% 30%,rgba(var(--accent-rgb),0.50),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:3fr 2fr;padding:52px 64px;gap:48px;align-items:center;">
  <!-- LEFT: Text-hero conclusion -->
  <div style="display:flex;flex-direction:column;justify-content:center;gap:20px;">
    <h1 style="font-size:2.6rem;font-weight:900;color:var(--color-text);margin:0;font-family:var(--font-heading);line-height:1.1;">Рынок консолидируется<br>до 3 крупных игроков к 2028</h1>
    <p style="font-size:1.3rem;color:var(--color-muted);line-height:1.5;margin:0;">M&amp;A-активность ускоряется: 12 сделок в 2025. Нишевые игроки покидают регионы. Вертикальная интеграция от поля до двери становится новым стандартом.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:4px;">
      <span class="label-pill">12 M&amp;A-сделок · 2025</span>
      <span class="label-pill">Вертикальная интеграция</span>
    </div>
  </div>
  <!-- RIGHT: Key metrics column -->
  <div style="display:flex;flex-direction:column;gap:14px;justify-content:center;">
    <!-- Metric: 3 игрока -->
    <div style="background:linear-gradient(145deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.05));border:2px solid var(--color-accent-dim);border-radius:16px;padding:20px 22px;text-align:center;">
      <div style="font-size:3.5rem;font-weight:900;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">3</div>
      <div style="font-size:1.1rem;color:var(--color-text);font-weight:600;margin-top:4px;">крупных игрока останется</div>
      <div style="font-size:1rem;color:var(--color-muted);">прогноз к 2028</div>
    </div>
    <!-- Metric: нишевые игроки -->
    <div style="background:rgba(255,255,255,0.65);border:1px solid rgba(var(--text-rgb),0.08);border-radius:14px;padding:16px 20px;text-align:center;">
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Уход нишевых игроков</div>
      <div style="font-size:1.1rem;color:var(--color-muted);margin-top:4px;line-height:1.4;">из регионов — сжатие конкуренции</div>
    </div>
    <!-- Source attribution -->
    <div style="font-size:0.9rem;color:var(--color-muted);text-align:center;padding-top:4px;">Источник: DataInsight + собственная аналитика, март 2025</div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
