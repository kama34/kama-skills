---
theme: default
layout: none
title: Транспорт будущего — умный город
fonts:
  sans: Sora
  serif: IBM Plex Sans
  mono: JetBrains Mono
colorSchema: light
aspectRatio: 16/9
transition: fade
---

<!-- ============================================================ -->
<!-- SLIDE 1 — Cover Hero — bg-accent — Транспорт будущего -->
<!-- ============================================================ -->

<div class="s1-root">
  <div class="s1-bg">
    <div class="s1-glow-tr"></div>
    <div class="s1-glow-bl"></div>
    <div class="s1-dots"></div>
  </div>
  <div class="s1-content">
    <div class="s1-label-wrap">
      <span class="s1-label">Smart City Conference 2026</span>
    </div>
    <h1 class="s1-heading">Транспорт будущего</h1>
    <p class="s1-sub">От пробок к потокам — как умный город меняет мобильность</p>
    <div class="s1-meta">
      <span>Аналитический обзор</span>
      <span class="s1-dot">·</span>
      <span>Smart City Conference</span>
      <span class="s1-dot">·</span>
      <span>2026</span>
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
.s1-heading { font-family: var(--font-heading); font-size: 5rem; font-weight: 800; color: #FFFFFF; margin: 0 0 16px; line-height: 1.0; letter-spacing: -0.02em; }
.s1-sub { font-family: var(--font-body); font-size: 1.35rem; color: rgba(255,255,255,0.85); margin: 0 0 36px; max-width: 700px; line-height: 1.4; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.9rem; color: rgba(255,255,255,0.65); }
.s1-dot { color: rgba(255,255,255,0.35); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 2 — Stat Hero (left-number-right-text) — bg-base — 320 часов в пробках -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow-left"></div>
    <div class="s2-dot-grid"></div>
  </div>
  <div class="s2-content">
    <div class="s2-left">
      <span class="s2-label">Цена городских пробок</span>
      <div class="s2-hero">320</div>
      <div class="s2-unit">часов в год</div>
      <div class="s2-caption">каждый москвич теряет в пробках — это 40 рабочих дней</div>
    </div>
    <div class="s2-divider"></div>
    <div class="s2-right">
      <h1 class="s2-heading">Транспортный кризис стоит городу больше, чем кажется</h1>
      <div class="s2-metrics">
        <div class="s2-metric">
          <div class="s2-met-icon">
            <Icon name="ruble" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s2-met-val">1,8 трлн ₽</span>
            <span class="s2-met-txt">ежегодные экономические потери по РФ от заторов</span>
          </div>
        </div>
        <div class="s2-metric">
          <div class="s2-met-icon">
            <Icon name="car" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s2-met-val">12 км/ч</span>
            <span class="s2-met-txt">средняя скорость в часы пик в центре Москвы</span>
          </div>
        </div>
        <div class="s2-metric s2-metric-warm">
          <div class="s2-met-icon-warm">
            <Icon name="wind" :size="20" color="#D97706" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s2-met-val-warm">27%</span>
            <span class="s2-met-txt">всех городских выбросов CO₂ — транспортный сектор</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow-left { position: absolute; left: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-dot-grid { position: absolute; top: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 2px 3fr; padding: 44px 64px; gap: 32px; align-items: center; }
.s2-left { display: flex; flex-direction: column; justify-content: center; gap: 8px; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; margin-bottom: 8px; }
.s2-hero { font-family: var(--font-heading); font-size: 6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-unit { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; color: var(--color-accent); opacity: 0.75; }
.s2-caption { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-muted); line-height: 1.45; margin-top: 6px; }
.s2-divider { width: 2px; background: var(--color-surface-border); align-self: stretch; border-radius: 2px; }
.s2-right { display: flex; flex-direction: column; justify-content: center; }
.s2-heading { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s2-metrics { display: flex; flex-direction: column; gap: 12px; }
.s2-metric { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 14px; }
.s2-metric-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-met-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-met-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-met-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-met-val-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-met-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Stat Hero (split-50-50) — bg-alt — Точка невозврата 2030 -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-glow"></div>
    <div class="s3-arc-outer"></div>
    <div class="s3-arc-inner"></div>
  </div>
  <div class="s3-content">
    <div class="s3-left">
      <span class="s3-label">Без изменений к 2030</span>
      <div class="s3-hero">8 км/ч</div>
      <p class="s3-caption">средняя скорость в часы пик — уровень пешехода</p>
      <div class="s3-pills">
        <div class="s3-pill">
          <span class="s3-pill-val">+8%</span>
          <span class="s3-pill-txt">рост автопарка ежегодно</span>
        </div>
        <div class="s3-pill s3-pill-warm">
          <span class="s3-pill-val-warm">+30%</span>
          <span class="s3-pill-txt">рост заторов к 2030</span>
        </div>
      </div>
    </div>
    <div class="s3-right">
      <span class="s3-right-label">Инфраструктурный разрыв</span>
      <h1 class="s3-right-heading">Каждый год без оптимизации — ещё 4 млн тонн CO₂</h1>
      <div class="s3-items">
        <div class="s3-item">
          <div class="s3-item-icon">
            <Icon name="road" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s3-item-txt">Дороги расширяются на 2% в год — автопарк на 8%</span>
        </div>
        <div class="s3-item">
          <div class="s3-item-icon">
            <Icon name="alert-triangle" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s3-item-txt">Инфраструктура не успевает за ростом спроса</span>
        </div>
        <div class="s3-item s3-item-warm">
          <div class="s3-item-icon-warm">
            <Icon name="zap" :size="18" color="#D97706" />
          </div>
          <span class="s3-item-txt-warm">Точка невозврата: без действий к 2030 коллапс</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 560px; height: 560px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s3-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 380px; height: 380px; border: 1.5px solid rgba(13,148,136,0.15); border-radius: 50%; pointer-events: none; }
.s3-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 240px; height: 240px; border: 1px solid rgba(13,148,136,0.09); border-radius: 50%; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 1fr 1fr; padding: 44px 64px; gap: 48px; align-items: center; }
.s3-left { display: flex; flex-direction: column; align-items: flex-start; justify-content: center; }
.s3-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 16px; }
.s3-hero { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s3-caption { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin: 10px 0 24px; line-height: 1.45; }
.s3-pills { display: flex; flex-direction: column; gap: 10px; width: 100%; }
.s3-pill { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 12px 18px; display: flex; flex-direction: column; gap: 2px; }
.s3-pill-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s3-pill-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-pill-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s3-pill-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s3-right { display: flex; flex-direction: column; justify-content: center; }
.s3-right-label { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; margin-bottom: 10px; }
.s3-right-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s3-items { display: flex; flex-direction: column; gap: 10px; }
.s3-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 12px; }
.s3-item-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s3-item-icon { width: 36px; height: 36px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-item-icon-warm { width: 36px; height: 36px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-item-txt { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-text); line-height: 1.4; }
.s3-item-txt-warm { font-family: var(--font-body); font-size: 0.85rem; color: #D97706; font-weight: 600; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Icon Trio 2×2+1 — bg-base — 5 технологий умного транспорта -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <span class="s4-label">Технологический стек</span>
    <h1 class="s4-heading">Пять технологий, которые уже перестраивают городской транспорт</h1>
    <div class="s4-grid">
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="car" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Автономный транспорт</span>
        <span class="s4-desc">Level 4–5 беспилотники на городских маршрутах</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="layers" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">MaaS-платформы</span>
        <span class="s4-desc">Mobility as a Service — всё в одном приложении</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="cpu" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">AI-управление</span>
        <span class="s4-desc">Динамическое управление трафиком в реальном времени</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="battery-charging" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Электрификация</span>
        <span class="s4-desc">Электробусы и зарядная инфраструктура нового поколения</span>
      </div>
      <div class="s4-item s4-item-warm">
        <div class="s4-icon-warm">
          <Icon name="plane" :size="26" color="#D97706" />
        </div>
        <span class="s4-title">eVTOL</span>
        <span class="s4-desc">Воздушное городское такси — коммерческий запуск с 2026</span>
      </div>
    </div>
  </div>
</div>

<style>
.s4-root { position: absolute; inset: 0; overflow: hidden; }
.s4-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s4-glow { position: absolute; bottom: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s4-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 64px; }
.s4-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s4-heading { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s4-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 12px; align-items: stretch; }
.s4-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 20px 22px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }
.s4-item-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s4-icon { width: 48px; height: 48px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s4-icon-warm { width: 48px; height: 48px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s4-title { font-family: var(--font-heading); font-size: 1.05rem; font-weight: 700; color: var(--color-text); }
.s4-desc { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Bento Grid — bg-alt — Автономные шаттлы: 23 города мира -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-deco-dot"></div>
  </div>
  <div class="s5-content">
    <span class="s5-label">Автономный транспорт</span>
    <h1 class="s5-heading">23 города мира уже запустили маршруты автономных шаттлов</h1>
    <div class="s5-grid">
      <div class="s5-featured">
        <div class="s5-feat-icon">
          <Icon name="car" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s5-feat-num">100 000</div>
        <div class="s5-feat-label">поездок в неделю — Waymo в Сан-Франциско</div>
        <div class="s5-feat-source">Waymo Safety Report, 2025</div>
      </div>
      <div class="s5-side-top">
        <div class="s5-side-icon">
          <Icon name="map-pin" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s5-side-val">23</span>
          <span class="s5-side-txt">города с коммерческими AV-маршрутами</span>
        </div>
      </div>
      <div class="s5-side-mid">
        <div class="s5-side-icon">
          <Icon name="trending-down" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s5-side-val">−90%</span>
          <span class="s5-side-txt">снижение аварийности на AV-маршрутах</span>
        </div>
      </div>
      <div class="s5-side-bot">
        <div class="s5-side-icon-warm">
          <Icon name="trending-up" :size="20" color="#D97706" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s5-side-val-warm">15%</span>
          <span class="s5-side-txt">городского трафика — автономный к 2030</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-deco-dot { position: absolute; top: 40px; right: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s5-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s5-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s5-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s5-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s5-feat-num { font-family: var(--font-heading); font-size: 4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-feat-label { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s5-feat-source { font-family: var(--font-body); font-size: 0.7rem; color: var(--color-muted); margin-top: 12px; opacity: 0.7; }
.s5-side-top, .s5-side-mid { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s5-side-bot { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s5-side-icon { width: 40px; height: 40px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-side-icon-warm { width: 40px; height: 40px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-side-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-side-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s5-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Asymmetric Split — bg-base — MaaS: одно приложение -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow-left"></div>
    <div class="s6-dot-grid"></div>
  </div>
  <div class="s6-content">
    <div class="s6-left">
      <div class="s6-visual">
        <div class="s6-big-icon">
          <Icon name="layers" :size="56" color="var(--color-accent)" />
        </div>
        <div class="s6-stat-block">
          <span class="s6-stat-val">35%</span>
          <span class="s6-stat-lbl">пользователей Whim<br/>продали личный авто</span>
        </div>
        <span class="s6-visual-label">Хельсинки · Whim · 2024</span>
      </div>
    </div>
    <div class="s6-right">
      <span class="s6-label">MaaS — Mobility as a Service</span>
      <h1 class="s6-heading">Одно приложение заменяет личный автомобиль</h1>
      <div class="s6-features">
        <div class="s6-feat">
          <div class="s6-feat-icon">
            <Icon name="train" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s6-feat-txt">Метро + автобус + каршеринг + велосипед + такси</span>
        </div>
        <div class="s6-feat">
          <div class="s6-feat-icon">
            <Icon name="map-pin" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s6-feat-txt">Москва (Тройка): первые шаги к мультимодальности</span>
        </div>
        <div class="s6-feat s6-feat-warm">
          <div class="s6-feat-icon-warm">
            <Icon name="ruble" :size="18" color="#D97706" />
          </div>
          <span class="s6-feat-txt-warm">Экономия пользователя до 40% расходов на транспорт</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-glow-left { position: absolute; left: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-dot-grid { position: absolute; bottom: 30px; left: 30px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s6-left { display: flex; justify-content: center; align-items: center; }
.s6-visual { display: flex; flex-direction: column; align-items: center; gap: 14px; }
.s6-big-icon { width: 130px; height: 130px; border-radius: 28px; background: var(--color-accent-bg); border: 2px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s6-stat-block { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 14px 22px; text-align: center; }
.s6-stat-val { display: block; font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s6-stat-lbl { display: block; font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); line-height: 1.4; margin-top: 4px; }
.s6-visual-label { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
.s6-right { display: flex; flex-direction: column; justify-content: center; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 22px; line-height: 1.25; }
.s6-features { display: flex; flex-direction: column; gap: 10px; }
.s6-feat { display: flex; align-items: center; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 13px 18px; }
.s6-feat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s6-feat-icon { width: 36px; height: 36px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s6-feat-icon-warm { width: 36px; height: 36px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s6-feat-txt { font-family: var(--font-body); font-size: 0.86rem; color: var(--color-text); line-height: 1.4; }
.s6-feat-txt-warm { font-family: var(--font-body); font-size: 0.86rem; color: #D97706; font-weight: 600; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Two-col-text — bg-alt — AI-управление трафиком: −25% заторов -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow"></div>
    <div class="s7-dot"></div>
  </div>
  <div class="s7-content">
    <span class="s7-label">AI-управление трафиком</span>
    <h1 class="s7-heading">Адаптивный интеллект снижает заторы на 25%</h1>
    <div class="s7-cols">
      <div class="s7-col">
        <div class="s7-col-head">
          <div class="s7-col-icon">
            <Icon name="cpu" :size="20" color="var(--color-accent)" />
          </div>
          <span class="s7-col-title">Как работает</span>
        </div>
        <div class="s7-items">
          <div class="s7-item">
            <div class="s7-item-dot"></div>
            <span class="s7-item-txt">Адаптивные светофоры — оптимизация циклов в реальном времени</span>
          </div>
          <div class="s7-item">
            <div class="s7-item-dot"></div>
            <span class="s7-item-txt">Предиктивная аналитика — прогноз заторов за 30 минут</span>
          </div>
          <div class="s7-item">
            <div class="s7-item-dot"></div>
            <span class="s7-item-txt">Динамическая маршрутизация общественного транспорта</span>
          </div>
        </div>
      </div>
      <div class="s7-col">
        <div class="s7-col-head">
          <div class="s7-col-icon">
            <Icon name="bar-chart" :size="20" color="var(--color-accent)" />
          </div>
          <span class="s7-col-title">Реальные результаты</span>
        </div>
        <div class="s7-results">
          <div class="s7-result">
            <span class="s7-result-val">−21%</span>
            <span class="s7-result-txt">Барселона: время в пути после внедрения AI-системы</span>
          </div>
          <div class="s7-result">
            <span class="s7-result-val">170 000</span>
            <span class="s7-result-txt">камер обрабатывает ИТС Москвы в реальном времени</span>
          </div>
          <div class="s7-result s7-result-warm">
            <span class="s7-result-val-warm">−25%</span>
            <span class="s7-result-txt">среднее снижение заторов в городах с AI-трафик-системой</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-glow { position: absolute; top: -80px; right: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-dot { position: absolute; bottom: 30px; left: 30px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s7-cols { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-content: start; }
.s7-col { display: flex; flex-direction: column; gap: 14px; }
.s7-col-head { display: flex; align-items: center; gap: 12px; margin-bottom: 2px; }
.s7-col-icon { width: 40px; height: 40px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-col-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); }
.s7-items { display: flex; flex-direction: column; gap: 10px; }
.s7-item { display: flex; align-items: flex-start; gap: 10px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; padding: 12px 16px; }
.s7-item-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--color-accent); flex-shrink: 0; margin-top: 5px; }
.s7-item-txt { font-family: var(--font-body); font-size: 0.84rem; color: var(--color-text); line-height: 1.45; }
.s7-results { display: flex; flex-direction: column; gap: 10px; }
.s7-result { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; padding: 12px 16px; display: flex; flex-direction: column; gap: 3px; }
.s7-result-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s7-result-val { font-family: var(--font-heading); font-size: 1.7rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-result-val-warm { font-family: var(--font-heading); font-size: 1.7rem; font-weight: 800; color: #D97706; line-height: 1; }
.s7-result-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Section Divider (breathing) — bg-alt — Электрификация транспорта -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow"></div>
    <div class="s8-arc-outer"></div>
    <div class="s8-arc-inner"></div>
  </div>
  <div class="s8-content">
    <span class="s8-sup">Умный город · Раздел 2</span>
    <h1 class="s8-heading">Электрификация транспорта</h1>
    <p class="s8-sub">Электрический транспорт как основа устойчивой городской мобильности</p>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s8-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 580px; height: 580px; background: radial-gradient(circle, rgba(13,148,136,0.16) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 400px; height: 400px; border: 1.5px solid rgba(13,148,136,0.18); border-radius: 50%; pointer-events: none; }
.s8-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 260px; height: 260px; border: 1px solid rgba(13,148,136,0.10); border-radius: 50%; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; }
.s8-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; margin-bottom: 18px; }
.s8-heading { font-family: var(--font-heading); font-size: 4rem; font-weight: 800; color: var(--color-text); margin: 0 0 20px; line-height: 1.05; letter-spacing: -0.02em; }
.s8-sub { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); max-width: 600px; line-height: 1.6; margin: 0; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — Bento Grid — bg-base — 40% электробусов к 2028 -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-glow"></div>
  </div>
  <div class="s9-content">
    <span class="s9-label">Электрификация автобусного парка</span>
    <h1 class="s9-heading">40% автобусного парка Москвы станет электрическим к 2028</h1>
    <div class="s9-grid">
      <div class="s9-featured">
        <div class="s9-feat-icon">
          <Icon name="bus" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s9-feat-num">1 200</div>
        <div class="s9-feat-label">электробусов сегодня — крупнейший парк в Европе</div>
        <div class="s9-feat-sub">
          <div class="s9-sub-row">
            <span class="s9-sub-val">3 800</span>
            <span class="s9-sub-lbl">план к 2028</span>
          </div>
        </div>
      </div>
      <div class="s9-side-top">
        <div class="s9-side-icon">
          <Icon name="ruble" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s9-side-val">18 млрд ₽</span>
          <span class="s9-side-txt">экономия на топливе за 5 лет</span>
        </div>
      </div>
      <div class="s9-side-mid">
        <div class="s9-side-icon">
          <Icon name="wind" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s9-side-val">−40%</span>
          <span class="s9-side-txt">снижение шума в жилых районах</span>
        </div>
      </div>
      <div class="s9-side-bot">
        <div class="s9-side-icon-warm">
          <Icon name="leaf" :size="20" color="#D97706" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s9-side-val-warm">−60%</span>
          <span class="s9-side-txt">выбросов CO₂ на маршруте vs дизель</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s9-glow { position: absolute; top: -80px; left: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s9-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s9-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s9-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s9-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s9-feat-icon { width: 52px; height: 52px; border-radius: 12px; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s9-feat-num { font-family: var(--font-heading); font-size: 4.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-feat-label { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s9-feat-sub { margin-top: 18px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; padding: 12px 16px; }
.s9-sub-row { display: flex; align-items: baseline; gap: 8px; }
.s9-sub-val { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-sub-lbl { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); }
.s9-side-top, .s9-side-mid { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s9-side-bot { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s9-side-icon { width: 40px; height: 40px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-side-icon-warm { width: 40px; height: 40px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-side-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-side-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s9-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 10 — Data Spotlight — bg-alt — Зарядная инфраструктура: 25 000 станций -->
<!-- ============================================================ -->

<div class="s10-root">
  <div class="s10-bg">
    <div class="s10-glow"></div>
    <div class="s10-dot"></div>
  </div>
  <div class="s10-content">
    <span class="s10-label">Зарядная инфраструктура РФ</span>
    <h1 class="s10-heading">25 000 станций нужно построить за 3 года — дефицит огромен</h1>
    <div class="s10-grid">
      <div class="s10-card">
        <div class="s10-card-icon">
          <Icon name="battery-charging" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s10-card-val">8 500</div>
        <div class="s10-card-lbl">текущее покрытие станций по всей России</div>
      </div>
      <div class="s10-card s10-card-warm">
        <div class="s10-card-icon-warm">
          <Icon name="alert-triangle" :size="22" color="#D97706" />
        </div>
        <div class="s10-card-val-warm">−16 500</div>
        <div class="s10-card-lbl">дефицит быстрых зарядок до цели 2028</div>
      </div>
      <div class="s10-card">
        <div class="s10-card-icon">
          <Icon name="ruble" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s10-card-val">75 млрд ₽</div>
        <div class="s10-card-lbl">совокупных инвестиций (45 млрд частных + 30 млрд гос.)</div>
      </div>
    </div>
    <div class="s10-standard">
      <div class="s10-std-icon">
        <Icon name="check-circle" :size="16" color="var(--color-accent)" />
      </div>
      <span class="s10-std-txt">Стандартизация: переход на единый CCS2 — совместимость с мировыми производителями</span>
    </div>
  </div>
</div>

<style>
.s10-root { position: absolute; inset: 0; overflow: hidden; }
.s10-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s10-glow { position: absolute; top: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s10-dot { position: absolute; bottom: 30px; left: 30px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s10-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s10-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s10-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; }
.s10-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-items: stretch; }
.s10-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 24px 28px; display: flex; flex-direction: column; justify-content: center; gap: 8px; }
.s10-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s10-card-icon { width: 48px; height: 48px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s10-card-icon-warm { width: 48px; height: 48px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; }
.s10-card-val { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s10-card-val-warm { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: #D97706; line-height: 1; }
.s10-card-lbl { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s10-standard { display: flex; align-items: center; gap: 10px; margin-top: 14px; padding: 12px 18px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; }
.s10-std-icon { flex-shrink: 0; }
.s10-std-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-accent); font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 11 — Card Mosaic — bg-base — eVTOL: воздушное такси к 2028 -->
<!-- ============================================================ -->

<div class="s11-root">
  <div class="s11-bg">
    <div class="s11-glow"></div>
  </div>
  <div class="s11-content">
    <span class="s11-label">eVTOL — воздушное городское такси</span>
    <h1 class="s11-heading">Воздушное такси станет реальностью к 2028</h1>
    <div class="s11-grid">
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="plane" :size="22" color="var(--color-accent)" />
        </div>
        <span class="s11-card-title">Joby Aviation</span>
        <span class="s11-card-val">2025</span>
        <span class="s11-card-desc">ожидаемый год сертификации FAA для коммерческих рейсов</span>
      </div>
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="map-pin" :size="22" color="var(--color-accent)" />
        </div>
        <span class="s11-card-title">Volocopter</span>
        <span class="s11-card-val">2026</span>
        <span class="s11-card-desc">коммерческие рейсы в Сингапуре с 2026 года</span>
      </div>
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="navigation" :size="22" color="var(--color-accent)" />
        </div>
        <span class="s11-card-title">Дальность и скорость</span>
        <span class="s11-card-val">250 км/ч</span>
        <span class="s11-card-desc">максимальная скорость, дальность 150–300 км на заряд</span>
      </div>
      <div class="s11-card s11-card-warm">
        <div class="s11-card-icon-warm">
          <Icon name="ruble" :size="22" color="#D97706" />
        </div>
        <span class="s11-card-title">Цена поездки</span>
        <span class="s11-card-val-warm">≈ Бизнес-такси</span>
        <span class="s11-card-desc">стоимость станет сопоставима с премиум-такси к 2030</span>
      </div>
    </div>
  </div>
</div>

<style>
.s11-root { position: absolute; inset: 0; overflow: hidden; }
.s11-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s11-glow { position: absolute; bottom: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s11-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s11-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s11-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s11-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px; align-items: stretch; }
.s11-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 22px 26px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }
.s11-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s11-card-icon { width: 48px; height: 48px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s11-card-icon-warm { width: 48px; height: 48px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s11-card-title { font-family: var(--font-heading); font-size: 0.85rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.08em; }
.s11-card-val { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s11-card-val-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s11-card-desc { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 12 — Comparison Table — bg-alt — Три сценария 2035 -->
<!-- ============================================================ -->

<div class="s12-root">
  <div class="s12-bg">
    <div class="s12-glow"></div>
    <div class="s12-dot"></div>
  </div>
  <div class="s12-content">
    <span class="s12-label">Сценарный анализ</span>
    <h1 class="s12-heading">Три сценария развития российских городов к 2035</h1>
    <div class="s12-table">
      <div class="s12-row-head">
        <span class="s12-th">Сценарий</span>
        <span class="s12-th">Электрификация</span>
        <span class="s12-th">Трафик</span>
        <span class="s12-th">Прогноз</span>
      </div>
      <div class="s12-row s12-row-pessimistic">
        <div class="s12-cell-name">
          <div class="s12-badge s12-badge-red">Пессимистичный</div>
        </div>
        <div class="s12-cell">
          <span class="s12-val-neg">5%</span>
          <span class="s12-lbl">электрификация</span>
        </div>
        <div class="s12-cell">
          <span class="s12-val-neg">+30%</span>
          <span class="s12-lbl">рост заторов</span>
        </div>
        <div class="s12-cell-desc">
          <span class="s12-desc">Инерционное развитие, коллапс инфраструктуры к 2035</span>
        </div>
      </div>
      <div class="s12-row s12-row-base">
        <div class="s12-cell-name">
          <div class="s12-badge s12-badge-teal">Базовый</div>
        </div>
        <div class="s12-cell">
          <span class="s12-val">30%</span>
          <span class="s12-lbl">электрификация</span>
        </div>
        <div class="s12-cell">
          <span class="s12-val">стаб.</span>
          <span class="s12-lbl">стабилизация трафика</span>
        </div>
        <div class="s12-cell-desc">
          <span class="s12-desc">Поэтапное внедрение технологий, умеренный прогресс</span>
        </div>
      </div>
      <div class="s12-row s12-row-optimistic">
        <div class="s12-cell-name">
          <div class="s12-badge s12-badge-warm">Оптимистичный</div>
        </div>
        <div class="s12-cell">
          <span class="s12-val-warm">60%</span>
          <span class="s12-lbl">электрификация</span>
        </div>
        <div class="s12-cell">
          <span class="s12-val-warm">−40%</span>
          <span class="s12-lbl">снижение заторов</span>
        </div>
        <div class="s12-cell-desc">
          <span class="s12-desc-warm">Полная интеграция MaaS + AI + электрификации — умный город</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s12-root { position: absolute; inset: 0; overflow: hidden; }
.s12-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s12-glow { position: absolute; top: -80px; left: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s12-dot { position: absolute; bottom: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s12-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s12-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s12-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s12-table { flex: 1; display: flex; flex-direction: column; gap: 10px; justify-content: center; }
.s12-row-head { display: grid; grid-template-columns: 1.4fr 1fr 1fr 2fr; gap: 12px; padding: 0 18px; }
.s12-th { font-family: var(--font-heading); font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-muted); }
.s12-row { display: grid; grid-template-columns: 1.4fr 1fr 1fr 2fr; gap: 12px; border-radius: 12px; padding: 16px 18px; align-items: center; }
.s12-row-pessimistic { background: rgba(239,68,68,0.06); border: 1px solid rgba(239,68,68,0.2); }
.s12-row-base { background: var(--color-surface); border: 1.5px solid var(--color-accent-dim); }
.s12-row-optimistic { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.30); }
.s12-cell-name { display: flex; align-items: center; }
.s12-badge { display: inline-flex; align-items: center; border-radius: 8px; padding: 4px 12px; font-family: var(--font-heading); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }
.s12-badge-red { background: rgba(239,68,68,0.10); color: #DC2626; border: 1px solid rgba(239,68,68,0.25); }
.s12-badge-teal { background: var(--color-accent-bg); color: var(--color-accent); border: 1px solid var(--color-accent-dim); }
.s12-badge-warm { background: rgba(217,119,6,0.10); color: #D97706; border: 1px solid rgba(217,119,6,0.30); }
.s12-cell { display: flex; flex-direction: column; gap: 2px; }
.s12-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s12-val-neg { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #DC2626; line-height: 1; }
.s12-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s12-lbl { font-family: var(--font-body); font-size: 0.72rem; color: var(--color-muted); }
.s12-cell-desc { display: flex; align-items: center; }
.s12-desc { font-family: var(--font-body); font-size: 0.84rem; color: var(--color-text); line-height: 1.4; }
.s12-desc-warm { font-family: var(--font-body); font-size: 0.84rem; color: #D97706; font-weight: 600; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 13 — Timeline Horizontal — bg-base — Дорожная карта 2026-2030 -->
<!-- ============================================================ -->

<div class="s13-root">
  <div class="s13-bg">
    <div class="s13-glow"></div>
  </div>
  <div class="s13-content">
    <span class="s13-label">Дорожная карта умного транспорта</span>
    <h1 class="s13-heading">Пять лет до интегрированной мобильности: 2026–2030</h1>
    <div class="s13-grid">
      <div class="s13-step">
        <span class="s13-year">2026</span>
        <span class="s13-title">AI-светофоры</span>
        <span class="s13-body">AI-управление трафиком во всех городах-миллионниках России</span>
      </div>
      <div class="s13-step s13-step-accent">
        <span class="s13-year">2027</span>
        <span class="s13-title">MaaS-платформа</span>
        <span class="s13-body">Единый тариф и приложение для 5 крупнейших городов</span>
      </div>
      <div class="s13-step">
        <span class="s13-year">2028</span>
        <span class="s13-title">40% электробусов</span>
        <span class="s13-body">Электрификация парка + первые маршруты автономных шаттлов</span>
      </div>
      <div class="s13-step">
        <span class="s13-year">2029</span>
        <span class="s13-title">eVTOL-пилот</span>
        <span class="s13-body">Первые пилотные рейсы воздушного такси в Москве</span>
      </div>
      <div class="s13-step s13-step-warm">
        <span class="s13-year">2030</span>
        <span class="s13-title">Умная мобильность</span>
        <span class="s13-body">Интегрированная мультимодальная система — полная готовность</span>
      </div>
    </div>
    <div class="s13-footer">
      <div class="s13-milestone">
        <Icon name="check-circle" :size="15" color="var(--color-accent)" />
        <span class="s13-mile-txt">Все инициативы согласованы с нацпроектом «Цифровая экономика»</span>
      </div>
      <div class="s13-milestone">
        <Icon name="check-circle" :size="15" color="#D97706" />
        <span class="s13-mile-txt-warm">Окупаемость инвестиций в smart-транспорт: 5–7 лет</span>
      </div>
    </div>
  </div>
</div>

<style>
.s13-root { position: absolute; inset: 0; overflow: hidden; }
.s13-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s13-glow { position: absolute; top: -100px; right: -100px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s13-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s13-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s13-heading { font-family: var(--font-heading); font-size: 1.95rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s13-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr 1fr 1fr; gap: 12px; align-items: stretch; }
.s13-step { border-radius: 14px; padding: 20px 18px; display: flex; flex-direction: column; gap: 8px; background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s13-step-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s13-step-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s13-year { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); }
.s13-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); }
.s13-body { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.45; }
.s13-footer { display: flex; align-items: center; gap: 28px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s13-milestone { display: flex; align-items: center; gap: 8px; }
.s13-mile-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s13-mile-txt-warm { font-family: var(--font-body); font-size: 0.78rem; color: #D97706; font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 14 — Stat Hero (centered / breathing) — bg-alt — ROI умного транспорта -->
<!-- ============================================================ -->

<div class="s14-root">
  <div class="s14-bg">
    <div class="s14-glow"></div>
    <div class="s14-arc"></div>
  </div>
  <div class="s14-content">
    <span class="s14-label">Выгоды умного транспорта</span>
    <div class="s14-hero">5–7 лет</div>
    <p class="s14-caption">срок окупаемости инвестиций в smart-транспорт</p>
    <div class="s14-pills">
      <div class="s14-pill">
        <span class="s14-pill-num">+23%</span>
        <span class="s14-pill-txt">рост качества жизни в рейтинге Mercer</span>
      </div>
      <div class="s14-pill s14-pill-warm">
        <span class="s14-pill-num-warm">+18%</span>
        <span class="s14-pill-txt">рост инвестиционной привлекательности городов</span>
      </div>
      <div class="s14-pill">
        <span class="s14-pill-num">−40%</span>
        <span class="s14-pill-txt">заторов при полной реализации сценария</span>
      </div>
    </div>
  </div>
</div>

<style>
.s14-root { position: absolute; inset: 0; overflow: hidden; }
.s14-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s14-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 560px; height: 560px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s14-arc { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 380px; height: 380px; border: 1.5px solid rgba(13,148,136,0.14); border-radius: 50%; pointer-events: none; }
.s14-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 48px 80px; }
.s14-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s14-hero { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s14-caption { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); margin: 10px 0 32px; }
.s14-pills { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
.s14-pill { display: flex; flex-direction: column; align-items: center; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 28px; min-width: 160px; }
.s14-pill-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s14-pill-num { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s14-pill-num-warm { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s14-pill-txt { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); margin-top: 4px; text-align: center; max-width: 150px; line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 15 — CTA Warm — bg-accent — Smart Mobility Alliance -->
<!-- ============================================================ -->

<div class="s15-root">
  <div class="s15-bg"></div>
  <div class="s15-glow-tl"></div>
  <div class="s15-glow-br"></div>
  <div class="s15-dots"></div>
  <div class="s15-content">
    <span class="s15-sup">Smart City Conference 2026</span>
    <h1 class="s15-heading">Присоединяйтесь к Smart Mobility Alliance — формируем стандарты вместе</h1>
    <div class="s15-steps">
      <div class="s15-step">
        <div class="s15-step-num">01</div>
        <span class="s15-step-txt">Отсканируйте QR-код — мгновенное вступление в альянс</span>
      </div>
      <div class="s15-step">
        <div class="s15-step-num">02</div>
        <span class="s15-step-txt">Ежеквартальные отчёты и бенчмарки по рынку умного транспорта</span>
      </div>
      <div class="s15-step">
        <div class="s15-step-num">03</div>
        <span class="s15-step-txt">Совместные пилоты, стандарты и лоббирование транспортных инициатив</span>
      </div>
    </div>
    <div class="s15-contacts">
      <div class="s15-contact">
        <Icon name="mail" :size="16" color="rgba(255,255,255,0.9)" />
        <span class="s15-contact-txt">alliance@smartcity2026.ru</span>
      </div>
      <span class="s15-contact-dot">·</span>
      <div class="s15-contact">
        <Icon name="globe" :size="16" color="rgba(255,255,255,0.9)" />
        <span class="s15-contact-txt">smartcity2026.ru</span>
      </div>
      <span class="s15-contact-dot">·</span>
      <div class="s15-contact">
        <Icon name="qr-code" :size="16" color="rgba(255,255,255,0.9)" />
        <span class="s15-contact-txt">QR-код для вступления</span>
      </div>
    </div>
  </div>
</div>

<style>
.s15-root { position: absolute; inset: 0; overflow: hidden; }
.s15-bg { position: absolute; inset: 0; z-index: 0; background: linear-gradient(145deg, var(--bg-accent) 0%, #0a7870 100%); }
.s15-glow-tl { position: absolute; top: -120px; left: -120px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; z-index: 0; pointer-events: none; }
.s15-glow-br { position: absolute; bottom: -100px; right: -100px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 65%); border-radius: 50%; z-index: 0; pointer-events: none; }
.s15-dots { position: absolute; top: 40px; right: 60px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; z-index: 0; pointer-events: none; }
.s15-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s15-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.75); font-weight: 600; margin-bottom: 16px; }
.s15-heading { font-family: var(--font-heading); font-size: 2.3rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.2; max-width: 820px; }
.s15-steps { display: flex; flex-direction: column; gap: 12px; max-width: 680px; width: 100%; margin-bottom: 36px; }
.s15-step { display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.25); border-radius: 12px; padding: 14px 20px; text-align: left; }
.s15-step-num { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 800; color: rgba(255,255,255,0.5); min-width: 28px; line-height: 1; }
.s15-step-txt { font-family: var(--font-body); font-size: 0.88rem; color: rgba(255,255,255,0.9); line-height: 1.4; }
.s15-contacts { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; justify-content: center; }
.s15-contact { display: flex; align-items: center; gap: 8px; }
.s15-contact-txt { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 600; color: #FFFFFF; }
.s15-contact-dot { color: rgba(255,255,255,0.4); font-size: 1.2rem; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
