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
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 80% 80% at 50% 50%,rgba(255,255,255,0.30) 0%,transparent 65%);z-index:0;pointer-events:none;"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 40% 50% at 85% 15%,rgba(255,255,255,0.12) 0%,transparent 55%);z-index:0;pointer-events:none;"></div>
<div style="position:absolute;width:600px;height:600px;border-radius:50%;border:2px solid rgba(255,255,255,0.28);top:-100px;left:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:360px;height:360px;border-radius:50%;border:2px solid rgba(255,255,255,0.18);top:-65px;left:-65px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:480px;height:480px;border-radius:50%;border:2px solid rgba(255,255,255,0.14);bottom:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(255,255,255,0.22) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:60px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.50);border-radius:20px;padding:6px 20px;margin-bottom:32px;">
    <span style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:#ffffff;font-weight:600;font-family:var(--font-heading);">Курс для специалистов здравоохранения</span>
  </div>
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.06;text-align:center;">Осознанное питание</h1>
  <p style="font-size:1.5rem;color:rgba(255,255,255,0.90);margin:0 0 12px;font-family:var(--font-body);text-align:center;font-weight:500;">Научный подход к здоровью через еду</p>
  <p style="font-size:1.15rem;color:rgba(255,255,255,0.70);margin:0 0 36px;font-family:var(--font-body);">к здоровью через еду</p>
  <div style="display:flex;align-items:center;gap:20px;color:rgba(255,255,255,0.75);font-size:1.05rem;font-family:var(--font-body);">
    <span>Доктор Елена Волкова</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);flex-shrink:0;"></span>
    <span>Нутрициология</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);flex-shrink:0;"></span>
    <span>2025</span>
  </div>
</div>

<style>
.slidev-page-1 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 2: stat-hero — bg-base — 78% хронических заболеваний -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:700px;height:700px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 65%);filter:blur(35px);top:-180px;right:-140px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:420px;height:420px;background:radial-gradient(ellipse,rgba(217,119,6,0.14) 0%,transparent 70%);filter:blur(20px);bottom:-80px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:220px;height:220px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:50px;right:70px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:14px;font-family:var(--font-heading);">Масштаб проблемы</span>
  <div style="font-size:6rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">78%</div>
  <p style="font-size:1.45rem;color:var(--color-text);margin:10px 0 8px;font-family:var(--font-body);max-width:580px;line-height:1.4;">хронических заболеваний связаны с питанием</p>
  <p style="font-size:0.9rem;color:var(--color-muted);margin:0 0 32px;font-family:var(--font-body);">(Источник: ВОЗ, Глобальный доклад о неинфекционных болезнях, 2023)</p>
  <div style="display:flex;gap:20px;align-items:stretch;flex-wrap:wrap;justify-content:center;">
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:18px 28px;text-align:center;min-width:220px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">1,8 трлн ₽</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;line-height:1.35;">расходов на алиментарные болезни/год<br><span style="font-size:0.78rem;opacity:0.85;">(Источник: Минздрав РФ, 2023)</span></div>
    </div>
    <div style="background:rgba(var(--accent-rgb),0.05);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:18px 28px;text-align:center;min-width:220px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent-warm);font-family:var(--font-heading);line-height:1;">12%</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;line-height:1.35;">врачей проходят нутрициологию в вузе<br><span style="font-size:0.78rem;opacity:0.85;">(Источник: НИИ Питания РАМН, 2022)</span></div>
    </div>
  </div>
</div>

