---
theme: default
colorSchema: light
fonts:
  sans: Manrope
  body: DM Sans
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
layout: none
---

<!-- SLIDE 1: cover-hero — bg-accent -->
<div style="position:absolute;inset:0;background:var(--bg-accent);z-index:0;"></div>
<div style="position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,0.18) 0%,transparent 65%);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;border:2px solid rgba(255,255,255,0.22);border-radius:50%;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:360px;height:360px;border:2px solid rgba(255,255,255,0.14);border-radius:50%;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background-image:radial-gradient(circle,rgba(255,255,255,0.12) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:-40px;right:-40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.40);border-radius:20px;padding:6px 20px;margin-bottom:28px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.95);font-weight:600;font-family:var(--font-heading);">Квартальный отчёт · Q1 2025</div>
  <h1 style="font-size:3.2rem;font-weight:800;color:#FFFFFF;margin:0 0 12px;font-family:var(--font-heading);line-height:1.1;text-align:center;">SaaS-платформа «Облако»</h1>
  <p style="font-size:1.5rem;color:rgba(255,255,255,0.80);margin:0 0 32px;font-family:var(--font-body);text-align:center;">Результаты для совета директоров</p>
  <div style="display:flex;align-items:center;gap:20px;color:rgba(255,255,255,0.70);font-size:1.1rem;font-family:var(--font-body);">
    <span>28 марта 2025</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>Конфиденциально</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>ceo@oblako.tech</span>
  </div>
</div>

<style>
.slidev-page-1 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 2: stat-hero VARIANT 1 (centered with dual glow) — bg-base — 847 млн ₽ -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 65%);filter:blur(30px);top:50%;left:50%;transform:translate(-50%,-55%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(217,119,6,0.14) 0%,transparent 65%);filter:blur(40px);bottom:0;right:10%;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;border:2px solid rgba(var(--accent-rgb),0.25);border-radius:50%;top:-100px;right:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;font-family:var(--font-heading);margin-bottom:12px;">Выручка Q1 2025 · Ключевой результат</span>
  <div style="font-size:6rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">847 млн ₽</div>
  <div style="font-size:1.6rem;color:var(--color-text);margin:8px 0 10px;font-family:var(--font-body);font-weight:600;">Рост +23% — выручка впервые превысила 800 млн ₽</div>
  <div style="font-size:1.1rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);">Чистая выручка после оттока: 812 млн ₽</div>
  <div style="display:flex;gap:14px;flex-wrap:wrap;justify-content:center;">
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:20px;padding:8px 20px;font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);font-weight:500;">MRR <strong style="color:var(--color-accent);font-weight:700;">282 млн ₽</strong> +18% к Q4</div>
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:20px;padding:8px 20px;font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);font-weight:500;">ARR run rate <strong style="color:var(--color-accent);font-weight:700;">3,4 млрд ₽</strong></div>
  </div>
  <div style="margin-top:20px;font-size:0.75rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Внутренняя финансовая отчётность, март 2025)</div>
</div>

<style>
.slidev-page-2 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 3: bento-grid — bg-base — NRR hero 118%, CAC and LTV/CAC side cards -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.20) 0%,transparent 70%);filter:blur(40px);top:-60px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:30px;right:30px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">Метрики здоровья бизнеса — всё зелёное</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="trending" :size="22" color="var(--color-accent)" />
      </div>
      <div style="font-size:4.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">118%</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;">NRR — Net Revenue Retention</div>
      <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);margin-top:10px;font-weight:500;">Каждый рубль клиента 2023 вернулся + 18 коп. сверху</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="clock" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">14 мес</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">CAC Payback (было 19 мес)</div>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="pie" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">4,2×</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">LTV/CAC · Gross Margin 72%</div>
      </div>
    </div>
  </div>
  <div style="margin-top:10px;font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Внутренняя аналитика продаж и удержания, Q1 2025)</div>
</div>

