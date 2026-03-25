---
theme: default
layout: none
title: Маркетинг Q1 — квартальный отчёт
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
      <span class="s1-label">Маркетинг Q1 2026</span>
    </div>
    <h1 class="s1-heading">Удвоение конверсии<br>за 90 дней</h1>
    <p class="s1-sub">Без увеличения рекламного бюджета</p>
    <div class="s1-meta">
      <span>Квартальный отчёт</span>
      <span class="s1-dot">·</span>
      <span>Совет директоров</span>
      <span class="s1-dot">·</span>
      <span>Q1 2026</span>
    </div>
  </div>
</div>

<style>
.s1-root { position: absolute; inset: 0; overflow: hidden; }
.s1-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-accent); }
.s1-glow-tr { position: absolute; top: -120px; right: -120px; width: 540px; height: 540px; background: radial-gradient(circle, rgba(255,255,255,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-glow-bl { position: absolute; bottom: -80px; left: -80px; width: 440px; height: 440px; background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s1-dots { position: absolute; bottom: 40px; right: 56px; width: 280px; height: 280px; background-image: radial-gradient(circle, rgba(255,255,255,0.20) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s1-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; }
.s1-label-wrap { display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.15); border: 1.5px solid rgba(255,255,255,0.35); border-radius: 20px; padding: 6px 20px; margin-bottom: 28px; line-height: 1; }
.s1-label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: #FFFFFF; font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.s1-heading { font-family: var(--font-heading); font-size: 4.8rem; font-weight: 800; color: #FFFFFF; margin: 0 0 18px; line-height: 1.08; letter-spacing: -0.02em; text-align: center; }
.s1-sub { font-family: var(--font-body); font-size: 1.35rem; color: rgba(255,255,255,0.82); margin: 0 0 36px; text-align: center; }
.s1-meta { display: flex; align-items: center; gap: 14px; font-family: var(--font-body); font-size: 0.88rem; color: rgba(255,255,255,0.60); }
.s1-dot { color: rgba(255,255,255,0.30); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 2 — Stat Hero (left-number-right-text) — bg-base — конверсия 2,1% → 4,3% -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow"></div>
    <div class="s2-arc"></div>
    <div class="s2-dots"></div>
  </div>
  <div class="s2-content">
    <div class="s2-left">
      <span class="s2-label">Главный результат Q1</span>
      <div class="s2-from">2,1%</div>
      <div class="s2-arrow">→</div>
      <div class="s2-to">4,3%</div>
      <div class="s2-caption">конверсия сайта</div>
    </div>
    <div class="s2-divider"></div>
    <div class="s2-right">
      <h1 class="s2-heading">Удвоение конверсии<br>за один квартал</h1>
      <div class="s2-stats">
        <div class="s2-stat">
          <span class="s2-stat-num">+45%</span>
          <span class="s2-stat-txt">органический трафик</span>
        </div>
        <div class="s2-stat s2-stat-warm">
          <span class="s2-stat-num-warm">−49%</span>
          <span class="s2-stat-txt">CAC: с 1 800 ₽ до 920 ₽</span>
        </div>
        <div class="s2-stat">
          <span class="s2-stat-num">0 ₽</span>
          <span class="s2-stat-txt">прирост рекламного бюджета</span>
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
.s2-dots { position: absolute; top: 32px; right: 48px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 1fr 2px 1.4fr; align-items: center; padding: 52px 72px; gap: 48px; }
.s2-left { display: flex; flex-direction: column; align-items: flex-start; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 20px; }
.s2-from { font-family: var(--font-heading); font-size: 3.4rem; font-weight: 800; color: var(--color-muted); line-height: 1; }
.s2-arrow { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 300; color: var(--color-accent-dim); line-height: 1.2; }
.s2-to { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-caption { font-family: var(--font-body); font-size: 0.9rem; color: var(--color-muted); margin-top: 6px; }
.s2-divider { width: 2px; background: linear-gradient(to bottom, transparent, var(--color-accent-dim), transparent); align-self: stretch; }
.s2-right { display: flex; flex-direction: column; justify-content: center; }
.s2-heading { font-family: var(--font-heading); font-size: 2.0rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.2; }
.s2-stats { display: flex; flex-direction: column; gap: 12px; }
.s2-stat { display: flex; align-items: center; gap: 16px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 20px; }
.s2-stat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-stat-num { font-family: var(--font-heading); font-size: 1.7rem; font-weight: 800; color: var(--color-accent); line-height: 1; min-width: 70px; }
.s2-stat-num-warm { font-family: var(--font-heading); font-size: 1.7rem; font-weight: 800; color: #D97706; line-height: 1; min-width: 70px; }
.s2-stat-txt { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Section Divider — bg-alt — Три ключевых инициативы -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-glow-c"></div>
    <div class="s3-arc-outer"></div>
    <div class="s3-arc-inner"></div>
  </div>
  <div class="s3-content">
    <span class="s3-eyebrow">Раздел 1 из 2</span>
    <h1 class="s3-heading">Три ключевых инициативы</h1>
    <p class="s3-sub">Что именно мы изменили и почему это сработало</p>
    <div class="s3-chips">
      <span class="s3-chip">Лендинги</span>
      <span class="s3-chip">SEO-кластеризация</span>
      <span class="s3-chip">Email-реактивация</span>
    </div>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-glow-c { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 600px; height: 600px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s3-arc-outer { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 420px; height: 420px; border: 1.5px solid rgba(13,148,136,0.16); border-radius: 50%; pointer-events: none; }
.s3-arc-inner { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 240px; height: 240px; border: 1px solid rgba(13,148,136,0.10); border-radius: 50%; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 100px; }
.s3-eyebrow { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--color-accent); font-weight: 600; font-family: var(--font-heading); margin-bottom: 16px; }
.s3-heading { font-family: var(--font-heading); font-size: 3.8rem; font-weight: 800; color: var(--color-text); margin: 0 0 20px; line-height: 1.1; text-align: center; letter-spacing: -0.01em; }
.s3-sub { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); max-width: 640px; line-height: 1.6; margin: 0 0 32px; text-align: center; }
.s3-chips { display: flex; gap: 12px; }
.s3-chip { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 8px 20px; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Asymmetric Split — bg-base — Лендинги +68% -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <div class="s4-left">
      <div class="s4-visual">
        <div class="s4-big-num">+68%</div>
        <div class="s4-big-label">конверсия<br>лендингов</div>
        <div class="s4-badge">A/B тест • 99% significance</div>
      </div>
    </div>
    <div class="s4-right">
      <span class="s4-label">Инициатива 1</span>
      <h1 class="s4-heading">«Один экран — одно действие»</h1>
      <div class="s4-compare">
        <div class="s4-before">
          <div class="s4-compare-header s4-before-header">
            <Icon name="trending-down" :size="16" color="#D97706" />
            <span>Было</span>
          </div>
          <ul class="s4-list">
            <li>7 секций на странице</li>
            <li>3 разных CTA</li>
            <li>2 формы одновременно</li>
          </ul>
        </div>
        <div class="s4-after">
          <div class="s4-compare-header s4-after-header">
            <Icon name="check-circle" :size="16" color="var(--color-accent)" />
            <span>Стало</span>
          </div>
          <ul class="s4-list">
            <li>1 hero-блок</li>
            <li>1 CTA</li>
            <li>Social proof</li>
          </ul>
        </div>
      </div>
      <div class="s4-result">
        <Icon name="zap" :size="18" color="var(--color-accent)" />
        <span>Новый вариант победил за 5 дней</span>
      </div>
    </div>
  </div>
</div>

<style>
.s4-root { position: absolute; inset: 0; overflow: hidden; }
.s4-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s4-glow { position: absolute; top: -60px; left: -60px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s4-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; align-items: center; padding: 52px 72px; gap: 48px; }
.s4-left { display: flex; justify-content: center; align-items: center; }
.s4-visual { display: flex; flex-direction: column; align-items: center; text-align: center; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 36px 28px; width: 100%; }
.s4-big-num { font-family: var(--font-heading); font-size: 5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s4-big-label { font-family: var(--font-body); font-size: 0.95rem; color: var(--color-muted); line-height: 1.4; margin-top: 8px; text-align: center; }
.s4-badge { display: inline-flex; align-items: center; background: rgba(13,148,136,0.10); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 6px 14px; font-size: 0.68rem; color: var(--color-accent); font-weight: 600; font-family: var(--font-heading); margin-top: 18px; line-height: 1; }
.s4-right { display: flex; flex-direction: column; justify-content: center; }
.s4-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s4-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; line-height: 1.2; }
.s4-compare { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px; }
.s4-before { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; }
.s4-after { background: var(--color-surface); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 16px 20px; }
.s4-compare-header { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
.s4-before-header { color: #D97706; font-family: var(--font-heading); font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }
.s4-after-header { color: var(--color-accent); font-family: var(--font-heading); font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }
.s4-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px; }
.s4-list li { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-text); line-height: 1.35; padding-left: 14px; position: relative; }
.s4-list li::before { content: '—'; position: absolute; left: 0; color: var(--color-muted); }
.s4-result { display: flex; align-items: center; gap: 10px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 10px; padding: 12px 16px; }
.s4-result span { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-accent); font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Bento Grid — bg-alt — SEO 12 000 визитов -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-dot"></div>
  </div>
  <div class="s5-content">
    <span class="s5-label">Инициатива 2</span>
    <h1 class="s5-heading">SEO-кластеризация: 12 000 новых визитов в месяц</h1>
    <div class="s5-grid">
      <div class="s5-featured">
        <div class="s5-feat-icon">
          <Icon name="globe" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s5-feat-num">12 000</div>
        <div class="s5-feat-sub">новых визитов<br>из поиска / мес</div>
        <div class="s5-feat-detail">85 статей → 12 тематических кластеров</div>
      </div>
      <div class="s5-side-a">
        <div class="s5-side-icon">
          <Icon name="trending-up" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s5-side-body">
          <span class="s5-side-val">с 18 → 5</span>
          <span class="s5-side-txt">средняя позиция по целевым запросам</span>
        </div>
      </div>
      <div class="s5-side-b">
        <div class="s5-side-icon-warm">
          <Icon name="target" :size="20" color="#D97706" />
        </div>
        <div class="s5-side-body">
          <span class="s5-side-val-warm">3,8%</span>
          <span class="s5-side-txt">конверсия из блога (было 1,2%)</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-dot { position: absolute; top: 36px; right: 48px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(13,148,136,0.36) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s5-heading { font-family: var(--font-heading); font-size: 2.0rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; line-height: 1.2; }
.s5-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr; gap: 12px; }
.s5-featured { grid-row: 1 / 3; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s5-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s5-feat-num { font-family: var(--font-heading); font-size: 4.2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-feat-sub { font-family: var(--font-body); font-size: 0.95rem; color: var(--color-muted); margin-top: 6px; line-height: 1.45; }
.s5-feat-detail { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); opacity: 0.8; line-height: 1.5; }
.s5-side-a { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 18px 20px; display: flex; align-items: center; gap: 14px; }
.s5-side-b { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 18px 20px; display: flex; align-items: center; gap: 14px; }
.s5-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-side-body { display: flex; flex-direction: column; gap: 3px; }
.s5-side-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-side-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s5-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Card Mosaic 2×2 — bg-base — Email-реактивация -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Инициатива 3</span>
    <h1 class="s6-heading">Email-реактивация: 2 300 «спящих» клиентов вернулись</h1>
    <div class="s6-grid">
      <div class="s6-card s6-card-accent">
        <div class="s6-card-icon">
          <Icon name="users" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s6-card-num">2 300</div>
        <div class="s6-card-txt">реактивированных клиентов</div>
      </div>
      <div class="s6-card s6-card-warm">
        <div class="s6-card-icon-warm">
          <Icon name="dollar-sign" :size="22" color="#D97706" />
        </div>
        <div class="s6-card-num-warm">8 500 ₽</div>
        <div class="s6-card-txt">средний LTV реактивированного</div>
      </div>
      <div class="s6-card s6-card-solid">
        <div class="s6-card-icon">
          <Icon name="mail" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s6-card-num">+42%</div>
        <div class="s6-card-txt">open rate с AI subject lines</div>
      </div>
      <div class="s6-card s6-card-solid">
        <div class="s6-card-icon">
          <Icon name="layers" :size="22" color="var(--color-accent)" />
        </div>
        <div class="s6-card-num">7 писем</div>
        <div class="s6-card-txt">цепочка за 21 день по 5 RFM-когортам</div>
      </div>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-glow { position: absolute; bottom: -60px; right: -60px; width: 500px; height: 500px; background: radial-gradient(circle, rgba(13,148,136,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; line-height: 1.25; }
.s6-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 14px; }
.s6-card { border-radius: 14px; padding: 22px 24px; display: flex; flex-direction: column; justify-content: center; }
.s6-card-accent { background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); }
.s6-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s6-card-solid { background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s6-card-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; }
.s6-card-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; }
.s6-card-num { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s6-card-num-warm { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: #D97706; line-height: 1; }
.s6-card-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); margin-top: 6px; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Comparison Table (funnel) — bg-alt — Воронка продаж -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-dots"></div>
  </div>
  <div class="s7-content">
    <span class="s7-label">Аналитика воронки</span>
    <h1 class="s7-heading">Где теряем и что починим в Q2</h1>
    <div class="s7-funnel">
      <div class="s7-stage s7-stage-ok">
        <div class="s7-stage-left">
          <div class="s7-stage-icon">
            <Icon name="users" :size="18" color="var(--color-accent)" />
          </div>
          <div class="s7-stage-info">
            <span class="s7-stage-name">Awareness → Interest</span>
            <span class="s7-stage-note">Норма · стабильно</span>
          </div>
        </div>
        <div class="s7-stage-right">
          <span class="s7-pct s7-pct-ok">85%</span>
        </div>
        <div class="s7-bar-wrap">
          <div class="s7-bar s7-bar-ok" style="width:85%"></div>
        </div>
      </div>
      <div class="s7-stage s7-stage-improved">
        <div class="s7-stage-left">
          <div class="s7-stage-icon-warm">
            <Icon name="trending-up" :size="18" color="#D97706" />
          </div>
          <div class="s7-stage-info">
            <span class="s7-stage-name">Interest → Consideration</span>
            <span class="s7-stage-note">Улучшили с 34% → 52%</span>
          </div>
        </div>
        <div class="s7-stage-right">
          <span class="s7-pct s7-pct-warm">52%</span>
        </div>
        <div class="s7-bar-wrap">
          <div class="s7-bar s7-bar-warm" style="width:52%"></div>
        </div>
      </div>
      <div class="s7-stage s7-stage-focus">
        <div class="s7-stage-left">
          <div class="s7-stage-icon-focus">
            <Icon name="target" :size="18" color="var(--color-accent)" />
          </div>
          <div class="s7-stage-info">
            <span class="s7-stage-name">Consideration → Purchase</span>
            <span class="s7-stage-note s7-focus-note">Зона роста · цель Q2: 28%</span>
          </div>
        </div>
        <div class="s7-stage-right">
          <span class="s7-pct s7-pct-focus">18%</span>
          <span class="s7-target">→ 28%</span>
        </div>
        <div class="s7-bar-wrap">
          <div class="s7-bar s7-bar-focus" style="width:18%"></div>
          <div class="s7-bar-target" style="width:28%"></div>
        </div>
      </div>
    </div>
    <div class="s7-footer">
      <Icon name="zap" :size="16" color="var(--color-accent)" />
      <span>Конверсия Consideration → Purchase — главный приоритет Q2: +10 п.п. = ~1 200 дополнительных сделок/мес</span>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-dots { position: absolute; bottom: 32px; left: 48px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.30) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 2.0rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; line-height: 1.2; }
.s7-funnel { flex: 1; display: flex; flex-direction: column; gap: 14px; justify-content: center; }
.s7-stage { border-radius: 14px; padding: 18px 22px; display: flex; flex-direction: column; gap: 10px; position: relative; }
.s7-stage-ok { background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s7-stage-improved { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s7-stage-focus { background: linear-gradient(135deg, rgba(13,148,136,0.09), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); }
.s7-stage-left { display: flex; align-items: center; gap: 14px; }
.s7-stage-right { position: absolute; right: 22px; top: 18px; display: flex; align-items: center; gap: 10px; }
.s7-stage-icon { width: 38px; height: 38px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-stage-icon-warm { width: 38px; height: 38px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-stage-icon-focus { width: 38px; height: 38px; border-radius: 10px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-stage-info { display: flex; flex-direction: column; gap: 2px; }
.s7-stage-name { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: var(--color-text); }
.s7-stage-note { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); }
.s7-focus-note { color: var(--color-accent); font-weight: 600; }
.s7-pct { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; line-height: 1; }
.s7-pct-ok { color: var(--color-accent); }
.s7-pct-warm { color: #D97706; }
.s7-pct-focus { color: var(--color-accent); }
.s7-target { font-family: var(--font-heading); font-size: 1.0rem; font-weight: 700; color: var(--color-muted); }
.s7-bar-wrap { position: relative; height: 6px; background: rgba(13,148,136,0.10); border-radius: 3px; overflow: visible; }
.s7-bar { height: 6px; border-radius: 3px; }
.s7-bar-ok { background: var(--color-accent); }
.s7-bar-warm { background: #D97706; }
.s7-bar-focus { background: var(--color-accent); position: relative; z-index: 1; }
.s7-bar-target { position: absolute; top: 0; left: 0; height: 6px; border-radius: 3px; background: rgba(13,148,136,0.30); border-right: 2px dashed var(--color-accent); }
.s7-footer { display: flex; align-items: center; gap: 10px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 10px; padding: 12px 16px; margin-top: 6px; }
.s7-footer span { font-family: var(--font-body); font-size: 0.8rem; color: var(--color-accent); font-weight: 600; line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Data Spotlight — bg-base — Бюджет Q1 ROI 340% -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow-c"></div>
    <div class="s8-arc"></div>
  </div>
  <div class="s8-content">
    <span class="s8-label">Финансы Q1</span>
    <h1 class="s8-heading">Бюджет 12,4 млн ₽ · ROI 340%</h1>
    <div class="s8-grid">
      <div class="s8-card s8-card-hero">
        <div class="s8-hero-icon">
          <Icon name="trending-up" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-hero-num">340%</div>
        <div class="s8-hero-txt">итоговый ROI маркетинга Q1</div>
      </div>
      <div class="s8-card s8-card-solid">
        <div class="s8-mini-row">
          <div class="s8-channel-icon">
            <Icon name="bar-chart-2" :size="16" color="var(--color-accent)" />
          </div>
          <span class="s8-channel-name">Paid</span>
        </div>
        <div class="s8-channel-num">5,8 млн ₽</div>
        <div class="s8-channel-result">3 200 лидов</div>
      </div>
      <div class="s8-card s8-card-accent">
        <div class="s8-mini-row">
          <div class="s8-channel-icon-accent">
            <Icon name="search" :size="16" color="var(--color-accent)" />
          </div>
          <span class="s8-channel-name-accent">SEO/Content</span>
        </div>
        <div class="s8-channel-num-accent">3,2 млн ₽</div>
        <div class="s8-channel-result-accent">1 800 лидов · самый дешёвый канал</div>
      </div>
      <div class="s8-card s8-card-solid">
        <div class="s8-mini-row">
          <div class="s8-channel-icon">
            <Icon name="mail" :size="16" color="var(--color-accent)" />
          </div>
          <span class="s8-channel-name">Email</span>
        </div>
        <div class="s8-channel-num">0,8 млн ₽</div>
        <div class="s8-channel-result">2 300 реактиваций</div>
      </div>
      <div class="s8-card s8-card-warm">
        <div class="s8-mini-row">
          <div class="s8-channel-icon-warm">
            <Icon name="star" :size="16" color="#D97706" />
          </div>
          <span class="s8-channel-name-warm">Events</span>
        </div>
        <div class="s8-channel-num-warm">2,6 млн ₽</div>
        <div class="s8-channel-result-warm">450 enterprise-лидов</div>
      </div>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s8-glow-c { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 520px; height: 520px; background: radial-gradient(circle, rgba(13,148,136,0.09) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-arc { position: absolute; top: 50%; right: -100px; transform: translateY(-50%); width: 380px; height: 380px; border: 1.5px solid rgba(13,148,136,0.12); border-radius: 50%; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s8-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s8-heading { font-family: var(--font-heading); font-size: 2.0rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; line-height: 1.2; }
.s8-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 12px; }
.s8-card { border-radius: 14px; padding: 18px 22px; display: flex; flex-direction: column; justify-content: center; }
.s8-card-hero { grid-column: 1; grid-row: 1 / 3; background: linear-gradient(135deg, rgba(13,148,136,0.14), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); align-items: flex-start; }
.s8-card-solid { background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s8-card-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s8-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s8-hero-icon { width: 44px; height: 44px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.s8-hero-num { font-family: var(--font-heading); font-size: 4.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s8-hero-txt { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s8-mini-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.s8-channel-icon { width: 30px; height: 30px; border-radius: 8px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-channel-icon-accent { width: 30px; height: 30px; border-radius: 8px; background: rgba(13,148,136,0.14); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-channel-icon-warm { width: 30px; height: 30px; border-radius: 8px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s8-channel-name { font-family: var(--font-heading); font-size: 0.78rem; font-weight: 700; color: var(--color-muted); text-transform: uppercase; letter-spacing: 0.08em; }
.s8-channel-name-accent { font-family: var(--font-heading); font-size: 0.78rem; font-weight: 700; color: var(--color-accent); text-transform: uppercase; letter-spacing: 0.08em; }
.s8-channel-name-warm { font-family: var(--font-heading); font-size: 0.78rem; font-weight: 700; color: #D97706; text-transform: uppercase; letter-spacing: 0.08em; }
.s8-channel-num { font-family: var(--font-heading); font-size: 1.55rem; font-weight: 800; color: var(--color-text); line-height: 1; }
.s8-channel-num-accent { font-family: var(--font-heading); font-size: 1.55rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s8-channel-num-warm { font-family: var(--font-heading); font-size: 1.55rem; font-weight: 800; color: #D97706; line-height: 1; }
.s8-channel-result { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); margin-top: 3px; line-height: 1.35; }
.s8-channel-result-accent { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-accent); margin-top: 3px; line-height: 1.35; font-weight: 600; }
.s8-channel-result-warm { font-family: var(--font-body); font-size: 0.75rem; color: #D97706; margin-top: 3px; line-height: 1.35; font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — CTA Warm — bg-accent — Приоритеты Q2 -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-bg-grad"></div>
    <div class="s9-glow-tl"></div>
    <div class="s9-glow-br"></div>
    <div class="s9-dots"></div>
  </div>
  <div class="s9-content">
    <span class="s9-eyebrow">Следующий шаг</span>
    <h1 class="s9-heading">Приоритеты Q2 — видео и<br>AI-персонализация</h1>
    <div class="s9-steps">
      <div class="s9-step">
        <div class="s9-step-num">01</div>
        <div class="s9-step-body">
          <span class="s9-step-title">YouTube-канал</span>
          <span class="s9-step-desc">12 экспертных видео в месяц</span>
        </div>
      </div>
      <div class="s9-step">
        <div class="s9-step-num">02</div>
        <div class="s9-step-body">
          <span class="s9-step-title">AI-персонализация главной</span>
          <span class="s9-step-desc">Динамические сегменты, цель: конверсия 5,5%</span>
        </div>
      </div>
      <div class="s9-step s9-step-warm">
        <div class="s9-step-num-warm">03</div>
        <div class="s9-step-body">
          <span class="s9-step-title">CAC &lt; 750 ₽</span>
          <span class="s9-step-desc">Запрашиваемый бюджет: 14,2 млн ₽ (+15%)</span>
        </div>
      </div>
    </div>
    <div class="s9-metrics">
      <div class="s9-metric">
        <span class="s9-m-num">5,5%</span>
        <span class="s9-m-lbl">целевая конверсия</span>
      </div>
      <div class="s9-sep">·</div>
      <div class="s9-metric">
        <span class="s9-m-num">&lt;750 ₽</span>
        <span class="s9-m-lbl">целевой CAC</span>
      </div>
      <div class="s9-sep">·</div>
      <div class="s9-metric">
        <span class="s9-m-num">14,2 млн</span>
        <span class="s9-m-lbl">бюджет Q2</span>
      </div>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; }
.s9-bg-grad { position: absolute; inset: 0; background: linear-gradient(145deg, var(--bg-accent) 0%, color-mix(in srgb, var(--bg-accent) 70%, #000000) 100%); }
.s9-glow-tl { position: absolute; top: -100px; left: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-glow-br { position: absolute; bottom: -80px; right: -80px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-dots { position: absolute; top: 36px; right: 56px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 52px 100px; }
.s9-eyebrow { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.70); font-weight: 600; font-family: var(--font-heading); margin-bottom: 14px; }
.s9-heading { font-family: var(--font-heading); font-size: 3.0rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.15; text-align: center; letter-spacing: -0.01em; }
.s9-steps { display: flex; flex-direction: column; gap: 10px; width: 100%; max-width: 640px; margin-bottom: 28px; }
.s9-step { display: flex; align-items: center; gap: 20px; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.22); border-radius: 14px; padding: 14px 22px; text-align: left; }
.s9-step-warm { background: rgba(217,119,6,0.20); border: 1.5px solid rgba(217,119,6,0.45); }
.s9-step-num { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: rgba(255,255,255,0.50); line-height: 1; min-width: 32px; }
.s9-step-num-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; min-width: 32px; }
.s9-step-body { display: flex; flex-direction: column; gap: 3px; }
.s9-step-title { font-family: var(--font-heading); font-size: 0.95rem; font-weight: 700; color: #FFFFFF; }
.s9-step-desc { font-family: var(--font-body); font-size: 0.78rem; color: rgba(255,255,255,0.65); line-height: 1.35; }
.s9-metrics { display: flex; align-items: center; gap: 24px; }
.s9-metric { display: flex; flex-direction: column; align-items: center; gap: 3px; }
.s9-m-num { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #FFFFFF; line-height: 1; }
.s9-m-lbl { font-family: var(--font-body); font-size: 0.72rem; color: rgba(255,255,255,0.60); text-transform: uppercase; letter-spacing: 0.1em; }
.s9-sep { font-size: 1.5rem; color: rgba(255,255,255,0.25); line-height: 1; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
