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

<!-- Slide 1: Cover — bg-accent, white text, radial glow decor -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:600px;height:600px;background:radial-gradient(circle,rgba(255,255,255,0.18),transparent 65%);pointer-events:none;"></div>
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(255,255,255,0.12) 1.2px,transparent 1.2px);background-size:24px 24px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:44px 80px;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#ffffff;font-weight:600;width:fit-content;margin-bottom:24px;">GreenTech Solutions · 2025</span>
  <h1 style="font-family:'Outfit',sans-serif;font-size:3.6rem;font-weight:800;color:#ffffff;line-height:1.1;margin:0 0 20px 0;max-width:700px;">Зелёная энергетика для бизнеса</h1>
  <p style="font-size:1.4rem;color:rgba(255,255,255,0.88);margin:0;max-width:560px;font-family:'DM Sans',sans-serif;">Снижаем затраты на 40% и углеродный след</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 2: Мировой контекст — bento-grid, bg-base + dot grid -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.40) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Мировой контекст</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;">−89% стоимость солнечной энергии за 10 лет</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:10px;">
      <div class="icon-container"><Icon name="sun" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">−89%</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">Стоимость солнечной энергии за 10 лет</div>
      <div style="font-size:1rem;color:var(--color-muted);">IRENA, 2024</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:10px;">
      <div class="icon-container"><Icon name="globe" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">2026</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">ЕС вводит углеродный налог</div>
      <div style="font-size:1rem;color:var(--color-muted);">Новое регулирование</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:10px;">
      <div class="icon-container"><Icon name="chart" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:2rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">73%</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">крупных компаний с ESG-стратегией</div>
      <div style="font-size:1rem;color:var(--color-muted);">Глобальный тренд</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 3: Секция — section-divider, bg-alt + arc decor, CENTERED, no label -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.40);border-radius:50%;pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;right:-80px;width:260px;height:260px;border:2px solid rgba(var(--accent-rgb),0.20);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 64px;text-align:center;">
  <div style="width:48px;height:3px;background:var(--color-accent);border-radius:2px;margin-bottom:28px;"></div>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.8rem;font-weight:800;color:var(--color-text);margin:0 0 20px 0;max-width:700px;line-height:1.2;">Почему зелёная энергетика выгодна уже сейчас</h2>
  <p style="font-size:1.3rem;color:var(--color-muted);margin:0;max-width:520px;">Экономика, субсидии и независимость от тарифов</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 4: Экономика перехода — icon-trio, bg-base + glow decor -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Экономика перехода</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 32px 0;">Окупаемость 4–6 лет при субсидии 30%</h2>
  <div style="display:flex;gap:20px;flex:1;">
    <div class="card-solid" style="flex:1;display:flex;flex-direction:column;gap:14px;">
      <div class="icon-container"><Icon name="sun" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">4–6 лет</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">Окупаемость солнечных панелей</div>
    </div>
    <div class="card-ghost" style="flex:1;display:flex;flex-direction:column;gap:14px;">
      <div class="icon-container"><Icon name="battery" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">−55%</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">Снижение пиковых тарифов с накопителями</div>
    </div>
    <div class="card-accent" style="flex:1;display:flex;flex-direction:column;gap:14px;">
      <div class="icon-container"><Icon name="shield" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">до 30%</div>
      <div style="font-size:1.25rem;color:var(--color-text);font-weight:500;">Государственные субсидии на инвестиции</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 5: Сравнение — two-col-text, bg-alt + dot grid -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.40) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Сравнение</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;">3.4₽ vs 8.2₽ за кВт·ч: зелёная выгоднее</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1;">
    <div style="display:flex;flex-direction:column;gap:10px;">
      <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-muted);font-weight:600;margin-bottom:4px;">Традиционная энергия</div>
      <div class="card-ghost" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Стоимость кВт·ч</span>
        <span style="font-size:1.4rem;font-weight:700;color:#B91C1C;">8.2₽</span>
      </div>
      <div class="card-ghost" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Углеродный след</span>
        <span style="font-size:1.3rem;font-weight:700;color:#B91C1C;">450 г CO₂</span>
      </div>
      <div class="card-ghost" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Волатильность цен</span>
        <span style="font-size:1.3rem;font-weight:700;color:#B91C1C;">Высокая</span>
      </div>
      <div class="card-ghost" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Срок службы</span>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-muted);">15 лет</span>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:10px;">
      <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:600;margin-bottom:4px;">Зелёная энергия</div>
      <div class="card-accent" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Стоимость кВт·ч</span>
        <span style="font-size:1.4rem;font-weight:700;color:var(--color-accent);">3.4₽</span>
      </div>
      <div class="card-accent" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Углеродный след</span>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-accent);">25 г CO₂</span>
      </div>
      <div class="card-accent" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Волатильность цен</span>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-accent);">Фиксированная</span>
      </div>
      <div class="card-accent" style="display:flex;justify-content:space-between;align-items:center;padding:14px 20px;">
        <span style="font-size:1.25rem;color:var(--color-text);">Срок службы</span>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-accent);">25+ лет</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 6: 340% ROI — stat-hero, bg-base + arc decor, CENTERED, hero number -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.40);border-radius:50%;pointer-events:none;"></div>
  <div style="position:absolute;bottom:-60px;right:-60px;width:220px;height:220px;border:2px solid rgba(var(--accent-rgb),0.20);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 64px;text-align:center;">
  <span class="label-pill" style="margin-bottom:24px;">Ключевая метрика</span>
  <div style="font-size:7rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:'Outfit',sans-serif;">340%</div>
  <div style="font-size:2rem;font-weight:700;color:var(--color-text);font-family:'Outfit',sans-serif;margin-top:12px;">ROI за 10 лет</div>
  <p class="stat-caption" style="margin-top:16px;max-width:500px;">При переходе на гибридную энергосистему с солнечными панелями и накопителями</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 7: Наши решения — card-mosaic, bg-base + glow decor -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Наши решения</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 28px 0;">Полный цикл: от панелей до AI-оптимизации</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;flex:1;">
    <div class="card-solid" style="display:flex;align-items:flex-start;gap:16px;">
      <div class="icon-container" style="flex-shrink:0;"><Icon name="sun" size="22" style="color:var(--color-accent);" /></div>
      <div>
        <div style="font-size:1.3rem;font-weight:600;color:var(--color-text);margin-bottom:6px;">Солнечные фермы</div>
        <div style="font-size:1.1rem;color:var(--color-muted);">Для производств и складов любого масштаба</div>
      </div>
    </div>
    <div class="card-ghost" style="display:flex;align-items:flex-start;gap:16px;">
      <div class="icon-container" style="flex-shrink:0;"><Icon name="wind" size="22" style="color:var(--color-accent);" /></div>
      <div>
        <div style="font-size:1.3rem;font-weight:600;color:var(--color-text);margin-bottom:6px;">Ветрогенерация</div>
        <div style="font-size:1.1rem;color:var(--color-muted);">Для удалённых объектов без сети</div>
      </div>
    </div>
    <div class="card-accent" style="display:flex;align-items:flex-start;gap:16px;">
      <div class="icon-container" style="flex-shrink:0;"><Icon name="battery" size="22" style="color:var(--color-accent);" /></div>
      <div>
        <div style="font-size:1.3rem;font-weight:600;color:var(--color-text);margin-bottom:6px;">Накопители LFP</div>
        <div style="font-size:1.1rem;color:var(--color-muted);">Системы хранения энергии — стабильность 24/7</div>
      </div>
    </div>
    <div class="card-solid" style="display:flex;align-items:flex-start;gap:16px;">
      <div class="icon-container" style="flex-shrink:0;"><Icon name="bolt" size="22" style="color:var(--color-accent);" /></div>
      <div>
        <div style="font-size:1.3rem;font-weight:600;color:var(--color-text);margin-bottom:6px;">AI-оптимизация</div>
        <div style="font-size:1.1rem;color:var(--color-muted);">Умное управление потреблением в реальном времени</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 8: Портфолио — bento-grid, bg-alt + dot grid (1 large + 3 small) -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.40) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Портфолио</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 24px 0;">2.4 МВт на Востоке, 100% в Сколково</h2>
  <div style="display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:1fr 1fr;gap:14px;flex:1;">
    <div class="card-accent" style="grid-row:span 2;display:flex;flex-direction:column;justify-content:flex-end;gap:10px;">
      <div class="icon-container"><Icon name="factory" size="22" style="color:var(--color-accent);" /></div>
      <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">2.4 МВт</div>
      <div style="font-size:1.3rem;font-weight:600;color:var(--color-text);">Логистический центр «Восток»</div>
      <div style="font-size:1.1rem;color:var(--color-muted);">Экономия 18 млн ₽/год</div>
    </div>
    <div class="card-solid" style="display:flex;flex-direction:column;gap:6px;">
      <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">Агрохолдинг «Нива»</div>
      <div style="font-size:1.1rem;color:var(--color-accent);font-weight:700;">−62% CO₂</div>
      <div style="font-size:0.95rem;color:var(--color-muted);">Гибридная система</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:6px;">
      <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">IT-кампус «Сколково»</div>
      <div style="font-size:1.1rem;color:var(--color-accent);font-weight:700;">100% зелёная</div>
      <div style="font-size:0.95rem;color:var(--color-muted);">Полностью возобновляемая</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 9: Процесс — timeline-horizontal, bg-base + arc decor -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.40);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="width:fit-content;margin-bottom:16px;">Процесс внедрения</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 32px 0;">От аудита до запуска за 4–5 месяцев</h2>
  <div style="display:flex;align-items:flex-start;gap:0;flex:1;position:relative;">
    <!-- Connecting line -->
    <div style="position:absolute;top:27px;left:27px;right:27px;height:2px;background:var(--color-accent-dim);z-index:0;"></div>
    <!-- Step 1 -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:1;">
      <div style="width:54px;height:54px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;">
        <Icon name="target" size="24" style="color:#ffffff;" />
      </div>
      <div style="text-align:center;">
        <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">2 недели</div>
        <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">Энергоаудит</div>
        <div style="font-size:1rem;color:var(--color-muted);">Анализ потребления</div>
      </div>
    </div>
    <!-- Step 2 -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:1;">
      <div style="width:54px;height:54px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;">
        <Icon name="chart" size="24" style="color:var(--color-accent);" />
      </div>
      <div style="text-align:center;">
        <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">1 месяц</div>
        <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">Проектирование</div>
        <div style="font-size:1rem;color:var(--color-muted);">Оптимальная система</div>
      </div>
    </div>
    <!-- Step 3 -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:1;">
      <div style="width:54px;height:54px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;">
        <Icon name="factory" size="24" style="color:var(--color-accent);" />
      </div>
      <div style="text-align:center;">
        <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">2–4 месяца</div>
        <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">Монтаж</div>
        <div style="font-size:1rem;color:var(--color-muted);">Поставка и установка</div>
      </div>
    </div>
    <!-- Step 4 -->
    <div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:14px;z-index:1;">
      <div style="width:54px;height:54px;border-radius:50%;background:var(--color-surface);border:2px solid var(--color-accent);display:flex;align-items:center;justify-content:center;">
        <Icon name="bolt" size="24" style="color:var(--color-accent);" />
      </div>
      <div style="text-align:center;">
        <div style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">Постоянно</div>
        <div style="font-size:1.2rem;font-weight:600;color:var(--color-text);">Запуск и мониторинг</div>
        <div style="font-size:1rem;color:var(--color-muted);">AI-оптимизация</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 10: Гарантии — asymmetric-split, bg-base + glow decor, visual-dominant -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);">
  <div style="position:absolute;bottom:-60px;right:-60px;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;padding:44px 64px;gap:48px;">
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;">
    <span class="label-pill" style="width:fit-content;margin-bottom:20px;">Гарантии</span>
    <h2 style="font-family:'Outfit',sans-serif;font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 12px 0;line-height:1.15;">25 лет гарантии, 99.5% SLA, IoT 24/7</h2>
    <p style="font-size:1.25rem;color:var(--color-muted);margin:0;">Полная поддержка на весь жизненный цикл оборудования</p>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px;">
    <div class="card-solid" style="display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="shield" size="24" style="color:#ffffff;" />
      </div>
      <div>
        <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">25 лет</div>
        <div style="font-size:1.1rem;color:var(--color-text);">Гарантия на панели</div>
      </div>
    </div>
    <div class="card-ghost" style="display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="check" size="24" style="color:var(--color-accent);" />
      </div>
      <div>
        <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">99.5% SLA</div>
        <div style="font-size:1.1rem;color:var(--color-text);">Гарантия доступности сервиса</div>
      </div>
    </div>
    <div class="card-accent" style="display:flex;align-items:center;gap:18px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="globe" size="24" style="color:var(--color-accent);" />
      </div>
      <div>
        <div style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:'Outfit',sans-serif;">IoT 24/7</div>
        <div style="font-size:1.1rem;color:var(--color-text);">Мониторинг через IoT-платформу</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 11: Секция 2 — section-divider, bg-alt + dot grid, CENTERED -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);">
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.40) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;left:-80px;width:280px;height:280px;border:2.5px solid rgba(var(--accent-rgb),0.25);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 64px;text-align:center;">
  <div style="width:48px;height:3px;background:var(--color-accent);border-radius:2px;margin-bottom:28px;"></div>
  <h2 style="font-family:'Outfit',sans-serif;font-size:2.8rem;font-weight:800;color:var(--color-text);margin:0 0 20px 0;max-width:700px;line-height:1.2;">Начните экономить уже сегодня</h2>
  <p style="font-size:1.3rem;color:var(--color-muted);margin:0;max-width:500px;">Бесплатный аудит и расчёт ROI за 48 часов</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---