<style>
.slidev-page-3 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 4: stat-hero VARIANT 2 (asymmetric split, left visual / right text) — bg-base — Enterprise +47% -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.26) 0%,transparent 65%);filter:blur(35px);top:50%;left:15%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:350px;height:350px;background:radial-gradient(circle,rgba(217,119,6,0.12) 0%,transparent 70%);filter:blur(40px);bottom:-30px;right:5%;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;border:2px solid rgba(var(--accent-rgb),0.25);border-radius:50%;bottom:-80px;left:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;">
    <div style="font-size:5.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">+47%</div>
    <div style="font-size:1.8rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">YoY</div>
    <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;">Рост Enterprise-сегмента</div>
    <div style="margin-top:12px;display:inline-flex;align-items:center;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.30);border-radius:20px;padding:6px 16px;font-size:1rem;color:#B45309;font-weight:600;font-family:var(--font-body);">Рынок: +19% YoY</div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.15;">Enterprise растёт в 2,5× быстрее рынка</h1>
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:12px 18px;">
        <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="users" :size="18" color="var(--color-accent)" />
        </div>
        <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;min-width:100px;">12</div>
        <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);">новых enterprise-клиентов в Q1</div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:12px 18px;">
        <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="dollar" :size="18" color="var(--color-accent)" />
        </div>
        <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;min-width:100px;">2,8 млн ₽</div>
        <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);">средний чек/год (+31% к Q4)</div>
      </div>
    </div>
    <div style="margin-top:16px;font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: CRM-отчёт по Enterprise, Q1 2025)</div>
  </div>
</div>

<style>
.slidev-page-4 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 5: section-divider — bg-accent teal — Продуктовое развитие -->
<div style="position:absolute;inset:0;background:var(--bg-accent);z-index:0;"></div>
<div style="position:absolute;width:700px;height:700px;background:radial-gradient(circle,rgba(255,255,255,0.16) 0%,transparent 65%);filter:blur(20px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:520px;height:520px;border:2px solid rgba(255,255,255,0.25);border-radius:50%;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:310px;height:310px;border:2px solid rgba(255,255,255,0.15);border-radius:50%;top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.65);font-weight:600;font-family:var(--font-heading);margin-bottom:16px;">Раздел 01</div>
  <h1 style="font-size:3.8rem;font-weight:800;color:#FFFFFF;margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;text-align:center;">Продуктовое<br>развитие</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.75);font-family:var(--font-body);max-width:600px;line-height:1.6;text-align:center;">Что запустили в Q1 и что строим в Q2–Q3</p>
</div>

<style>
.slidev-page-5 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 6: card-mosaic — bg-base — 3 крупных релиза (accent card left tall, 2 cards right) -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.20) 0%,transparent 70%);filter:blur(40px);top:-80px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">3 крупных релиза изменили конкурентную позицию</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <div style="grid-column:1;grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.06));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:flex-end;">
      <div style="width:48px;height:48px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:2px solid rgba(var(--accent-rgb),0.30);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="cpu" :size="22" color="var(--color-accent)" />
      </div>
      <div style="font-size:1.4rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:8px;line-height:1.2;">AI-ассистент для автоматизации отчётов</div>
      <div style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Генерация отчётов за секунды. Февраль 2025.</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.10);border:1.5px solid rgba(var(--accent-rgb),0.28);border-radius:12px;padding:5px 14px;font-size:1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);margin-top:12px;align-self:flex-start;">NPS +12 пунктов</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;margin-bottom:10px;">
        <Icon name="layers" :size="20" color="var(--color-accent)" />
      </div>
      <div style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:6px;">Мультитенантная архитектура v2</div>
      <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">Изоляция данных enterprise</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.22);border-radius:10px;padding:4px 12px;font-size:0.95rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);margin-top:10px;align-self:flex-start;">Latency −40%</div>
    </div>
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:22px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;margin-bottom:10px;">
        <Icon name="zap" :size="20" color="var(--color-accent)" />
      </div>
      <div style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:6px;">Интеграция с 1С и Битрикс24</div>
      <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">Закрыли 34% pipeline-запросов</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.22);border-radius:10px;padding:4px 12px;font-size:0.95rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);margin-top:10px;align-self:flex-start;">34% запросов закрыто</div>
    </div>
  </div>
</div>

