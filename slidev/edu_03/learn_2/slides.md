---
theme: default
title: Ремесло — Инвестиционное обновление Q1 2026
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

---
layout: none
---

<div class="s1-root">
  <div class="s1-bg">
    <div class="s1-glow-tl"></div>
    <div class="s1-glow-br"></div>
    <div class="s1-dot-grid"></div>
  </div>
  <div class="s1-content">
    <div class="s1-label-wrap">
      <span class="s1-label">Обновление для инвесторов · Q1 2026</span>
    </div>
    <h1 class="s1-heading">Ремесло</h1>
    <p class="s1-sub">Платформа, где мастера находят ценителей</p>
    <div class="s1-meta">
      <span>Маркетплейс handmade-товаров</span>
      <span class="s1-dot">·</span>
      <span>Раунд B</span>
      <span class="s1-dot">·</span>
      <span>Март 2026</span>
    </div>
  </div>
</div>

<style>
.s1-root { position: absolute; inset: 0; overflow: hidden; }
.s1-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-accent); }
.s1-glow-tl { position: absolute; top: -120px; left: -120px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-glow-br { position: absolute; bottom: -100px; right: -100px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-dot-grid { position: absolute; top: 40px; right: 60px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(255,255,255,0.22) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s1-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s1-label-wrap { display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; margin-bottom: 28px; }
.s1-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.s1-heading { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: #FFFFFF; margin: 0 0 16px; line-height: 1.0; letter-spacing: -0.02em; }
.s1-sub { font-family: var(--font-body); font-size: 1.4rem; color: rgba(255,255,255,0.85); margin: 0 0 36px; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.9rem; color: rgba(255,255,255,0.65); }
.s1-dot { color: rgba(255,255,255,0.35); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 2 — Stat Hero centered — bg-base — Рынок 89 млрд ₽ -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow"></div>
    <div class="s2-arc"></div>
  </div>
  <div class="s2-content">
    <span class="s2-label">Рынок handmade в России</span>
    <div class="s2-hero">89 млрд ₽</div>
    <p class="s2-caption">Объём рынка в 2025 году</p>
    <div class="s2-pills">
      <span class="s2-pill">
        <span class="s2-pill-num">+35%</span>
        <span class="s2-pill-txt">рост год к году</span>
      </span>
      <span class="s2-pill">
        <span class="s2-pill-num">2,3 млн</span>
        <span class="s2-pill-txt">активных мастеров</span>
      </span>
      <span class="s2-pill s2-pill-warm">
        <span class="s2-pill-num-warm">68%</span>
        <span class="s2-pill-txt">готовы платить премию</span>
      </span>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 560px; height: 560px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-arc { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 380px; height: 380px; border: 1.5px solid rgba(13,148,136,0.14); border-radius: 50%; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 48px 80px; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s2-hero { font-family: var(--font-heading); font-size: 6rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s2-caption { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); margin: 10px 0 32px; }
.s2-pills { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
.s2-pill { display: flex; flex-direction: column; align-items: center; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 14px 24px; min-width: 140px; }
.s2-pill-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-pill-num { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-pill-num-warm { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-pill-txt { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); margin-top: 4px; text-align: center; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 3 — Asymmetric split — bg-alt — GMV +47% -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-deco-dot"></div>
  </div>
  <div class="s3-content">
    <div class="s3-left">
      <div class="s3-metric-block">
        <span class="s3-metric-label">GMV Q1 2026</span>
        <div class="s3-big-num">265</div>
        <span class="s3-big-unit">млн ₽</span>
        <div class="s3-badge">
          <Icon name="trending-up" :size="14" color="#D97706" />
          <span class="s3-badge-txt">+47% за квартал</span>
        </div>
      </div>
    </div>
    <div class="s3-right">
      <span class="s3-label">Рост GMV ускоряется</span>
      <h1 class="s3-heading">+47% GMV за квартал</h1>
      <div class="s3-cards">
        <div class="s3-card">
          <span class="s3-card-period">Q4 2025</span>
          <span class="s3-card-val">180 млн ₽</span>
          <span class="s3-card-sub">GMV</span>
        </div>
        <div class="s3-card s3-card-accent">
          <span class="s3-card-period">Q1 2026</span>
          <span class="s3-card-val-accent">265 млн ₽</span>
          <span class="s3-card-sub">GMV</span>
        </div>
        <div class="s3-card s3-card-full">
          <Icon name="percent" :size="20" color="var(--color-accent)" />
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s3-card-val">12%</span>
            <span class="s3-card-sub">Take rate стабильный</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-deco-dot { position: absolute; bottom: 30px; left: 30px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s3-left { display: flex; justify-content: center; align-items: center; }
.s3-metric-block { display: flex; flex-direction: column; align-items: center; text-align: center; }
.s3-metric-label { font-family: var(--font-body); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--color-muted); font-weight: 600; margin-bottom: 8px; }
.s3-big-num { font-family: var(--font-heading); font-size: 7rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-big-unit { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-accent); margin-top: -4px; }
.s3-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); border-radius: 20px; padding: 6px 14px; margin-top: 16px; }
.s3-badge-txt { font-family: var(--font-body); font-size: 0.78rem; color: #D97706; font-weight: 700; }
.s3-right { display: flex; flex-direction: column; justify-content: center; }
.s3-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s3-heading { font-family: var(--font-heading); font-size: 2.1rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s3-cards { display: flex; flex-direction: column; gap: 10px; }
.s3-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 14px 20px; display: flex; flex-direction: column; gap: 2px; }
.s3-card-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s3-card-full { flex-direction: row; align-items: center; gap: 14px; }
.s3-card-period { font-family: var(--font-body); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-muted); font-weight: 600; }
.s3-card-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-text); line-height: 1.1; }
.s3-card-val-accent { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1.1; }
.s3-card-sub { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 4 — Icon Trio (3 revenue sources) — bg-base — rounded-square containers -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <span class="s4-label">Модель монетизации</span>
    <h1 class="s4-heading">Три источника дохода — диверсифицированная модель</h1>
    <div class="s4-trio">
      <div class="s4-item">
        <div class="s4-icon-wrap">
          <Icon name="percent" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s4-item-title">Комиссия с продаж</span>
        <span class="s4-item-num">12%</span>
        <span class="s4-item-share">70% выручки</span>
        <span class="s4-item-desc">Основной источник — с каждой транзакции на платформе</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon-wrap">
          <Icon name="star" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s4-item-title">Подписка Pro</span>
        <span class="s4-item-num s4-num-warm">20%</span>
        <span class="s4-item-share">выручки</span>
        <span class="s4-item-desc">Аналитика и продвижение для мастеров</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon-wrap">
          <Icon name="megaphone" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s4-item-title">Реклама брендов</span>
        <span class="s4-item-num">10%</span>
        <span class="s4-item-share">выручки</span>
        <span class="s4-item-desc">Интеграции с брендами в экосистеме платформы</span>
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
.s4-heading { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-text); margin: 0 0 28px; }
.s4-trio { flex: 1; display: flex; justify-content: center; align-items: center; gap: 24px; }
.s4-item { display: flex; flex-direction: column; align-items: center; text-align: center; flex: 1; max-width: 240px; }
.s4-icon-wrap { width: 60px; height: 60px; border-radius: 14px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s4-item-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); margin-bottom: 4px; }
.s4-item-num { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 2px 0; }
.s4-num-warm { color: #D97706; }
.s4-item-share { display: inline-flex; align-items: center; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 20px; padding: 3px 10px; font-size: 0.7rem; font-weight: 600; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.08em; margin: 6px 0 8px; font-family: var(--font-body); }
.s4-item-desc { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 5 — Stat Hero left-number-right-text — bg-alt — NPS 72 -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow-left"></div>
    <div class="s5-dot-grid"></div>
  </div>
  <div class="s5-content">
    <div class="s5-left">
      <span class="s5-label">Удержание аудитории</span>
      <div class="s5-nps">72</div>
      <p class="s5-nps-sub">Net Promoter Score</p>
    </div>
    <div class="s5-divider"></div>
    <div class="s5-right">
      <h1 class="s5-heading">Мастера рекомендуют платформу друг другу</h1>
      <div class="s5-metrics">
        <div class="s5-metric">
          <div class="s5-metric-icon">
            <Icon name="users" :size="22" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s5-metric-val">45%</span>
            <span class="s5-metric-txt">новых мастеров — по рекомендации</span>
          </div>
        </div>
        <div class="s5-metric">
          <div class="s5-metric-icon">
            <Icon name="heart" :size="22" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s5-metric-val">14 мес.</span>
            <span class="s5-metric-txt">средний срок жизни мастера</span>
          </div>
        </div>
        <div class="s5-metric">
          <div class="s5-metric-icon-warm">
            <Icon name="trending-up" :size="22" color="#D97706" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s5-metric-val-warm">8% → 3,5%</span>
            <span class="s5-metric-txt">отток снизился за квартал</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-glow-left { position: absolute; top: 50%; left: -80px; transform: translateY(-50%); width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.16) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-dot-grid { position: absolute; top: 40px; right: 60px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 1fr 2px 1.5fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s5-left { display: flex; flex-direction: column; align-items: flex-start; justify-content: center; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 16px; }
.s5-nps { font-family: var(--font-heading); font-size: 8rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s5-nps-sub { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); margin: 4px 0 0; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; }
.s5-divider { background: var(--color-accent-dim); border-radius: 2px; align-self: stretch; }
.s5-right { display: flex; flex-direction: column; justify-content: center; }
.s5-heading { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s5-metrics { display: flex; flex-direction: column; gap: 12px; }
.s5-metric { display: flex; align-items: center; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 14px 20px; }
.s5-metric-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-metric-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-metric-val { font-family: var(--font-heading); font-size: 1.3rem; font-weight: 800; color: var(--color-text); line-height: 1; }
.s5-metric-val-warm { font-family: var(--font-heading); font-size: 1.3rem; font-weight: 800; color: #D97706; line-height: 1; }
.s5-metric-txt { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); line-height: 1.3; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 6 — Timeline Horizontal 3 days — bg-base — Customer journey -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Путь мастера</span>
    <h1 class="s6-heading">От регистрации до первой продажи за 3 дня</h1>
    <div class="s6-timeline">
      <div class="s6-stage">
        <div class="s6-stage-head">
          <div class="s6-day-badge">День 1</div>
          <div class="s6-stage-icon">
            <Icon name="user-check" :size="22" color="var(--color-accent)" />
          </div>
        </div>
        <div class="s6-stage-body">
          <span class="s6-stage-title">Регистрация</span>
          <span class="s6-stage-desc">AI-генерация описаний товаров — профиль готов за минуты</span>
        </div>
      </div>
      <div class="s6-connector">
        <div class="s6-conn-line"></div>
        <Icon name="arrow-right" :size="18" color="var(--color-accent-dim)" />
      </div>
      <div class="s6-stage">
        <div class="s6-stage-head">
          <div class="s6-day-badge">День 2</div>
          <div class="s6-stage-icon">
            <Icon name="camera" :size="22" color="var(--color-accent)" />
          </div>
        </div>
        <div class="s6-stage-body">
          <span class="s6-stage-title">Фотосессия</span>
          <span class="s6-stage-desc">Автоматическая мобильная студия — товары выглядят профессионально</span>
        </div>
      </div>
      <div class="s6-connector">
        <div class="s6-conn-line"></div>
        <Icon name="arrow-right" :size="18" color="var(--color-accent-dim)" />
      </div>
      <div class="s6-stage s6-stage-accent">
        <div class="s6-stage-head">
          <div class="s6-day-badge-warm">День 3</div>
          <div class="s6-stage-icon-warm">
            <Icon name="zap" :size="22" color="#D97706" />
          </div>
        </div>
        <div class="s6-stage-body">
          <span class="s6-stage-title">Первая продажа</span>
          <span class="s6-stage-desc-accent">Рекомендательная система находит первого покупателя</span>
        </div>
      </div>
    </div>
    <div class="s6-footer">
      <Icon name="check-circle" :size="16" color="var(--color-accent)" />
      <span class="s6-footer-txt">Средний мастер завершает воронку за 2,8 дня</span>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-glow { position: absolute; top: -60px; right: -60px; width: 420px; height: 420px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; }
.s6-timeline { flex: 1; display: flex; align-items: center; gap: 0; }
.s6-stage { flex: 1; display: flex; flex-direction: column; gap: 16px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 20px; align-self: stretch; }
.s6-stage-accent { background: rgba(217,119,6,0.06); border: 1.5px solid rgba(217,119,6,0.28); }
.s6-stage-head { display: flex; flex-direction: column; align-items: flex-start; gap: 12px; }
.s6-day-badge { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 4px 12px; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); font-weight: 700; line-height: 1; font-family: var(--font-heading); }
.s6-day-badge-warm { display: inline-flex; align-items: center; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); border-radius: 20px; padding: 4px 12px; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.12em; color: #D97706; font-weight: 700; line-height: 1; font-family: var(--font-heading); }
.s6-stage-icon { width: 48px; height: 48px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s6-stage-icon-warm { width: 48px; height: 48px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; }
.s6-stage-body { display: flex; flex-direction: column; gap: 6px; }
.s6-stage-title { font-family: var(--font-heading); font-size: 1.1rem; font-weight: 700; color: var(--color-text); }
.s6-stage-desc { font-family: var(--font-body); font-size: 0.83rem; color: var(--color-muted); line-height: 1.45; }
.s6-stage-desc-accent { font-family: var(--font-body); font-size: 0.83rem; color: #D97706; line-height: 1.45; font-weight: 600; }
.s6-connector { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 0 8px; gap: 4px; }
.s6-conn-line { width: 1px; height: 40px; background: var(--color-accent-dim); }
.s6-footer { display: flex; align-items: center; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s6-footer-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 7 — Bento Grid — bg-alt — Plans 2026 -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow"></div>
  </div>
  <div class="s7-content">
    <span class="s7-label">Стратегия на 2026</span>
    <h1 class="s7-heading">GMV 2 млрд ₽ и выход в СНГ</h1>
    <div class="s7-grid">
      <!-- Featured card -->
      <div class="s7-featured">
        <div class="s7-feat-icon">
          <Icon name="globe" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s7-feat-num">2 млрд ₽</div>
        <div class="s7-feat-label">целевой GMV в 2026</div>
        <div class="s7-feat-subs">
          <div class="s7-feat-sub">
            <span class="s7-sub-val">Q2</span>
            <span class="s7-sub-txt">запуск в Казахстане и Беларуси</span>
          </div>
          <div class="s7-feat-sub">
            <span class="s7-sub-val">5</span>
            <span class="s7-sub-txt">городов «Ремесло Live»</span>
          </div>
        </div>
      </div>
      <!-- Side card 1 -->
      <div class="s7-side">
        <div class="s7-side-icon">
          <Icon name="map-pin" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:3px;">
          <span class="s7-side-title">Экспансия в СНГ</span>
          <span class="s7-side-desc">Казахстан + Беларусь — Q2 2026. Локализованные платёжные интеграции.</span>
        </div>
      </div>
      <!-- Side card 2 -->
      <div class="s7-side">
        <div class="s7-side-icon s7-side-icon-warm">
          <Icon name="cpu" :size="20" color="#D97706" />
        </div>
        <div style="display:flex;flex-direction:column;gap:3px;">
          <span class="s7-side-title">AI-стилист</span>
          <span class="s7-side-desc">Персональный подбор товаров для покупателей на основе ML-рекомендаций.</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-glow { position: absolute; top: -80px; left: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 2.0rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s7-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px; }
.s7-featured { grid-row: 1 / 3; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 24px; display: flex; flex-direction: column; justify-content: center; }
.s7-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; }
.s7-feat-num { font-family: var(--font-heading); font-size: 4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-feat-label { font-family: var(--font-body); font-size: 0.95rem; color: var(--color-muted); margin-top: 4px; margin-bottom: 20px; }
.s7-feat-subs { display: flex; flex-direction: column; gap: 10px; }
.s7-feat-sub { display: flex; align-items: baseline; gap: 8px; }
.s7-sub-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-text); line-height: 1; }
.s7-sub-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.35; }
.s7-side { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 22px; display: flex; align-items: flex-start; gap: 14px; }
.s7-side-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-side-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-side-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); }
.s7-side-desc { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

<!-- ============================================================ -->
<!-- SLIDE 8 — CTA Warm — bg-accent — Investment Ask -->
<!-- ============================================================ -->

---
layout: none
---

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow-tl"></div>
    <div class="s8-glow-br"></div>
    <div class="s8-dot-grid"></div>
  </div>
  <div class="s8-content">
    <span class="s8-label">Раунд B · 2026</span>
    <h1 class="s8-heading">Привлекаем 250 млн ₽ на масштабирование платформы</h1>
    <div class="s8-valuation">
      <span class="s8-val-num">1,8 млрд ₽</span>
      <span class="s8-val-txt">оценка компании</span>
    </div>
    <div class="s8-alloc">
      <div class="s8-alloc-item">
        <span class="s8-alloc-pct">60%</span>
        <span class="s8-alloc-label">Рост и маркетинг</span>
      </div>
      <div class="s8-alloc-sep"></div>
      <div class="s8-alloc-item">
        <span class="s8-alloc-pct">25%</span>
        <span class="s8-alloc-label">Технологии</span>
      </div>
      <div class="s8-alloc-sep"></div>
      <div class="s8-alloc-item">
        <span class="s8-alloc-pct">15%</span>
        <span class="s8-alloc-label">Экспансия в СНГ</span>
      </div>
    </div>
    <div class="s8-contact">
      <Icon name="mail" :size="18" color="rgba(255,255,255,0.75)" />
      <span class="s8-contact-txt">invest@remeslo.market</span>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: linear-gradient(145deg, var(--bg-accent) 0%, #0a6e66 100%); }
.s8-glow-tl { position: absolute; top: -100px; left: -100px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(255,255,255,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-glow-br { position: absolute; bottom: -80px; right: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(255,255,255,0.09) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-dot-grid { position: absolute; bottom: 50px; left: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(255,255,255,0.20) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s8-label { display: inline-flex; align-items: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s8-heading { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: #FFFFFF; margin: 0 0 24px; line-height: 1.15; max-width: 760px; }
.s8-valuation { display: flex; align-items: baseline; gap: 12px; margin-bottom: 28px; }
.s8-val-num { font-family: var(--font-heading); font-size: 3.5rem; font-weight: 800; color: #FFFFFF; line-height: 1; }
.s8-val-txt { font-family: var(--font-body); font-size: 1rem; color: rgba(255,255,255,0.70); }
.s8-alloc { display: flex; align-items: center; gap: 0; background: rgba(255,255,255,0.10); border: 1.5px solid rgba(255,255,255,0.25); border-radius: 14px; padding: 16px 32px; margin-bottom: 28px; }
.s8-alloc-item { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 0 24px; }
.s8-alloc-pct { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #FFFFFF; line-height: 1; }
.s8-alloc-label { font-family: var(--font-body); font-size: 0.78rem; color: rgba(255,255,255,0.72); text-align: center; }
.s8-alloc-sep { width: 1px; height: 48px; background: rgba(255,255,255,0.25); }
.s8-contact { display: flex; align-items: center; gap: 10px; }
.s8-contact-txt { font-family: var(--font-body); font-size: 1.1rem; color: rgba(255,255,255,0.85); font-weight: 500; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
