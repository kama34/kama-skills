---
theme: default
colorSchema: light
fonts:
  sans: Manrope
  body: DM Sans
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
layout: none
---

<!-- SLIDE 1: cover-hero — bg-accent -->
<div style="position:absolute;inset:0;background:var(--bg-accent);z-index:0;"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 70% at 50% 50%,rgba(255,255,255,0.18) 0%,transparent 70%);z-index:0;pointer-events:none;"></div>
<div style="position:absolute;width:600px;height:600px;border-radius:50%;border:2px solid rgba(255,255,255,0.25);top:-100px;left:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:360px;height:360px;border-radius:50%;border:2px solid rgba(255,255,255,0.18);top:-65px;left:-65px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;border-radius:50%;border:2px solid rgba(255,255,255,0.20);bottom:-80px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.40);border-radius:20px;padding:6px 18px;margin-bottom:28px;">
    <span style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:#ffffff;font-weight:600;font-family:var(--font-heading);">ЛогТех Консалтинг · 2025</span>
  </div>
  <h1 style="font-size:3.6rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;text-align:center;">Цифровая трансформация<br>логистики</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.85);margin:0 0 32px;font-family:var(--font-body);text-align:center;max-width:680px;">Как технологии сокращают издержки на 35%<br>и ускоряют доставку</p>
  <div style="display:flex;align-items:center;gap:20px;color:rgba(255,255,255,0.70);font-size:1rem;font-family:var(--font-body);">
    <span>Цифровая трансформация</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>Логистика</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>2025</span>
  </div>
</div>

<style>
.s1 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 2: bento-grid — bg-base — Pain metrics -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.12) 0%,transparent 70%);top:-60px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:40px;left:40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.15;">Логистика теряет 2,4 трлн ₽<br>на ручных процессах ежегодно</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="warehouse" :size="24" color="var(--color-accent)" />
      </div>
      <div style="font-size:4.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">67%</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:8px;line-height:1.4;">складских операций<br>выполняется вручную</div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.10);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="warning" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">3,2%</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">средняя ошибка комплектации</div>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.10);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="clock" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.4rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">18%</div>
        <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">простой транспорта от цикла</div>
      </div>
    </div>
  </div>
</div>

<style>
.s2 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 3: stat-hero — bg-base — Cost of inaction (breathing slide) -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 70%);filter:blur(30px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(217,119,6,0.14) 0%,transparent 70%);filter:blur(24px);bottom:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;border-radius:50%;border:2px solid rgba(var(--accent-rgb),0.28);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:260px;height:260px;border-radius:50%;border:2px solid rgba(var(--accent-rgb),0.18);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;font-family:var(--font-heading);">ЦЕНА ПРОМЕДЛЕНИЯ</span>
  <h1 style="font-size:6rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);text-align:center;">12 млн ₽</h1>
  <p style="font-size:1.35rem;color:var(--color-text);margin:12px 0 36px;font-family:var(--font-body);text-align:center;">теряет бизнес каждый месяц без автоматизации</p>
  <div style="display:flex;gap:12px;">
    <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:var(--bg-base);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:8px 18px;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:600;font-family:var(--font-heading);">ручная маршрутизация: 8 млн/мес</div>
    <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:var(--bg-base);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:8px 18px;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:600;font-family:var(--font-heading);">простой флота: 4 млн/мес</div>
  </div>
  <p style="font-size:1rem;color:var(--color-muted);margin:20px 0 0;font-family:var(--font-body);text-align:center;">Конкуренты с WMS растут в <strong style="color:var(--color-accent);">2,8×</strong> быстрее</p>
</div>

<style>
.s3 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 4: icon-trio — bg-alt — Three technologies -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10) 0%,transparent 70%);top:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;border:2px solid rgba(var(--accent-rgb),0.25);border-radius:50%;bottom:-60px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.15;">Три технологии меняют<br>правила игры</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:48px;">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;">
      <div style="width:76px;height:76px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <Icon name="wms" :size="32" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);text-align:center;">WMS нового поколения</span>
      <span style="font-size:1.1rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);text-align:center;">с ML-оптимизацией складских операций</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;">
      <div style="width:76px;height:76px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <Icon name="iot" :size="32" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);text-align:center;">IoT-датчики</span>
      <span style="font-size:1.1rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);text-align:center;">на каждом этапе цепочки поставок</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:220px;">
      <div style="width:76px;height:76px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <Icon name="analytics" :size="32" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);text-align:center;">Предиктивная аналитика</span>
      <span style="font-size:1.1rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);text-align:center;">прогноз спроса с точностью 94%</span>
    </div>
  </div>