<style>
.slidev-page-6 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 7: timeline-horizontal WITH connector line — bg-alt — Roadmap Q2 -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 0%,transparent 70%);filter:blur(50px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;border:2px solid rgba(var(--accent-rgb),0.28);border-radius:50%;bottom:-100px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Roadmap Q2: фокус на AI и безопасность</h1>
  <!-- CONNECTOR LINE between phases — CRITICAL rule -->
  <div style="display:flex;align-items:center;margin-bottom:16px;gap:0;">
    <div style="width:10px;height:10px;border-radius:50%;background:var(--color-accent);flex-shrink:0;"></div>
    <div style="flex:1;height:2px;background:linear-gradient(90deg,rgba(var(--accent-rgb),0.55),rgba(var(--accent-rgb),0.35),rgba(var(--accent-rgb),0.55));border-radius:2px;"></div>
    <div style="width:10px;height:10px;border-radius:50%;background:var(--color-accent);flex-shrink:0;"></div>
    <div style="flex:1;height:2px;background:linear-gradient(90deg,rgba(var(--accent-rgb),0.55),rgba(var(--accent-rgb),0.35),rgba(var(--accent-rgb),0.55));border-radius:2px;"></div>
    <div style="width:10px;height:10px;border-radius:50%;background:var(--color-accent);flex-shrink:0;"></div>
    <div style="flex:1;height:2px;background:linear-gradient(90deg,rgba(var(--accent-rgb),0.35),rgba(var(--accent-rgb),0.20),rgba(var(--accent-rgb),0.15));border-radius:2px;"></div>
    <div style="width:10px;height:10px;border-radius:50%;border:2px solid rgba(var(--accent-rgb),0.35);background:transparent;flex-shrink:0;"></div>
  </div>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;">
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.06));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;">
      <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);margin-bottom:8px;">Апрель 2025</div>
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:8px;line-height:1.2;">AI-прогнозирование оттока</div>
      <div style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;flex:1;">ML-модель раннего предупреждения об уходе клиента</div>
      <div style="margin-top:12px;font-size:0.9rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">Accuracy 89%</div>
    </div>
    <div style="background:rgba(255,255,255,0.70);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;">
      <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);margin-bottom:8px;">Май 2025</div>
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:8px;line-height:1.2;">Мобильное приложение</div>
      <div style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;flex:1;">Beta iOS и Android для мобильного доступа к дашбордам</div>
      <div style="margin-top:12px;font-size:0.9rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">Beta · Май</div>
    </div>
    <div style="background:rgba(255,255,255,0.70);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:20px 22px;display:flex;flex-direction:column;">
      <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);margin-bottom:8px;">Июнь 2025</div>
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:8px;line-height:1.2;">SOC 2 Type II</div>
      <div style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;flex:1;">Сертификация безопасности для enterprise и госсектора</div>
      <div style="margin-top:12px;font-size:0.9rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">Certif. Q2</div>
    </div>
  </div>
</div>

<style>
.slidev-page-7 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 8: section-divider VARIANT 2 (left-aligned, deeper teal, diamond decoration) — bg-accent -->
<div style="position:absolute;inset:0;background:color-mix(in srgb,#0D9488 82%,#0a1a14 18%);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(255,255,255,0.12) 0%,transparent 65%);filter:blur(20px);top:50%;left:20%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background-image:radial-gradient(circle,rgba(255,255,255,0.15) 1.2px,transparent 1.2px);background-size:24px 24px;top:-40px;right:-20px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:160px;height:160px;border:2px solid rgba(255,255,255,0.20);transform:rotate(45deg);bottom:40px;right:200px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;border:2px solid rgba(255,255,255,0.14);transform:rotate(45deg);bottom:0px;right:120px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;text-align:left;padding:60px 100px;">
  <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.60);font-weight:600;font-family:var(--font-heading);margin-bottom:16px;">Раздел 02</div>
  <h1 style="font-size:4rem;font-weight:800;color:#FFFFFF;margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;text-align:left;">Финансы<br>и unit-экономика</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.72);font-family:var(--font-body);max-width:600px;line-height:1.6;text-align:left;">Детализация P&amp;L · Впервые выходим в плюс</p>
</div>

