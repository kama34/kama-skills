---
theme: default
colorSchema: light
fonts:
  heading: Outfit
  body: DM Sans
  mono: JetBrains Mono
transition: fade
aspectRatio: '16/9'
---

<!-- ============================================================
     SLIDE 1 — Cover  |  bg-accent, white text
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);">
  <!-- Radial glow bottom-right -->
  <div style="position:absolute;bottom:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(255,255,255,0.13),transparent 65%);pointer-events:none;"></div>
  <!-- Dot grid top-right -->
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(255,255,255,0.12) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:56px 72px;">
  <div style="margin-bottom:18px;">
    <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-body);">MedTech Summit 2025</span>
  </div>
  <h1 style="font-family:var(--font-heading);font-size:3.6rem;font-weight:800;color:#fff;line-height:1.1;margin:0 0 18px 0;">Нейросети<br>в медицине</h1>
  <p style="font-family:var(--font-body);font-size:1.4rem;color:rgba(255,255,255,0.85);margin:0;max-width:560px;line-height:1.5;">От диагностики до персонализированного лечения</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 2 — Ключевой факт  |  stat-hero CENTERED, bg-base + dot grid
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:44px 72px;">
  <div style="font-family:var(--font-heading);font-size:8rem;font-weight:800;color:var(--color-accent);line-height:1;">92%</div>
  <div style="font-family:var(--font-body);font-size:1.5rem;color:var(--color-text);margin-top:16px;max-width:520px;line-height:1.4;">радиологов подтверждают: AI повышает точность диагностики</div>
  <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);margin-top:12px;">Lancet, 2024</div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 3 — Проблема  |  bento-grid, bg-base + radial glow
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:18px;align-self:flex-start;">Проблема</span>
  <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;line-height:1.2;">Усталость снижает точность<br>на 30% к концу смены</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:10px;">
      <div style="font-family:var(--font-heading);font-size:2.6rem;font-weight:800;color:var(--color-accent);line-height:1;">50–100</div>
      <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-text);line-height:1.4;">снимков анализирует радиолог за смену</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:10px;">
      <div style="font-family:var(--font-heading);font-size:2.6rem;font-weight:800;color:var(--color-accent);line-height:1;">−30%</div>
      <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-text);line-height:1.4;">точности диагностики к концу смены</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:10px;">
      <div style="font-family:var(--font-heading);font-size:2.6rem;font-weight:800;color:var(--color-accent);line-height:1;">15%</div>
      <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-text);line-height:1.4;">редких патологий пропускается при усталости</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 4 — Секция 1  |  section-divider CENTERED, bg-alt + arc
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.18);border-radius:50%;pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;right:-80px;width:400px;height:400px;border:2px solid rgba(var(--accent-rgb),0.10);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:44px 72px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:24px;">Часть I</span>
  <h2 style="font-family:var(--font-heading);font-size:3rem;font-weight:800;color:var(--color-text);margin:0;line-height:1.2;max-width:600px;">Как AI трансформирует здравоохранение</h2>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 5 — Области применения  |  icon-trio, bg-base + dot grid
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:18px;align-self:flex-start;">Применение</span>
  <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;line-height:1.2;">От снимков до молекул: 4 направления AI</h2>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:14px;align-items:flex-start;">
      <div class="icon-container" style="color:var(--color-accent);">
        <Icon name="brain" :size="26" />
      </div>
      <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Анализ изображений</div>
      <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);line-height:1.4;">КТ, МРТ, рентген</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:14px;align-items:flex-start;">
      <div class="icon-container" style="color:var(--color-accent);">
        <Icon name="chart" :size="26" />
      </div>
      <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Предиктивная аналитика</div>
      <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);line-height:1.4;">Прогноз осложнений</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:14px;align-items:flex-start;">
      <div class="icon-container" style="color:var(--color-accent);">
        <Icon name="target" :size="26" />
      </div>
      <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Персонализация терапии</div>
      <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);line-height:1.4;">Подбор дозировок</div>
    </div>
    <div class="card-solid" style="display:flex;flex-direction:column;gap:14px;align-items:flex-start;">
      <div class="icon-container" style="color:var(--color-accent);">
        <Icon name="dna" :size="26" />
      </div>
      <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Разработка лекарств</div>
      <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);line-height:1.4;">Моделирование молекул</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 6 — Кейс рак лёгких  |  asymmetric-split VISUAL-DOMINANT, bg-alt + radial glow
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:row;align-items:stretch;">
  <!-- Large number left — visual dominant -->
  <div style="flex:0 0 46%;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 40px;border-right:1.5px solid var(--color-surface-border);">
    <div style="font-family:var(--font-heading);font-size:7rem;font-weight:800;color:var(--color-accent);line-height:1;text-align:center;">96.3%</div>
    <div style="font-family:var(--font-body);font-size:1.3rem;color:var(--color-muted);margin-top:10px;text-align:center;">точность AI-модели</div>
    <div style="margin-top:18px;display:flex;align-items:center;gap:10px;">
      <span style="font-family:var(--font-heading);font-size:2rem;font-weight:700;color:var(--color-text);">vs</span>
      <span style="font-family:var(--font-heading);font-size:2.8rem;font-weight:700;color:var(--color-text);">87.1%</span>
    </div>
    <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);margin-top:6px;">у среднего радиолога</div>
  </div>
  <!-- Right content -->
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;padding:44px 48px;gap:22px;">
    <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);align-self:flex-start;">Кейс</span>
    <h2 style="font-family:var(--font-heading);font-size:2rem;font-weight:700;color:var(--color-text);margin:0;line-height:1.2;">Диагностика рака лёгких</h2>
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);flex-shrink:0;width:38px;height:38px;">
          <Icon name="clock" :size="20" />
        </div>
        <div>
          <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">2.4 сек vs 12 мин</div>
          <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-muted);">скорость анализа снимка</div>
        </div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);flex-shrink:0;width:38px;height:38px;">
          <Icon name="chart" :size="20" />
        </div>
        <div>
          <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">+41% ранних выявлений</div>
          <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-muted);">на начальных стадиях</div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 7 — Этические вопросы  |  two-col-text, bg-base + arc
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.18);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:18px;align-self:flex-start;">Этика</span>
  <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;line-height:1.2;">Доверие и ответственность: 4 барьера</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);">
          <Icon name="shield" :size="24" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.3rem;font-weight:600;color:var(--color-text);">Конфиденциальность</div>
      </div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.45;">Данные пациентов требуют особой защиты и деперсонализации</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);">
          <Icon name="target" :size="24" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.3rem;font-weight:600;color:var(--color-text);">Ответственность</div>
      </div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.45;">Кто отвечает за ошибку AI: разработчик, врач или клиника?</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);">
          <Icon name="users" :size="24" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.3rem;font-weight:600;color:var(--color-text);">Доверие врачей</div>
      </div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.45;">Алгоритмам нужна прозрачность — «чёрный ящик» не принимают</div>
    </div>
    <div class="card-solid" style="display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="icon-container" style="color:var(--color-accent);">
          <Icon name="globe" :size="24" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.3rem;font-weight:600;color:var(--color-text);">Регуляторика</div>
      </div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.45;">Разные стандарты одобрения AI в ЕС, США, России</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 8 — Секция 2  |  section-divider CENTERED, bg-alt + dot grid
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:44px 72px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:24px;">Часть II</span>
  <h2 style="font-family:var(--font-heading);font-size:3rem;font-weight:800;color:var(--color-text);margin:0;line-height:1.2;max-width:560px;">Путь к внедрению</h2>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 9 — Этапы интеграции  |  timeline-horizontal, bg-base + radial glow
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:18px;align-self:flex-start;">Интеграция</span>
  <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 32px 0;line-height:1.2;">От данных до масштабирования за 15 месяцев</h2>
  <!-- Timeline horizontal -->
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0;flex:1;position:relative;">
    <!-- connecting line -->
    <div style="position:absolute;top:34px;left:calc(12.5%);right:calc(12.5%);height:2px;background:linear-gradient(to right,var(--color-accent),var(--color-accent-dim));z-index:0;"></div>
    <!-- Step 1 -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:14px;position:relative;z-index:1;">
      <div style="width:68px;height:68px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;color:#fff;font-family:var(--font-heading);font-size:1.6rem;font-weight:800;">1</div>
      <div style="text-align:center;">
        <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Данные</div>
        <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-accent);font-weight:600;margin-top:4px;">6 мес</div>
        <div style="font-family:var(--font-body);font-size:1rem;color:var(--color-muted);margin-top:4px;line-height:1.35;">Сбор и разметка датасета</div>
      </div>
    </div>
    <!-- Step 2 -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:14px;position:relative;z-index:1;">
      <div style="width:68px;height:68px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;color:var(--color-accent);font-family:var(--font-heading);font-size:1.6rem;font-weight:800;">2</div>
      <div style="text-align:center;">
        <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Модель</div>
        <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-accent);font-weight:600;margin-top:4px;">4 мес</div>
        <div style="font-family:var(--font-body);font-size:1rem;color:var(--color-muted);margin-top:4px;line-height:1.35;">Обучение и валидация</div>
      </div>
    </div>
    <!-- Step 3 -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:14px;position:relative;z-index:1;">
      <div style="width:68px;height:68px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;color:var(--color-accent);font-family:var(--font-heading);font-size:1.6rem;font-weight:800;">3</div>
      <div style="text-align:center;">
        <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Пилот</div>
        <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-accent);font-weight:600;margin-top:4px;">3 мес</div>
        <div style="font-family:var(--font-body);font-size:1rem;color:var(--color-muted);margin-top:4px;line-height:1.35;">2–3 отделения клиники</div>
      </div>
    </div>
    <!-- Step 4 -->
    <div style="display:flex;flex-direction:column;align-items:center;gap:14px;position:relative;z-index:1;">
      <div style="width:68px;height:68px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;color:var(--color-accent);font-family:var(--font-heading);font-size:1.6rem;font-weight:800;">4</div>
      <div style="text-align:center;">
        <div style="font-family:var(--font-body);font-size:1.25rem;font-weight:600;color:var(--color-text);">Масштаб</div>
        <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-accent);font-weight:600;margin-top:4px;">ongoing</div>
        <div style="font-family:var(--font-body);font-size:1rem;color:var(--color-muted);margin-top:4px;line-height:1.35;">Развёртка и мониторинг</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 10 — Экономический эффект  |  stat-hero CENTERED, bg-base + arc
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.18);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 64px;gap:36px;">
  <div style="text-align:center;">
    <div style="font-family:var(--font-heading);font-size:7rem;font-weight:800;color:var(--color-accent);line-height:1;">−35%</div>
    <div style="font-family:var(--font-body);font-size:1.5rem;color:var(--color-text);margin-top:10px;">стоимость диагностики</div>
  </div>
  <div style="display:flex;gap:48px;align-items:flex-start;justify-content:center;">
    <div style="text-align:center;">
      <div style="font-family:var(--font-heading);font-size:2.8rem;font-weight:800;color:var(--color-text);line-height:1;">−28%</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);margin-top:6px;">повторных обследований</div>
    </div>
    <div style="width:1.5px;height:70px;background:var(--color-surface-border);align-self:center;"></div>
    <div style="text-align:center;">
      <div style="font-family:var(--font-heading);font-size:2.8rem;font-weight:800;color:var(--color-text);line-height:1;">1.2 млрд ₽</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);margin-top:6px;">экономия в год для крупной клиники</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 11 — Мировые лидеры  |  card-mosaic, bg-alt + dot grid
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(var(--accent-rgb),0.08);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;font-family:var(--font-body);margin-bottom:18px;align-self:flex-start;">Рынок</span>
  <h2 style="font-family:var(--font-heading);font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 24px 0;line-height:1.2;">От DeepMind до Botkin.AI: кто ведёт</h2>
  <!-- Bento mosaic: 1 large + 3 smaller -->
  <div style="display:grid;grid-template-columns:1.4fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;flex:1;">
    <!-- Large card -->
    <div class="card-accent" style="grid-row:1/3;display:flex;flex-direction:column;gap:12px;justify-content:center;">
      <div class="icon-container" style="color:var(--color-accent);">
        <Icon name="globe" :size="26" />
      </div>
      <div style="font-family:var(--font-body);font-size:1.4rem;font-weight:700;color:var(--color-text);">Google DeepMind</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.4;">AlphaFold — расшифровка белковых структур, революция в фармакологии</div>
      <div style="font-family:var(--font-heading);font-size:1.9rem;font-weight:800;color:var(--color-accent);">$45 млрд</div>
      <div style="font-family:var(--font-body);font-size:1rem;color:var(--color-muted);">рынок AI-медицины к 2030</div>
    </div>
    <!-- Top-right cards -->
    <div class="card-solid" style="display:flex;flex-direction:column;gap:8px;">
      <div style="font-family:var(--font-body);font-size:1.2rem;font-weight:700;color:var(--color-text);">IBM Watson Health</div>
      <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-muted);line-height:1.35;">Онкологические решения для клиник</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:8px;">
      <div style="font-family:var(--font-body);font-size:1.2rem;font-weight:700;color:var(--color-text);">Botkin.AI</div>
      <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-muted);line-height:1.35;">Российский лидер КТ-диагностики</div>
    </div>
    <!-- Bottom-right -->
    <div class="card-solid" style="grid-column:2/4;display:flex;align-items:center;gap:16px;">
      <div class="icon-container" style="color:var(--color-accent);flex-shrink:0;">
        <Icon name="microscope" :size="24" />
      </div>
      <div>
        <div style="font-family:var(--font-body);font-size:1.2rem;font-weight:600;color:var(--color-text);">CoBrain — российские нейросети для МРТ</div>
        <div style="font-family:var(--font-body);font-size:1.05rem;color:var(--color-muted);">Нейрорадиология и сосудистая патология</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- ============================================================
     SLIDE 12 — CTA  |  cta-warm, bg-accent, ALL white
     ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);">
  <!-- Dot grid overlay -->
  <div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,0.10) 1px,transparent 1px);background-size:24px 24px;pointer-events:none;"></div>
  <!-- Arc top-right -->
  <div style="position:absolute;top:-80px;right:-80px;width:360px;height:360px;border:2.5px solid rgba(255,255,255,0.18);border-radius:50%;pointer-events:none;"></div>
  <!-- Arc bottom-left -->
  <div style="position:absolute;bottom:-100px;left:-100px;width:420px;height:420px;border:2px solid rgba(255,255,255,0.10);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:56px 80px;gap:28px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#fff;font-weight:600;font-family:var(--font-body);">Следующий шаг</span>
  <h2 style="font-family:var(--font-heading);font-size:3rem;font-weight:800;color:#fff;margin:0;line-height:1.15;max-width:660px;">Ваш первый шаг<br>в AI-медицину</h2>
  <p style="font-family:var(--font-body);font-size:1.35rem;color:rgba(255,255,255,0.85);margin:0;max-width:560px;line-height:1.5;">Начните с пилотного проекта в одном отделении</p>
  <!-- Steps row -->
  <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:4px;">
    <div style="background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.30);border-radius:12px;padding:10px 20px;font-family:var(--font-body);font-size:1.2rem;font-weight:600;color:#fff;">Аудит</div>
    <div style="color:rgba(255,255,255,0.6);font-size:1.4rem;">→</div>
    <div style="background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.30);border-radius:12px;padding:10px 20px;font-family:var(--font-body);font-size:1.2rem;font-weight:600;color:#fff;">Разметка</div>
    <div style="color:rgba(255,255,255,0.6);font-size:1.4rem;">→</div>
    <div style="background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.30);border-radius:12px;padding:10px 20px;font-family:var(--font-body);font-size:1.2rem;font-weight:600;color:#fff;">Модель</div>
    <div style="color:rgba(255,255,255,0.6);font-size:1.4rem;">→</div>
    <div style="background:rgba(255,255,255,0.20);border:1.5px solid rgba(255,255,255,0.45);border-radius:12px;padding:10px 20px;font-family:var(--font-body);font-size:1.2rem;font-weight:700;color:#fff;">Внедрение</div>
  </div>
  <div style="font-family:var(--font-body);font-size:1.25rem;color:rgba(255,255,255,0.75);margin-top:4px;">ai-med@medtechsummit.ru</div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