<style>
.slidev-page-2 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 3: asymmetric-split — bg-base — Что такое осознанное питание -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 0%,transparent 65%);filter:blur(25px);top:-100px;left:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;border:2px solid rgba(var(--accent-rgb),0.28);border-radius:50%;bottom:-80px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:180px;height:180px;border:2px solid rgba(var(--accent-rgb),0.20);border-radius:50%;bottom:-50px;right:130px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="width:250px;height:250px;border-radius:50%;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.15),rgba(var(--accent-rgb),0.04));border:2px solid rgba(var(--accent-rgb),0.35);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:8px;padding:20px;">
      <div style="font-size:4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">−2,4</div>
      <div style="font-size:0.9rem;color:var(--color-text);font-family:var(--font-body);line-height:1.35;font-weight:600;">пункта ИМТ</div>
      <div style="font-size:0.78rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.3;max-width:140px;">без подсчёта калорий</div>
      <div style="margin-top:4px;background:rgba(var(--accent-rgb),0.10);border:1px solid rgba(var(--accent-rgb),0.25);border-radius:12px;padding:4px 12px;font-size:0.68rem;color:var(--color-accent);font-family:var(--font-heading);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;">Мета-анализ 2024</div>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:8px;font-family:var(--font-heading);">Определение</span>
    <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);line-height:1.12;">Не диета —<br>понимание тела</h1>
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="display:flex;align-items:flex-start;gap:14px;">
        <div style="width:9px;height:9px;border-radius:50%;background:var(--color-accent);flex-shrink:0;margin-top:9px;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.45;font-family:var(--font-body);">Слушать сигналы тела, а не считать калории</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:14px;">
        <div style="width:9px;height:9px;border-radius:50%;background:var(--color-accent);flex-shrink:0;margin-top:9px;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.45;font-family:var(--font-body);">3 компонента: <strong style="color:var(--color-accent);">интероцепция</strong>, нутрициология, поведение</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:14px;">
        <div style="width:9px;height:9px;border-radius:50%;background:var(--color-accent-warm);flex-shrink:0;margin-top:9px;"></div>
        <span style="font-size:1.1rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">(Источник: Kristeller &amp; Wolever, Mindful Eating Meta-Analysis, 2024)</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-page-3 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 4: bento-grid — bg-base — Пирамида осознанного питания -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:550px;height:550px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 0%,transparent 65%);filter:blur(30px);bottom:-120px;right:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 1.2px,transparent 1.2px);background-size:20px 20px;top:40px;right:50px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Структура</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);">Три уровня осознанного питания</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- FEATURED: Фундамент — вода и сон -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.04));border:1.5px solid rgba(var(--accent-rgb),0.40);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:flex-start;">
      <div style="width:52px;height:52px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.40);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="heart" :size="22" color="var(--color-accent)" />
      </div>
      <div style="font-size:1rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:6px;">Фундамент</div>
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);margin-bottom:6px;">Вода · Сон</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.45;margin-bottom:12px;">Гормональная регуляция голода и насыщения</div>
      <div style="display:flex;flex-direction:column;gap:8px;margin-top:auto;">
        <div style="display:flex;align-items:center;gap:8px;">
          <div style="width:6px;height:6px;border-radius:50%;background:var(--color-accent);flex-shrink:0;"></div>
          <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);">Лептин и грелин — сигналы сытости</span>
        </div>
        <div style="display:flex;align-items:center;gap:8px;">
          <div style="width:6px;height:6px;border-radius:50%;background:var(--color-accent);flex-shrink:0;"></div>
          <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);">Дефицит сна → рост аппетита на 24%</span>
        </div>
      </div>
    </div>
    <!-- Card 2: Средний уровень -->
    <div style="background:rgba(var(--accent-rgb),0.05);border:1px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.10);border:1.5px solid rgba(var(--accent-rgb),0.35);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="leaf" :size="18" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Средний уровень</span>
      </div>
      <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Макронутриенты и баланс микробиома</span>
    </div>
    <!-- Card 3: Вершина -->
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.06);border:1.5px solid rgba(var(--accent-rgb),0.28);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="chart" :size="18" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Вершина</span>
      </div>
      <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Биомаркеры и генетика питания</span>
    </div>
  </div>
</div>