<style>
.slidev-page-8 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 9: data-spotlight — bg-base — P&L hero EBITDA +30 млн ₽ -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.26) 0%,transparent 65%);filter:blur(35px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;background:radial-gradient(circle,rgba(217,119,6,0.14) 0%,transparent 70%);filter:blur(40px);bottom:0;left:10%;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:44px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;font-family:var(--font-heading);margin-bottom:8px;">P&amp;L Q1 2025 · Исторический момент</span>
  <div style="font-size:2rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);line-height:1.15;max-width:700px;">Впервые в истории: операционная прибыль положительная</div>
  <div style="font-size:5.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">+30 млн ₽</div>
  <div style="font-size:1.3rem;color:var(--color-text);margin:8px 0 22px;font-family:var(--font-body);font-weight:600;">EBITDA — первый положительный квартал</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;max-width:680px;width:100%;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">847 млн</div>
      <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">Выручка</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">237 млн</div>
      <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">COGS (28%)</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">580 млн</div>
      <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">OpEx</div>
    </div>
  </div>
  <div style="margin-top:14px;font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Управленческая отчётность P&amp;L Q1 2025, аудит KPMG)</div>
</div>

<style>
.slidev-page-9 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 10: comparison-table — bg-base — Unit-экономика по когортам -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:450px;height:450px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 0%,transparent 70%);filter:blur(45px);bottom:-40px;right:-40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 1.2px,transparent 1.2px);background-size:20px 20px;top:30px;left:30px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Unit-экономика: когорта 2024 — в 2,1× лучше 2023</h1>
  <div style="flex:1;display:flex;flex-direction:column;gap:10px;">
    <!-- Header -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:12px;padding:0 16px;">
      <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);">Когорта</div>
      <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);">LTV</div>
      <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);">CAC</div>
      <div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);">Retention 12 мес</div>
    </div>
    <!-- Row 1 -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:12px;align-items:center;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px;">
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Когорта 2023</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">3,1 млн ₽</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">680 тыс ₽</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;">94%</div>
    </div>
    <!-- Row 2 accent -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:12px;align-items:center;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),rgba(var(--accent-rgb),0.05));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px;">
      <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Когорта 2024</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">4,7 млн ₽</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">520 тыс ₽</div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">97%</div>
    </div>
    <!-- Row 3 delta -->
    <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr 1fr;gap:12px;align-items:center;background:rgba(var(--accent-rgb),0.05);border:1.5px solid rgba(var(--accent-rgb),0.20);border-radius:12px;padding:12px 16px;">
      <div style="font-size:1.1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">Улучшение</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.10);border:1.5px solid rgba(var(--accent-rgb),0.28);border-radius:10px;padding:4px 12px;font-size:1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">+52%</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.10);border:1.5px solid rgba(var(--accent-rgb),0.28);border-radius:10px;padding:4px 12px;font-size:1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">−24%</div>
      <div style="display:inline-flex;align-items:center;background:rgba(var(--accent-rgb),0.10);border:1.5px solid rgba(var(--accent-rgb),0.28);border-radius:10px;padding:4px 12px;font-size:1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);">+3 п.п.</div>
    </div>
  </div>
  <div style="margin-top:12px;font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Когортный анализ продукта, финансовый блок, Q1 2025)</div>
</div>

