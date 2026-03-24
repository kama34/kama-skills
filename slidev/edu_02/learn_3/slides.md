---
theme: default
colorSchema: light
transition: fade
aspectRatio: "16/9"
fonts:
  heading: Outfit
  body: DM Sans
  mono: JetBrains Mono
css: styles/index.css
---

<!-- ============================================================ -->
<!-- SLIDE 1 — COVER (cover-hero, bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-c">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">MedConnect · Телемедицина 2025</span>
  <h1 style="font-size:3.4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;">Доступная медицина<br>без расстояний</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Платформа телемедицины для региональных клиник</p>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.65);font-size:1rem;">
    <span>MedConnect</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Телемедицина для регионов</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>2025</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 2 — STAT-HERO (centered, bg-base): 62 млн россиян -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 100px;">
  <div class="stat-hero" style="font-size:6rem;">62 млн</div>
  <p style="font-size:1.5rem;color:var(--color-text);margin:12px 0 8px;font-family:var(--font-body);font-weight:500;">россиян не имеют доступа к узким специалистам</p>
  <p style="font-size:1.1rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);">Дефицит врачей в сельской местности критичен — 43% районов без специалистов</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">43% дефицит врачей</span>
    <span class="label-pill">28 дней до приёма</span>
    <span class="label-pill">17% отказов от лечения</span>
  </div>
