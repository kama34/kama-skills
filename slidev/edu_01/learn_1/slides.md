---
theme: default
title: Цифровая трансформация ритейла
fonts:
  sans: Outfit
  serif: DM Sans
  mono: JetBrains Mono
colorSchema: light
transition: fade
aspectRatio: 16/9
layout: none
---

<!-- SLIDE 1: Cover — cover-hero archetype, bg-accent -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);" class="cover-variant-b"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;justify-content:center;">
  <span class="label-pill" style="background:rgba(255,255,255,0.15);border-color:rgba(255,255,255,0.35);color:#fff;margin-bottom:28px;align-self:flex-start;">МАРТ 2025</span>
  <div style="font-family:var(--font-heading);font-size:3.8rem;font-weight:800;color:#fff;line-height:1.1;max-width:700px;margin-bottom:20px;">
    Цифровая трансформация ритейла
  </div>
  <div style="font-family:var(--font-body);font-size:1.4rem;color:rgba(255,255,255,0.85);max-width:560px;line-height:1.5;">
    Как технологии меняют покупательский опыт в 2025
  </div>
  <div style="margin-top:48px;display:flex;align-items:center;gap:16px;">
    <div class="icon-container" style="background:rgba(255,255,255,0.15);border-color:rgba(255,255,255,0.35);">
      <Icon name="rocket" :size="24" color="#fff" />
    </div>
    <span style="font-family:var(--font-body);font-size:1.1rem;color:rgba(255,255,255,0.75);">RetailTech · transform@retailtech.ru</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 2: Bento-grid — "78% покупателей ожидают персонализацию" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="margin-bottom:16px;align-self:flex-start;">КОНТЕКСТ РЫНКА</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:28px;line-height:1.15;">
    78% покупателей ожидают персонализацию
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;grid-template-rows:auto auto;gap:16px;flex:1;">
    <div class="card-solid" style="grid-column:1;grid-row:1 2;display:flex;flex-direction:column;gap:12px;justify-content:center;">
      <div class="icon-container">
        <Icon name="users" :size="24" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:4rem;font-weight:800;color:var(--color-accent);line-height:1;">78%</div>
      <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-muted);line-height:1.4;">покупателей ожидают<br>персонализацию</div>
      <div style="font-family:var(--font-body);font-size:0.9rem;color:var(--color-muted);">McKinsey, 2024</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:10px;justify-content:center;">
      <div class="icon-container">
        <Icon name="chart" :size="24" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:800;color:var(--color-accent);line-height:1;">−3–5%</div>
      <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-muted);line-height:1.4;">трафика офлайн-ритейла<br>ежегодно</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:10px;justify-content:center;">
      <div class="icon-container">
        <Icon name="sync" :size="24" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:1.6rem;font-weight:700;color:var(--color-text);line-height:1.2;">Omnichannel —<br>не опция</div>
      <div style="font-family:var(--font-body);font-size:1.1rem;color:var(--color-muted);">Это необходимость</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 3: Stat-hero — "−12% выручки каждый месяц без цифровизации" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;justify-content:center;">
  <span class="label-pill" style="margin-bottom:24px;align-self:flex-start;">СТОИМОСТЬ БЕЗДЕЙСТВИЯ</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:40px;line-height:1.15;max-width:700px;">
    −12% выручки каждый месяц без цифровизации
  </div>
  <div style="display:flex;gap:48px;align-items:flex-end;">
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div class="stat-hero">−12%</div>
      <span class="stat-caption">потенциальной выручки<br>каждый месяц</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:20px;flex:1;max-width:460px;">
      <div style="display:flex;align-items:flex-start;gap:14px;" class="card-ghost">
        <div class="icon-container" style="flex-shrink:0;">
          <Icon name="brain" :size="22" color="var(--color-accent)" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-text);line-height:1.4;">Конкуренты уже внедряют AI-рекомендации</div>
      </div>
      <div style="display:flex;align-items:flex-start;gap:14px;" class="card-solid">
        <div class="icon-container" style="flex-shrink:0;">
          <Icon name="chart" :size="22" color="var(--color-accent)" />
        </div>
        <div style="font-family:var(--font-body);font-size:1.25rem;color:var(--color-text);line-height:1.4;">Разрыв увеличивается экспоненциально</div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 4: Section-divider — bg-alt -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);" class="section-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;justify-content:center;align-items:center;text-align:center;">
  <span class="label-pill" style="margin-bottom:28px;">РАЗДЕЛ</span>
  <div style="font-family:var(--font-heading);font-size:3.2rem;font-weight:800;color:var(--color-text);line-height:1.15;max-width:680px;">
    Наш подход к трансформации
  </div>
  <div style="margin-top:32px;display:flex;gap:16px;">
    <div class="icon-container">
      <Icon name="target" :size="24" color="var(--color-accent)" />
    </div>
    <div class="icon-container">
      <Icon name="rocket" :size="24" color="var(--color-accent)" />
    </div>
    <div class="icon-container">
      <Icon name="globe" :size="24" color="var(--color-accent)" />
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 5: Icon-trio — "AI + Omnichannel + Аналитика = рост" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="margin-bottom:16px;align-self:flex-start;">ТРИ СТОЛПА</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:36px;line-height:1.15;">
    AI + Omnichannel + Аналитика = рост
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:16px;padding:28px 24px;">
      <div class="icon-container">
        <Icon name="brain" :size="26" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:1.5rem;font-weight:700;color:var(--color-text);">Персонализация через AI</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.5;">Индивидуальные рекомендации для каждого покупателя в реальном времени</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:16px;padding:28px 24px;">
      <div class="icon-container">
        <Icon name="sync" :size="26" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:1.5rem;font-weight:700;color:var(--color-text);">Бесшовный Omnichannel</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.5;">Единый опыт онлайн и офлайн без разрывов в пути покупателя</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:16px;padding:28px 24px;">
      <div class="icon-container">
        <Icon name="database" :size="26" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:1.5rem;font-weight:700;color:var(--color-text);">Аналитика реального времени</div>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.5;">Решения на основе данных, а не интуиции</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 6: Timeline-horizontal — "Дорожная карта внедрения" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="margin-bottom:16px;align-self:flex-start;">ДОРОЖНАЯ КАРТА</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:40px;line-height:1.15;">
    4 квартала к полной трансформации
  </div>
  <div style="display:flex;flex-direction:column;gap:0;flex:1;justify-content:center;">
    <!-- Timeline line -->
    <div style="display:flex;align-items:stretch;gap:0;">
      <!-- Q1 -->
      <div style="display:flex;flex-direction:column;align-items:center;flex:1;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-family:var(--font-heading);font-size:0.85rem;font-weight:800;color:#fff;">Q1</span>
        </div>
        <div style="width:2px;flex:1;background:var(--color-accent-dim);margin:8px 0;min-height:8px;"></div>
      </div>
      <div style="flex:4;padding:0 0 24px 20px;">
        <div class="card-solid" style="height:100%;">
          <div style="font-family:var(--font-heading);font-size:1.2rem;font-weight:700;color:var(--color-accent);margin-bottom:6px;">Аудит</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-text);">Аудит текущей инфраструктуры и данных</div>
        </div>
      </div>
    </div>
    <div style="display:flex;align-items:stretch;gap:0;">
      <!-- Q2 -->
      <div style="display:flex;flex-direction:column;align-items:center;flex:1;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-family:var(--font-heading);font-size:0.85rem;font-weight:800;color:#fff;">Q2</span>
        </div>
        <div style="width:2px;flex:1;background:var(--color-accent-dim);margin:8px 0;min-height:8px;"></div>
      </div>
      <div style="flex:4;padding:0 0 24px 20px;">
        <div class="card-ghost" style="height:100%;">
          <div style="font-family:var(--font-heading);font-size:1.2rem;font-weight:700;color:var(--color-accent);margin-bottom:6px;">Интеграция</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-text);">Интеграция CRM и аналитической платформы</div>
        </div>
      </div>
    </div>
    <div style="display:flex;align-items:stretch;gap:0;">
      <!-- Q3 -->
      <div style="display:flex;flex-direction:column;align-items:center;flex:1;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-family:var(--font-heading);font-size:0.85rem;font-weight:800;color:#fff;">Q3</span>
        </div>
        <div style="width:2px;flex:1;background:var(--color-accent-dim);margin:8px 0;min-height:8px;"></div>
      </div>
      <div style="flex:4;padding:0 0 24px 20px;">
        <div class="card-solid" style="height:100%;">
          <div style="font-family:var(--font-heading);font-size:1.2rem;font-weight:700;color:var(--color-accent);margin-bottom:6px;">AI-запуск</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-text);">Запуск AI-рекомендаций и персонализации</div>
        </div>
      </div>
    </div>
    <div style="display:flex;align-items:stretch;gap:0;">
      <!-- Q4 -->
      <div style="display:flex;flex-direction:column;align-items:center;flex:1;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="font-family:var(--font-heading);font-size:0.85rem;font-weight:800;color:#fff;">Q4</span>
        </div>
      </div>
      <div style="flex:4;padding:0 0 0 20px;">
        <div class="card-accent" style="height:100%;">
          <div style="font-family:var(--font-heading);font-size:1.2rem;font-weight:700;color:var(--color-accent);margin-bottom:6px;">Масштаб</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-text);">Omnichannel-интеграция и масштабирование</div>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 7: Stat-hero — "+34% конверсия за 6 месяцев пилота" — bg-alt -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-alt);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;justify-content:center;">
  <span class="label-pill" style="margin-bottom:24px;align-self:flex-start;">РЕЗУЛЬТАТЫ ПИЛОТА</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:36px;line-height:1.15;">
    +34% конверсия за 6 месяцев пилота
  </div>
  <div style="display:flex;gap:40px;align-items:flex-start;">
    <div style="display:flex;flex-direction:column;gap:6px;flex:1;">
      <div class="stat-hero">+34%</div>
      <span class="stat-caption">конверсия<br>в онлайн-канале</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:6px;flex:1;">
      <div class="stat-hero" style="font-size:4rem;">+18%</div>
      <span class="stat-caption">рост<br>среднего чека</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:6px;flex:1;">
      <div style="display:flex;align-items:baseline;gap:8px;">
        <div class="stat-hero" style="font-size:4rem;">42</div>
        <div style="font-family:var(--font-heading);font-size:2rem;font-weight:800;color:var(--color-accent);">→ 67</div>
      </div>
      <span class="stat-caption">NPS за<br>6 месяцев</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 8: Card-mosaic — "15+ лет опыта в каждой роли" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="margin-bottom:16px;align-self:flex-start;">КОМАНДА</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:32px;line-height:1.15;">
    15+ лет опыта в каждой роли
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;flex:1;">
    <div class="card-solid" style="display:flex;flex-direction:column;gap:14px;padding:28px 24px;">
      <div style="width:56px;height:56px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <span style="font-family:var(--font-heading);font-size:1.4rem;font-weight:800;color:var(--color-accent);">АИ</span>
      </div>
      <div style="font-family:var(--font-heading);font-size:1.3rem;font-weight:700;color:var(--color-text);">Алексей Иванов</div>
      <span class="label-pill" style="align-self:flex-start;font-size:0.65rem;">Руководитель проекта</span>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.4;">15 лет в ритейл-технологиях</div>
    </div>
    <div class="card-ghost" style="display:flex;flex-direction:column;gap:14px;padding:28px 24px;">
      <div style="width:56px;height:56px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <span style="font-family:var(--font-heading);font-size:1.4rem;font-weight:800;color:var(--color-accent);">МП</span>
      </div>
      <div style="font-family:var(--font-heading);font-size:1.3rem;font-weight:700;color:var(--color-text);">Мария Петрова</div>
      <span class="label-pill" style="align-self:flex-start;font-size:0.65rem;">Архитектор данных</span>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.4;">ex-Яндекс, эксперт в ML-платформах</div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;gap:14px;padding:28px 24px;">
      <div style="width:56px;height:56px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <span style="font-family:var(--font-heading);font-size:1.4rem;font-weight:800;color:var(--color-accent);">ДК</span>
      </div>
      <div style="font-family:var(--font-heading);font-size:1.3rem;font-weight:700;color:var(--color-text);">Дмитрий Козлов</div>
      <span class="label-pill" style="align-self:flex-start;font-size:0.65rem;">UX-лидер</span>
      <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);line-height:1.4;">200+ спроектированных интерфейсов</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 9: Asymmetric-split — "28 млн ₽ с возвратом 340% за 2 года" -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-base);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span class="label-pill" style="margin-bottom:16px;align-self:flex-start;">ИНВЕСТИЦИИ И ROI</span>
  <div style="font-family:var(--font-heading);font-size:2.4rem;font-weight:700;color:var(--color-text);margin-bottom:32px;line-height:1.15;">
    28 млн ₽ с возвратом 340% за 2 года
  </div>
  <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:24px;flex:1;">
    <div style="display:flex;flex-direction:column;gap:16px;">
      <div class="card-solid" style="display:flex;align-items:center;gap:20px;padding:22px 24px;">
        <div class="icon-container">
          <Icon name="target" :size="22" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-family:var(--font-heading);font-size:2rem;font-weight:800;color:var(--color-accent);">28 млн ₽</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);">Бюджет проекта</div>
        </div>
      </div>
      <div class="card-ghost" style="display:flex;align-items:center;gap:20px;padding:22px 24px;">
        <div class="icon-container">
          <Icon name="chart" :size="22" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-family:var(--font-heading);font-size:2rem;font-weight:800;color:var(--color-accent);">14 месяцев</div>
          <div style="font-family:var(--font-body);font-size:1.15rem;color:var(--color-muted);">Окупаемость</div>
        </div>
      </div>
    </div>
    <div class="card-accent" style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:32px 24px;">
      <div class="icon-container">
        <Icon name="rocket" :size="26" color="var(--color-accent)" />
      </div>
      <div style="font-family:var(--font-heading);font-size:4.5rem;font-weight:800;color:var(--color-accent);line-height:1;">340%</div>
      <div style="font-family:var(--font-body);font-size:1.2rem;color:var(--color-muted);text-align:center;line-height:1.4;">ROI к концу<br>2-го года</div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- SLIDE 10: CTA-warm — bg-accent, all text white -->