<style>
.slidev-page-10 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 11: two-col-text — bg-alt — Риски и митигация -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 70%);filter:blur(50px);top:50%;left:-60px;transform:translateY(-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:350px;height:350px;border:2px solid rgba(var(--accent-rgb),0.30);border-radius:50%;top:-80px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);line-height:1.1;">Риски идентифицированы — митигация в работе</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-content:center;position:relative;">
    <div style="position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);width:2px;background:rgba(var(--accent-rgb),0.25);border-radius:2px;"></div>
    <div>
      <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.14em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);margin-bottom:14px;">Риски</div>
      <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:18px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.10);border:2px solid rgba(217,119,6,0.30);display:flex;align-items:center;justify-content:center;">
          <Icon name="shield" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;"><strong>Ужесточение регуляции ПДн</strong> — ФЗ-152 и новые требования ФСТЭК</div>
      </div>
      <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:18px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.10);border:2px solid rgba(217,119,6,0.30);display:flex;align-items:center;justify-content:center;">
          <Icon name="alert" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;"><strong>Ценовое давление</strong> — конкуренты снизили цены на 15–20%</div>
      </div>
      <div style="display:flex;gap:12px;align-items:flex-start;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.10);border:2px solid rgba(217,119,6,0.30);display:flex;align-items:center;justify-content:center;">
          <Icon name="users" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;"><strong>Концентрация</strong> — 3 клиента дают 28% выручки</div>
      </div>
    </div>
    <div style="padding-left:32px;">
      <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:0.14em;color:var(--color-accent);font-weight:700;font-family:var(--font-heading);margin-bottom:14px;">Митигация</div>
      <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:18px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(var(--accent-rgb),0.10);border:2px solid rgba(var(--accent-rgb),0.28);display:flex;align-items:center;justify-content:center;">
          <Icon name="check" :size="16" color="var(--color-accent)" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">SOC 2 Type II + ФЗ-152 compliance в роадмапе Q2</div>
      </div>
      <div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:18px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(var(--accent-rgb),0.10);border:2px solid rgba(var(--accent-rgb),0.28);display:flex;align-items:center;justify-content:center;">
          <Icon name="trending" :size="16" color="var(--color-accent)" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Value-based pricing — цена привязана к ROI клиента</div>
      </div>
      <div style="display:flex;gap:12px;align-items:flex-start;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(var(--accent-rgb),0.10);border:2px solid rgba(var(--accent-rgb),0.28);display:flex;align-items:center;justify-content:center;">
          <Icon name="target" :size="16" color="var(--color-accent)" />
        </div>
        <div style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">47 сделок в pipeline на 890 млн ₽ — диверсификация</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-page-11 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 12: stat-hero VARIANT 3 (urgency amber tone, left/right grid) — bg-base — 18 месяцев -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(217,119,6,0.18) 0%,transparent 60%);filter:blur(40px);top:50%;left:30%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.20) 0%,transparent 65%);filter:blur(35px);top:-60px;right:-40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:450px;height:450px;border:2px solid rgba(217,119,6,0.25);border-radius:50%;bottom:-100px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <div style="display:flex;flex-direction:column;align-items:flex-start;">
    <div style="display:inline-flex;align-items:center;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.35);border-radius:20px;padding:6px 16px;margin-bottom:16px;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.15em;color:#B45309;font-weight:700;font-family:var(--font-heading);">Критический срок</div>
    <div style="font-size:5.5rem;font-weight:800;color:#B45309;line-height:1;font-family:var(--font-heading);">18 мес</div>
    <div style="font-size:1.3rem;color:var(--color-muted);font-family:var(--font-body);margin-top:8px;">Окно для захвата<br>enterprise-рынка</div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;gap:18px;">
    <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0;font-family:var(--font-heading);line-height:1.15;">Без масштабирования мы потеряем это окно</h1>
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:12px 16px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.08);border:2px solid rgba(217,119,6,0.25);display:flex;align-items:center;justify-content:center;">
          <Icon name="alert" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);line-height:1.4;">Конкуренты привлекли <strong style="color:#B45309;">$120 млн</strong> в 2024 на enterprise-экспансию</div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:12px 16px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.08);border:2px solid rgba(217,119,6,0.25);display:flex;align-items:center;justify-content:center;">
          <Icon name="briefcase" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);line-height:1.4;">Pipeline: <strong style="color:#B45309;">47 сделок на 890 млн ₽</strong> — без ресурсов уйдут</div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:12px 16px;">
        <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;background:rgba(217,119,6,0.08);border:2px solid rgba(217,119,6,0.25);display:flex;align-items:center;justify-content:center;">
          <Icon name="clock" :size="16" color="#B45309" />
        </div>
        <div style="font-size:1.05rem;color:var(--color-text);font-family:var(--font-body);line-height:1.4;">Каждый квартал задержки = <strong style="color:#B45309;">−3–5 enterprise-клиентов</strong></div>
      </div>
    </div>
    <div style="font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Gartner Q4 2024; внутренний CRM-pipeline)</div>
  </div>