<style>
.slidev-page-4 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 5: two-col-text — bg-alt (section) — Микробиом -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 65%);filter:blur(30px);top:-80px;left:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:350px;height:350px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 0%,transparent 65%);filter:blur(20px);bottom:-60px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:180px;height:180px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:40px;left:60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Наука</span>
  <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);">Микробиом — второй мозг</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-content:start;">
    <div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="gut" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">100 трлн бактерий</span>
      </div>
      <p style="font-size:1.25rem;color:var(--color-text);line-height:1.5;font-family:var(--font-body);margin:0 0 10px;">Влияют на настроение, вес и иммунитет одновременно</p>
      <p style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Sender et al., Cell, 2016)</p>
    </div>
    <div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="brain" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Ось кишечник–мозг</span>
      </div>
      <p style="font-size:1.25rem;color:var(--color-text);line-height:1.5;font-family:var(--font-body);margin:0 0 10px;">Пребиотики снижают тревожность у 64% пациентов с ВЗК</p>
      <p style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);">(Источник: Dinan &amp; Cryan, Nat Rev Gastroenterol, 2024)</p>
    </div>
    <div style="grid-column:1/3;background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:12px;padding:16px 20px;">
      <span style="font-size:1.15rem;color:var(--color-text);font-family:var(--font-body);line-height:1.5;">💡 <strong>Пребиотики</strong> (клетчатка) питают существующие бактерии · <strong>Пробиотики</strong> добавляют новые штаммы</span>
    </div>
  </div>
</div>

<style>
.slidev-page-5 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 6: section-divider — bg-accent — Практические инструменты -->
<div style="position:absolute;inset:0;background:linear-gradient(145deg,var(--bg-accent) 0%,color-mix(in srgb,var(--bg-accent) 75%,#000) 100%);z-index:0;"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 50% 40%,rgba(255,255,255,0.25) 0%,transparent 65%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 40% 40% at 80% 80%,rgba(255,255,255,0.10) 0%,transparent 50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;border-radius:50%;border:2px solid rgba(255,255,255,0.28);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:380px;height:380px;border-radius:50%;border:2px solid rgba(255,255,255,0.18);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(255,255,255,0.22) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:50px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.80);font-weight:600;margin-bottom:20px;font-family:var(--font-heading);">Часть 2</span>
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Практические<br>инструменты</h1>
  <p style="font-size:1.35rem;color:rgba(255,255,255,0.82);max-width:620px;line-height:1.55;font-family:var(--font-body);">От теории к протоколам клинической практики</p>
</div>