</div>
<div class="stat-footer-band">
  <span style="font-size:0.85rem;color:var(--color-muted);">Источник: Минздрав РФ · Анализ кадрового дефицита в здравоохранении, 2024</span>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 3 — SECTION DIVIDER (centered + glow, bg-accent) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="section-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <h1 style="font-size:3.5rem;font-weight:800;color:#ffffff;margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Как это решает<br>MedConnect</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.80);max-width:600px;line-height:1.6;font-family:var(--font-body);">Платформа соединяет пациентов с врачами-специалистами — без очередей, поездок и барьеров</p>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 4 — BENTO-GRID (bg-base): Платформа MedConnect -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Платформа соединяет пациента и врача за 15 минут</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- Featured: видеоконсультации -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(13,148,136,0.12),rgba(255,255,255,0.8));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div class="icon-circle" style="width:64px;height:64px;margin-bottom:20px;">
        <Icon name="video" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.4rem;font-weight:700;color:var(--color-text);margin-bottom:10px;font-family:var(--font-heading);">Видеоконсультации<br>с узкими специалистами</span>
      <span style="font-size:1.05rem;color:var(--color-muted);line-height:1.5;">Подключение за 15 минут. Кардиологи, неврологи, эндокринологи — без ожидания.</span>
    </div>
    <!-- Item 2: МИС интеграция -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:16px;">
      <div class="icon-rounded" style="width:48px;height:48px;flex-shrink:0;">
        <Icon name="database" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Интеграция с МИС</span>
        <span style="font-size:0.95rem;color:var(--color-muted);">Работает с существующими системами клиники</span>
      </div>
    </div>
    <!-- Item 3: рецепты + устройства -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:16px;">
      <div class="icon-ghost" style="width:48px;height:48px;flex-shrink:0;">
        <Icon name="check" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Рецепты и направления</span>
        <span style="font-size:0.95rem;color:var(--color-muted);">Электронные документы — на любом устройстве</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 5 — STAT-HERO (asymmetric, bg-alt): Результаты пилота -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <!-- Left: hero metric -->
  <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;">
    <span class="label-pill" style="margin-bottom:16px;">Тверская область · 6 мес.</span>
    <div class="stat-hero" style="font-size:5.5rem;margin-bottom:8px;">12 000</div>
    <span class="stat-caption">консультаций проведено</span>
    <div style="margin-top:20px;padding:16px 20px;background:var(--color-surface);border:1.5px solid var(--color-accent-dim);border-radius:12px;">
      <span style="font-size:1rem;color:var(--color-muted);">Пилот охватил</span>
      <span style="display:block;font-size:1.4rem;font-weight:700;color:var(--color-accent);">5 клиник · 48 врачей</span>
    </div>
  </div>
  <!-- Right: result cards -->
  <div style="display:flex;flex-direction:column;gap:12px;justify-content:center;">
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(13,148,136,0.10);border:1.5px solid rgba(13,148,136,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:1.1rem;font-weight:800;color:var(--color-accent);">82</span>
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">NPS пациентов</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Высший показатель в регионе</span>
      </div>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(13,148,136,0.10);border:1.5px solid rgba(13,148,136,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:1.1rem;font-weight:800;color:var(--color-accent);">76</span>
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">NPS врачей</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Врачи довольны платформой</span>
      </div>
    </div>
    <div style="background:linear-gradient(135deg,rgba(13,148,136,0.08),rgba(13,148,136,0.03));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:12px;background:rgba(13,148,136,0.10);border:1.5px solid rgba(13,148,136,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="activity" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">Очереди сокращены на 58%</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Экономия пациентам 4 200 ₽ на поездках</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 6 — ASYMMETRIC-SPLIT (bg-base): 340₽ за консультацию -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <!-- Left: big metric -->
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="text-align:center;">
      <div class="stat-hero" style="font-size:4.5rem;">340 ₽</div>
      <span class="stat-caption" style="display:block;margin-top:8px;">за консультацию</span>
      <div style="margin-top:16px;padding:10px 16px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:10px;">
        <span style="font-size:0.9rem;color:var(--color-accent);font-weight:600;">В 8 раз дешевле очного визита</span>
      </div>
    </div>
  </div>
  <!-- Right: breakdown -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <h1 style="font-size:1.9rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.2;">Экономика, которая работает для всех</h1>
    <div style="display:flex;flex-direction:column;gap:10px;">
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div class="icon-circle" style="width:40px;height:40px;flex-shrink:0;">
          <Icon name="heart" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">Для клиники</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Подписка или оплата за консультацию</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div class="icon-rounded" style="width:40px;height:40px;flex-shrink:0;">
          <Icon name="activity" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">ROI для региона</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">3,2x окупаемость за первый год</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,rgba(13,148,136,0.07),rgba(13,148,136,0.02));border:1.5px solid var(--color-accent-dim);border-radius:10px;padding:14px 18px;">
        <div class="icon-ghost" style="width:40px;height:40px;flex-shrink:0;">
          <Icon name="users" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">Для пациента</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Экономия до 4 200 ₽ на транспорте и времени</span>
        </div>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 7 — ICON-TRIO (bg-base): Безопасность данных -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 10px;font-family:var(--font-heading);">Безопасность данных — ГОСТ Р и 152-ФЗ</h1>
  <p style="font-size:1.05rem;color:var(--color-muted);margin:0 0 24px;">Каждый уровень защиты сертифицирован и проверяется независимым аудитом</p>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:40px;">
    <!-- Icon 1: шифрование — circle -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:200px;">
      <div class="icon-circle" style="width:72px;height:72px;margin-bottom:16px;">
        <Icon name="lock" :size="30" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Шифрование end-to-end</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Данные пациентов защищены на каждом этапе передачи</span>
    </div>
    <!-- Icon 2: хранение — rounded -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:200px;">
      <div class="icon-rounded" style="width:72px;height:72px;margin-bottom:16px;">
        <Icon name="database" :size="30" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Хранение в России</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Серверы на территории РФ, соответствие 152-ФЗ</span>
    </div>
    <!-- Icon 3: сертификация — ghost -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:200px;">
      <div class="icon-ghost" style="width:72px;height:72px;margin-bottom:16px;">
        <Icon name="shield" :size="30" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);margin-bottom:6px;">Сертификация ФСТЭК</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Аудит безопасности каждые 6 месяцев</span>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 8 — TIMELINE-HORIZONTAL (bg-alt): Интеграция за 2 недели -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Интеграция за 2 недели без замены текущих систем</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <!-- Stage 1 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">День 1–2</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Аудит МИС</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Анализ текущей инфраструктуры клиники</span>
    </div>
    <!-- Stage 2 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">День 3–7</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Подключение API</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Настройка интеграции с действующей МИС</span>
    </div>
    <!-- Stage 3 -->
    <div style="background:linear-gradient(135deg,rgba(13,148,136,0.09),rgba(13,148,136,0.03));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">День 8–10</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Обучение персонала</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">4 часа на врача и медсестру — и команда готова</span>
    </div>
    <!-- Stage 4 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">День 11–14</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Тестовый запуск</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Первые консультации под контролем команды</span>
    </div>
    <!-- Stage 5 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Постоянно</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Техподдержка 24/7</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Выделенный менеджер и круглосуточная поддержка</span>
    </div>
    <!-- Stage 6 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Результат</span>
      <span style="font-size:1rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Полная готовность</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Платформа работает, врачи ведут консультации</span>
    </div>
  </div>
  <div style="display:flex;justify-content:center;gap:24px;margin-top:12px;padding:10px 0;border-top:1px solid var(--color-surface-border);">
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">14 дней</strong> — от договора до первой консультации</span>
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">0 замен</strong> — работаем поверх вашей МИС</span>
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">4 часа</strong> — обучение сотрудника</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 9 — CTA-WARM (bg-accent): Запросите пилот -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);background:linear-gradient(145deg, var(--bg-accent, #0D9488) 0%, #0a7a70 100%);" class="cover-variant-a">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:20px;">Специальное предложение</span>
  <h1 style="font-size:2.8rem;font-weight:800;color:#ffffff;margin:0 0 12px;font-family:var(--font-heading);line-height:1.15;">Запросите пилот для вашего региона —<br>это бесплатно</h1>
  <p style="font-size:1.1rem;color:rgba(255,255,255,0.80);margin:0 0 32px;max-width:620px;line-height:1.5;">3 месяца полноценного пилота без оплаты. Вы убедитесь в результате сами, прежде чем подписать контракт.</p>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:560px;width:100%;margin-bottom:32px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:10px;padding:12px 20px;text-align:left;">
      <div class="icon-container-cover" style="width:40px;height:40px;flex-shrink:0;">
        <Icon name="clock" :size="18" color="#ffffff" />
      </div>
      <span style="font-size:1rem;color:#ffffff;font-weight:500;">3 месяца бесплатного пилота — без ограничений по функциям</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:10px;padding:12px 20px;text-align:left;">
      <div class="icon-container-cover" style="width:40px;height:40px;flex-shrink:0;">
        <Icon name="users" :size="18" color="#ffffff" />
      </div>
      <span style="font-size:1rem;color:#ffffff;font-weight:500;">До 50 врачей и 5 клиник в рамках пилота</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.80);font-size:1rem;">
    <div style="display:flex;align-items:center;gap:8px;">
      <Icon name="mail" :size="16" color="rgba(255,255,255,0.80)" />
      <span>pilot@medconnect.ru</span>
    </div>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <div style="display:flex;align-items:center;gap:8px;">
      <Icon name="phone" :size="16" color="rgba(255,255,255,0.80)" />
      <span>medconnect.ru</span>
    </div>
  </div>
</div>
