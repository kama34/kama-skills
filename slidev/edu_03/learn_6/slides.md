---
theme: default
layout: none
title: TechTalk — онлайн-школа английского для IT
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
      <span class="s1-label">Английский для IT · Series A · 2026</span>
    </div>
    <h1 class="s1-heading">TechTalk</h1>
    <p class="s1-sub">Английский, который открывает двери в глобальный IT</p>
    <div class="s1-meta">
      <span>Pitch Deck</span>
      <span class="s1-dot">·</span>
      <span>Раунд A</span>
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
<!-- SLIDE 2 — Stat Hero (left-number-right-text) — bg-base — 83% теряют офферы -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow-left"></div>
    <div class="s2-dots"></div>
  </div>
  <div class="s2-content">
    <div class="s2-left">
      <span class="s2-label">Проблема рынка</span>
      <div class="s2-hero">83%</div>
      <div class="s2-caption">российских разработчиков теряют зарубежные офферы из-за слабого английского</div>
    </div>
    <div class="s2-divider"></div>
    <div class="s2-right">
      <h1 class="s2-heading">Языковой барьер стоит карьеры и денег</h1>
      <div class="s2-stats">
        <div class="s2-stat">
          <div class="s2-stat-icon">
            <Icon name="trending-up" :size="20" color="var(--color-accent)" />
          </div>
          <div class="s2-stat-body">
            <span class="s2-stat-val">+65%</span>
            <span class="s2-stat-txt">разница в зарплате для свободно говорящих специалистов</span>
          </div>
        </div>
        <div class="s2-stat">
          <div class="s2-stat-icon">
            <Icon name="globe" :size="20" color="var(--color-accent)" />
          </div>
          <div class="s2-stat-body">
            <span class="s2-stat-val">92%</span>
            <span class="s2-stat-txt">документации и Stack Overflow — на английском</span>
          </div>
        </div>
        <div class="s2-stat s2-stat-warm">
          <div class="s2-stat-icon-warm">
            <Icon name="user-check" :size="20" color="#D97706" />
          </div>
          <div class="s2-stat-body">
            <span class="s2-stat-val-warm">4 из 5</span>
            <span class="s2-stat-txt">зарубежных компаний требуют B2+ на собеседовании</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s2-root { position: absolute; inset: 0; overflow: hidden; }