<style>
.slidev-page-6 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 7: card-mosaic — bg-base — 5 протоколов для ежедневной практики -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 0%,transparent 65%);filter:blur(30px);top:-100px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;background:radial-gradient(circle,rgba(217,119,6,0.12) 0%,transparent 65%);filter:blur(20px);bottom:-60px;left:-40px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:40px 60px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:4px;font-family:var(--font-heading);">Клиническая практика</span>
  <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 14px;font-family:var(--font-heading);">5 протоколов ежедневной практики</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <!-- Card 1: solid -->
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.32);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(var(--accent-rgb),0.14);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="clock" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Утреннее окно питания</span>
      </div>
      <span style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Time-Restricted Eating (TRE) — 8–10 часовое окно</span>
    </div>
    <!-- Card 2: ghost -->
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(var(--accent-rgb),0.06);border:1.5px solid rgba(var(--accent-rgb),0.28);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="leaf" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Ротация овощей</span>
      </div>
      <span style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Цветовое кодирование по группам фитонутриентов</span>
    </div>
    <!-- Card 3: ghost -->
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(var(--accent-rgb),0.06);border:1.5px solid rgba(var(--accent-rgb),0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="scale" :size="16" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Шкала голода 1–10</span>
      </div>
      <span style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Интуитивная оценка для пациентов на каждом приёме</span>
    </div>
    <!-- Card 4: accent (featured) -->
    <div style="background:var(--color-accent);border:1.5px solid var(--color-accent);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.18);border:1.5px solid rgba(255,255,255,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="clipboard" :size="16" color="#ffffff" />
        </div>
        <span style="font-size:1.1rem;font-weight:700;color:#ffffff;font-family:var(--font-heading);">Дневник реакций</span>
      </div>
      <span style="font-size:1.05rem;color:rgba(255,255,255,0.88);font-family:var(--font-body);line-height:1.4;">3-дневный пищевой журнал + медитативное питание</span>
    </div>
  </div>
</div>

<style>
.slidev-page-7 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 8: data-spotlight — bg-base — Кейс: Городская поликлиника №17 -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:650px;height:650px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 65%);filter:blur(35px);top:-160px;right:-140px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:400px;height:400px;background:radial-gradient(ellipse,rgba(217,119,6,0.14) 0%,transparent 70%);filter:blur(22px);bottom:-80px;left:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:50px;right:60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:14px;font-family:var(--font-heading);">Реальный кейс · Поликлиника №17</span>
  <!-- HERO METRIC: HbA1c promoted to hero -->
  <div style="display:flex;align-items:baseline;gap:8px;justify-content:center;margin-bottom:6px;">
    <div style="font-size:5.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">6,2%</div>
    <div style="font-size:1.8rem;font-weight:600;color:var(--color-muted);font-family:var(--font-heading);">HbA1c</div>
  </div>
  <p style="font-size:1.3rem;color:var(--color-text);margin:4px 0 6px;font-family:var(--font-body);">средний уровень после 6 месяцев программы (было 7,8%)</p>
  <p style="font-size:0.9rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);">(Источник: Внутренний аудит ГБУЗ «Поликлиника №17», 2024)</p>
  <div style="display:flex;gap:18px;flex-wrap:wrap;justify-content:center;">
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:16px 24px;text-align:center;min-width:180px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">340</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">пациентов в программе</div>
    </div>
    <div style="background:rgba(var(--accent-rgb),0.05);border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:16px 24px;text-align:center;min-width:180px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent-warm);font-family:var(--font-heading);line-height:1;">89%</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">продолжили практику самостоятельно</div>
    </div>
    <div style="background:rgba(var(--accent-rgb),0.05);border:1.5px solid rgba(var(--accent-rgb),0.22);border-radius:14px;padding:16px 24px;text-align:center;min-width:180px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">−20%</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;">снижение HbA1c (с 7,8% до 6,2%)</div>
    </div>
  </div>
</div>

<style>
.slidev-page-8 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 9: bento-grid — bg-alt — Мифы о питании -->
<div style="position:absolute;inset:0;background:var(--bg-alt);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 0%,transparent 65%);filter:blur(28px);top:-80px;right:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:320px;height:320px;background:radial-gradient(circle,rgba(217,119,6,0.12) 0%,transparent 65%);filter:blur(18px);bottom:-50px;left:-50px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:180px;height:180px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:40px;right:60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Доказательная база</span>
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Мифы, которые вредят пациентам</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- FEATURED: Миф о жире -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),rgba(var(--accent-rgb),0.03));border:1.5px solid rgba(var(--accent-rgb),0.38);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:flex-start;">
      <div style="width:48px;height:48px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="alert" :size="20" color="var(--color-accent)" />
      </div>
      <div style="font-size:0.75rem;font-weight:700;color:var(--color-accent);font-family:var(--font-heading);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:8px;">Миф №1</div>
      <div style="font-size:1.8rem;font-weight:800;color:var(--color-text);line-height:1.2;font-family:var(--font-heading);margin-bottom:10px;">«Жир — враг»</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.5;margin-bottom:12px;">Трансжиры вредны. Омега-3 защищают сердце и мозг</div>
      <div style="background:rgba(var(--accent-rgb),0.08);border:1px solid rgba(var(--accent-rgb),0.22);border-radius:10px;padding:10px 14px;margin-top:auto;">
        <span style="font-size:0.88rem;color:var(--color-text);font-family:var(--font-body);line-height:1.4;">Реальность: качество жиров, не их количество</span>
      </div>
    </div>
    <!-- Card 2: Миф о калориях -->
    <div style="background:rgba(var(--accent-rgb),0.06);border:1px solid rgba(var(--accent-rgb),0.22);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <div style="font-size:1rem;font-weight:700;color:var(--color-accent-warm);font-family:var(--font-heading);margin-bottom:4px;">Миф №2</div>
      <div style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:6px;">«Калории — это всё»</div>
      <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Качество > количество: 200 ккал из брокколи ≠ 200 ккал из сахара</div>
    </div>
    <!-- Card 3: Миф о суперфудах -->
    <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <div style="font-size:1rem;font-weight:700;color:var(--color-accent-warm);font-family:var(--font-heading);margin-bottom:4px;">Миф №3</div>
      <div style="font-size:1.2rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);margin-bottom:6px;">«Суперфуды спасут»</div>
      <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;">Маркетинг ≠ доказательная база. Нет единого «суперфуда»</div>
    </div>
  </div>
