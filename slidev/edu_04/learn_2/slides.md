---
theme: default
layout: none
title: Микросервисы в бою — 5 уроков из продакшена на 10 000 RPS
fonts:
  sans: Sora
  serif: IBM Plex Sans
  mono: JetBrains Mono
colorSchema: light
aspectRatio: 16/9
transition: fade
---

<!-- ============================================================ -->
<!-- SLIDE 1 — Cover Hero — bg-accent — Заголовок доклада -->
<!-- ============================================================ -->

<div class="s1-root">
  <div class="s1-bg">
    <div class="s1-glow-tr"></div>
    <div class="s1-glow-bl"></div>
    <div class="s1-dots"></div>
  </div>
  <div class="s1-content">
    <div class="s1-label-wrap">
      <span class="s1-label">DevOps Days · 2026</span>
    </div>
    <h1 class="s1-heading">Микросервисы в бою</h1>
    <p class="s1-sub">Что мы узнали за 3 года на пути к 10 000 RPS</p>
    <div class="s1-meta">
      <span>Архитектура микросервисов</span>
      <span class="s1-dot">·</span>
      <span>5 уроков из продакшена</span>
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
.s1-sub { font-family: var(--font-body); font-size: 1.4rem; color: rgba(255,255,255,0.85); margin: 0 0 36px; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.9rem; color: rgba(255,255,255,0.65); }
.s1-dot { color: rgba(255,255,255,0.35); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 2 — Quote Pull / Stat Hero — bg-base — Первые 6 месяцев -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow"></div>
    <div class="s2-arc-outer"></div>
    <div class="s2-arc-inner"></div>
  </div>
  <div class="s2-content">
    <span class="s2-label">Наш первый год с микросервисами</span>
    <h1 class="s2-hero">Первые 6 месяцев<br>были адом</h1>
    <p class="s2-caption">Мы перешли с монолита на 47 микросервисов — и немедленно поплатились</p>
    <div class="s2-pills">
      <span class="s2-pill">
        <span class="s2-pill-num">800ms</span>
        <span class="s2-pill-txt">latency вместо 50ms</span>
      </span>
      <span class="s2-pill s2-pill-warm">
        <span class="s2-pill-num-warm">3</span>
        <span class="s2-pill-txt">major outage за первый квартал</span>
      </span>
      <span class="s2-pill">
        <span class="s2-pill-num">12</span>
        <span class="s2-pill-txt">инженеров чуть не уволились</span>
      </span>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 560px; height: 560px; background: radial-gradient(circle, rgba(13,148,136,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 400px; height: 400px; border: 1.5px solid rgba(13,148,136,0.12); border-radius: 50%; pointer-events: none; }
.s2-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 260px; height: 260px; border: 1px solid rgba(13,148,136,0.07); border-radius: 50%; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 48px 80px; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s2-hero { font-family: var(--font-heading); font-size: 4rem; font-weight: 800; color: var(--color-text); line-height: 1.1; margin: 0 0 16px; letter-spacing: -0.02em; }
.s2-caption { font-family: var(--font-body); font-size: 1.1rem; color: var(--color-muted); margin: 0 0 32px; max-width: 620px; line-height: 1.5; }
.s2-pills { display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; }
.s2-pill { display: flex; flex-direction: column; align-items: center; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 28px; min-width: 160px; }
.s2-pill-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-pill-num { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-pill-num-warm { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-pill-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); margin-top: 5px; text-align: center; max-width: 140px; line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Section Divider — bg-alt — 5 уроков -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-glow"></div>
    <div class="s3-arc-outer"></div>
    <div class="s3-arc-inner"></div>
  </div>
  <div class="s3-content">
    <span class="s3-sup">Архитектура микросервисов · DevOps Days 2026</span>
    <h1 class="s3-heading">5 уроков, которые мы<br>выучили на своих ошибках</h1>
    <p class="s3-sub">Каждый стоил нам от 2 до 15 млн ₽ — теперь они бесплатны для вас</p>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(13,148,136,0.16) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s3-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 440px; height: 440px; border: 1.5px solid rgba(13,148,136,0.18); border-radius: 50%; pointer-events: none; }
.s3-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 280px; height: 280px; border: 1px solid rgba(13,148,136,0.10); border-radius: 50%; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; }
.s3-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; margin-bottom: 18px; }
.s3-heading { font-family: var(--font-heading); font-size: 3.8rem; font-weight: 800; color: var(--color-text); margin: 0 0 20px; line-height: 1.08; letter-spacing: -0.02em; }
.s3-sub { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); max-width: 620px; line-height: 1.6; margin: 0; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Asymmetric Split — bg-base — Урок 1: Event Storming -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow-left"></div>
    <div class="s4-dot-grid"></div>
  </div>
  <div class="s4-content">
    <div class="s4-left">
      <div class="s4-visual">
        <div class="s4-badge">01</div>
        <div class="s4-big-icon">
          <Icon name="map" :size="52" color="var(--color-accent)" />
        </div>
        <span class="s4-visual-label">Event Storming</span>
      </div>
    </div>
    <div class="s4-right">
      <span class="s4-label">Урок 1</span>
      <h1 class="s4-heading">Начните с event storming, а не с диаграммы сервисов</h1>
      <div class="s4-items">
        <div class="s4-item">
          <div class="s4-item-icon">
            <Icon name="check-circle" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s4-item-txt">Domain boundaries определяют границы сервисов</span>
        </div>
        <div class="s4-item s4-item-err">
          <div class="s4-item-icon-warn">
            <Icon name="alert-triangle" :size="18" color="#D97706" />
          </div>
          <span class="s4-item-txt-warn">Ошибка: делили по техническим слоям (auth, payments, users)</span>
        </div>
        <div class="s4-item">
          <div class="s4-item-icon">
            <Icon name="check-circle" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s4-item-txt">Правильно: делить по бизнес-доменам (заказы, каталог, доставка)</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s4-root { position: absolute; inset: 0; overflow: hidden; }