.s2-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s2-glow-left { position: absolute; left: -100px; top: 50%; transform: translateY(-50%); width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s2-dots { position: absolute; top: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s2-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 2px 3fr; padding: 44px 64px; gap: 32px; align-items: center; }
.s2-left { display: flex; flex-direction: column; justify-content: center; gap: 12px; }
.s2-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; }
.s2-hero { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-caption { font-family: var(--font-body); font-size: 0.92rem; color: var(--color-muted); line-height: 1.5; max-width: 260px; }
.s2-divider { width: 2px; background: var(--color-surface-border); align-self: stretch; border-radius: 2px; }
.s2-right { display: flex; flex-direction: column; justify-content: center; }
.s2-heading { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-text); margin: 0 0 22px; line-height: 1.25; }
.s2-stats { display: flex; flex-direction: column; gap: 12px; }
.s2-stat { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 14px; }
.s2-stat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-stat-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-stat-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s2-stat-body { display: flex; flex-direction: column; gap: 2px; }
.s2-stat-val { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-stat-val-warm { font-family: var(--font-heading); font-size: 1.4rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-stat-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Two-Col Text — bg-alt — Почему общие курсы не работают -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-glow"></div>
    <div class="s3-dots"></div>
  </div>
  <div class="s3-content">
    <span class="s3-label">Провал существующих решений</span>
    <h1 class="s3-heading">70% бросают общие курсы английского до уровня B1</h1>
    <div class="s3-grid">
      <div class="s3-col">
        <div class="s3-col-header">
          <div class="s3-col-icon">
            <Icon name="book" :size="20" color="var(--color-accent)" />
          </div>
          <span class="s3-col-title">Общие курсы английского</span>
        </div>
        <div class="s3-rows">
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-bad">✕</span>
            <span class="s3-row-txt">Нерелевантные темы: «мой отпуск», «в ресторане»</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-bad">✕</span>
            <span class="s3-row-txt">Нет практики технических собеседований и стендапов</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-bad">✕</span>
            <span class="s3-row-txt">Групповые занятия по 20 человек — 3 минуты на ученика</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-bad">✕</span>
            <span class="s3-row-txt">12+ месяцев до B2 — слишком долго для карьерных целей</span>
          </div>
        </div>
      </div>
      <div class="s3-col s3-col-accent">
        <div class="s3-col-header">
          <div class="s3-col-icon-accent">
            <Icon name="code" :size="20" color="var(--color-accent)" />
          </div>
          <span class="s3-col-title">TechTalk</span>
        </div>
        <div class="s3-rows">
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-good">✓</span>
            <span class="s3-row-txt">Реальные IT-ситуации: код-ревью, дейли, документация</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-good">✓</span>
            <span class="s3-row-txt">Симуляции интервью в Google, Meta, Stripe</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-good">✓</span>
            <span class="s3-row-txt">AI-тьютор для индивидуальной практики 24/7</span>
          </div>
          <div class="s3-row">
            <span class="s3-row-mark s3-row-mark-good">✓</span>
            <span class="s3-row-txt">A2 → B2 за 6 месяцев при 30 минутах в день</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s3-root { position: absolute; inset: 0; overflow: hidden; }
.s3-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s3-glow { position: absolute; top: -80px; right: -80px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s3-dots { position: absolute; bottom: 30px; left: 30px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s3-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s3-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s3-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s3-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; align-content: stretch; }
.s3-col { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 22px 24px; display: flex; flex-direction: column; gap: 16px; }
.s3-col-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s3-col-header { display: flex; align-items: center; gap: 12px; }
.s3-col-icon { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-col-icon-accent { width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.7); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-col-title { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-text); }
.s3-rows { display: flex; flex-direction: column; gap: 10px; }
.s3-row { display: flex; align-items: flex-start; gap: 10px; }
.s3-row-mark { font-size: 0.85rem; font-weight: 700; flex-shrink: 0; line-height: 1.4; }
.s3-row-mark-bad { color: #DC2626; }
.s3-row-mark-good { color: var(--color-accent); }
.s3-row-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Icon Trio 2×2 (rounded-square containers) — bg-base — 4 метода TechTalk -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <span class="s4-label">Методология TechTalk</span>
    <h1 class="s4-heading">Обучение на реальных рабочих ситуациях IT-специалиста</h1>
    <div class="s4-grid">
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="code" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Code Review</span>
        <span class="s4-desc">Объясняем архитектурные решения и пишем PR-комментарии на английском</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="mic" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Mock Interview</span>
        <span class="s4-desc">Симуляции технических интервью по стандартам Google, Meta и Stripe</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="clock" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Daily Standup</span>
        <span class="s4-desc">Симулятор дейли-стендапов — 15 минут практики каждый день</span>
      </div>
      <div class="s4-item s4-item-warm">
        <div class="s4-icon-warm">
          <Icon name="book-open" :size="26" color="#D97706" />
        </div>
        <span class="s4-title">Docs & RFC</span>
        <span class="s4-desc">Чтение и обсуждение реальной технической документации и RFC</span>
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
.s4-heading { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; }
.s4-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-content: stretch; }
.s4-item { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 24px 28px; display: flex; flex-direction: column; align-items: flex-start; gap: 8px; }
.s4-item-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s4-icon { width: 52px; height: 52px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s4-icon-warm { width: 52px; height: 52px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.s4-title { font-family: var(--font-heading); font-size: 1.15rem; font-weight: 700; color: var(--color-text); }
.s4-desc { font-family: var(--font-body); font-size: 0.84rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Stat Hero (split-50-50) — bg-base — A2→B2 за 6 месяцев + AI -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow-center"></div>
    <div class="s5-arc-outer"></div>
    <div class="s5-arc-inner"></div>
    <div class="s5-dots"></div>
  </div>
  <div class="s5-content">
    <span class="s5-label">Результаты обучения</span>
    <div class="s5-split">
      <div class="s5-left">
        <div class="s5-hero">6 мес.</div>
        <p class="s5-hero-caption">от A2 до B2 при 30 минутах в день</p>
        <div class="s5-compare">
          <div class="s5-compare-item s5-compare-bad">
            <span class="s5-compare-label">Традиционные школы</span>
            <span class="s5-compare-val">12+ мес.</span>
          </div>
          <div class="s5-compare-item s5-compare-good">
            <span class="s5-compare-label">TechTalk</span>
            <span class="s5-compare-val-good">6 мес.</span>
          </div>
        </div>
      </div>
      <div class="s5-divider"></div>
      <div class="s5-right">
        <h1 class="s5-heading">AI-тьютор + персональная программа под ваш стек</h1>
        <div class="s5-features">
          <div class="s5-feat">
            <div class="s5-feat-icon">
              <Icon name="brain" :size="18" color="var(--color-accent)" />
            </div>
            <span class="s5-feat-txt">AI-тьютор доступен 24/7 для разговорной практики</span>
          </div>
          <div class="s5-feat">
            <div class="s5-feat-icon">
              <Icon name="layers" :size="18" color="var(--color-accent)" />
            </div>
            <span class="s5-feat-txt">Персональная программа на основе вашего стека: Python, JS, Go...</span>
          </div>
          <div class="s5-feat s5-feat-warm">
            <div class="s5-feat-icon-warm">
              <Icon name="trending-up" :size="18" color="#D97706" />
            </div>
            <span class="s5-feat-txt">2–3 языковых уровня за 6 месяцев — подтверждено сертификатами</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s5-glow-center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 560px; height: 560px; background: radial-gradient(circle, rgba(13,148,136,0.10) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-arc-outer { position: absolute; top: 50%; left: 28%; transform: translate(-50%, -50%); width: 340px; height: 340px; border: 1.5px solid rgba(13,148,136,0.14); border-radius: 50%; pointer-events: none; }
.s5-arc-inner { position: absolute; top: 50%; left: 28%; transform: translate(-50%, -50%); width: 220px; height: 220px; border: 1px solid rgba(13,148,136,0.08); border-radius: 50%; pointer-events: none; }
.s5-dots { position: absolute; bottom: 30px; right: 40px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 16px; align-self: flex-start; }
.s5-split { flex: 1; display: grid; grid-template-columns: 1fr 2px 1fr; gap: 32px; align-items: center; }
.s5-left { display: flex; flex-direction: column; justify-content: center; align-items: flex-start; gap: 14px; }
.s5-hero { font-family: var(--font-heading); font-size: 5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s5-hero-caption { font-family: var(--font-body); font-size: 0.92rem; color: var(--color-muted); margin: 0; line-height: 1.45; max-width: 220px; }
.s5-compare { display: flex; flex-direction: column; gap: 8px; width: 100%; }
.s5-compare-item { border-radius: 10px; padding: 10px 16px; display: flex; justify-content: space-between; align-items: center; }
.s5-compare-bad { background: rgba(220,38,38,0.06); border: 1px solid rgba(220,38,38,0.18); }
.s5-compare-good { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s5-compare-label { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s5-compare-val { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: #DC2626; }
.s5-compare-val-good { font-family: var(--font-heading); font-size: 1rem; font-weight: 700; color: var(--color-accent); }
.s5-divider { width: 2px; background: var(--color-surface-border); align-self: stretch; border-radius: 2px; }
.s5-right { display: flex; flex-direction: column; justify-content: center; }
.s5-heading { font-family: var(--font-heading); font-size: 1.75rem; font-weight: 700; color: var(--color-text); margin: 0 0 22px; line-height: 1.3; }
.s5-features { display: flex; flex-direction: column; gap: 12px; }
.s5-feat { display: flex; align-items: center; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; }
.s5-feat-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s5-feat-icon { width: 38px; height: 38px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-feat-icon-warm { width: 38px; height: 38px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-feat-txt { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-text); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Bento Grid — bg-alt — Тракция +320% MRR -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-deco-dot"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Тракция · 12 месяцев роста</span>
    <h1 class="s6-heading">+320% рост выручки — от 2 до 8,4 млн ₽ MRR</h1>
    <div class="s6-grid">
      <div class="s6-featured">
        <div class="s6-feat-icon">
          <Icon name="trending-up" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s6-feat-num">+320%</div>
        <div class="s6-feat-label">рост MRR за 12 месяцев</div>
        <div class="s6-feat-sub-grid">
          <div class="s6-sub-item">
            <span class="s6-sub-val">2 млн ₽</span>
            <span class="s6-sub-lbl">MRR старт</span>
          </div>
          <div class="s6-sub-arrow">→</div>
          <div class="s6-sub-item">
            <span class="s6-sub-val-accent">8,4 млн ₽</span>
            <span class="s6-sub-lbl">MRR сейчас</span>
          </div>
        </div>
      </div>
      <div class="s6-side-top">
        <div class="s6-side-icon">
          <Icon name="users" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s6-side-body">
          <span class="s6-side-val">800 → 3 500</span>
          <span class="s6-side-txt">платящих студентов</span>
        </div>
      </div>
      <div class="s6-side-bot">
        <div class="s6-side-icon-warm">
          <Icon name="percent" :size="20" color="#D97706" />
        </div>
        <div class="s6-side-body">
          <span class="s6-side-val-warm">LTV/CAC = 10×</span>
          <span class="s6-side-txt">LTV 42 000 ₽ · CAC 4 200 ₽</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s6-deco-dot { position: absolute; top: 40px; right: 50px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s6-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr; gap: 12px; }
.s6-featured { grid-row: 1 / 3; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s6-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s6-feat-num { font-family: var(--font-heading); font-size: 4.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s6-feat-label { font-family: var(--font-body); font-size: 0.95rem; color: var(--color-muted); margin-top: 6px; line-height: 1.4; }
.s6-feat-sub-grid { display: flex; align-items: center; gap: 12px; margin-top: 20px; }
.s6-sub-item { display: flex; flex-direction: column; gap: 2px; }
.s6-sub-val { font-family: var(--font-heading); font-size: 1.15rem; font-weight: 700; color: var(--color-muted); line-height: 1; }
.s6-sub-val-accent { font-family: var(--font-heading); font-size: 1.15rem; font-weight: 700; color: var(--color-accent); line-height: 1; }
.s6-sub-lbl { font-family: var(--font-body); font-size: 0.7rem; color: var(--color-muted); opacity: 0.7; }
.s6-sub-arrow { font-family: var(--font-heading); font-size: 1.2rem; color: var(--color-accent-dim); font-weight: 700; }
.s6-side-top { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s6-side-bot { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s6-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s6-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s6-side-body { display: flex; flex-direction: column; gap: 2px; }
.s6-side-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s6-side-val-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s6-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Profile Grid — bg-base — Команда (CEO, CTO, Head of Content) -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow-right"></div>
    <div class="s7-dots"></div>
  </div>
  <div class="s7-content">
    <span class="s7-label">Команда</span>
    <h1 class="s7-heading">EdTech-опыт и кремниевый бэкграунд в одной команде</h1>
    <div class="s7-grid">
      <div class="s7-card">
        <div class="s7-avatar">
          <Icon name="user" :size="28" color="var(--color-accent)" />
        </div>
        <div class="s7-card-body">
          <span class="s7-role">CEO</span>
          <span class="s7-name">Экс-продакт Skyeng</span>
          <span class="s7-bio">8 лет в EdTech · 3 запущенных продукта · 500k+ пользователей</span>
        </div>
      </div>
      <div class="s7-card s7-card-accent">
        <div class="s7-avatar s7-avatar-accent">
          <Icon name="cpu" :size="28" color="var(--color-accent)" />
        </div>
        <div class="s7-card-body">
          <span class="s7-role">CTO</span>
          <span class="s7-name">Ex-Google Engineer</span>
          <span class="s7-bio">NLP и Speech Recognition · экс-Google · патенты в AI/ML</span>
        </div>
      </div>
      <div class="s7-card s7-card-warm">
        <div class="s7-avatar s7-avatar-warm">
          <Icon name="book-open" :size="28" color="#D97706" />
        </div>
        <div class="s7-card-body">
          <span class="s7-role">Head of Content</span>
          <span class="s7-name">CELTA-методист</span>
          <span class="s7-bio">CELTA-сертификат · 5 лет в IT-компаниях · разработала 12 IT-курсов</span>
        </div>
      </div>
    </div>
    <div class="s7-footer">
      <div class="s7-footer-item">
        <Icon name="award" :size="16" color="var(--color-accent)" />
        <span class="s7-footer-txt">Команда ранее привлекла $2M в EdTech-проектах</span>
      </div>
      <div class="s7-footer-item">
        <Icon name="users" :size="16" color="var(--color-accent)" />
        <span class="s7-footer-txt">12 человек в команде, 6 инженеров AI/ML</span>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s7-glow-right { position: absolute; right: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-dots { position: absolute; bottom: 30px; left: 30px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s7-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s7-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: stretch; }
.s7-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 22px 24px; display: flex; align-items: flex-start; gap: 16px; }
.s7-card-accent { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s7-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s7-avatar { width: 56px; height: 56px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-avatar-accent { background: rgba(255,255,255,0.65); border: 1.5px solid var(--color-accent-dim); }
.s7-avatar-warm { background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); }
.s7-card-body { display: flex; flex-direction: column; gap: 4px; }
.s7-role { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); }
.s7-name { font-family: var(--font-heading); font-size: 1.05rem; font-weight: 700; color: var(--color-text); line-height: 1.2; }
.s7-bio { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.45; margin-top: 2px; }
.s7-footer { display: flex; align-items: center; gap: 28px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s7-footer-item { display: flex; align-items: center; gap: 8px; }
.s7-footer-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Data Spotlight — bg-alt — Рынок 28 млрд ₽ к 2027 -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow"></div>
    <div class="s8-dots"></div>
  </div>
  <div class="s8-content">
    <span class="s8-label">Рыночная возможность</span>
    <h1 class="s8-heading">EdTech для IT-специалистов — 28 млрд ₽ к 2027 году</h1>
    <div class="s8-grid">
      <div class="s8-card">
        <div class="s8-card-icon">
          <Icon name="globe" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-card-val">28 млрд ₽</div>
        <div class="s8-card-lbl">рынок EdTech для IT-специалистов РФ к 2027</div>
      </div>
      <div class="s8-card">
        <div class="s8-card-icon">
          <Icon name="users" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s8-card-val">1,8 млн</div>
        <div class="s8-card-lbl">разработчиков в РФ — наша целевая аудитория</div>
      </div>
      <div class="s8-card s8-card-warm">
        <div class="s8-card-icon-warm">
          <Icon name="trending-up" :size="20" color="#D97706" />
        </div>
        <div class="s8-card-val-warm">34%</div>
        <div class="s8-card-lbl">проникновение онлайн-обучения и продолжает расти</div>
      </div>
    </div>
    <div class="s8-insight">
      <div class="s8-insight-icon">
        <Icon name="target" :size="16" color="var(--color-accent)" />
      </div>
      <span class="s8-insight-txt">Конкуренты (Skyeng, Puzzle English) не адресуют IT-нишу — TechTalk занимает незаполненную позицию</span>
    </div>
  </div>
</div>

<style>
.s8-root { position: absolute; inset: 0; overflow: hidden; }
.s8-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s8-glow { position: absolute; top: -80px; right: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s8-dots { position: absolute; bottom: 30px; left: 30px; width: 200px; height: 200px; background-image: radial-gradient(circle, rgba(13,148,136,0.35) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s8-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s8-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s8-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; }
.s8-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: stretch; }
.s8-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 24px; display: flex; flex-direction: column; align-items: flex-start; gap: 10px; }
.s8-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s8-card-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s8-card-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; }
.s8-card-val { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s8-card-val-warm { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: #D97706; line-height: 1; }
.s8-card-lbl { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s8-insight { display: flex; align-items: flex-start; gap: 10px; margin-top: 16px; padding: 14px 18px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; }
.s8-insight-icon { width: 30px; height: 30px; border-radius: 50%; background: var(--color-accent-bg); border: 1px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; }
.s8-insight-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.5; font-style: italic; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 9 — CTA Warm — bg-accent — Раунд A 180 млн ₽ -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg"></div>
  <div class="s9-glow-tl"></div>
  <div class="s9-glow-br"></div>
  <div class="s9-dots"></div>
  <div class="s9-content">
    <span class="s9-sup">TechTalk · Series A · 2026</span>
    <h1 class="s9-heading">Привлекаем 180 млн ₽ на AI-платформу и экспансию в СНГ</h1>
    <div class="s9-allocations">
      <div class="s9-alloc">
        <div class="s9-alloc-num">50%</div>
        <span class="s9-alloc-txt">AI-платформа: speech analysis, adaptive learning</span>
      </div>
      <div class="s9-alloc">
        <div class="s9-alloc-num">30%</div>
        <span class="s9-alloc-txt">Маркетинг и рост до 15 000 студентов</span>
      </div>
      <div class="s9-alloc s9-alloc-warm">
        <div class="s9-alloc-num-warm">20%</div>
        <span class="s9-alloc-txt">Экспансия: Казахстан, Узбекистан, Грузия</span>
      </div>
    </div>
    <div class="s9-contact">
      <div class="s9-contact-item">
        <Icon name="mail" :size="16" color="rgba(255,255,255,0.8)" />
        <span class="s9-contact-txt">invest@techtalk.school</span>
      </div>
      <span class="s9-contact-dot">·</span>
      <div class="s9-contact-item">
        <Icon name="globe" :size="16" color="rgba(255,255,255,0.8)" />
        <span class="s9-contact-txt">techtalk.school</span>
      </div>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: linear-gradient(145deg, var(--color-accent) 0%, color-mix(in srgb, var(--color-accent) 70%, black) 100%); }
.s9-glow-tl { position: absolute; top: -100px; left: -100px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; z-index: 0; }
.s9-glow-br { position: absolute; bottom: -80px; right: -80px; width: 420px; height: 420px; background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 65%); border-radius: 50%; pointer-events: none; z-index: 0; }
.s9-dots { position: absolute; bottom: 44px; right: 60px; width: 260px; height: 260px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; z-index: 0; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s9-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.75); font-weight: 600; margin-bottom: 18px; }
.s9-heading { font-family: var(--font-heading); font-size: 2.5rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.15; max-width: 800px; }
.s9-allocations { display: flex; gap: 14px; margin-bottom: 36px; }
.s9-alloc { background: rgba(255,255,255,0.14); border: 1.5px solid rgba(255,255,255,0.28); border-radius: 14px; padding: 18px 24px; display: flex; flex-direction: column; align-items: center; gap: 8px; min-width: 180px; }
.s9-alloc-warm { background: rgba(217,119,6,0.25); border: 1.5px solid rgba(217,119,6,0.55); }
.s9-alloc-num { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: #FFFFFF; line-height: 1; }
.s9-alloc-num-warm { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: #FDE68A; line-height: 1; }
.s9-alloc-txt { font-family: var(--font-body); font-size: 0.78rem; color: rgba(255,255,255,0.78); line-height: 1.4; text-align: center; }
.s9-contact { display: flex; align-items: center; gap: 18px; }
.s9-contact-item { display: flex; align-items: center; gap: 8px; }
.s9-contact-txt { font-family: var(--font-body); font-size: 0.95rem; color: rgba(255,255,255,0.85); font-weight: 500; }
.s9-contact-dot { color: rgba(255,255,255,0.35); font-size: 1.2rem; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