</div>

<style>
.slidev-page-9 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 10: stat-hero — bg-base — Цена бездействия -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:700px;height:700px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 0%,transparent 65%);filter:blur(35px);bottom:-160px;left:-120px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:420px;height:420px;background:radial-gradient(ellipse,rgba(217,119,6,0.14) 0%,transparent 70%);filter:blur(20px);top:-80px;right:-60px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.25) 1.2px,transparent 1.2px);background-size:20px 20px;top:50px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:14px;font-family:var(--font-heading);">Цена бездействия</span>
  <div style="font-size:6rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">92%</div>
  <p style="font-size:1.45rem;color:var(--color-text);margin:10px 0 8px;font-family:var(--font-body);max-width:580px;line-height:1.4;">пациентов забывают рекомендации через 2 недели</p>
  <p style="font-size:0.9rem;color:var(--color-muted);margin:0 0 32px;font-family:var(--font-body);">(Источник: Kessels R.P.C., Patient Education and Counseling, 2003)</p>
  <div style="display:flex;gap:20px;align-items:stretch;flex-wrap:wrap;justify-content:center;">
    <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:14px;padding:16px 24px;text-align:center;min-width:200px;">
      <div style="font-size:2.6rem;font-weight:800;color:var(--color-accent-warm);font-family:var(--font-heading);line-height:1;">+35%</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;line-height:1.35;">повторных визитов без follow-up протокола<br><span style="font-size:0.78rem;opacity:0.85;">(Источник: NHS Digital, 2023)</span></div>
    </div>
    <div style="background:rgba(217,119,6,0.08);border:1.5px solid rgba(217,119,6,0.28);border-radius:14px;padding:16px 24px;text-align:center;min-width:200px;">
      <div style="font-size:1.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1.3;">Каждый<br>неприменённый<br>протокол</div>
      <div style="font-size:0.9rem;color:var(--color-muted);font-family:var(--font-body);margin-top:6px;">=&nbsp;упущенная ремиссия</div>
    </div>
  </div>
</div>