</div>

<style>
.s4 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 5: timeline-horizontal — bg-base — 6-month journey -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10) 0%,transparent 70%);bottom:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:20px 20px;top:40px;right:60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.15;">От хаоса к системе за 6 месяцев</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Месяц 1–2</span>
      <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);line-height:1.35;font-family:var(--font-heading);">Аудит процессов</span>
      <span style="font-size:1rem;color:var(--color-muted);line-height:1.4;margin-top:4px;font-family:var(--font-body);">Диагностика и интеграция WMS</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Месяц 3–4</span>
      <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);line-height:1.35;font-family:var(--font-heading);">IoT-инфраструктура</span>
      <span style="font-size:1rem;color:var(--color-muted);line-height:1.4;margin-top:4px;font-family:var(--font-body);">Датчики и мониторинг в реальном времени</span>
    </div>
    <div style="background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Месяц 5–6</span>
      <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);line-height:1.35;font-family:var(--font-heading);">Аналитика и обучение</span>
      <span style="font-size:1rem;color:var(--color-muted);line-height:1.4;margin-top:4px;font-family:var(--font-body);">Предиктивные модели и команда</span>
    </div>
    <div style="grid-column:1/4;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 24px;display:flex;align-items:center;gap:32px;">
      <span style="font-size:0.75rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;font-family:var(--font-heading);">КЛЮЧЕВЫЕ РЕЗУЛЬТАТЫ</span>
      <div style="display:flex;gap:32px;align-items:center;">
        <div style="display:flex;align-items:center;gap:8px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);"></div>
          <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);">WMS запущена</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);"></div>
          <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);">IoT в сети</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);"></div>
          <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);">ROI за год: 340%</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.s5 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 6: data-spotlight — bg-alt — Case study X5 Group -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.14) 0%,transparent 70%);filter:blur(20px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;border:2px solid rgba(var(--accent-rgb),0.25);border-radius:50%;bottom:-40px;left:-40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:14px;font-family:var(--font-heading);">КЕЙС: X5 GROUP</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 28px;font-family:var(--font-heading);line-height:1.15;text-align:center;">Пилот сократил потери на 41%</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;max-width:760px;width:100%;">
    <div style="background:rgba(var(--accent-rgb),0.12);border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:22px 18px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:3.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">0,8%</div>
      <div style="font-size:0.85rem;color:var(--color-muted);margin-top:6px;text-align:center;font-family:var(--font-body);line-height:1.4;">ошибки комплектации<br><span style="color:var(--color-accent);font-weight:600;">было 3,2%</span></div>
    </div>
    <div style="background:rgba(var(--accent-rgb),0.07);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 18px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:3.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">+28%</div>
      <div style="font-size:0.85rem;color:var(--color-muted);margin-top:6px;text-align:center;font-family:var(--font-body);line-height:1.4;">скорость доставки<br>в среднем</div>
    </div>
    <div style="background:rgba(var(--accent-rgb),0.07);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px 18px;display:flex;flex-direction:column;align-items:center;">
      <div style="font-size:3.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">340%</div>
      <div style="font-size:0.85rem;color:var(--color-muted);margin-top:6px;text-align:center;font-family:var(--font-body);line-height:1.4;">ROI за<br>первый год</div>
    </div>
  </div>
  <p style="font-size:1.1rem;color:var(--color-accent);margin-top:22px;font-weight:600;font-family:var(--font-body);text-align:center;">Внедрение завершено за 4 месяца</p>
</div>

<style>
.s6 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 7: comparison-table — bg-base — Pricing -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10) 0%,transparent 70%);top:-60px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:60px;left:60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.15;">Инвестиция с окупаемостью<br>за 8 месяцев</h1>
  <div style="flex:1;display:grid;grid-template-rows:1fr 1fr 1fr;gap:10px;align-items:stretch;">
    <div style="display:flex;align-items:center;gap:20px;background:transparent;border:1px solid var(--color-surface-border);border-radius:12px;padding:0 24px;">
      <div style="width:44px;height:44px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="package" :size="20" color="var(--color-accent)" />
      </div>
      <div style="flex:1;">
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Базовый</span>
        <span style="font-size:1rem;color:var(--color-muted);margin-left:8px;font-family:var(--font-body);">WMS + обучение</span>
      </div>
      <span style="font-size:1.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">4,2 млн ₽</span>
    </div>
    <div style="display:flex;align-items:center;gap:20px;background:transparent;border:1px solid var(--color-surface-border);border-radius:12px;padding:0 24px;">
      <div style="width:44px;height:44px;border-radius:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="iot" :size="20" color="var(--color-accent)" />
      </div>
      <div style="flex:1;">
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Продвинутый</span>
        <span style="font-size:1rem;color:var(--color-muted);margin-left:8px;font-family:var(--font-body);">WMS + IoT + аналитика</span>
      </div>
      <span style="font-size:1.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">8,7 млн ₽</span>
    </div>
    <div style="display:flex;align-items:center;gap:20px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 24px;">
      <div style="width:44px;height:44px;border-radius:14px;background:rgba(var(--accent-rgb),0.20);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="rocket" :size="20" color="var(--color-accent)" />
      </div>
      <div style="flex:1;">
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Enterprise</span>
        <span style="font-size:1rem;color:var(--color-muted);margin-left:8px;font-family:var(--font-body);">полная трансформация</span>
      </div>
      <span style="font-size:1.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">от 15 млн ₽</span>
    </div>
  </div>
