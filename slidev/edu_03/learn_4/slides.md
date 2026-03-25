---
theme: default
layout: none
title: FitCorp — корпоративный wellness
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
      <span class="s1-label">Корпоративный wellness · 2026</span>
    </div>
    <h1 class="s1-heading">FitCorp</h1>
    <p class="s1-sub">Здоровый сотрудник = прибыльная компания</p>
    <div class="s1-meta">
      <span>Программа корпоративного wellness</span>
      <span class="s1-dot">·</span>
      <span>HR-презентация</span>
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
<!-- SLIDE 2 — Stat Hero (centered) — bg-base — 1,5 трлн ₽ потери -->
<!-- ============================================================ -->

<div class="s2-root">
  <div class="s2-bg">
    <div class="s2-glow"></div>
    <div class="s2-arc"></div>
  </div>
  <div class="s2-content">
    <span class="s2-label">Цена выгорания для бизнеса</span>
    <div class="s2-hero">1,5 трлн ₽</div>
    <p class="s2-caption">ежегодные потери российского бизнеса</p>
    <div class="s2-pills">
      <span class="s2-pill">
        <span class="s2-pill-num">67%</span>
        <span class="s2-pill-txt">хроническая усталость офисных сотрудников</span>
      </span>
      <span class="s2-pill s2-pill-warm">
        <span class="s2-pill-num-warm">+23%</span>
        <span class="s2-pill-txt">рост больничных за 3 года</span>
      </span>
      <span class="s2-pill">
        <span class="s2-pill-num">28%</span>
        <span class="s2-pill-txt">увольнений из-за стресса</span>
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
.s2-hero { font-family: var(--font-heading); font-size: 5.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; margin: 0; }
.s2-caption { font-family: var(--font-body); font-size: 1.2rem; color: var(--color-muted); margin: 10px 0 32px; }
.s2-pills { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
.s2-pill { display: flex; flex-direction: column; align-items: center; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 14px 24px; min-width: 150px; }
.s2-pill-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s2-pill-num { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s2-pill-num-warm { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: #D97706; line-height: 1; }
.s2-pill-txt { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); margin-top: 4px; text-align: center; max-width: 140px; line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 3 — Bento Grid — bg-alt — ROI 3,2₽ на каждый вложенный 1₽ -->
<!-- ============================================================ -->

<div class="s3-root">
  <div class="s3-bg">
    <div class="s3-deco-dot"></div>
  </div>
  <div class="s3-content">
    <span class="s3-label">Экономическая эффективность wellness</span>
    <h1 class="s3-heading">Каждый рубль в wellness возвращает 3,2 ₽</h1>
    <div class="s3-grid">
      <div class="s3-featured">
        <div class="s3-feat-icon">
          <Icon name="trending-up" :size="24" color="var(--color-accent)" />
        </div>
        <div class="s3-feat-num">3,2 ₽</div>
        <div class="s3-feat-label">возврат на каждый вложенный рубль</div>
        <div class="s3-feat-source">Deloitte Global Wellness Survey, 2025</div>
      </div>
      <div class="s3-side-top">
        <div class="s3-side-icon">
          <Icon name="trending-down" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s3-side-val">−25%</span>
          <span class="s3-side-txt">снижение абсентеизма</span>
        </div>
      </div>
      <div class="s3-side-mid">
        <div class="s3-side-icon">
          <Icon name="zap" :size="20" color="var(--color-accent)" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s3-side-val">+18%</span>
          <span class="s3-side-txt">рост продуктивности</span>
        </div>
      </div>
      <div class="s3-side-bot">
        <div class="s3-side-icon-warm">
          <Icon name="users" :size="20" color="#D97706" />
        </div>
        <div style="display:flex;flex-direction:column;gap:2px;">
          <span class="s3-side-val-warm">−32%</span>
          <span class="s3-side-txt">снижение текучести кадров</span>
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
.s3-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 16px; }
.s3-grid { flex: 1; display: grid; grid-template-columns: 1.2fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 12px; }
.s3-featured { grid-row: 1 / 4; background: linear-gradient(135deg, rgba(13,148,136,0.12), var(--color-surface)); border: 1.5px solid var(--color-accent-dim); border-radius: 14px; padding: 28px; display: flex; flex-direction: column; justify-content: center; }
.s3-feat-icon { width: 52px; height: 52px; border-radius: 50%; background: rgba(13,148,136,0.12); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; }
.s3-feat-num { font-family: var(--font-heading); font-size: 4.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-feat-label { font-family: var(--font-body); font-size: 1rem; color: var(--color-muted); margin-top: 8px; line-height: 1.4; }
.s3-feat-source { font-family: var(--font-body); font-size: 0.7rem; color: var(--color-muted); margin-top: 12px; opacity: 0.7; }
.s3-side-top, .s3-side-mid { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s3-side-bot { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 16px 20px; display: flex; align-items: center; gap: 14px; }
.s3-side-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-side-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s3-side-val { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s3-side-val-warm { font-family: var(--font-heading); font-size: 1.6rem; font-weight: 800; color: #D97706; line-height: 1; }
.s3-side-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 4 — Icon Trio 2×2 — bg-base — 4 модуля платформы -->
<!-- ============================================================ -->

<div class="s4-root">
  <div class="s4-bg">
    <div class="s4-glow"></div>
  </div>
  <div class="s4-content">
    <span class="s4-label">Платформа FitCorp</span>
    <h1 class="s4-heading">Четыре модуля — от физической формы до ментального здоровья</h1>
    <div class="s4-grid">
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="zap" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Move</span>
        <span class="s4-desc">Тренировки, шаговые челленджи, спортивные секции</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="moon" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Mind</span>
        <span class="s4-desc">Медитации, практики осознанности, sleep-программы</span>
      </div>
      <div class="s4-item">
        <div class="s4-icon">
          <Icon name="leaf" :size="26" color="var(--color-accent)" />
        </div>
        <span class="s4-title">Nutrition</span>
        <span class="s4-desc">Персональные планы питания, корпоративные обеды</span>
      </div>
      <div class="s4-item s4-item-warm">
        <div class="s4-icon-warm">
          <Icon name="shield" :size="26" color="#D97706" />
        </div>
        <span class="s4-title">Balance</span>
        <span class="s4-desc">Консультации психолога, управление стрессом</span>
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
.s4-title { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; color: var(--color-text); }
.s4-desc { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); line-height: 1.45; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 5 — Asymmetric Split — bg-alt — Платформа (описание) -->
<!-- ============================================================ -->

<div class="s5-root">
  <div class="s5-bg">
    <div class="s5-glow-left"></div>
    <div class="s5-dot-grid"></div>
  </div>
  <div class="s5-content">
    <div class="s5-left">
      <div class="s5-visual">
        <div class="s5-big-icon">
          <Icon name="smartphone" :size="52" color="var(--color-accent)" />
        </div>
        <span class="s5-visual-label">Мобильное приложение</span>
      </div>
    </div>
    <div class="s5-right">
      <span class="s5-label">FitCorp — всё в одном</span>
      <h1 class="s5-heading">Платформа, которая объединяет все форматы заботы о команде</h1>
      <div class="s5-features">
        <div class="s5-feat">
          <div class="s5-feat-icon">
            <Icon name="activity" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s5-feat-txt">Трекер активности и онлайн-тренировки</span>
        </div>
        <div class="s5-feat">
          <div class="s5-feat-icon">
            <Icon name="gamepad" :size="18" color="var(--color-accent)" />
          </div>
          <span class="s5-feat-txt">Корпоративные челленджи и геймификация</span>
        </div>
        <div class="s5-feat">
          <div class="s5-feat-icon-warm">
            <Icon name="plus-square" :size="18" color="#D97706" />
          </div>
          <span class="s5-feat-txt">Интеграция с ДМС и психологической поддержкой</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5-root { position: absolute; inset: 0; overflow: hidden; }
.s5-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s5-glow-left { position: absolute; left: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.14) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s5-dot-grid { position: absolute; bottom: 30px; left: 30px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.38) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s5-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 3fr; padding: 44px 64px; gap: 40px; align-items: center; }
.s5-left { display: flex; justify-content: center; align-items: center; }
.s5-visual { display: flex; flex-direction: column; align-items: center; gap: 16px; }
.s5-big-icon { width: 140px; height: 140px; border-radius: 28px; background: var(--color-accent-bg); border: 2px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s5-visual-label { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
.s5-right { display: flex; flex-direction: column; justify-content: center; }
.s5-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 10px; align-self: flex-start; }
.s5-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s5-features { display: flex; flex-direction: column; gap: 12px; }
.s5-feat { display: flex; align-items: center; gap: 14px; background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; }
.s5-feat-icon { width: 38px; height: 38px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-feat-icon-warm { width: 38px; height: 38px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s5-feat-txt { font-family: var(--font-body); font-size: 0.88rem; color: var(--color-text); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 6 — Timeline Horizontal — bg-base — 3 недели до запуска -->
<!-- ============================================================ -->

<div class="s6-root">
  <div class="s6-bg">
    <div class="s6-glow"></div>
  </div>
  <div class="s6-content">
    <span class="s6-label">Запуск программы</span>
    <h1 class="s6-heading">3 недели от решения до первого челленджа</h1>
    <div class="s6-grid">
      <div class="s6-week s6-week-1">
        <span class="s6-week-badge">Неделя 1</span>
        <span class="s6-week-title">Аудит и настройка</span>
        <span class="s6-week-body">Аудит здоровья команды, настройка платформы под специфику компании</span>
      </div>
      <div class="s6-week s6-week-2">
        <span class="s6-week-badge">Неделя 2</span>
        <span class="s6-week-title">Онбординг</span>
        <span class="s6-week-body">Регистрация сотрудников, старт базовых активностей, обучение руководителей</span>
      </div>
      <div class="s6-week s6-week-3">
        <span class="s6-week-badge">Неделя 3</span>
        <span class="s6-week-title">Первый челлендж</span>
        <span class="s6-week-body">Запуск корпоративного челленджа, первые метрики вовлечённости</span>
      </div>
    </div>
    <div class="s6-footer">
      <div class="s6-milestone">
        <Icon name="check-circle" :size="16" color="var(--color-accent)" />
        <span class="s6-mile-txt">Персональный менеджер с первого дня</span>
      </div>
      <div class="s6-milestone">
        <Icon name="check-circle" :size="16" color="var(--color-accent)" />
        <span class="s6-mile-txt">Техподдержка 24/7</span>
      </div>
      <div class="s6-milestone">
        <Icon name="check-circle" :size="16" color="#D97706" />
        <span class="s6-mile-txt-warm">Гарантия результата: 78%+ вовлечённость за 30 дней</span>
      </div>
    </div>
  </div>
</div>

<style>
.s6-root { position: absolute; inset: 0; overflow: hidden; }
.s6-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s6-glow { position: absolute; top: -100px; left: -100px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.11) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s6-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s6-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s6-heading { font-family: var(--font-heading); font-size: 2rem; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.s6-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-items: stretch; }
.s6-week { border-radius: 14px; padding: 22px 24px; display: flex; flex-direction: column; gap: 8px; }
.s6-week-1 { background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s6-week-2 { background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); }
.s6-week-3 { background: var(--color-surface); border: 1px solid var(--color-surface-border); }
.s6-week-badge { font-family: var(--font-heading); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; color: var(--color-accent); }
.s6-week-title { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 700; color: var(--color-text); }
.s6-week-body { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.45; }
.s6-footer { display: flex; align-items: center; gap: 28px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s6-milestone { display: flex; align-items: center; gap: 8px; }
.s6-mile-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s6-mile-txt-warm { font-family: var(--font-body); font-size: 0.78rem; color: #D97706; font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 7 — Stat Hero (left-number-right-text) — bg-alt — Кейс Альфа-Банк -->
<!-- ============================================================ -->

<div class="s7-root">
  <div class="s7-bg">
    <div class="s7-glow-right"></div>
    <div class="s7-dot"></div>
  </div>
  <div class="s7-content">
    <div class="s7-left">
      <span class="s7-label">Кейс реального внедрения</span>
      <div class="s7-case-name">«Альфа-Банк»</div>
      <div class="s7-case-sub">2 000 сотрудников · 6 месяцев</div>
      <div class="s7-economy">
        <span class="s7-econ-val">45 млн ₽</span>
        <span class="s7-econ-txt">экономический эффект за первый год</span>
      </div>
    </div>
    <div class="s7-divider"></div>
    <div class="s7-right">
      <h1 class="s7-heading">Результаты за 6 месяцев превзошли ожидания</h1>
      <div class="s7-metrics">
        <div class="s7-metric">
          <div class="s7-met-icon">
            <Icon name="users" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s7-met-val">78%</span>
            <span class="s7-met-txt">активных пользователей платформы</span>
          </div>
        </div>
        <div class="s7-metric">
          <div class="s7-met-icon">
            <Icon name="trending-down" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s7-met-val">−31%</span>
            <span class="s7-met-txt">снижение количества больничных дней</span>
          </div>
        </div>
        <div class="s7-metric s7-metric-warm">
          <div class="s7-met-icon-warm">
            <Icon name="trending-up" :size="20" color="#D97706" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s7-met-val-warm">24 → 52</span>
            <span class="s7-met-txt">рост eNPS сотрудников</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s7-root { position: absolute; inset: 0; overflow: hidden; }
.s7-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-alt); }
.s7-glow-right { position: absolute; right: -100px; top: 50%; transform: translateY(-50%); width: 460px; height: 460px; background: radial-gradient(circle, rgba(13,148,136,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s7-dot { position: absolute; top: 40px; right: 50px; width: 220px; height: 220px; background-image: radial-gradient(circle, rgba(13,148,136,0.32) 1.5px, transparent 1.5px); background-size: 22px 22px; pointer-events: none; }
.s7-content { position: absolute; inset: 0; z-index: 1; display: grid; grid-template-columns: 2fr 2px 3fr; padding: 44px 64px; gap: 32px; align-items: center; }
.s7-left { display: flex; flex-direction: column; justify-content: center; gap: 12px; }
.s7-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); align-self: flex-start; }
.s7-case-name { font-family: var(--font-heading); font-size: 3.2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-case-sub { font-family: var(--font-body); font-size: 0.85rem; color: var(--color-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; }
.s7-economy { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); border-radius: 14px; padding: 14px 18px; display: flex; flex-direction: column; gap: 4px; margin-top: 8px; }
.s7-econ-val { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 800; color: #D97706; line-height: 1; }
.s7-econ-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); }
.s7-divider { width: 2px; background: var(--color-surface-border); align-self: stretch; border-radius: 2px; }
.s7-right { display: flex; flex-direction: column; justify-content: center; }
.s7-heading { font-family: var(--font-heading); font-size: 1.8rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; line-height: 1.25; }
.s7-metrics { display: flex; flex-direction: column; gap: 12px; }
.s7-metric { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 12px; padding: 14px 18px; display: flex; align-items: center; gap: 14px; }
.s7-metric-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s7-met-icon { width: 40px; height: 40px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-met-icon-warm { width: 40px; height: 40px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s7-met-val { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s7-met-val-warm { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 800; color: #D97706; line-height: 1; }
.s7-met-txt { font-family: var(--font-body); font-size: 0.78rem; color: var(--color-muted); line-height: 1.35; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 8 — Section Divider — bg-alt — Тарифы и условия -->
<!-- ============================================================ -->

<div class="s8-root">
  <div class="s8-bg">
    <div class="s8-glow"></div>
    <div class="s8-arc-outer"></div>
    <div class="s8-arc-inner"></div>
  </div>
  <div class="s8-content">
    <span class="s8-sup">FitCorp · Ценовые планы</span>
    <h1 class="s8-heading">Тарифы и условия</h1>
    <p class="s8-sub">Прозрачные тарифы для команд любого размера — от стартапа до корпорации</p>
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
<!-- SLIDE 9 — Comparison Table — bg-base — 3 тарифа Start/Growth/Enterprise -->
<!-- ============================================================ -->

<div class="s9-root">
  <div class="s9-bg">
    <div class="s9-glow"></div>
  </div>
  <div class="s9-content">
    <span class="s9-label">Ценовые планы</span>
    <h1 class="s9-heading">Три тарифа — от 450 ₽ до 1 200 ₽ за сотрудника в месяц</h1>
    <div class="s9-plans">
      <div class="s9-plan">
        <div class="s9-plan-head">
          <div class="s9-plan-icon">
            <Icon name="zap" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s9-plan-name">Start</span>
            <span class="s9-plan-size">до 100 сотрудников</span>
          </div>
        </div>
        <div class="s9-plan-price">450 ₽ <span class="s9-per">/ чел. в мес.</span></div>
        <span class="s9-plan-modules">Move + базовый Mind</span>
      </div>
      <div class="s9-plan s9-plan-featured">
        <div class="s9-popular-badge">Популярный</div>
        <div class="s9-plan-head">
          <div class="s9-plan-icon">
            <Icon name="star" :size="20" color="var(--color-accent)" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s9-plan-name">Growth</span>
            <span class="s9-plan-size">100–500 сотрудников</span>
          </div>
        </div>
        <div class="s9-plan-price">850 ₽ <span class="s9-per">/ чел. в мес.</span></div>
        <span class="s9-plan-modules">Все 4 модуля платформы</span>
      </div>
      <div class="s9-plan s9-plan-warm">
        <div class="s9-plan-head">
          <div class="s9-plan-icon-warm">
            <Icon name="award" :size="20" color="#D97706" />
          </div>
          <div style="display:flex;flex-direction:column;gap:2px;">
            <span class="s9-plan-name">Enterprise</span>
            <span class="s9-plan-size">500+ сотрудников</span>
          </div>
        </div>
        <div class="s9-plan-price-warm">1 200 ₽ <span class="s9-per-warm">/ чел. в мес.</span></div>
        <span class="s9-plan-modules">Все модули + индивидуальная настройка + аналитика</span>
      </div>
    </div>
  </div>
</div>

<style>
.s9-root { position: absolute; inset: 0; overflow: hidden; }
.s9-bg { position: absolute; inset: 0; z-index: 0; background: var(--bg-base); }
.s9-glow { position: absolute; bottom: -80px; left: -80px; width: 480px; height: 480px; background: radial-gradient(circle, rgba(13,148,136,0.12) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.s9-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; padding: 44px 64px; }
.s9-label { display: inline-flex; align-items: center; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); border-radius: 20px; padding: 6px 18px; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--color-accent); font-weight: 600; line-height: 1; font-family: var(--font-heading); margin-bottom: 8px; align-self: flex-start; }
.s9-heading { font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-text); margin: 0 0 24px; }
.s9-plans { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: stretch; }
.s9-plan { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 24px; display: flex; flex-direction: column; gap: 12px; position: relative; }
.s9-plan-featured { background: var(--color-accent-bg); border: 2px solid var(--color-accent); }
.s9-plan-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.30); }
.s9-popular-badge { position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--color-accent); color: #FFF; font-family: var(--font-heading); font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; padding: 4px 14px; border-radius: 20px; white-space: nowrap; }
.s9-plan-head { display: flex; align-items: center; gap: 12px; }
.s9-plan-icon { width: 44px; height: 44px; border-radius: 12px; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-plan-icon-warm { width: 44px; height: 44px; border-radius: 12px; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.s9-plan-name { font-family: var(--font-heading); font-size: 1.1rem; font-weight: 700; color: var(--color-text); }
.s9-plan-size { font-family: var(--font-body); font-size: 0.75rem; color: var(--color-muted); }
.s9-plan-price { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s9-plan-price-warm { font-family: var(--font-heading); font-size: 2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s9-per { font-family: var(--font-body); font-size: 0.8rem; font-weight: 400; color: var(--color-muted); }
.s9-per-warm { font-family: var(--font-body); font-size: 0.8rem; font-weight: 400; color: var(--color-muted); }
.s9-plan-modules { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 10 — Data Spotlight — bg-alt — ROI-калькулятор -->
<!-- ============================================================ -->

<div class="s10-root">
  <div class="s10-bg">
    <div class="s10-glow"></div>
    <div class="s10-dot"></div>
  </div>
  <div class="s10-content">
    <span class="s10-label">Финансовое обоснование</span>
    <h1 class="s10-heading">ROI-калькулятор: посчитайте экономию для вашей компании</h1>
    <div class="s10-formula">
      <span class="s10-formula-txt">Формула: (снижение больничных × средняя з/п) + (снижение текучести × стоимость найма)</span>
    </div>
    <div class="s10-grid">
      <div class="s10-card">
        <div class="s10-card-icon">
          <Icon name="bar-chart" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s10-card-val">12–18 млн ₽</div>
        <div class="s10-card-lbl">экономия/год для компании 300 чел.</div>
      </div>
      <div class="s10-card">
        <div class="s10-card-icon">
          <Icon name="clock" :size="20" color="var(--color-accent)" />
        </div>
        <div class="s10-card-val">3–4 мес.</div>
        <div class="s10-card-lbl">срок окупаемости программы</div>
      </div>
      <div class="s10-card s10-card-warm">
        <div class="s10-card-icon-warm">
          <Icon name="trending-up" :size="20" color="#D97706" />
        </div>
        <div class="s10-card-val-warm">3,2×</div>
        <div class="s10-card-lbl">ROI — средний показатель клиентов FitCorp</div>
      </div>
    </div>
    <div class="s10-bottom">
      <Icon name="check-circle" :size="16" color="var(--color-accent)" />
      <span class="s10-bottom-txt">Бесплатный расчёт ROI для вашей компании — занимает 15 минут</span>
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
.s10-heading { font-family: var(--font-heading); font-size: 1.9rem; font-weight: 700; color: var(--color-text); margin: 0 0 14px; }
.s10-formula { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 10px; padding: 12px 18px; margin-bottom: 18px; }
.s10-formula-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.45; font-style: italic; }
.s10-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-items: stretch; }
.s10-card { background: var(--color-surface); border: 1px solid var(--color-surface-border); border-radius: 14px; padding: 22px 24px; display: flex; flex-direction: column; align-items: flex-start; gap: 8px; }
.s10-card-warm { background: rgba(217,119,6,0.07); border: 1.5px solid rgba(217,119,6,0.25); }
.s10-card-icon { width: 44px; height: 44px; border-radius: 50%; background: var(--color-accent-bg); border: 1.5px solid var(--color-accent-dim); display: flex; align-items: center; justify-content: center; }
.s10-card-icon-warm { width: 44px; height: 44px; border-radius: 50%; background: rgba(217,119,6,0.10); border: 1.5px solid rgba(217,119,6,0.30); display: flex; align-items: center; justify-content: center; }
.s10-card-val { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: var(--color-accent); line-height: 1; }
.s10-card-val-warm { font-family: var(--font-heading); font-size: 2.2rem; font-weight: 800; color: #D97706; line-height: 1; }
.s10-card-lbl { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-muted); line-height: 1.4; }
.s10-bottom { display: flex; align-items: center; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid var(--color-surface-border); }
.s10-bottom-txt { font-family: var(--font-body); font-size: 0.82rem; color: var(--color-accent); font-weight: 600; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- ============================================================ -->
<!-- SLIDE 11 — CTA Warm — bg-accent — 30-дневный бесплатный пилот -->
<!-- ============================================================ -->

<div class="s11-root">
  <div class="s11-bg"></div>
  <div class="s11-glow-tl"></div>
  <div class="s11-glow-br"></div>
  <div class="s11-dots"></div>
  <div class="s11-content">
    <span class="s11-sup">FitCorp · Специальное предложение</span>
    <h1 class="s11-heading">15 компаний уже в пилоте — присоединяйтесь бесплатно на 30 дней</h1>
    <div class="s11-steps">
      <div class="s11-step">
        <div class="s11-step-num">01</div>
        <span class="s11-step-txt">30 дней, все модули, до 50 сотрудников — полностью бесплатно</span>
      </div>
      <div class="s11-step">
        <div class="s11-step-num">02</div>
        <span class="s11-step-txt">Персональный менеджер и аналитика вовлечённости с первого дня</span>
      </div>
      <div class="s11-step">
        <div class="s11-step-num">03</div>
        <span class="s11-step-txt">ROI-отчёт после пилота — готовое обоснование для руководства</span>
      </div>
    </div>
    <div class="s11-contacts">
      <div class="s11-contact">
        <Icon name="mail" :size="16" color="rgba(255,255,255,0.9)" />
        <span class="s11-contact-txt">pilot@fitcorp.ru</span>
      </div>
      <span class="s11-contact-dot">·</span>
      <div class="s11-contact">
        <Icon name="phone" :size="16" color="rgba(255,255,255,0.9)" />
        <span class="s11-contact-txt">+7 (495) 123-45-67</span>
      </div>
    </div>
  </div>
</div>

<style>
.s11-root { position: absolute; inset: 0; overflow: hidden; }
.s11-bg { position: absolute; inset: 0; z-index: 0; background: linear-gradient(145deg, var(--bg-accent) 0%, #0a7870 100%); }
.s11-glow-tl { position: absolute; top: -120px; left: -120px; width: 520px; height: 520px; background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 65%); border-radius: 50%; z-index: 0; pointer-events: none; }
.s11-glow-br { position: absolute; bottom: -100px; right: -100px; width: 460px; height: 460px; background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 65%); border-radius: 50%; z-index: 0; pointer-events: none; }
.s11-dots { position: absolute; top: 40px; right: 60px; width: 240px; height: 240px; background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px); background-size: 22px 22px; z-index: 0; pointer-events: none; }
.s11-content { position: absolute; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 60px 80px; }
.s11-sup { font-family: var(--font-heading); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.75); font-weight: 600; margin-bottom: 16px; }
.s11-heading { font-family: var(--font-heading); font-size: 2.4rem; font-weight: 800; color: #FFFFFF; margin: 0 0 32px; line-height: 1.2; max-width: 780px; }
.s11-steps { display: flex; flex-direction: column; gap: 12px; max-width: 640px; width: 100%; margin-bottom: 36px; }
.s11-step { display: flex; align-items: center; gap: 16px; background: rgba(255,255,255,0.14); border: 1px solid rgba(255,255,255,0.25); border-radius: 12px; padding: 14px 20px; text-align: left; }
.s11-step-num { font-family: var(--font-heading); font-size: 1.2rem; font-weight: 800; color: rgba(255,255,255,0.5); min-width: 28px; line-height: 1; }
.s11-step-txt { font-family: var(--font-body); font-size: 0.88rem; color: rgba(255,255,255,0.9); line-height: 1.4; }
.s11-contacts { display: flex; align-items: center; gap: 16px; }
.s11-contact { display: flex; align-items: center; gap: 8px; }
.s11-contact-txt { font-family: var(--font-heading); font-size: 1rem; font-weight: 600; color: #FFFFFF; }
.s11-contact-dot { color: rgba(255,255,255,0.4); font-size: 1.2rem; }
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
