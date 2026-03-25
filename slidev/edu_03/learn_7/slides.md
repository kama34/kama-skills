---
theme: default
layout: none
title: ChainProof — блокчейн-верификация цепочек поставок
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
    <div class="s1-glow-tl"></div>
    <div class="s1-glow-br"></div>
    <div class="s1-dots"></div>
    <div class="s1-arc"></div>
  </div>
  <div class="s1-content">
    <div class="s1-label-wrap">
      <span class="s1-label">Воркшоп · 2026</span>
    </div>
    <h1 class="s1-heading">ChainProof</h1>
    <p class="s1-sub">Блокчейн-верификация цепочек поставок</p>
    <div class="s1-meta">
      <span>Прозрачность каждого звена</span>
      <span class="s1-dot">·</span>
      <span>Логистика и дистрибуция</span>
      <span class="s1-dot">·</span>
      <span>2026</span>
    </div>
  </div>
</div>

<style>
.s1-root { position: absolute; inset: 0; overflow: hidden; }
.s1-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-accent); }
.s1-glow-tl { position: absolute; top: -120px; left: -80px; width: 560px; height: 560px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-glow-br { position: absolute; bottom: -100px; right: -60px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-dots { position: absolute; top: 44px; right: 64px; width: 280px; height: 280px; background-image: radial-gradient(circle, rgba(255,255,255,0.22) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s1-arc { position: absolute; bottom: 40px; left: 60px; width: 320px; height: 320px; border: 1.5px solid rgba(255,255,255,0.14); border-radius: 50%; pointer-events: none; }
.s1-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s1-label-wrap { display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; margin-bottom: 28px; }
.s1-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.s1-heading { font-family: var(--font-heading); font-size: 5.8rem; font-weight: 800; color: #FFFFFF; margin: 0 0 16px; line-height: 1.0; letter-spacing: -0.02em; }
.s1-sub { font-family: var(--font-body); font-size: 1.4rem; color: rgba(255,255,255,0.88); margin: 0 0 36px; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.9rem; color: rgba(255,255,255,0.62); }
.s1-dot { color: rgba(255,255,255,0.32); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 2 — Stat Hero (left-number-right-text) — bg-base -->
<!-- Доверие потребителей: 42% не верят маркировке -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow-left"></div>
    <div class="s2-dot-grid"></div>
  </div>
  <div class="s2-content">
    <div class="s2-left">
      <span class="s2-label">Кризис доверия</span>
      <div class="s2-hero">42%</div>
      <p class="s2-caption">потребителей не доверяют маркировке «сделано в России»</p>
    </div>
    <div class="s2-right">
      <div class="s2-card">
        <div class="s2-card-icon">
          <Icon name="package" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s2-card-body">
          <span class="s2-card-val">12%</span>
          <span class="s2-card-txt">контрафакт в фармацевтике</span>
        </div>
      </div>
      <div class="s2-card s2-card-warm">
        <div class="s2-card-icon-warm">
          <Icon name="trending-down" :size="20" color="#D97706" />
        </div>
        <div class="s2-card-body">
          <span class="s2-card-val-warm">340 млрд ₽</span>
          <span class="s2-card-txt">потери от продовольственного фрода в год</span>
        </div>
      </div>
      <div class="s2-card">
        <div class="s2-card-icon">
          <Icon name="users" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s2-card-body">
          <span class="s2-card-val">78%</span>
          <span class="s2-card-txt">B2B-закупщиков хотят верифицируемое происхождение</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow-left { position: absolute; left: -60px; top: 50%; transform: translateY(-50%); width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-dot-grid { position: absolute; bottom: 40px; right: 56px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 48px; padding: 56px 72px; align-items: center; }
.s2-left { display: flex; flex-direction: column; justify-content: center; }
.s2-label { display: inline-flex; align-items: center; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s2-hero { font-family: var(--font-heading); font-size: 6rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0 0 12px; }
.s2-caption { font-family: var(--font-body); font-size: 1.1rem; color: var(--color-muted); margin: 0; line-height: 1.5; max-width: 280px; }
.s2-right { display: flex; flex-direction: column; gap: 14px; }
.s2-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 20px; display: flex; align-items: center; gap: 14px; }
.s2-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-card-icon { width: 40px; height: 40px; border-radius: 10px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-card-icon-warm { width: 40px; height: 40px; border-radius: 10px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-card-body { display: flex; flex-direction: column; gap: 3px; }
.s2-card-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-card-val-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-card-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Section Divider — bg-alt -->
<!-- Секция: Проблемы текущих систем -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-glow"></div>
    <div class="s3-arc-outer"></div>
    <div class="s3-arc-inner"></div>
  </div>
  <div class="s3-content">
    <span class="s3-section-label">Часть 1</span>
    <h1 class="s3-heading">Проблемы текущих систем</h1>
    <p class="s3-sub">Почему бумажные сертификаты и Excel не работают</p>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-glow { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s3-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 420px; height: 420px; border: 1.5px solid rgba(13,148,136,0.16); border-radius: 50%; pointer-events: none; }
.s3-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 260px; height: 260px; border: 1px solid rgba(13,148,136,0.10); border-radius: 50%; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s3-section-label { display: block; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; margin-bottom: 18px; font-family: var(--font-heading); }
.s3-heading { font-family: var(--font-heading); font-size: 3.8rem; font-weight: 800; color: var(--color-text); margin: 0 0 24px; line-height: 1.1; letter-spacing: -0.01em; }
.s3-sub { font-family: var(--font-body); font-size: 1.25rem; color: var(--color-muted); margin: 0; max-width: 640px; line-height: 1.6; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Asymmetric Split — bg-base -->
<!-- 35% инцидентов невозможно отследить до источника -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-dot-grid"></div>
  </div>
  <div class="s4-content">
    <div class="s4-visual">
      <div class="s4-visual-circle">
        <Icon name="x-circle" :size="52" color="var(--color-accent)" />
      </div>
      <div class="s4-visual-stat">35%</div>
      <div class="s4-visual-caption">инцидентов без источника</div>
    </div>
    <div class="s4-text">
      <span class="s4-label">Провал прослеживаемости</span>
      <h1 class="s4-heading">Бумажный след теряется</h1>
      <div class="s4-items">
        <div class="s4-item">
          <div class="s4-item-num">14</div>
          <div class="s4-item-body">
            <span class="s4-item-title">дней</span>
            <span class="s4-item-desc">среднее время расследования инцидента</span>
          </div>
        </div>
        <div class="s4-item">
          <div class="s4-item-num">60%</div>
          <div class="s4-item-body">
            <span class="s4-item-title">документов</span>
            <span class="s4-item-desc">содержат ошибки ручного ввода</span>
          </div>
        </div>
        <div class="s4-item s4-item-warm">
          <div class="s4-item-num s4-item-num-warm">0</div>
          <div class="s4-item-body">
            <span class="s4-item-title">единый стандарт</span>
            <span class="s4-item-desc">нет единого обмена данными между участниками цепочки</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s4-root { position: absolute; inset: 0; overflow: hidden; }
.s4-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s4-dot-grid { position: absolute; top: 40px; right: 48px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s4-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s4-visual { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; }
.s4-visual-circle { width: 100px; height: 100px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s4-visual-stat { font-family: var(--font-heading); font-size: 3.2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s4-visual-caption { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); text-align: center; max-width: 160px; line-height: 1.4; }
.s4-text { display: flex; flex-direction: column; justify-content: center; }
.s4-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; }
.s4-heading { font-family: var(--font-heading); font-size: 2.1rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; line-height: 1.15; }
.s4-items { display: flex; flex-direction: column; gap: 10px; }
.s4-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 16px; }
.s4-item-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s4-item-num { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; min-width: 60px; }
.s4-item-num-warm { color: #D97706; }
.s4-item-body { display: flex; flex-direction: column; gap: 2px; }
.s4-item-title { font-family: var(--font-heading); font-size: 0.85rem; font-weight: 700; color: var(--color-text); }
.s4-item-desc { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Icon Trio (3 items, rounded-square) — bg-alt -->
<!-- Блокчейн решает три ключевые проблемы верификации -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow"></div>
  </div>
  <div class="s5-content">
    <span class="s5-label">Решение</span>
    <h1 class="s5-heading">Блокчейн решает три ключевые проблемы верификации</h1>
    <div class="s5-grid">
      <div class="s5-item">
        <div class="s5-icon">
          <Icon name="lock" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s5-title">Неизменяемость</span>
        <span class="s5-desc">Данные нельзя подделать после записи в распределённый реестр</span>
      </div>
      <div class="s5-item">
        <div class="s5-icon">
          <Icon name="globe" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s5-title">Прозрачность</span>
        <span class="s5-desc">Все участники видят полную историю движения товара</span>
      </div>
      <div class="s5-item">
        <div class="s5-icon">
          <Icon name="zap" :size="28" color="var(--color-accent)" />
        </div>
        <span class="s5-title">Автоматизация</span>
        <span class="s5-desc">Смарт-контракты исполняют условия без посредников</span>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-glow { position: absolute; bottom: -80px; right: -80px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s5-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s5-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.2; }
.s5-grid { flex: 1; display: flex; justify-content: center; align-items: center; gap: 48px; }
.s5-item { display: flex; flex-direction: column; align-items: center; text-align: center; max-width: 220px; }
.s5-icon { width: 72px; height: 72px; border-radius: 16px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 18px; }
.s5-title { font-family: var(--font-heading); font-size: 1.15rem; font-weight: 700; color: var(--color-text); margin-bottom: 8px; }
.s5-desc { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-muted); line-height: 1.5; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Timeline Horizontal — bg-base -->
<!-- Как работает ChainProof — 4 шага от производителя до полки -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-dots"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Как работает ChainProof</span>
    <h1 class="s6-heading">4 шага от производителя до полки</h1>
    <div class="s6-steps">
      <div class="s6-step">
        <div class="s6-step-header">
          <div class="s6-step-num">01</div>
          <div class="s6-step-icon">
            <Icon name="package" :size="18" color="var(--color-accent)" />
          </div>
        </div>
        <span class="s6-step-title">Производитель</span>
        <span class="s6-step-desc">Сканирует QR-код партии → запись в блокчейн</span>
      </div>
      <div class="s6-arrow">→</div>
      <div class="s6-step">
        <div class="s6-step-header">
          <div class="s6-step-num">02</div>
          <div class="s6-step-icon">
            <Icon name="thermometer" :size="18" color="var(--color-accent)" />
          </div>
        </div>
        <span class="s6-step-title">Логистика</span>
        <span class="s6-step-desc">IoT-сенсоры фиксируют температуру и GPS в реальном времени</span>
      </div>
      <div class="s6-arrow">→</div>
      <div class="s6-step">
        <div class="s6-step-header">
          <div class="s6-step-num">03</div>
          <div class="s6-step-icon">
            <Icon name="check-circle" :size="18" color="var(--color-accent)" />
          </div>
        </div>
        <span class="s6-step-title">Дистрибьютор</span>
        <span class="s6-step-desc">Подтверждает приёмку → смарт-контракт проверяет условия</span>
      </div>
      <div class="s6-arrow">→</div>
      <div class="s6-step s6-step-accent">
        <div class="s6-step-header">
          <div class="s6-step-num s6-step-num-accent">04</div>
          <div class="s6-step-icon s6-step-icon-accent">
            <Icon name="scan" :size="18" color="var(--color-accent)" />
          </div>
        </div>
        <span class="s6-step-title">Покупатель</span>
        <span class="s6-step-desc">Сканирует QR-код → полная история товара за 2 секунды</span>
      </div>
    </div>
    <div class="s6-footer">
      <span class="s6-footer-item">
        <Icon name="shield-check" :size="14" color="var(--color-accent)" />
        <span>Hyperledger Fabric</span>
      </span>
      <span class="s6-footer-sep">·</span>
      <span class="s6-footer-item">
        <Icon name="wifi" :size="14" color="var(--color-accent)" />
        <span>IoT-сенсоры</span>
      </span>
      <span class="s6-footer-sep">·</span>
      <span class="s6-footer-item">
        <Icon name="code" :size="14" color="var(--color-accent)" />
        <span>Смарт-контракты</span>
      </span>
      <span class="s6-footer-sep">·</span>
      <span class="s6-footer-item">
        <Icon name="smartphone" :size="14" color="var(--color-accent)" />
        <span>Мобильное приложение</span>
      </span>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-dots { position: absolute; top: 36px; right: 52px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 60px; }
.s6-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s6-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s6-steps { flex: 1; display: flex; align-items: center; gap: 8px; }
.s6-step { flex: 1; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 16px; display: flex; flex-direction: column; height: 100%; max-height: 180px; }
.s6-step-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s6-step-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
.s6-step-num { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; opacity: 0.5; }
.s6-step-num-accent { opacity: 1; }
.s6-step-icon { width: 34px; height: 34px; border-radius: 8px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s6-step-icon-accent { background: rgba(13,148,136,0.18); }
.s6-step-title { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: var(--color-text); margin-bottom: 6px; }
.s6-step-desc { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.45; flex: 1; }
.s6-arrow { font-size: 1.4rem; color: var(--color-accent-dim); flex-shrink: 0; }
.s6-footer { display: flex; align-items: center; gap: 14px; margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--color-surface-border); }
.s6-footer-item { display: flex; align-items: center; gap: 6px; font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s6-footer-sep { color: var(--color-accent-dim); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Section Divider — bg-alt (different from s3) -->
<!-- Секция: Технология -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow-left"></div>
    <div class="s7-dot-grid"></div>
  </div>
  <div class="s7-content">
    <span class="s7-section-label">Часть 2</span>
    <h1 class="s7-heading">Технология</h1>
    <p class="s7-sub">Архитектура и стек ChainProof</p>
    <div class="s7-tags">
      <span class="s7-tag">
        <Icon name="database" :size="13" color="var(--color-accent)" />
        <span>Hyperledger Fabric</span>
      </span>
      <span class="s7-tag">
        <Icon name="wifi" :size="13" color="var(--color-accent)" />
        <span>IoT</span>
      </span>
      <span class="s7-tag">
        <Icon name="layers" :size="13" color="var(--color-accent)" />
        <span>API-интеграции</span>
      </span>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-glow-left { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 640px; height: 640px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-dot-grid { position: absolute; bottom: 48px; left: 60px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s7-section-label { display: block; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; margin-bottom: 18px; font-family: var(--font-heading); }
.s7-heading { font-family: var(--font-heading); font-size: 4.2rem; font-weight: 800; color: var(--color-text); margin: 0 0 20px; line-height: 1.05; letter-spacing: -0.01em; }
.s7-sub { font-family: var(--font-body); font-size: 1.25rem; color: var(--color-muted); margin: 0 0 32px; max-width: 560px; line-height: 1.6; }
.s7-tags { display: flex; align-items: center; gap: 12px; }
.s7-tag { display: inline-flex; align-items: center; gap: 7px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 7px 16px; font-size: 0.78rem; color: var(--color-accent); font-weight: 600; font-family: var(--font-body); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Bento Grid — bg-base -->
<!-- Архитектура: Hyperledger + IoT + API + App -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow"></div>
  </div>
  <div class="s8-content">
    <span class="s8-label">Архитектура ChainProof</span>
    <h1 class="s8-heading">Hyperledger Fabric + IoT-сенсоры + мобильное приложение</h1>
    <div class="s8-grid">
      <div class="s8-featured">
        <div class="s8-feat-icon">
          <Icon name="database" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s8-feat-title">Hyperledger Fabric</div>
        <div class="s8-feat-badge">permissioned blockchain</div>
        <div class="s8-feat-desc">Enterprise-grade блокчейн с разграничением доступа для участников цепочки поставок</div>
        <div class="s8-feat-sub">
          <span class="s8-feat-sub-item">
            <Icon name="shield-check" :size="13" color="var(--color-accent)" />
            <span>Неизменяемый реестр</span>
          </span>
          <span class="s8-feat-sub-item">
            <Icon name="lock" :size="13" color="var(--color-accent)" />
            <span>Приватные каналы</span>
          </span>
        </div>
      </div>
      <div class="s8-side-a">
        <div class="s8-side-icon">
          <Icon name="thermometer" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-side-body">
          <span class="s8-side-title">IoT-сенсоры</span>
          <span class="s8-side-desc">Температура, влажность, геолокация в реальном времени</span>
        </div>
      </div>
      <div class="s8-side-b">
        <div class="s8-side-icon">
          <Icon name="layers" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-side-body">
          <span class="s8-side-title">API за 5 дней</span>
          <span class="s8-side-desc">Интеграция с 1С, SAP, Oracle без кастомной разработки</span>
        </div>
      </div>
      <div class="s8-side-c">
        <div class="s8-side-icon-warm">
          <Icon name="smartphone" :size="20" color="#D97706" />
        </div>
        <div class="s8-side-body">
          <span class="s8-side-title-warm">Мобильное приложение</span>
          <span class="s8-side-desc">Верификация по QR-коду за 2 секунды</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s8-glow { position: absolute; top: 50%; right: -60px; transform: translateY(-50%); width: 440px; height: 440px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 60px; }
.s8-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s8-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 14px; line-height: 1.2; }
.s8-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s8-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 26px; display: flex; flex-direction: column; justify-content: center; }
.s8-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.s8-feat-title { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-text); line-height: 1; }
.s8-feat-badge { display: inline-flex; background: var(--color-accent-bg); border: 1px solid var(--color-accent-dim); border-radius: 10px; padding: 3px 10px; font-size: 0.68rem; color: var(--color-accent); font-weight: 600; margin: 8px 0 12px; }
.s8-feat-desc { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-muted); line-height: 1.5; margin-bottom: 16px; }
.s8-feat-sub { display: flex; flex-direction: column; gap: 7px; }
.s8-feat-sub-item { display: flex; align-items: center; gap: 7px; font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s8-side-a, .s8-side-b { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 18px; display: flex; align-items: center; gap: 14px; }
.s8-side-c { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 18px; display: flex; align-items: center; gap: 14px; }
.s8-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-side-body { display: flex; flex-direction: column; gap: 3px; }
.s8-side-title { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: var(--color-text); }
.s8-side-title-warm { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: #D97706; }
.s8-side-desc { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — Stat Hero (split-50-50) — bg-alt -->
<!-- Кейс ФармСтандарт: 100% отслеживаемость, ROI 450% -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-glow-top"></div>
    <div class="s9-dots"></div>
  </div>
  <div class="s9-content">
    <div class="s9-header">
      <span class="s9-label">Кейс</span>
      <h1 class="s9-heading">«ФармСтандарт» — 100% отслеживаемость за 3 месяца</h1>
    </div>
    <div class="s9-body">
      <div class="s9-hero-block">
        <div class="s9-hero-icon">
          <Icon name="award" :size="32" color="var(--color-accent)" />
        </div>
        <div class="s9-hero-num">450%</div>
        <div class="s9-hero-label">ROI за первый год</div>
      </div>
      <div class="s9-stats-grid">
        <div class="s9-stat-card">
          <span class="s9-stat-val">12</span>
          <span class="s9-stat-unit">складов</span>
          <span class="s9-stat-desc">охвачено внедрением</span>
        </div>
        <div class="s9-stat-card">
          <span class="s9-stat-val">3 000</span>
          <span class="s9-stat-unit">SKU</span>
          <span class="s9-stat-desc">под полным контролем</span>
        </div>
        <div class="s9-stat-card s9-stat-card-warm">
          <span class="s9-stat-val-warm">340</span>
          <span class="s9-stat-unit-warm">партий</span>
          <span class="s9-stat-desc">контрафакт выявлен и заблокирован</span>
        </div>
        <div class="s9-stat-card s9-stat-card-accent">
          <span class="s9-stat-val">14→2</span>
          <span class="s9-stat-unit">дня</span>
          <span class="s9-stat-desc">время расследования инцидента</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s9-glow-top { position: absolute; top: -80px; left: 50%; transform: translateX(-50%); width: 600px; height: 400px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 70%); border-radius: 50%; pointer-events: none; }
.s9-dots { position: absolute; bottom: 40px; right: 56px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 64px; }
.s9-header { margin-bottom: 18px; }
.s9-label { display: inline-flex; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s9-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0; line-height: 1.2; }
.s9-body { flex: 1; display: grid; grid-template-columns: 1fr 2fr; gap: 24px; align-items: center; }
.s9-hero-block { display: flex; flex-direction: column; align-items: center; text-align: center; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 16px; padding: 32px 24px; height: 100%; justify-content: center; }
.s9-hero-icon { width: 64px; height: 64px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s9-hero-num { font-family: var(--font-heading); font-size: 4.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-hero-label { font-family: var(--font-body); font-size: 0.9rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s9-stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; align-content: stretch; }
.s9-stat-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 20px; display: flex; flex-direction: column; }
.s9-stat-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s9-stat-card-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s9-stat-val { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-stat-val-warm { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s9-stat-unit { font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 3px; }
.s9-stat-unit-warm { font-family: var(--font-heading); font-size: 0.75rem; font-weight: 700; color: rgba(217,119,6,0.65); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 3px; }
.s9-stat-desc { font-family: var(--font-body); font-size: 0.76rem; color: var(--color-muted); margin-top: 6px; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 10 — Comparison Table — bg-base -->
<!-- ChainProof vs традиционные системы -->
<!-- ============================================================ -->

<div class="s10-root">
  <div class="s10-bg">
    <div class="s10-glow"></div>
  </div>
  <div class="s10-content">
    <span class="s10-label">Сравнение</span>
    <h1 class="s10-heading">ChainProof vs традиционные системы отслеживания</h1>
    <div class="s10-table">
      <div class="s10-thead">
        <div class="s10-thead-empty"></div>
        <div class="s10-thead-col s10-thead-chain">ChainProof</div>
        <div class="s10-thead-col s10-thead-trad">Бумажный документооборот</div>
      </div>
      <div class="s10-row">
        <div class="s10-row-label">
          <Icon name="clock" :size="16" color="var(--color-accent)" />
          <span>Скорость верификации</span>
        </div>
        <div class="s10-cell s10-cell-good">2 сек</div>
        <div class="s10-cell s10-cell-bad">14 дней</div>
      </div>
      <div class="s10-row">
        <div class="s10-row-label">
          <Icon name="ruble" :size="16" color="var(--color-accent)" />
          <span>Стоимость на единицу</span>
        </div>
        <div class="s10-cell s10-cell-good">0,3 ₽</div>
        <div class="s10-cell s10-cell-bad">2,5 ₽</div>
      </div>
      <div class="s10-row">
        <div class="s10-row-label">
          <Icon name="shield" :size="16" color="var(--color-accent)" />
          <span>Защита от подделки</span>
        </div>
        <div class="s10-cell s10-cell-good">Криптографическая</div>
        <div class="s10-cell s10-cell-bad">Физическая маркировка</div>
      </div>
      <div class="s10-row s10-row-accent">
        <div class="s10-row-label">
          <Icon name="code" :size="16" color="var(--color-accent)" />
          <span>Интеграция в систему</span>
        </div>
        <div class="s10-cell s10-cell-good">API за 5 дней</div>
        <div class="s10-cell s10-cell-bad">3–6 месяцев разработки</div>
      </div>
    </div>
  </div>
</div>

<style>
.s10-root { position: absolute; inset: 0; overflow: hidden; }
.s10-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s10-glow { position: absolute; bottom: -80px; left: -60px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s10-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 64px; }
.s10-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s10-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 18px; }
.s10-table { flex: 1; display: flex; flex-direction: column; gap: 8px; }
.s10-thead { display: grid; grid-template-columns: 2fr 1.2fr 1.2fr; gap: 8px; margin-bottom: 4px; }
.s10-thead-empty {}
.s10-thead-col { font-family: var(--font-heading); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; text-align: center; padding: 8px 12px; border-radius: 8px; }
.s10-thead-chain { background: var(--color-accent-bg); color: var(--color-accent); border: 1.5px solid var(--color-accent-dim); }
.s10-thead-trad { background: rgba(107,107,107,0.08); color: var(--color-muted); border: 1px solid rgba(107,107,107,0.15); }
.s10-row { display: grid; grid-template-columns: 2fr 1.2fr 1.2fr; gap: 8px; align-items: stretch; }
.s10-row-accent { }
.s10-row-label { display: flex; align-items: center; gap: 10px; background: transparent; border: 1px solid var(--color-surface-border); border-radius: 10px; padding: 14px 16px; font-family: var(--font-body); font-size: 0.88rem; color: var(--color-text); }
.s10-cell { display: flex; align-items: center; justify-content: center; text-align: center; border-radius: 10px; padding: 14px 12px; font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; }
.s10-cell-good { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); color: var(--color-accent); }
.s10-cell-bad { background: rgba(107,107,107,0.07); border: 1px solid rgba(107,107,107,0.15); color: var(--color-muted); text-decoration: line-through; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 11 — Card Mosaic 2×2 — bg-alt -->
<!-- Экономика внедрения — окупаемость за 8 месяцев -->
<!-- ============================================================ -->

<div class="s11-root">
  <div class="s11-bg">
    <div class="s11-glow"></div>
    <div class="s11-dots"></div>
  </div>
  <div class="s11-content">
    <span class="s11-label">Экономика</span>
    <h1 class="s11-heading">Окупаемость за 8 месяцев</h1>
    <div class="s11-grid">
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="ruble" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s11-card-val">2–5 млн ₽</div>
        <div class="s11-card-title">Стоимость внедрения</div>
        <div class="s11-card-desc">в зависимости от масштаба и числа участников цепочки</div>
      </div>
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="trending-down" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s11-card-val">−40%</div>
        <div class="s11-card-title">Экономия документооборота</div>
        <div class="s11-card-desc">автоматизация бумажных процессов и ручного ввода</div>
      </div>
      <div class="s11-card">
        <div class="s11-card-icon">
          <Icon name="shield-check" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s11-card-val">−60–80%</div>
        <div class="s11-card-title">Снижение потерь от контрафакта</div>
        <div class="s11-card-desc">благодаря криптографической верификации каждой партии</div>
      </div>
      <div class="s11-card s11-card-warm">
        <div class="s11-card-icon-warm">
          <Icon name="percent" :size="22" color="#D97706" />
        </div>
        <div class="s11-card-val-warm">−15%</div>
        <div class="s11-card-title-warm">Страховые премии</div>
        <div class="s11-card-desc">для верифицированных цепочек поставок</div>
      </div>
    </div>
  </div>
</div>

<style>
.s11-root { position: absolute; inset: 0; overflow: hidden; }
.s11-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s11-glow { position: absolute; top: -60px; right: -60px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s11-dots { position: absolute; bottom: 40px; left: 56px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s11-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 40px 60px; }
.s11-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s11-heading { font-family: var(--font-heading); font-size: 2.1rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s11-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px; }
.s11-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 20px 22px; display: flex; flex-direction: column; }
.s11-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s11-card-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; }
.s11-card-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; }
.s11-card-val { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin-bottom: 4px; }
.s11-card-val-warm { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 800; color: #D97706; line-height: 1; margin-bottom: 4px; }
.s11-card-title { font-family: var(--font-heading); font-size: 0.9rem; font-weight: 700; color: var(--color-text); margin-bottom: 6px; }
.s11-card-title-warm { font-family: var(--font-heading); font-size: 0.9rem; font-weight: 700; color: #D97706; margin-bottom: 6px; }
.s11-card-desc { font-family: var(--font-body); font-size: 0.76rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 12 — Data Spotlight — bg-base -->
<!-- Практическое задание — запустите свой первый смарт-контракт -->
<!-- ============================================================ -->

<div class="s12-root">
  <div class="s12-bg">
    <div class="s12-glow"></div>
    <div class="s12-arc"></div>
  </div>
  <div class="s12-content">
    <span class="s12-label">Практика</span>
    <h1 class="s12-heading">Запустите свой первый смарт-контракт</h1>
    <div class="s12-steps">
      <div class="s12-step">
        <div class="s12-step-badge">01</div>
        <div class="s12-step-body">
          <span class="s12-step-title">Откройте sandbox</span>
          <span class="s12-step-desc">Перейдите на sandbox.chainproof.io в браузере</span>
        </div>
      </div>
      <div class="s12-step">
        <div class="s12-step-badge">02</div>
        <div class="s12-step-body">
          <span class="s12-step-title">Создайте цепочку</span>
          <span class="s12-step-desc">Добавьте 3 участника: производитель, логист, дистрибьютор</span>
        </div>
      </div>
      <div class="s12-step">
        <div class="s12-step-badge">03</div>
        <div class="s12-step-body">
          <span class="s12-step-title">Загрузите партию</span>
          <span class="s12-step-desc">Запишите тестовую партию и проследите путь в реестре</span>
        </div>
      </div>
      <div class="s12-step s12-step-accent">
        <div class="s12-step-badge s12-step-badge-accent">
          <Icon name="clock" :size="16" color="var(--color-accent)" />
        </div>
        <div class="s12-step-body">
          <span class="s12-step-title">20 минут</span>
          <span class="s12-step-desc">Время на выполнение задания</span>
        </div>
      </div>
    </div>
    <div class="s12-url">
      <Icon name="link-2" :size="15" color="var(--color-accent)" />
      <span>sandbox.chainproof.io</span>
    </div>
  </div>
</div>

<style>
.s12-root { position: absolute; inset: 0; overflow: hidden; }
.s12-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s12-glow { position: absolute; top: 50%; right: -80px; transform: translateY(-50%); width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s12-arc { position: absolute; top: 50%; right: -80px; transform: translateY(-50%); width: 320px; height: 320px; border: 1.5px solid rgba(13,148,136,0.16); border-radius: 50%; pointer-events: none; }
.s12-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s12-label { display: inline-flex; align-self: flex-start; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; }
.s12-heading { font-family: var(--font-heading); font-size: 2.1rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s12-steps { flex: 1; display: flex; flex-direction: column; gap: 10px; }
.s12-step { display: flex; align-items: center; gap: 16px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 16px 20px; }
.s12-step-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s12-step-badge { width: 38px; height: 38px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; font-family: var(--font-heading); font-size: 0.85rem; font-weight: 800; color: var(--color-accent); flex-shrink: 0; }
.s12-step-badge-accent { background: rgba(13,148,136,0.18); }
.s12-step-body { display: flex; flex-direction: column; gap: 3px; }
.s12-step-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); }
.s12-step-desc { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s12-url { display: flex; align-items: center; gap: 8px; margin-top: 14px; font-family: var(--font-heading); font-size: 0.9rem; font-weight: 700; color: var(--color-accent); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 13 — CTA Warm — bg-accent -->
<!-- Запустите пилот на 1 цепочке бесплатно -->
<!-- ============================================================ -->

<div class="s13-root">
  <div class="s13-bg">
    <div class="s13-bg-gradient"></div>
    <div class="s13-glow-tr"></div>
    <div class="s13-glow-bl"></div>
    <div class="s13-dots"></div>
  </div>
  <div class="s13-content">
    <span class="s13-label">Следующий шаг</span>
    <h1 class="s13-heading">Запустите пилот на 1 цепочке — бесплатно</h1>
    <div class="s13-steps">
      <div class="s13-step">
        <div class="s13-step-num">1</div>
        <span class="s13-step-text">Бесплатный пилот — 1 цепочка, до 500 транзакций</span>
      </div>
      <div class="s13-step">
        <div class="s13-step-num">2</div>
        <span class="s13-step-text">Полный отчёт с ROI-расчётом через 30 дней</span>
      </div>
      <div class="s13-step s13-step-warm">
        <div class="s13-step-num s13-step-num-warm">3</div>
        <span class="s13-step-text">Результат за 30 дней или возврат средств</span>
      </div>
    </div>
    <div class="s13-contact">
      <span class="s13-contact-item">
        <Icon name="mail" :size="16" color="rgba(255,255,255,0.85)" />
        <span>pilot@chainproof.io</span>
      </span>
      <span class="s13-sep">·</span>
      <span class="s13-contact-item">
        <Icon name="globe" :size="16" color="rgba(255,255,255,0.85)" />
        <span>chainproof.io/workshop</span>
      </span>
    </div>
  </div>
</div>

<style>
.s13-root { position: absolute; inset: 0; overflow: hidden; }
.s13-bg { position: absolute; inset: 0; z-index: 0; }
.s13-bg-gradient { position: absolute; inset: 0; background: linear-gradient(145deg, var(--color-accent) 0%, color-mix(in srgb, var(--color-accent) 70%, black) 100%); }
.s13-glow-tr { position: absolute; top: -100px; right: -80px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s13-glow-bl { position: absolute; bottom: -100px; left: -80px; width: 440px; height: 440px; background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s13-dots { position: absolute; top: 40px; left: 60px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s13-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s13-label { display: inline-flex; align-items: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 24px; }
.s13-heading { font-family: var(--font-heading); font-size: 2.8rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.15; letter-spacing: -0.01em; max-width: 700px; }
.s13-steps { display: flex; flex-direction: column; gap: 12px; max-width: 560px; width: 100%; margin-bottom: 36px; }
.s13-step { display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22); border-radius: 12px; padding: 14px 20px; text-align: left; }
.s13-step-warm { background: rgba(217,119,6,0.25); border: 1px solid rgba(217,119,6,0.40); }
.s13-step-num { width: 32px; height: 32px; border-radius: 50%; background: rgba(255,255,255,0.2); border: 1.5px solid rgba(255,255,255,0.4); display: flex; align-items: center; justify-content: center; font-family: var(--font-heading); font-size: 0.85rem; font-weight: 800; color: #FFFFFF; flex-shrink: 0; }
.s13-step-num-warm { background: rgba(217,119,6,0.35); border-color: rgba(217,119,6,0.6); color: #FFFFFF; }
.s13-step-text { font-family: var(--font-body); font-size: 0.95rem; color: rgba(255,255,255,0.92); line-height: 1.4; }
.s13-contact { display: flex; align-items: center; gap: 20px; }
.s13-contact-item { display: flex; align-items: center; gap: 8px; font-family: var(--font-heading); font-size: 0.95rem; font-weight: 600; color: rgba(255,255,255,0.88); }
.s13-sep { color: rgba(255,255,255,0.4); font-size: 1.1rem; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