<!-- Slide 12: CTA — cta-warm, bg-accent, white text -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);">
  <div style="position:absolute;top:0;right:0;width:420px;height:420px;background-image:radial-gradient(circle,rgba(255,255,255,0.12) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;"></div>
  <div style="position:absolute;bottom:-60px;left:-60px;width:500px;height:500px;background:radial-gradient(circle,rgba(255,255,255,0.12),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:44px 80px;text-align:center;">
  <span style="display:inline-flex;align-items:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:#ffffff;font-weight:600;margin-bottom:24px;">Рассчитайте свою экономию</span>
  <h2 style="font-family:'Outfit',sans-serif;font-size:3.2rem;font-weight:800;color:#ffffff;margin:0 0 20px 0;line-height:1.1;max-width:700px;">Бесплатный энергоаудит за 48 часов</h2>
  <p style="font-size:1.4rem;color:rgba(255,255,255,0.88);margin:0 0 36px 0;max-width:540px;">Персональный расчёт ROI под ваш объект — без обязательств</p>
  <div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap;justify-content:center;">
    <div style="background:rgba(255,255,255,0.18);border:1.5px solid rgba(255,255,255,0.35);border-radius:12px;padding:14px 28px;font-size:1.25rem;font-weight:600;color:#ffffff;">green@greentech.ru</div>
    <div style="background:rgba(255,255,255,0.18);border:1.5px solid rgba(255,255,255,0.35);border-radius:12px;padding:14px 28px;font-size:1.25rem;font-weight:600;color:#ffffff;">+7 (800) 555-35-35</div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