<style>
.slidev-page-10 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 11: two-col-text — bg-base — Ресурсы и следующие шаги -->
<div style="position:absolute;inset:0;background:var(--bg-base);z-index:0;"></div>
<div style="position:absolute;width:500px;height:500px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.22) 0%,transparent 65%);filter:blur(28px);top:-80px;left:-80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:300px;height:300px;border:2px solid rgba(var(--accent-rgb),0.28);border-radius:50%;bottom:-70px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:180px;height:180px;border:2px solid rgba(var(--accent-rgb),0.20);border-radius:50%;bottom:-40px;right:130px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Следующие шаги</span>
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Ресурсы для вашей практики</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:28px;align-content:start;">
    <div style="display:flex;flex-direction:column;gap:14px;">
      <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:12px;padding:16px 20px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
          <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="clipboard" :size="18" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">PDF-протоколы</span>
        </div>
        <p style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;margin:0;">Скачать все 5 протоколов — QR-код на выходе</p>
      </div>
      <div style="background:transparent;border:1.5px solid rgba(var(--accent-rgb),0.25);border-radius:12px;padding:16px 20px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
          <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.06);border:1.5px solid rgba(var(--accent-rgb),0.22);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="users" :size="18" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Сообщество</span>
        </div>
        <p style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.4;margin:0;">Телеграм-канал: <strong style="color:var(--color-accent);">@nutriscience_pro</strong></p>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:flex-start;gap:14px;">
      <div style="background:rgba(var(--accent-rgb),0.08);border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:12px;padding:16px 20px;flex:1;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
          <div style="width:40px;height:40px;border-radius:50%;background:rgba(var(--accent-rgb),0.12);border:1.5px solid rgba(var(--accent-rgb),0.38);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="book" :size="18" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Следующий модуль</span>
        </div>
        <p style="font-size:1.1rem;color:var(--color-text);font-family:var(--font-body);font-weight:600;margin:0 0 6px;">«Нутригеномика в клинической практике»</p>
        <p style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);margin:0;">15 апреля 2025 · онлайн</p>
      </div>
      <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.10),rgba(var(--accent-rgb),0.03));border:1.5px solid rgba(var(--accent-rgb),0.30);border-radius:12px;padding:14px 18px;">
        <p style="font-size:1.05rem;color:var(--color-muted);font-family:var(--font-body);margin:0;line-height:1.45;">Обратная связь:<br><strong style="color:var(--color-accent);">nutriscience.ru/feedback</strong></p>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-page-11 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 12: cta-warm — bg-accent — Начните с одного протокола -->
<div style="position:absolute;inset:0;background:linear-gradient(145deg,var(--bg-accent) 0%,color-mix(in srgb,var(--bg-accent) 70%,#000) 100%);z-index:0;"></div>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 80% at 50% 35%,rgba(255,255,255,0.28) 0%,transparent 65%);pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:600px;height:600px;border-radius:50%;border:2px solid rgba(255,255,255,0.28);top:-100px;left:-100px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:380px;height:380px;border-radius:50%;border:2px solid rgba(255,255,255,0.18);top:-65px;left:-65px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;width:200px;height:200px;background-image:radial-gradient(circle,rgba(255,255,255,0.22) 1.2px,transparent 1.2px);background-size:20px 20px;bottom:60px;right:80px;pointer-events:none;z-index:0;"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.80);font-weight:600;margin-bottom:16px;font-family:var(--font-heading);">Призыв к действию</span>
  <h1 style="font-size:3rem;font-weight:800;color:#ffffff;margin:0 0 28px;font-family:var(--font-heading);line-height:1.12;">Начните с одного протокола<br>на следующем приёме</h1>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:560px;width:100%;margin-bottom:32px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:12px;padding:12px 20px;text-align:left;">
      <span style="font-size:1.35rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);min-width:28px;">1</span>
      <span style="font-size:1.1rem;color:rgba(255,255,255,0.92);font-family:var(--font-body);">Выберите 1 из 5 протоколов — сегодня</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.10);border:1.5px solid rgba(255,255,255,0.22);border-radius:12px;padding:12px 20px;text-align:left;">
      <span style="font-size:1.35rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);min-width:28px;">2</span>
      <span style="font-size:1.1rem;color:rgba(255,255,255,0.88);font-family:var(--font-body);">Внедрите на ближайшем приёме пациента</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.08);border:1.5px solid rgba(255,255,255,0.18);border-radius:12px;padding:12px 20px;text-align:left;">
      <span style="font-size:1.35rem;font-weight:800;color:#ffffff;font-family:var(--font-heading);min-width:28px;">3</span>
      <span style="font-size:1.1rem;color:rgba(255,255,255,0.85);font-family:var(--font-body);">Поделитесь результатом с коллегами</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.78);font-size:1.05rem;font-family:var(--font-body);">
    <span>Telegram: @dr_volkova_nutrition</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);flex-shrink:0;"></span>
    <span>nutriscience.ru/feedback</span>
  </div>
</div>

<style>
.slidev-page-12 .slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