<div style="position:absolute;inset:0;z-index:0;overflow:hidden;background:var(--bg-accent);" class="cover-variant-c"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;justify-content:center;">
  <span class="label-pill" style="background:rgba(255,255,255,0.15);border-color:rgba(255,255,255,0.35);color:#fff;margin-bottom:24px;align-self:flex-start;">СЛЕДУЮЩИЙ ШАГ</span>
  <div style="font-family:var(--font-heading);font-size:3.2rem;font-weight:800;color:#fff;line-height:1.15;max-width:680px;margin-bottom:20px;">
    Запланируем стратегическую сессию вместе
  </div>
  <div style="font-family:var(--font-body);font-size:1.35rem;color:rgba(255,255,255,0.85);max-width:500px;line-height:1.5;margin-bottom:40px;">
    Покажем, как трансформация работает для вашего бизнеса — без воды, с конкретными цифрами
  </div>
  <div style="display:flex;flex-direction:column;gap:14px;">
    <div style="display:flex;align-items:center;gap:16px;">
      <div class="icon-container" style="background:rgba(255,255,255,0.15);border-color:rgba(255,255,255,0.35);flex-shrink:0;">
        <Icon name="phone" :size="22" color="#fff" />
      </div>
      <span style="font-family:var(--font-body);font-size:1.3rem;color:#fff;">+7 (495) 123-45-67</span>
    </div>
    <div style="display:flex;align-items:center;gap:16px;">
      <div class="icon-container" style="background:rgba(255,255,255,0.15);border-color:rgba(255,255,255,0.35);flex-shrink:0;">
        <Icon name="globe" :size="22" color="#fff" />
      </div>
      <span style="font-family:var(--font-body);font-size:1.3rem;color:#fff;">transform@retailtech.ru</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
