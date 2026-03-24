---
theme: default
layout: none
colorSchema: light
transition: fade
fonts:
  heading: Outfit
  body: DM Sans
  mono: JetBrains Mono
---

<!-- Slide 1: Обложка — cover-hero, bg-accent -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent);" class="cover-variant-a">
    <div class="cover-circle-accent"></div>
  </div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <span class="label-pill-cover" style="margin-bottom:28px;">Логистика 4.0</span>
    <h1 style="font-size:3.4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;">Цифровая трансформация<br>цепочек поставок</h1>
    <p style="font-size:1.3rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Как технологии меняют грузоперевозки в России</p>
    <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.70);font-size:1.15rem;font-family:var(--font-body);">
      <span>Март 2026</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);display:inline-block;"></span>
      <span>Россия</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.50);display:inline-block;"></span>
      <span>Аналитический обзор</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 2: Рынок грузоперевозок — stat-hero, bg-base, decor-dots -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-dots"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 96px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;font-family:var(--font-body);">Рынок грузоперевозок</span>
    <div class="stat-row" style="justify-content:center;margin-bottom:12px;">
      <div style="display:flex;flex-direction:column;align-items:center;">
        <span class="stat-hero">8,2</span>
        <span class="stat-caption">трлн ₽ к 2027</span>
      </div>
      <div style="width:1px;height:80px;background:var(--color-surface-border);align-self:center;"></div>
      <div style="display:flex;flex-direction:column;align-items:center;">
        <span class="stat-hero">+21%</span>
        <span class="stat-caption">рост за 2 года</span>
      </div>
    </div>
    <p style="font-size:1.3rem;color:var(--color-muted);margin:0 0 24px;font-family:var(--font-body);max-width:580px;line-height:1.5;">Объём рынка в 2025 составляет 6,8 трлн ₽ — при взрывном росте цифровых решений</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
      <span class="label-pill">14% → цифровых сейчас</span>
      <span class="label-pill">38% → к 2027</span>
      <span class="label-pill">×2,7 рост доли</span>
    </div>
  </div>
  <div class="stat-footer-band">
    <span style="font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">Источник: аналитика рынка грузоперевозок РФ, 2025</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 3: Три барьера цифровизации — icon-trio, bg-base, decor-glow -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-glow"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-body);">Ключевые вызовы</span>
    <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);">Три барьера цифровизации</h1>
    <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:48px;">
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="users" :size="28" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Фрагментация</span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">85% участников рынка — малый бизнес</span>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="clock" :size="28" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Устаревшие системы</span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Legacy IT на складах тормозит интеграцию</span>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="shield" :size="28" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Кадровый дефицит</span>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Нехватка специалистов с цифровыми компетенциями</span>
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

<!-- Slide 4: Секция — section-divider, bg-alt -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt);" class="section-glow"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;font-family:var(--font-body);">Часть II</span>
    <h1 style="font-size:3.6rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Решения, которые<br>уже работают</h1>
    <p style="font-size:1.3rem;color:var(--color-muted);max-width:620px;line-height:1.6;font-family:var(--font-body);">IoT-мониторинг и предиктивная аналитика — реальные кейсы российских компаний</p>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 5: IoT-мониторинг — bento-grid, bg-base, decor-arc -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-arc"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-body);">Технология</span>
    <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">IoT-мониторинг снижает потери на 34%</h1>
    <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
      <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="sensor" :size="26" color="var(--color-accent)" />
        </div>
        <span style="font-size:3rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">−28%</span>
        <span class="stat-caption" style="margin-top:6px;margin-bottom:14px;">порчи продуктов — кейс X5 Group</span>
        <p style="font-size:1.25rem;color:var(--color-muted);line-height:1.5;font-family:var(--font-body);margin:0;">Датчики температуры и влажности в рефрижераторах с автоматическими алертами при отклонениях</p>
      </div>
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="route" :size="20" color="var(--color-accent)" />
        </div>
        <div>
          <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">GPS-трекинг</span>
          <span style="display:block;font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">в реальном времени</span>
        </div>
      </div>
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="shield" :size="20" color="var(--color-accent)" />
        </div>
        <div>
          <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Автоалерты</span>
          <span style="display:block;font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">при отклонениях от нормы</span>
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

<!-- Slide 6: Предиктивная аналитика — two-col-text, bg-base, decor-dots -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-dots"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-body);">ML-решения</span>
    <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Предиктивная аналитика маршрутов</h1>
    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-content:center;">
      <div>
        <div class="card-solid" style="margin-bottom:14px;">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
            <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <Icon name="chart" :size="20" color="var(--color-accent)" />
            </div>
            <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">ML-оптимизация маршрутов</span>
          </div>
          <p style="font-size:1.25rem;color:var(--color-muted);margin:0;line-height:1.5;font-family:var(--font-body);">Модели машинного обучения анализируют исторические данные и строят оптимальные маршруты</p>
        </div>
        <div class="card-ghost">
          <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);display:block;margin-bottom:6px;">Экономия топлива</span>
          <span style="font-size:2.8rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">12–18%</span>
          <span class="stat-caption" style="display:block;margin-top:4px;">на весь парк автомобилей</span>
        </div>
      </div>
      <div>
        <div class="card-accent" style="margin-bottom:14px;">
          <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);display:block;margin-bottom:6px;">Сокращение простоев</span>
          <span style="font-size:2.8rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">до 40%</span>
          <span class="stat-caption" style="display:block;margin-top:4px;">снижение времени ожидания</span>
        </div>
        <div class="card-solid">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
            <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <Icon name="truck" :size="20" color="var(--color-accent)" />
            </div>
            <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Предиктивное ТО</span>
          </div>
          <p style="font-size:1.25rem;color:var(--color-muted);margin:0;line-height:1.5;font-family:var(--font-body);">Предупреждение поломок до их возникновения</p>
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