</div>

<style>
.s7 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 8: card-mosaic — bg-alt — Team -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10) 0%,transparent 70%);bottom:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;border:2px solid rgba(var(--accent-rgb),0.25);border-radius:50%;top:-60px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.15;">200+ внедрений — проверенная<br>экспертиза</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <div style="background:var(--bg-base);border:1px solid var(--color-surface-border);border-radius:14px;padding:22px;display:flex;align-items:center;gap:16px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="users" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">47</div>
        <div style="font-size:1rem;color:var(--color-muted);margin-top:2px;font-family:var(--font-body);">сертифицированных инженеров</div>
      </div>
    </div>
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:22px;display:flex;align-items:center;gap:16px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="shield" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:1.25rem;font-weight:700;color:var(--color-text);line-height:1.3;font-family:var(--font-heading);">Партнёры</div>
        <div style="font-size:1rem;color:var(--color-muted);margin-top:2px;font-family:var(--font-body);">SAP · Oracle · 1С</div>
      </div>
    </div>
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:22px;display:flex;align-items:center;gap:16px;">
      <div style="width:52px;height:52px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="clock" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">4,5 мес</div>
        <div style="font-size:1rem;color:var(--color-muted);margin-top:2px;font-family:var(--font-body);">средний срок внедрения</div>
      </div>
    </div>
    <div style="background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:22px;display:flex;align-items:center;gap:16px;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.20);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="chart" :size="24" color="var(--color-accent)" />
      </div>
      <div>
        <div style="font-size:2.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">200+</div>
        <div style="font-size:1rem;color:var(--color-muted);margin-top:2px;font-family:var(--font-body);">успешных внедрений</div>
      </div>
    </div>
  </div>
</div>

<style>
.s8 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 9: cta-warm — bg-accent — CTA -->
<div style="position:absolute;inset:0;background:linear-gradient(145deg, var(--bg-accent) 0%, color-mix(in srgb, var(--bg-accent) 70%, black) 100%);z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;background:radial-gradient(circle,rgba(255,255,255,0.18) 0%,transparent 70%);filter:blur(30px);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;border-radius:50%;border:2px solid rgba(255,255,255,0.25);top:-100px;left:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:360px;height:360px;border-radius:50%;border:2px solid rgba(255,255,255,0.18);top:-65px;left:-65px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.80);font-weight:600;margin-bottom:16px;font-family:var(--font-heading);">СЛЕДУЮЩИЙ ШАГ</span>
  <h1 style="font-size:3rem;font-weight:800;color:#ffffff;margin:0 0 28px;font-family:var(--font-heading);line-height:1.15;text-align:center;">Запустите пилот за 2 недели —<br>бесплатно</h1>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:580px;width:100%;margin-bottom:32px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:0.85rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);">1</span>
      </div>
      <span style="font-size:1.15rem;color:#ffffff;font-family:var(--font-body);text-align:left;">Бесплатный аудит текущих процессов</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:0.85rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);">2</span>
      </div>
      <span style="font-size:1.15rem;color:#ffffff;font-family:var(--font-body);text-align:left;">Демо WMS на ваших реальных данных</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1px solid rgba(255,255,255,0.25);border-radius:12px;padding:12px 20px;">
      <div style="width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.20);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:0.85rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);">3</span>
      </div>
      <span style="font-size:1.15rem;color:#ffffff;font-family:var(--font-body);text-align:left;">Детальный план ROI для вашего бизнеса</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.85);font-size:1.1rem;font-family:var(--font-body);">
    <span>Telegram: @logtech_pilot</span>
    <span style="width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,0.50);flex-shrink:0;"></span>
    <span>logtech.ru/demo</span>
  </div>
</div>

<style>
.s9 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