.s4-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s4-glow-left { position: absolute; left: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s4-dot-grid { position: absolute; bottom: 30px; left: 30px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s4-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s4-left { display: flex; justify-content: center; align-items: center; }
.s4-visual { display: flex; flex-direction: column; align-items: center; gap: 12px; }
.s4-badge { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 5px 16px; }
.s4-big-icon { width: 130px; height: 130px; border-radius: 24px; background: var(--color-accent-bg); border: 2px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s4-visual-label { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
.s4-right { display: flex; flex-direction: column; justify-content: center; }
.s4-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s4-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s4-items { display: flex; flex-direction: column; gap: 10px; }
.s4-item { display: flex; align-items: flex-start; gap: 12px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 13px 16px; }
.s4-item-err { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s4-item-icon { width: 34px; height: 34px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s4-item-icon-warn { width: 34px; height: 34px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s4-item-txt { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-text); line-height: 1.4; }
.s4-item-txt-warn { font-family: var(--font-body); font-size: 0.88rem; color: #D97706; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Stat Hero (split-50-50) — bg-alt — Урок 2: Kafka latency -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow"></div>
    <div class="s5-dot"></div>
  </div>
  <div class="s5-content">
    <span class="s5-label">Урок 2 · Асинхронность везде</span>
    <h1 class="s5-heading">Kafka снизила latency в 4 раза — с 800ms до 120ms</h1>
    <div class="s5-compare">
      <div class="s5-before">
        <span class="s5-compare-tag s5-tag-err">До</span>
        <div class="s5-num-big s5-num-err">800<span class="s5-unit">ms</span></div>
        <span class="s5-compare-desc">синхронные REST-цепочки из 5+ сервисов</span>
        <div class="s5-sub-item">
          <Icon name="alert-triangle" :size="14" color="#D97706" />
          <span class="s5-sub-txt">single point of failure</span>
        </div>
      </div>
      <div class="s5-divider"></div>
      <div class="s5-after">
        <span class="s5-compare-tag s5-tag-ok">После</span>
        <div class="s5-num-big s5-num-ok">120<span class="s5-unit">ms</span></div>
        <span class="s5-compare-desc">Kafka + event sourcing + Saga-паттерн</span>
        <div class="s5-sub-item">
          <Icon name="check-circle" :size="14" color="var(--color-accent)" />
          <span class="s5-sub-txt">распределённые транзакции без блокировок</span>
        </div>
      </div>
    </div>
    <div class="s5-footer">
      <div class="s5-foot-pill s5-foot-warm">
        <span class="s5-foot-val">4×</span>
        <span class="s5-foot-txt">ускорение P99 latency</span>
      </div>
      <div class="s5-foot-pill">
        <span class="s5-foot-val">Saga</span>
        <span class="s5-foot-txt">паттерн для распределённых транзакций</span>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-glow { position: absolute; top: -80px; right: -80px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-dot { position: absolute; bottom: 30px; left: 30px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s5-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s5-compare { flex: 1; display: grid; grid-template-columns: 1fr 2px 1fr; gap: 28px; align-items: center; }
.s5-before, .s5-after { display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; }
.s5-divider { background: var(--color-surface-border); align-self: stretch; border-radius: 2px; }
.s5-compare-tag { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; padding: 4px 14px; border-radius: 20px; }
.s5-tag-err { background: rgba(217,119,6,0.10); color: #D97706; border: 1.5px solid rgba(217,119,6,0.35); }
.s5-tag-ok { background: var(--color-accent-bg); color: var(--color-accent); border: 1.5px solid var(--color-accent-dim); }
.s5-num-big { font-family: var(--font-heading); font-size: 5rem; font-weight: 800; line-height: 1; }
.s5-num-err { color: #D97706; }
.s5-num-ok { color: var(--color-accent); }
.s5-unit { font-size: 2rem; font-weight: 700; }
.s5-compare-desc { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); max-width: 280px; line-height: 1.4; }
.s5-sub-item { display: flex; align-items: center; gap: 6px; }
.s5-sub-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s5-footer { display: flex; gap: 14px; padding-top: 16px; border-top: 1px solid var(--color-surface-border); }
.s5-foot-pill { display: flex; align-items: center; gap: 10px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 10px 18px; }
.s5-foot-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s5-foot-val { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: #D97706; line-height: 1; }
.s5-foot-warm .s5-foot-val { color: #D97706; }
.s5-foot-pill:not(.s5-foot-warm) .s5-foot-val { color: var(--color-accent); }
.s5-foot-txt { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Icon Trio 3-col — bg-base — Урок 3: Observability 3 сигнала -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Урок 3 · Observability — не роскошь</span>
    <h1 class="s6-heading">Каждый сервис обязан экспортировать 3 сигнала</h1>
    <div class="s6-trio">
      <div class="s6-item">
        <div class="s6-icon">
          <Icon name="bar-chart" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s6-title">Metrics</span>
        <span class="s6-tool">Prometheus</span>
        <span class="s6-desc">Счётчики, гистограммы, gauges — каждые 15 секунд</span>
      </div>
      <div class="s6-item s6-item-mid">
        <div class="s6-icon s6-icon-rounded">
          <Icon name="activity" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s6-title">Logs</span>
        <span class="s6-tool">Loki</span>
        <span class="s6-desc">Структурированные логи с trace ID в каждой записи</span>
      </div>
      <div class="s6-item">
        <div class="s6-icon s6-icon-warm">
          <Icon name="network" :size="28" color="#D97706" />
        </div>
        <span class="s6-title">Traces</span>
        <span class="s6-tool s6-tool-warm">Jaeger</span>
        <span class="s6-desc">Distributed tracing — MTTR с 4 часов до 18 минут</span>
      </div>
    </div>
    <div class="s6-rule">
      <Icon name="shield" :size="16" color="var(--color-accent)" />
      <span class="s6-rule-txt">Правило: нет trace ID — сервис не идёт в продакшен</span>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-glow { position: absolute; bottom: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 22px; }
.s6-trio { flex: 1; display: flex; justify-content: center; align-items: center; gap: 20px; }
.s6-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 28px 24px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; flex: 1; }
.s6-item-mid { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s6-icon { width: 60px; height: 60px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 8px; }
.s6-icon-rounded { border-radius: 12px; }
.s6-icon-warm { width: 60px; height: 60px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 8px; }
.s6-title { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: var(--color-text); line-height: 1; }
.s6-tool { font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); }
.s6-tool-warm { color: #D97706; }
.s6-desc { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); line-height: 1.45; }
.s6-rule { display: flex; align-items: center; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s6-rule-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-accent); font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Bento Grid — bg-alt — Урок 4: Service Mesh сэкономил 200ч -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-deco-dot"></div>
  </div>
  <div class="s7-content">
    <span class="s7-label">Урок 4 · Service Mesh</span>
    <h1 class="s7-heading">Istio сэкономил 200 часов в год на retry и circuit breaker</h1>
    <div class="s7-grid">
      <div class="s7-featured">
        <div class="s7-feat-icon">
          <Icon name="layers" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s7-feat-num">200<span class="s7-feat-unit">ч/год</span></div>
        <div class="s7-feat-label">сэкономлено на инфраструктурном коде</div>
        <div class="s7-feat-note">Каждая команда писала свой retry-механизм — теперь единая политика</div>
      </div>
      <div class="s7-side-a">
        <div class="s7-side-icon">
          <Icon name="refresh-cw" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s7-side-val">Retry</span>
          <span class="s7-side-txt">автоматические повторы из коробки</span>
        </div>
      </div>
      <div class="s7-side-b">
        <div class="s7-side-icon">
          <Icon name="zap" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s7-side-val">Circuit Breaker</span>
          <span class="s7-side-txt">защита от каскадных отказов</span>
        </div>
      </div>
      <div class="s7-side-c">
        <div class="s7-side-icon-warm">
          <Icon name="lock" :size="20" color="#D97706" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s7-side-val-warm">mTLS</span>
          <span class="s7-side-txt">шифрование трафика между сервисами</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-deco-dot { position: absolute; top: 40px; right: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s7-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s7-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s7-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s7-feat-num { font-family: var(--font-heading); font-size: 4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-feat-unit { font-size: 1.6rem; font-weight: 700; margin-left: 4px; }
.s7-feat-label { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s7-feat-note { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); margin-top: 12px; opacity: 0.8; line-height: 1.45; }
.s7-side-a, .s7-side-b { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s7-side-c { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s7-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-side-val { font-family: var(--font-heading); font-size: 1.1rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-side-val-warm { font-family: var(--font-heading); font-size: 1.1rem; font-weight: 800; color: #D97706; line-height: 1; }
.s7-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Asymmetric Split — bg-base — Урок 5: 47→23 сервиса -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow-right"></div>
    <div class="s8-dot-grid"></div>
  </div>
  <div class="s8-content">
    <div class="s8-left">
      <div class="s8-visual">
        <div class="s8-badge">05</div>
        <div class="s8-counter-wrap">
          <div class="s8-num-before">47</div>
          <div class="s8-arrow">→</div>
          <div class="s8-num-after">23</div>
        </div>
        <span class="s8-visual-label">сервисов</span>
      </div>
    </div>
    <div class="s8-right">
      <span class="s8-label">Урок 5</span>
      <h1 class="s8-heading">Не каждый сервис должен быть «микро» — правило «2 пиццы» не про размер кода</h1>
      <div class="s8-items">
        <div class="s8-item s8-item-err">
          <div class="s8-item-icon-warn">
            <Icon name="alert-triangle" :size="18" color="#D97706" />
          </div>
          <span class="s8-item-txt-warn">Нано-сервисы (100 строк) создают больше проблем, чем решают</span>
        </div>
        <div class="s8-item">
          <div class="s8-item-icon">
            <Icon name="users" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s8-item-txt">Оптимум: 1 команда из 3–5 человек → 3–7 сервисов</span>
        </div>
        <div class="s8-item s8-item-accent">
          <div class="s8-item-icon">
            <Icon name="trending-up" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s8-item-txt">Объединили 47→23 сервиса — и стало <strong>лучше</strong></span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s8-glow-right { position: absolute; right: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-dot-grid { position: absolute; top: 40px; left: 40px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s8-left { display: flex; justify-content: center; align-items: center; }
.s8-visual { display: flex; flex-direction: column; align-items: center; gap: 12px; }
.s8-badge { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 5px 16px; }
.s8-counter-wrap { display: flex; align-items: center; gap: 10px; }
.s8-num-before { font-family: var(--font-heading); font-size: 3.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s8-arrow { font-family: var(--font-heading); font-size: 2rem; color: var(--color-muted); }
.s8-num-after { font-family: var(--font-heading); font-size: 3.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s8-visual-label { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
.s8-right { display: flex; flex-direction: column; justify-content: center; }
.s8-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s8-heading { font-family: var(--font-heading); font-size: 1.7rem; font-weight: 700; color: var(--color-text); margin: 0 0 22px; line-height: 1.28; }
.s8-items { display: flex; flex-direction: column; gap: 10px; }
.s8-item { display: flex; align-items: flex-start; gap: 12px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 13px 16px; }
.s8-item-err { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s8-item-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s8-item-icon { width: 34px; height: 34px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-item-icon-warn { width: 34px; height: 34px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-item-txt { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-text); line-height: 1.4; }
.s8-item-txt-warn { font-family: var(--font-body); font-size: 0.88rem; color: #D97706; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — Data Spotlight — bg-alt — Результаты: 99.95%, 95ms, 10K RPS -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-glow"></div>
    <div class="s9-dot"></div>
  </div>
  <div class="s9-content">
    <span class="s9-label">Результаты после 18 месяцев работы</span>
    <h1 class="s9-heading">99.95% uptime · P99 95ms · 10 000 RPS</h1>
    <div class="s9-compare-bar">
      <span class="s9-cmp-tag">До миграции</span>
      <span class="s9-cmp-sep">→</span>
      <span class="s9-cmp-tag s9-cmp-ok">После 18 месяцев</span>
    </div>
    <div class="s9-grid">
      <div class="s9-card">
        <div class="s9-card-icon">
          <Icon name="activity" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s9-card-row">
          <span class="s9-card-before">99.2%</span>
          <span class="s9-card-arrow">→</span>
          <span class="s9-card-after">99.95%</span>
        </div>
        <div class="s9-card-lbl">Uptime</div>
      </div>
      <div class="s9-card">
        <div class="s9-card-icon">
          <Icon name="clock" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s9-card-row">
          <span class="s9-card-before">800ms</span>
          <span class="s9-card-arrow">→</span>
          <span class="s9-card-after">95ms</span>
        </div>
        <div class="s9-card-lbl">P99 Latency</div>
      </div>
      <div class="s9-card s9-card-warm">
        <div class="s9-card-icon-warm">
          <Icon name="trending-up" :size="20" color="#D97706" />
        </div>
        <div class="s9-card-row">
          <span class="s9-card-before">2 000</span>
          <span class="s9-card-arrow">→</span>
          <span class="s9-card-after-warm">10 000</span>
        </div>
        <div class="s9-card-lbl">RPS</div>
      </div>
    </div>
    <div class="s9-invest">
      <Icon name="check-circle" :size="16" color="var(--color-accent)" />
      <span class="s9-invest-txt">Инвестиции: 45 млн ₽ в инструменты + 3 дополнительных DevOps-инженера · Путь занял 18 месяцев</span>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s9-glow { position: absolute; top: -80px; left: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-dot { position: absolute; bottom: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s9-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s9-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 14px; }
.s9-compare-bar { display: flex; align-items: center; gap: 10px; margin-bottom: 18px; }
.s9-cmp-tag { font-family: var(--font-heading); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-muted); background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 20px; padding: 4px 14px; }
.s9-cmp-ok { color: var(--color-accent); background: var(--color-accent-bg); border-color: var(--color-accent-dim); }
.s9-cmp-sep { font-family: var(--font-heading); font-size: 1rem; color: var(--color-muted); }
.s9-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-items: stretch; }
.s9-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 22px 24px; display: flex; flex-direction: column; align-items: flex-start; gap: 10px; }
.s9-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s9-card-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s9-card-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; }
.s9-card-row { display: flex; align-items: baseline; gap: 8px; }
.s9-card-before { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; color: var(--color-muted); line-height: 1; }
.s9-card-arrow { font-family: var(--font-heading); font-size: 1rem; color: var(--color-muted); }
.s9-card-after { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-card-after-warm { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s9-card-lbl { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s9-invest { display: flex; align-items: flex-start; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s9-invest-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 10 — CTA Warm — bg-accent — Чек-лист + контакт -->
<!-- ============================================================ -->

<div class="s10-root">
  <div class="s10-bg-grad"></div>
  <div class="s10-glow-tr"></div>
  <div class="s10-dots"></div>
  <div class="s10-content">
    <span class="s10-sup">Возьмите с собой</span>
    <h1 class="s10-heading">Чек-лист для вашей миграции</h1>
    <div class="s10-steps">
      <div class="s10-step">
        <span class="s10-num">01</span>
        <span class="s10-step-txt">Начните с event storming — определите границы доменов</span>
      </div>
      <div class="s10-step">
        <span class="s10-num">02</span>
        <span class="s10-step-txt">Kafka + event sourcing → асинхронность везде, где возможно</span>
      </div>
      <div class="s10-step">
        <span class="s10-num">03</span>
        <span class="s10-step-txt">Observability с первого дня: Metrics + Logs + Traces</span>
      </div>
      <div class="s10-step">
        <span class="s10-num">04</span>
        <span class="s10-step-txt">Service mesh для retry / circuit breaker / mTLS</span>
      </div>
      <div class="s10-step s10-step-warm">
        <span class="s10-num-warm">05</span>
        <span class="s10-step-txt">Размер сервиса = размер команды, не размер кода</span>
      </div>
    </div>
    <div class="s10-contact">
      <div class="s10-contact-item">
        <Icon name="git-branch" :size="16" color="rgba(255,255,255,0.75)" />
        <span class="s10-contact-txt">github.com/repo — шаблоны event storming + checklist</span>
      </div>
      <span class="s10-dot">·</span>
      <div class="s10-contact-item">
        <Icon name="send" :size="16" color="rgba(255,255,255,0.75)" />
        <span class="s10-contact-txt">@speaker_handle в Telegram</span>
      </div>
    </div>
  </div>
</div>

<style>
.s10-root { position: absolute; inset: 0; overflow: hidden; }
.s10-bg-grad { position: absolute; inset: 0; z-index: 0; background: linear-gradient(145deg, var(--color-accent) 0%, color-mix(in srgb, var(--color-accent) 70%, black) 100%); }
.s10-glow-tr { position: absolute; top: -100px; right: -100px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; z-index: 1; }
.s10-dots { position: absolute; bottom: 40px; left: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; z-index: 1; }
.s10-content { position: absolute; inset: 0; z-index: 2; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 50px 80px; }
.s10-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.75); font-weight: 600; margin-bottom: 10px; }
.s10-heading { font-family: var(--font-heading); font-size: 2.6rem; font-weight: 800; color: #FFFFFF; margin: 0 0 24px; line-height: 1.12; letter-spacing: -0.01em; }
.s10-steps { display: flex; flex-direction: column; gap: 8px; max-width: 640px; width: 100%; margin-bottom: 28px; }
.s10-step { display: flex; align-items: center; gap: 14px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22); border-radius: 12px; padding: 11px 18px; text-align: left; }
.s10-step-warm { background: rgba(217,119,6,0.25); border-color: rgba(217,119,6,0.45); }
.s10-num { font-family: var(--font-heading); font-size: 0.75rem; font-weight: 800; color: rgba(255,255,255,0.65); letter-spacing: 0.08em; flex-shrink: 0; min-width: 28px; }
.s10-num-warm { font-family: var(--font-heading); font-size: 0.75rem; font-weight: 800; color: #D97706; letter-spacing: 0.08em; flex-shrink: 0; min-width: 28px; }
.s10-step-txt { font-family: var(--font-body); font-size: 0.88rem; color: rgba(255,255,255,0.90); line-height: 1.4; }
.s10-contact { display: flex; align-items: center; gap: 18px; flex-wrap: wrap; justify-content: center; }
.s10-contact-item { display: flex; align-items: center; gap: 8px; }
.s10-contact-txt { font-family: var(--font-body); font-size: 0.85rem; color: rgba(255,255,255,0.80); }
.s10-dot { color: rgba(255,255,255,0.35); font-size: 1.2rem; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