<!-- Slide 7: Секция — section-divider, bg-alt -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt);" class="section-glow"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;font-family:var(--font-body);">Часть III</span>
    <h1 style="font-size:3.6rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Что теряет бизнес<br>без цифровизации</h1>
    <p style="font-size:1.3rem;color:var(--color-muted);max-width:620px;line-height:1.6;font-family:var(--font-body);">Каждый месяц промедления — конкретные финансовые потери</p>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 8: Стоимость бездействия — stat-hero, bg-base, decor-glow -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-glow"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 96px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;font-family:var(--font-body);">Стоимость бездействия</span>
    <h1 style="font-size:5.5rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);">2,3 млн ₽</h1>
    <p style="font-size:1.3rem;color:var(--color-text);margin:10px 0 28px;font-family:var(--font-body);">ежемесячные потери на каждые 100 единиц парка</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-bottom:8px;">
      <span class="label-pill">Неоптимальные маршруты</span>
      <span class="label-pill">Штрафы за срывы сроков</span>
      <span class="label-pill">Порча грузов</span>
    </div>
  </div>
  <div class="stat-footer-band">
    <span style="font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">Расчёт на основе отраслевой статистики — средний парк 100 авт.</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 9: Дорожная карта — timeline-horizontal, bg-base, decor-arc -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:var(--bg-base);" class="slide-decor-arc"></div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-body);">План внедрения</span>
    <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Дорожная карта внедрения</h1>
    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:20px 18px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-body);">Q2 2026</span>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="chart" :size="16" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Аудит процессов</span>
        </div>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Диагностика текущего состояния логистики и IT-инфраструктуры</span>
      </div>
      <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.08),rgba(var(--accent-rgb),0.03));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:20px 18px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-body);">Q3 2026</span>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="sensor" :size="16" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Пилот IoT</span>
        </div>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Развёртывание IoT-мониторинга на пилотном парке транспорта</span>
      </div>
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:20px 18px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-body);">Q4 2026</span>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="truck" :size="16" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Масштабирование</span>
        </div>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Распространение IoT на всю сеть — полный охват парка</span>
      </div>
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:20px 18px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-body);">Q1 2027</span>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
          <div style="width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="chart" :size="16" color="var(--color-accent)" />
          </div>
          <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Предиктивная аналитика</span>
        </div>
        <span style="font-size:1.25rem;color:var(--color-muted);line-height:1.4;font-family:var(--font-body);">Запуск ML-платформы для оптимизации маршрутов и ТО</span>
      </div>
    </div>
    <div style="display:flex;justify-content:center;gap:24px;margin-top:12px;padding:10px 0;border-top:1px solid var(--color-surface-border);">
      <span style="display:flex;align-items:center;gap:6px;font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);display:inline-block;"></span>
        Аудит → Q2
      </span>
      <span style="display:flex;align-items:center;gap:6px;font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);display:inline-block;"></span>
        Пилот → Q3
      </span>
      <span style="display:flex;align-items:center;gap:6px;font-size:1.15rem;color:var(--color-muted);font-family:var(--font-body);">
        <span style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);display:inline-block;"></span>
        ROI → Q4+
      </span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 10: CTA — cta-warm, bg-accent -->
<div style="position:relative;width:100%;height:100%;">
  <div style="position:absolute;inset:0;z-index:0;background:linear-gradient(145deg, var(--color-accent) 0%, color-mix(in srgb, var(--color-accent) 70%, black) 100%);">
    <div class="cover-circle-accent"></div>
  </div>
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <span class="label-pill-cover" style="margin-bottom:20px;">Следующий шаг</span>
    <h1 style="font-size:2.9rem;font-weight:800;color:#ffffff;margin:0 0 28px;font-family:var(--font-heading);line-height:1.15;">Запросите демо платформы</h1>
    <div style="display:flex;flex-direction:column;gap:10px;max-width:560px;width:100%;margin-bottom:36px;">
      <div style="display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);border-radius:12px;padding:14px 20px;">
        <div class="icon-container-cover" style="width:36px;height:36px;flex-shrink:0;">
          <Icon name="chart" :size="18" color="#ffffff" />
        </div>
        <span style="font-size:1.25rem;color:#ffffff;font-family:var(--font-body);">Бесплатный аудит логистики за 5 дней</span>
      </div>
      <div style="display:flex;align-items:center;gap:12px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);border-radius:12px;padding:14px 20px;">
        <div class="icon-container-cover" style="width:36px;height:36px;flex-shrink:0;">
          <Icon name="truck" :size="18" color="#ffffff" />
        </div>
        <span style="font-size:1.25rem;color:#ffffff;font-family:var(--font-body);">Индивидуальный расчёт ROI под ваш парк</span>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.85);font-size:1.25rem;font-family:var(--font-body);">
      <div style="display:flex;align-items:center;gap:8px;">
        <Icon name="mail" :size="18" color="rgba(255,255,255,0.85)" />
        <span>logistics@example.ru</span>
      </div>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
      <div style="display:flex;align-items:center;gap:8px;">
        <Icon name="phone" :size="18" color="rgba(255,255,255,0.85)" />
        <span>@logistics_demo</span>
      </div>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