</div>

<style>
.slidev-page-12 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 13: bento-grid — bg-base — Прогноз Q2, hero 1.08 млрд ₽ -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:550px;height:550px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.26) 0%,transparent 65%);filter:blur(35px);top:50%;left:35%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:320px;height:320px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:20px;right:20px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">Q2 прогноз: рост 28% при текущем темпе инвестиций</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.05));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="chart" :size="22" color="var(--color-accent)" />
      </div>
      <div style="font-size:4rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">1,08 млрд ₽</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;">Целевая выручка Q2 2025</div>
      <div style="margin-top:14px;background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:10px;padding:10px 14px;font-size:1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.4;">Enterprise + AI-модуль + рост Retention</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="trending" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">+85 млн ₽</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">Ожидаемый EBITDA Q2</div>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.08);border:2px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="rocket" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">+28%</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);">Рост выручки QoQ</div>
      </div>
    </div>
  </div>
  <div style="margin-top:10px;font-size:0.72rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Финансовая модель на основе текущего pipeline, внутренние данные)</div>
</div>

<style>
.slidev-page-13 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 14: cta-warm — bg-accent — Запрос на утверждение бюджета 340 млн ₽ -->
<div style="position:absolute;inset:0;background:linear-gradient(145deg,var(--color-accent) 0%,color-mix(in srgb,var(--color-accent) 70%,black) 100%);z-index:0;"></div>
<div style="position:absolute;width:700px;height:700px;background:radial-gradient(circle,rgba(255,255,255,0.16) 0%,transparent 65%);filter:blur(20px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:580px;height:580px;border:2px solid rgba(255,255,255,0.22);border-radius:50%;top:-100px;left:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:350px;height:350px;border:2px solid rgba(255,255,255,0.14);border-radius:50%;top:-65px;left:-65px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:350px;height:350px;background-image:radial-gradient(circle,rgba(255,255,255,0.12) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:-20px;right:-20px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 20px;margin-bottom:20px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.90);font-weight:600;font-family:var(--font-heading);">Запрос к совету директоров</div>
  <h1 style="font-size:2.8rem;font-weight:800;color:#FFFFFF;margin:0 0 8px;font-family:var(--font-heading);line-height:1.15;text-align:center;">Утвердите 340 млн ₽<br>на enterprise-экспансию</h1>
  <p style="font-size:1.2rem;color:rgba(255,255,255,0.75);margin:0 0 28px;font-family:var(--font-body);text-align:center;">Окупаемость за 3 квартала · Q2–Q3 2025</p>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:560px;width:100%;margin-bottom:28px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;text-align:left;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);border:1.5px solid rgba(255,255,255,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:0.85rem;font-weight:700;color:#FFFFFF;font-family:var(--font-heading);">45%</div>
      <div style="font-size:1.1rem;color:rgba(255,255,255,0.92);font-family:var(--font-body);"><strong style="color:#FFFFFF;">153 млн ₽</strong> — найм: 24 AE + 8 SE + 6 CSM</div>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;text-align:left;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);border:1.5px solid rgba(255,255,255,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:0.85rem;font-weight:700;color:#FFFFFF;font-family:var(--font-heading);">30%</div>
      <div style="font-size:1.1rem;color:rgba(255,255,255,0.92);font-family:var(--font-body);"><strong style="color:#FFFFFF;">102 млн ₽</strong> — маркетинг: ABM, ивенты, PR</div>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;text-align:left;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);border:1.5px solid rgba(255,255,255,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:0.85rem;font-weight:700;color:#FFFFFF;font-family:var(--font-heading);">25%</div>
      <div style="font-size:1.1rem;color:rgba(255,255,255,0.92);font-family:var(--font-body);"><strong style="color:#FFFFFF;">85 млн ₽</strong> — инфраструктура: SOC 2, масштабирование</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.75);font-size:1.05rem;font-family:var(--font-body);">
    <span>ceo@oblako.tech</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>oblako.tech</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>Москва · 28 марта 2025</span>
  </div>
</div>

<style>
.slidev-page-14 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
