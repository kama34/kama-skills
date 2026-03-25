---
theme: default
layout: none
title: AgroTech — точное земледелие с AI-аналитикой
fonts:
  sans: Sora
  serif: IBM Plex Sans
  mono: JetBrains Mono
colorSchema: light
aspectRatio: 16/9
transition: fade
---

<!-- ============================================================ -->
<!-- SLIDE 1 — Cover Hero — bg-accent -->
<!-- ============================================================ -->

<div class="s1-root">
  <div class="s1-bg">
    <div class="s1-glow-tr"></div>
    <div class="s1-glow-bl"></div>
    <div class="s1-dots"></div>
  </div>
  <div class="s1-content">
    <div class="s1-label-wrap">
      <span class="s1-label">AgroTech · Pitch Deck · 2026</span>
    </div>
    <h1 class="s1-heading">AgroTech</h1>
    <p class="s1-sub">Урожайность на уровне данных</p>
    <div class="s1-meta">
      <span>Точное земледелие</span>
      <span class="s1-dot">·</span>
      <span>AI-аналитика</span>
      <span class="s1-dot">·</span>
      <span>Инвесторам</span>
    </div>
  </div>
</div>

<style>
.s1-root { position: absolute; inset: 0; overflow: hidden; }
.s1-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-accent); }
.s1-glow-tr { position: absolute; top: -100px; right: -100px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-glow-bl { position: absolute; bottom: -80px; left: -80px; width: 420px; height: 420px; background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-dots { position: absolute; bottom: 44px; right: 60px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(255,255,255,0.22) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s1-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s1-label-wrap { display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; margin-bottom: 28px; }
.s1-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.s1-heading { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: #FFFFFF; margin: 0 0 16px; line-height: 1.0; letter-spacing: -0.02em; }
.s1-sub { font-family: var(--font-body); font-size: 1.4rem; color: rgba(255,255,255,0.85); margin: 0 0 36px; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.9rem; color: rgba(255,255,255,0.65); }
.s1-dot { color: rgba(255,255,255,0.35); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 2 — Stat Hero (left-number-right-text) — bg-base — 890 млрд ₽ потери -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow"></div>
    <div class="s2-arc"></div>
    <div class="s2-dots"></div>
  </div>
  <div class="s2-content">
    <div class="s2-left">
      <span class="s2-label">Цена проблемы</span>
      <div class="s2-hero">890<br><span class="s2-hero-unit">млрд ₽</span></div>
      <p class="s2-caption">ежегодные потери российского АПК</p>
    </div>
    <div class="s2-right">
      <div class="s2-stat-card">
        <div class="s2-stat-icon">
          <Icon name="trending-down" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s2-stat-body">
          <span class="s2-stat-val">40%</span>
          <span class="s2-stat-txt">удобрений вносится впустую — не в то время, не в том объёме</span>
        </div>
      </div>
      <div class="s2-stat-card">
        <div class="s2-stat-icon">
          <Icon name="bar-chart" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s2-stat-body">
          <span class="s2-stat-val">1,8×</span>
          <span class="s2-stat-txt">урожайность отстаёт от Германии и Канады</span>
        </div>
      </div>
      <div class="s2-stat-card s2-stat-warm">
        <div class="s2-stat-icon-warm">
          <Icon name="leaf" :size="22" color="#D97706" />
        </div>
        <div class="s2-stat-body">
          <span class="s2-stat-val-warm">Источник</span>
          <span class="s2-stat-txt">Минсельхоз РФ, 2025</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow { position: absolute; top: 50%; left: 30%; transform: translate(-50%, -50%); width: 500px; height: 500px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-arc { position: absolute; top: 50%; left: 28%; transform: translate(-50%, -50%); width: 340px; height: 340px; border: 1.5px solid rgba(13,148,136,0.13); border-radius: 50%; pointer-events: none; }
.s2-dots { position: absolute; top: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 1fr 1fr; padding: 44px 64px; gap: 48px; align-items: center; }
.s2-left { display: flex; flex-direction: column; justify-content: center; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; align-self: flex-start; }
.s2-hero { font-family: var(--font-heading); font-size: 5rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s2-hero-unit { font-size: 2.8rem; font-weight: 700; color: var(--color-accent); }
.s2-caption { font-family: var(--font-body); font-size: 1.05rem; color: var(--color-muted); margin: 12px 0 0; line-height: 1.5; }
.s2-right { display: flex; flex-direction: column; gap: 12px; justify-content: center; }
.s2-stat-card { display: flex; align-items: flex-start; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; }
.s2-stat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-stat-icon { width: 42px; height: 42px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-stat-icon-warm { width: 42px; height: 42px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-stat-body { display: flex; flex-direction: column; gap: 4px; }
.s2-stat-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-stat-val-warm { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: #D97706; line-height: 1; text-transform: uppercase; letter-spacing: 0.08em; }
.s2-stat-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Bento Grid — bg-alt — +28% урожайность, −35% затраты -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-deco-dot"></div>
  </div>
  <div class="s3-content">
    <span class="s3-label">Результат AgroTech</span>
    <h1 class="s3-heading">AgroTech повышает урожайность на 28% и снижает затраты на 35%</h1>
    <div class="s3-grid">
      <div class="s3-featured">
        <div class="s3-feat-icon">
          <Icon name="trending-up" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s3-feat-num">+28%</div>
        <div class="s3-feat-label">рост урожайности в среднем по хозяйствам</div>
        <div class="s3-feat-tags">
          <span class="s3-tag">Спутник</span>
          <span class="s3-tag">Сенсоры</span>
          <span class="s3-tag">ML</span>
        </div>
      </div>
      <div class="s3-side-top">
        <div class="s3-side-icon">
          <Icon name="percent" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s3-side-body">
          <span class="s3-side-val">−35%</span>
          <span class="s3-side-txt">затраты на удобрения</span>
        </div>
      </div>
      <div class="s3-side-mid">
        <div class="s3-side-icon">
          <Icon name="smartphone" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s3-side-body">
          <span class="s3-side-val">2 клика</span>
          <span class="s3-side-txt">рекомендации в мобильном приложении</span>
        </div>
      </div>
      <div class="s3-side-bot">
        <div class="s3-side-icon-warm">
          <Icon name="map" :size="20" color="#D97706" />
        </div>
        <div class="s3-side-body">
          <span class="s3-side-val-warm">Карта</span>
          <span class="s3-side-txt">персональная карта внесения для каждого поля</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-deco-dot { position: absolute; top: 40px; right: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s3-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s3-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; line-height: 1.2; }
.s3-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s3-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s3-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s3-feat-num { font-family: var(--font-heading); font-size: 4.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-feat-label { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s3-feat-tags { display: flex; gap: 8px; margin-top: 20px; flex-wrap: wrap; }
.s3-tag { display: inline-flex; align-items: center; background: rgba(13,148,136,0.10); border: 1px solid rgba(13,148,136,0.25); border-radius: 12px; padding: 4px 12px; font-size: 0.72rem; font-weight: 600; color: var(--color-accent); font-family: var(--font-heading); line-height: 1; }
.s3-side-top, .s3-side-mid { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s3-side-bot { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s3-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-side-body { display: flex; flex-direction: column; gap: 3px; }
.s3-side-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-side-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s3-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Icon Trio 2×2 — bg-base — Три продукта -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <span class="s4-label">Продуктовая линейка</span>
    <h1 class="s4-heading">Три продукта закрывают весь цикл — от анализа до техники</h1>
    <div class="s4-grid">
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="satellite" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">FieldScan</span>
        <span class="s4-price">120 ₽/га/сезон</span>
        <span class="s4-desc">Мониторинг полей по спутниковым снимкам — выявляет проблемные зоны</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="cpu" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">SoilIQ</span>
        <span class="s4-price">280 ₽/га/сезон</span>
        <span class="s4-desc">Почвенная аналитика + персональные карты внесения удобрений</span>
      </div>
      <div class="s4-item s4-item-right">
        <div class="s4-icon">
          <Icon name="zap" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">AutoSpray</span>
        <span class="s4-price-warm">50 000 ₽/единица</span>
        <span class="s4-desc">Интеграция с опрыскивателями John Deere и Ростсельмаш — автоматическое внесение</span>
      </div>
      <div class="s4-item s4-item-accent">
        <div class="s4-icon-warm">
          <Icon name="layers" :size="26" color="#D97706" />
        </div>
        <span class="s4-title">Полный цикл</span>
        <span class="s4-price-warm">Единая экосистема</span>
        <span class="s4-desc">Спутник → сенсоры → ML → приложение → техника в одной платформе</span>
      </div>
    </div>
  </div>
</div>

<style>
.s4-root { position: absolute; inset: 0; overflow: hidden; }
.s4-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s4-glow { position: absolute; bottom: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s4-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s4-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s4-heading { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; line-height: 1.25; }
.s4-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-content: stretch; }
.s4-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 20px 24px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }
.s4-item-accent { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s4-icon { width: 48px; height: 48px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 6px; }
.s4-icon-warm { width: 48px; height: 48px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 6px; }
.s4-title { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; color: var(--color-text); }
.s4-price { font-family: var(--font-heading); font-size: 0.85rem; font-weight: 700; color: var(--color-accent); }
.s4-price-warm { font-family: var(--font-heading); font-size: 0.85rem; font-weight: 700; color: #D97706; }
.s4-desc { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Stat Hero (split-50-50) — bg-alt — Тяга: 180 хозяйств -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow-left"></div>
    <div class="s5-dots-right"></div>
  </div>
  <div class="s5-content">
    <div class="s5-header">
      <span class="s5-label">Тяга за 18 месяцев</span>
      <h1 class="s5-heading">180 хозяйств и 420 000 га под управлением</h1>
    </div>
    <div class="s5-metrics">
      <div class="s5-metric-main">
        <span class="s5-metric-val">8,5 млн ₽</span>
        <span class="s5-metric-lbl">MRR</span>
      </div>
      <div class="s5-divider"></div>
      <div class="s5-metric-main">
        <span class="s5-metric-val-warm">+22%</span>
        <span class="s5-metric-lbl">рост в месяц</span>
      </div>
      <div class="s5-divider"></div>
      <div class="s5-metric-main">
        <span class="s5-metric-val">47 000 ₽</span>
        <span class="s5-metric-lbl">средний чек / хозяйство / сезон</span>
      </div>
    </div>
    <div class="s5-retention">
      <div class="s5-ret-icon">
        <Icon name="check-circle" :size="22" color="var(--color-accent)" />
      </div>
      <div class="s5-ret-body">
        <span class="s5-ret-val">92% Retention</span>
        <span class="s5-ret-txt">фермеры возвращаются после первого урожая — доказанный product-market fit</span>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-glow-left { position: absolute; left: -80px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-dots-right { position: absolute; bottom: 30px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; padding: 48px 72px; gap: 28px; }
.s5-header { display: flex; flex-direction: column; gap: 6px; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; }
.s5-heading { font-family: var(--font-heading); font-size: 2.1rem; font-weight: 700; color: var(--color-text); margin: 0; line-height: 1.2; }
.s5-metrics { display: flex; align-items: center; gap: 0; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 24px 32px; }
.s5-metric-main { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; }
.s5-metric-val { font-family: var(--font-heading); font-size: 2.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-metric-val-warm { font-family: var(--font-heading); font-size: 2.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s5-metric-lbl { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); text-align: center; }
.s5-divider { width: 1px; height: 56px; background: var(--color-surface-border); flex-shrink: 0; margin: 0 16px; }
.s5-retention { display: flex; align-items: flex-start; gap: 16px; background: linear-gradient(135deg, rgba(13,148,136,0.08), transparent); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 18px 24px; }
.s5-ret-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; }
.s5-ret-body { display: flex; flex-direction: column; gap: 4px; }
.s5-ret-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-ret-txt { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Section Divider — bg-alt — Технология и рынок -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow"></div>
    <div class="s6-arc-outer"></div>
    <div class="s6-arc-inner"></div>
    <div class="s6-dots"></div>
  </div>
  <div class="s6-content">
    <span class="s6-eyebrow">Часть II</span>
    <h1 class="s6-heading">Технология и рынок</h1>
    <p class="s6-sub">Как работает AI-платформа и куда растёт рынок AgTech</p>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s6-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 440px; height: 440px; border: 1.5px solid rgba(13,148,136,0.18); border-radius: 50%; pointer-events: none; }
.s6-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 280px; height: 280px; border: 1px solid rgba(13,148,136,0.12); border-radius: 50%; pointer-events: none; }
.s6-dots { position: absolute; bottom: 50px; right: 60px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.30) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; }
.s6-eyebrow { display: inline-block; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; font-family: var(--font-heading); margin-bottom: 16px; }
.s6-heading { font-family: var(--font-heading); font-size: 3.5rem; font-weight: 800; color: var(--color-text); margin: 0 0 20px; line-height: 1.1; }
.s6-sub { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); max-width: 600px; line-height: 1.6; margin: 0; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Asymmetric Split — bg-base — ML 91% точность -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow"></div>
    <div class="s7-dots"></div>
  </div>
  <div class="s7-content">
    <div class="s7-left">
      <div class="s7-visual">
        <div class="s7-big-icon">
          <Icon name="brain" :size="56" color="var(--color-accent)" />
        </div>
        <div class="s7-accuracy">
          <span class="s7-acc-val">91%</span>
          <span class="s7-acc-lbl">точность прогноза</span>
        </div>
      </div>
    </div>
    <div class="s7-right">
      <span class="s7-label">ML-платформа</span>
      <h1 class="s7-heading">Предсказывает урожайность за 45 дней до уборки</h1>
      <div class="s7-features">
        <div class="s7-feat">
          <div class="s7-feat-icon">
            <Icon name="activity" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s7-feat-txt">3 года обучения на данных 2 000 полей</span>
        </div>
        <div class="s7-feat">
          <div class="s7-feat-icon">
            <Icon name="layers" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s7-feat-txt">Модель учитывает: спутник, погоду, почву, историю внесения</span>
        </div>
        <div class="s7-feat s7-feat-warm">
          <div class="s7-feat-icon-warm">
            <Icon name="trending-up" :size="18" color="#D97706" />
          </div>
          <span class="s7-feat-txt">Краснодарский край: +31% пшеница, +24% подсолнечник</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s7-glow { position: absolute; left: -80px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-dots { position: absolute; top: 40px; right: 48px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 48px; align-items: center; }
.s7-left { display: flex; justify-content: center; align-items: center; }
.s7-visual { display: flex; flex-direction: column; align-items: center; gap: 20px; }
.s7-big-icon { width: 148px; height: 148px; border-radius: 28px; background: var(--color-accent-bg); border: 2px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s7-accuracy { display: flex; flex-direction: column; align-items: center; gap: 4px; }
.s7-acc-val { font-family: var(--font-heading); font-size: 3rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-acc-lbl { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); }
.s7-right { display: flex; flex-direction: column; justify-content: center; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s7-features { display: flex; flex-direction: column; gap: 12px; }
.s7-feat { display: flex; align-items: flex-start; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; }
.s7-feat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s7-feat-icon { width: 36px; height: 36px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px; }
.s7-feat-icon-warm { width: 36px; height: 36px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px; }
.s7-feat-txt { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-text); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Data Spotlight — bg-alt — Рынок 85 млрд к 2028 -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow"></div>
    <div class="s8-dots"></div>
  </div>
  <div class="s8-content">
    <span class="s8-label">Рынок AgTech РФ</span>
    <h1 class="s8-heading">Рынок вырастет до 85 млрд ₽ к 2028 году — CAGR 38%</h1>
    <div class="s8-metrics">
      <div class="s8-card s8-card-featured">
        <div class="s8-card-icon">
          <Icon name="trending-up" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-card-val">85 млрд ₽</div>
        <div class="s8-card-lbl">объём рынка к 2028</div>
      </div>
      <div class="s8-card">
        <div class="s8-card-icon">
          <Icon name="bar-chart" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-card-val">32 млрд ₽</div>
        <div class="s8-card-lbl">текущий объём рынка</div>
      </div>
      <div class="s8-card s8-card-warm">
        <div class="s8-card-icon-warm">
          <Icon name="zap" :size="20" color="#D97706" />
        </div>
        <div class="s8-card-val-warm">38%</div>
        <div class="s8-card-lbl">CAGR — опережает мировой рынок</div>
      </div>
    </div>
    <div class="s8-competition">
      <span class="s8-comp-title">Конкурентное окно</span>
      <div class="s8-comp-items">
        <div class="s8-comp-item">
          <Icon name="check-circle" :size="16" color="var(--color-accent)" />
          <span class="s8-comp-txt">Cropio — импортный, нет локализации под РФ-агробизнес</span>
        </div>
        <div class="s8-comp-item">
          <Icon name="check-circle" :size="16" color="var(--color-accent)" />
          <span class="s8-comp-txt">OneSoil — общие рекомендации без интеграции с техникой</span>
        </div>
        <div class="s8-comp-item s8-comp-warm">
          <Icon name="target" :size="16" color="#D97706" />
          <span class="s8-comp-txt-warm">AgroTech — единственная полная экосистема с русскоязычной поддержкой</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s8-glow { position: absolute; top: -80px; right: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-dots { position: absolute; bottom: 40px; left: 50px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; gap: 16px; }
.s8-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; }
.s8-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0; line-height: 1.2; }
.s8-metrics { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
.s8-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 22px; display: flex; flex-direction: column; gap: 4px; }
.s8-card-featured { background: linear-gradient(135deg, rgba(13,148,136,0.1), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); }
.s8-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s8-card-icon { width: 36px; height: 36px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 8px; }
.s8-card-icon-warm { width: 36px; height: 36px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 8px; }
.s8-card-val { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s8-card-val-warm { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s8-card-lbl { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); line-height: 1.35; }
.s8-competition { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; }
.s8-comp-title { font-family: var(--font-heading); font-size: 0.82rem; font-weight: 700; color: var(--color-text); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; display: block; }
.s8-comp-items { display: flex; flex-direction: column; gap: 8px; }
.s8-comp-item { display: flex; align-items: flex-start; gap: 10px; }
.s8-comp-warm { }
.s8-comp-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s8-comp-txt-warm { font-family: var(--font-body); font-size: 0.82rem; color: #D97706; font-weight: 600; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — Profile Grid — bg-base — Команда -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-glow"></div>
    <div class="s9-dots"></div>
  </div>
  <div class="s9-content">
    <span class="s9-label">Команда</span>
    <h1 class="s9-heading">3 PhD в агрономии + 15 лет в Machine Learning</h1>
    <div class="s9-grid">
      <div class="s9-profile">
        <div class="s9-avatar">
          <Icon name="user" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s9-profile-body">
          <span class="s9-role">CEO</span>
          <span class="s9-bio">Кандидат с.-х. наук, 12 лет в агроконсалтинге. Построил 3 прибыльных хозяйства.</span>
        </div>
      </div>
      <div class="s9-profile">
        <div class="s9-avatar">
          <Icon name="cpu" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s9-profile-body">
          <span class="s9-role">CTO</span>
          <span class="s9-bio">Ex-Яндекс, lead ML engineer. Автор 8 патентов в области компьютерного зрения.</span>
        </div>
      </div>
      <div class="s9-profile s9-profile-warm">
        <div class="s9-avatar-warm">
          <Icon name="layers" :size="22" color="#D97706" />
        </div>
        <div class="s9-profile-body">
          <span class="s9-role-warm">COO</span>
          <span class="s9-bio">Построил логистику для агрохолдинга «Мираторг» — 500 000 га под управлением.</span>
        </div>
      </div>
    </div>
    <div class="s9-advisors">
      <div class="s9-adv-icon">
        <Icon name="award" :size="18" color="var(--color-accent)" />
      </div>
      <span class="s9-adv-txt">Научный совет: профессора РГАУ-МСХА им. Тимирязева и Сколтеха</span>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s9-glow { position: absolute; top: -60px; left: -60px; width: 420px; height: 420px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-dots { position: absolute; bottom: 44px; right: 60px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; gap: 20px; }
.s9-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; }
.s9-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0; line-height: 1.2; }
.s9-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; flex: 1; }
.s9-profile { display: flex; align-items: flex-start; gap: 14px; background: transparent; border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 20px 22px; }
.s9-profile-warm { background: rgba(217,119,6,0.05); border: 1.5px solid rgba(217,119,6,0.25); }
.s9-avatar { width: 48px; height: 48px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-avatar-warm { width: 48px; height: 48px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-profile-body { display: flex; flex-direction: column; gap: 6px; }
.s9-role { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-accent); }
.s9-role-warm { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: #D97706; }
.s9-bio { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.45; }
.s9-advisors { display: flex; align-items: center; gap: 12px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 20px; }
.s9-adv-icon { width: 34px; height: 34px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-adv-txt { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-text); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 10 — CTA Warm — bg-accent — Раунд А: 150 млн ₽ -->
<!-- ============================================================ -->

<div class="s10-root">
  <div class="s10-bg">
    <div class="s10-bg-gradient"></div>
    <div class="s10-glow-tr"></div>
    <div class="s10-glow-bl"></div>
    <div class="s10-dots"></div>
  </div>
  <div class="s10-content">
    <span class="s10-label">Раунд А</span>
    <h1 class="s10-heading">Привлекаем 150 млн ₽ на масштабирование до 2 млн га</h1>
    <div class="s10-goals">
      <div class="s10-goal">
        <span class="s10-goal-num">01</span>
        <span class="s10-goal-txt">800 хозяйств к концу 2026 года</span>
      </div>
      <div class="s10-goal">
        <span class="s10-goal-num">02</span>
        <span class="s10-goal-txt">2 000 000 га под управлением платформы</span>
      </div>
      <div class="s10-goal s10-goal-warm">
        <span class="s10-goal-num-warm">03</span>
        <span class="s10-goal-txt-warm">Выход в Казахстан — второй по объёму рынок СНГ</span>
      </div>
    </div>
    <div class="s10-contact">
      <div class="s10-contact-item">
        <Icon name="mail" :size="18" color="rgba(255,255,255,0.85)" />
        <span class="s10-contact-txt">invest@agrotech.farm</span>
      </div>
      <span class="s10-contact-sep">·</span>
      <div class="s10-contact-item">
        <Icon name="globe" :size="18" color="rgba(255,255,255,0.85)" />
        <span class="s10-contact-txt">agrotech.farm</span>
      </div>
    </div>
  </div>
</div>

<style>
.s10-root { position: absolute; inset: 0; overflow: hidden; }
.s10-bg { position: absolute; inset: 0; z-index: 0; }
.s10-bg-gradient { position: absolute; inset: 0; background: linear-gradient(145deg, var(--bg-accent) 0%, color-mix(in srgb, var(--bg-accent) 70%, black) 100%); }
.s10-glow-tr { position: absolute; top: -80px; right: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s10-glow-bl { position: absolute; bottom: -80px; left: -80px; width: 380px; height: 380px; background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s10-dots { position: absolute; bottom: 44px; right: 60px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s10-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s10-label { display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; margin-bottom: 24px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.s10-heading { font-family: var(--font-heading); font-size: 2.6rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.15; max-width: 780px; }
.s10-goals { display: flex; flex-direction: column; gap: 10px; max-width: 620px; width: 100%; margin-bottom: 32px; }
.s10-goal { display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22); border-radius: 12px; padding: 14px 20px; text-align: left; }
.s10-goal-warm { background: rgba(217,119,6,0.20); border: 1px solid rgba(217,119,6,0.40); }
.s10-goal-num { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: rgba(255,255,255,0.55); line-height: 1; flex-shrink: 0; width: 28px; }
.s10-goal-num-warm { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: #D97706; line-height: 1; flex-shrink: 0; width: 28px; }
.s10-goal-txt { font-family: var(--font-body); font-size: 0.95rem; color: rgba(255,255,255,0.90); line-height: 1.4; }
.s10-goal-txt-warm { font-family: var(--font-body); font-size: 0.95rem; color: rgba(255,255,255,0.95); font-weight: 600; line-height: 1.4; }
.s10-contact { display: flex; align-items: center; gap: 16px; }
.s10-contact-item { display: flex; align-items: center; gap: 8px; }
.s10-contact-txt { font-family: var(--font-body); font-size: 1rem; color: rgba(255,255,255,0.85); }
.s10-contact-sep { font-size: 1rem; color: rgba(255,255,255,0.35); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
