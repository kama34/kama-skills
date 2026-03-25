---
theme: default
title: Онбординг в TaskFlow SaaS
colorSchema: light
fonts:
  sans: Outfit
  serif: DM Sans
  mono: JetBrains Mono
transition: fade
aspectRatio: '16/9'
layout: none
---

<!-- Slide 1: cover-hero — bg-accent | TIER 1 typography -->
<!-- eyebrow: 0/3 — cover slide exempt -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-a">
  <div class="cover-circle-accent"></div>
  <!-- Decorative radial glow top-left -->
  <div style="position:absolute;top:-80px;left:-80px;width:500px;height:500px;background:radial-gradient(circle,rgba(255,255,255,0.12),transparent 65%);pointer-events:none;"></div>
  <!-- Small circle rings bottom-right -->
  <div style="position:absolute;bottom:-40px;right:80px;width:220px;height:220px;border:3px solid rgba(255,255,255,0.14);border-radius:50%;pointer-events:none;"></div>
  <div style="position:absolute;bottom:10px;right:130px;width:120px;height:120px;border:2px solid rgba(255,255,255,0.10);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">SaaS Онбординг · v3.0</span>
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;">Добро пожаловать<br>в TaskFlow</h1>
  <p style="font-size:1.4rem;color:rgba(255,255,255,0.82);margin:0 0 36px;font-family:var(--font-body);max-width:600px;">Всё, что нужно для старта за 30 минут</p>
  <div style="display:flex;align-items:center;gap:20px;color:rgba(255,255,255,0.65);font-size:1.1rem;font-family:var(--font-body);">
    <span>15 000+ команд</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>40 стран</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>2026</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 2: stat-hero (centered) — bg-base | TIER 1 hero number -->
<!-- eyebrow: 1/3 — using eyebrow here -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots">
  <!-- Radial glow bottom-left -->
  <div style="position:absolute;bottom:-40px;left:-40px;width:440px;height:440px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.18),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">Доказанный результат</span>
  <h1 style="font-size:6rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);">12 часов</h1>
  <p style="font-size:1.5rem;color:var(--color-text);margin:12px 0 36px;font-family:var(--font-body);">экономит TaskFlow каждой команде каждую неделю</p>
  <div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">Управление задачами</span>
    <span class="label-pill">Спринты</span>
    <span class="label-pill">Документация</span>
    <span class="label-pill">Интеграции</span>
  </div>
  <div class="stat-footer-band">
    <span style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);">Slack · GitHub · Figma · Jira — в одном пространстве</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 3: section-divider VARIANT A (centered+glow) — bg-accent -->
<!-- eyebrow: 1/3 — section dividers exempt from eyebrow count -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="section-glow">
  <!-- Large translucent circle — required visual weight on bg-accent -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:420px;height:420px;border-radius:50%;border:2px solid rgba(255,255,255,0.14);pointer-events:none;"></div>
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:280px;height:280px;border-radius:50%;border:1.5px solid rgba(255,255,255,0.10);pointer-events:none;"></div>
  <!-- Ghost section number -->
  <div style="position:absolute;bottom:-20px;right:40px;font-size:9rem;font-weight:900;color:rgba(255,255,255,0.11);font-family:var(--font-heading);line-height:1;pointer-events:none;user-select:none;">01</div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.75);font-weight:600;margin-bottom:16px;">Часть I</span>
  <h1 style="font-size:3.8rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Настройка рабочего<br>пространства</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:640px;line-height:1.55;font-family:var(--font-body);">Создайте проект, пригласите команду и подключите инструменты за 30 минут</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 4: bento-grid — bg-base | Шаг 1: Создание проекта -->
<!-- eyebrow: 1/3 — not using eyebrow (structural break from two consecutive teal slides) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Top-right dot grid decorative -->
  <div style="position:absolute;top:0;right:0;width:320px;height:320px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.28) 1.5px,transparent 1.5px);background-size:20px 20px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">Шаг 1 — Создайте проект<br><span style="color:var(--color-accent);">за 2 минуты</span></h1>
  <div style="flex:1;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- Featured card: templates -->
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:16px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <div class="icon-container">
          <Icon name="kanban" :size="24" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">4 шаблона на старт</span>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;">
        <span style="font-size:0.85rem;background:var(--color-accent-bg);color:var(--color-accent);border:1px solid var(--color-accent-dim);border-radius:8px;padding:4px 12px;font-weight:600;">Scrum</span>
        <span style="font-size:0.85rem;background:var(--color-surface);color:var(--color-text);border:1px solid var(--color-surface-border);border-radius:8px;padding:4px 12px;font-weight:500;">Kanban</span>
        <span style="font-size:0.85rem;background:var(--color-surface);color:var(--color-text);border:1px solid var(--color-surface-border);border-radius:8px;padding:4px 12px;font-weight:500;">Waterfall</span>
        <span style="font-size:0.85rem;background:var(--color-surface);color:var(--color-text);border:1px solid var(--color-surface-border);border-radius:8px;padding:4px 12px;font-weight:500;">Custom</span>
      </div>
      <p style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;margin:0;">Готовые рабочие процессы, настраиваемые под вашу команду</p>
    </div>
    <!-- Card 2: import -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded">
        <Icon name="download" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;margin-bottom:2px;">Импорт из Jira/Trello</span>
        <span style="font-size:1.1rem;color:var(--color-muted);">Одним кликом</span>
      </div>
    </div>
    <!-- Card 3: custom fields -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded">
        <Icon name="settings" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;margin-bottom:2px;">Поля и статусы</span>
        <span style="font-size:1.1rem;color:var(--color-muted);">Настройка под ваш процесс</span>
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

<!-- Slide 5: icon-trio — bg-alt | Шаг 2: Команда -->
<!-- eyebrow: 2/3 — using eyebrow here -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);">
  <!-- Bottom-left radial glow, stronger on bg-alt -->
  <div style="position:absolute;bottom:-60px;left:-60px;width:480px;height:480px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.30),transparent 65%);pointer-events:none;"></div>
  <!-- Top-right arc, stronger stroke for bg-alt visibility -->
  <div style="position:absolute;top:-50px;right:-50px;width:300px;height:300px;border:6px solid rgba(var(--accent-rgb),0.55);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Шаг 2</span>
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);">Пригласите команду — роли под любую структуру</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:44px;">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="shield" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Owner / Admin</span>
      <span style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;">Полный доступ к настройкам и участникам</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="users" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Member</span>
      <span style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;">SSO через Google и Microsoft — без паролей</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:50%;background:rgba(var(--text-rgb),0.06);border:1.5px solid rgba(var(--text-rgb),0.15);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="link" :size="28" color="var(--color-muted)" />
      </div>
      <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Guest</span>
      <span style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;">Ограниченный доступ по проектам</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 6: card-mosaic with hierarchy — bg-base | Шаг 3: Интеграции -->
<!-- eyebrow: 2/3 — not using eyebrow (structural break from icon-trio) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Bottom-right glow decorative -->
  <div style="position:absolute;bottom:-60px;right:-60px;width:420px;height:420px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.18),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">Шаг 3 — Подключите инструменты<br>которые уже используете</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <!-- Card 1: GitHub — accent (hero card) -->
    <div style="background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),rgba(var(--accent-rgb),0.04));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div class="icon-container">
          <Icon name="github" :size="24" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">GitHub</span>
      </div>
      <p style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;margin:0;">Автосинхронизация коммитов и PR прямо в задаче</p>
    </div>
    <!-- Card 2: Slack — solid -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div class="icon-rounded">
          <Icon name="slack" :size="22" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Slack</span>
      </div>
      <p style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;margin:0;">Уведомления и создание задач из сообщений</p>
    </div>
    <!-- Card 3: Figma — solid -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div class="icon-container">
          <Icon name="figma" :size="22" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Figma</span>
      </div>
      <p style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;margin:0;">Превью макетов прямо внутри задачи</p>
    </div>
    <!-- Card 4: API — ghost style -->
    <div style="background:rgba(var(--bg-base-rgb),0.55);border:1.5px solid rgba(var(--text-rgb),0.10);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:space-between;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
        <div class="icon-rounded">
          <Icon name="api" :size="22" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">API & Webhooks</span>
      </div>
      <p style="font-size:1.2rem;color:var(--color-muted);line-height:1.4;margin:0;">Кастомные сценарии для любых систем</p>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 7: section-divider VARIANT B (left-aligned + ghost "07") — bg-accent -->
<!-- eyebrow: 2/3 — section dividers exempt -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- Bold horizontal rule — positioned BELOW text, as footer anchor -->
  <div style="position:absolute;bottom:80px;left:64px;right:64px;height:4px;background:rgba(255,255,255,0.25);pointer-events:none;"></div>
  <!-- Ghost number — large, right side -->
  <div style="position:absolute;right:-10px;top:-20px;font-size:11rem;font-weight:900;color:rgba(255,255,255,0.13);font-family:var(--font-heading);line-height:1;pointer-events:none;user-select:none;">02</div>
  <!-- Dot grid top-left -->
  <div style="position:absolute;top:0;left:0;width:300px;height:300px;background-image:radial-gradient(circle,rgba(255,255,255,0.18) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.70);font-weight:600;margin-bottom:14px;">Часть II</span>
  <h1 style="font-size:4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.05;">Ежедневная работа</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:560px;line-height:1.55;font-family:var(--font-body);">Доска, спринты и документация — всё в одном месте</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 8: asymmetric-split — bg-base | Доска задач -->
<!-- eyebrow: 2/3 — not using eyebrow (break after 2 teal slides) -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Arc bottom-left -->
  <div style="position:absolute;bottom:-60px;left:-60px;width:300px;height:300px;border:6px solid rgba(var(--accent-rgb),0.32);border-radius:50%;pointer-events:none;"></div>
  <!-- Small glow top-right -->
  <div style="position:absolute;top:-20px;right:-20px;width:280px;height:280px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.15),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:48px;align-items:center;">
  <!-- Left: visual element — large kanban icon in circle -->
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="width:180px;height:180px;border-radius:50%;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.14),rgba(var(--accent-rgb),0.04));border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
      <Icon name="kanban" :size="80" color="var(--color-accent)" />
    </div>
  </div>
  <!-- Right: text content -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Доска задач — ваш центр управления</h1>
    <div style="display:flex;flex-direction:column;gap:12px;">
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:8px;flex-shrink:0;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;">Drag-and-drop между статусами</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:8px;flex-shrink:0;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;">Фильтры по исполнителю, приоритету, спринту</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:8px;flex-shrink:0;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;">Горячие клавиши для быстрых действий</span>
      </div>
      <div style="display:flex;align-items:flex-start;gap:12px;">
        <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent-warm);margin-top:8px;flex-shrink:0;"></div>
        <span style="font-size:1.25rem;color:var(--color-text);line-height:1.4;">WIP-лимиты для контроля нагрузки</span>
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

<!-- Slide 9: two-col-text — bg-base | Спринт-планирование -->
<!-- eyebrow: 3/3 — LAST allowed eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Top-right dot grid -->
  <div style="position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.26) 1.5px,transparent 1.5px);background-size:20px 20px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Спринты</span>
  <h1 style="font-size:2.3rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);">Спринт-планирование за 10 минут</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-content:center;">
    <!-- Left column -->
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
        <div class="icon-container">
          <Icon name="zap" :size="22" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Авто-velocity</span>
      </div>
      <p style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;margin:0 0 24px;">TaskFlow автоматически рассчитывает скорость команды и предлагает оптимальный объём спринта</p>
      <div style="padding:16px 20px;background:var(--color-accent-bg);border-left:3px solid var(--color-accent);border-radius:0 10px 10px 0;">
        <span style="font-size:1.2rem;color:var(--color-accent);font-weight:600;">Подсказки по объёму — без угадывания</span>
      </div>
    </div>
    <!-- Right column -->
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
        <div class="icon-rounded">
          <Icon name="check" :size="22" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Перенос задач</span>
      </div>
      <p style="font-size:1.25rem;color:var(--color-muted);line-height:1.45;margin:0 0 24px;">Незакрытые задачи переносятся в новый спринт одним кликом — без ручного перебора</p>
      <div style="padding:16px 20px;background:rgba(var(--accent-rgb),0.05);border:1px solid var(--color-surface-border);border-radius:10px;">
        <span style="font-size:1.2rem;color:var(--color-text);font-weight:500;">Ретроспектива сразу после спринта</span>
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

<!-- Slide 10: stat-hero VARIANT D (text hero / asymmetric) — bg-alt | Документация -->
<!-- eyebrow: 3/3 — LIMIT REACHED — NO eyebrow on this slide -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);">
  <!-- Radial glow bottom-right, stronger for bg-alt -->
  <div style="position:absolute;bottom:-80px;right:-80px;width:520px;height:520px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.28),transparent 65%);pointer-events:none;"></div>
  <!-- Arc top-left -->
  <div style="position:absolute;top:-50px;left:-50px;width:260px;height:260px;border:6px solid rgba(var(--accent-rgb),0.45);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:3fr 2fr;padding:44px 64px;gap:48px;align-items:center;">
  <!-- Left: text hero — large statement -->
  <div>
    <h1 style="font-size:3rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">Документация живёт<br><span style="color:var(--color-accent);">рядом с задачами</span></h1>
    <p style="font-size:1.3rem;color:var(--color-muted);line-height:1.5;margin:0 0 20px;">Встроенный wiki-редактор. Связь задача — документ: никаких вкладок, никаких потерь контекста</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;">
      <span class="label-pill">Версионирование</span>
      <span class="label-pill">Комментарии</span>
      <span class="label-pill">Wiki-редактор</span>
    </div>
  </div>
  <!-- Right: supporting visual — book icon in large circle -->
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="width:160px;height:160px;border-radius:50%;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.18),rgba(var(--accent-rgb),0.06));border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
      <Icon name="book" :size="72" color="var(--color-accent)" />
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 11: section-divider VARIANT C (full-width + horizontal rule) — bg-accent -->
<!-- eyebrow: 3/3 — section dividers exempt -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);">
  <!-- Full-width horizontal accent line -->
  <div style="position:absolute;top:50%;left:0;right:0;height:4px;background:rgba(255,255,255,0.25);transform:translateY(52px);pointer-events:none;"></div>
  <!-- Large transparent circle — anchors right side -->
  <div style="position:absolute;right:-80px;top:50%;transform:translateY(-50%);width:420px;height:420px;border-radius:50%;border:3px solid rgba(255,255,255,0.16);pointer-events:none;"></div>
  <div style="position:absolute;right:-20px;top:50%;transform:translateY(-50%);width:260px;height:260px;border-radius:50%;border:2px solid rgba(255,255,255,0.10);pointer-events:none;"></div>
  <!-- Ghost number -->
  <div style="position:absolute;left:-10px;bottom:-30px;font-size:10rem;font-weight:900;color:rgba(255,255,255,0.12);font-family:var(--font-heading);line-height:1;pointer-events:none;user-select:none;">03</div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <h1 style="font-size:4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.1;">Аналитика и отчёты</h1>
  <p style="font-size:1.3rem;color:rgba(255,255,255,0.78);max-width:600px;line-height:1.55;font-family:var(--font-body);">Видеть — значит управлять. Все данные команды в реальном времени</p>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 12: bento-grid — bg-base | Дашборд руководителя -->
<!-- eyebrow: 3/3 — LIMIT REACHED — no eyebrow, heading speaks for itself -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Dot grid top-right -->
  <div style="position:absolute;top:0;right:0;width:300px;height:300px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.26) 1.5px,transparent 1.5px);background-size:20px 20px;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.2rem;font-weight:800;color:var(--color-text);margin:0 0 18px;font-family:var(--font-heading);line-height:1.1;">Дашборд руководителя —<br><span style="color:var(--color-accent);">все метрики на одном экране</span></h1>
  <div style="flex:1;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- Featured card: burndown/burnup -->
    <div style="grid-row:1/3;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:16px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
        <div class="icon-container">
          <Icon name="chart" :size="24" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Burndown / Burnup</span>
      </div>
      <p style="font-size:1.2rem;color:var(--color-muted);line-height:1.45;margin:0 0 16px;">Динамика выполнения спринта в реальном времени</p>
      <!-- Mini chart mockup using CSS bars -->
      <div style="display:flex;align-items:flex-end;gap:6px;height:48px;margin-top:8px;">
        <div style="flex:1;background:var(--color-accent);opacity:0.9;border-radius:3px 3px 0 0;height:100%;"></div>
        <div style="flex:1;background:var(--color-accent);opacity:0.75;border-radius:3px 3px 0 0;height:80%;"></div>
        <div style="flex:1;background:var(--color-accent);opacity:0.60;border-radius:3px 3px 0 0;height:65%;"></div>
        <div style="flex:1;background:var(--color-accent);opacity:0.45;border-radius:3px 3px 0 0;height:45%;"></div>
        <div style="flex:1;background:var(--color-accent);opacity:0.30;border-radius:3px 3px 0 0;height:28%;"></div>
        <div style="flex:1;background:rgba(var(--accent-rgb),0.15);border-radius:3px 3px 0 0;height:15%;border:1px dashed var(--color-accent-dim);"></div>
      </div>
    </div>
    <!-- Card 2: velocity -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded">
        <Icon name="zap" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;margin-bottom:2px;">Velocity по спринтам</span>
        <span style="font-size:1.1rem;color:var(--color-muted);">Прогресс команды в динамике</span>
      </div>
    </div>
    <!-- Card 3: export -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:14px;">
      <div class="icon-rounded">
        <Icon name="download" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.25rem;font-weight:700;color:var(--color-text);display:block;margin-bottom:2px;">Экспорт в PDF</span>
        <span style="font-size:1.1rem;color:var(--color-muted);">Отчёт за 1 клик</span>
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

<!-- Slide 13: asymmetric-split — bg-alt | Авто-отчёты -->
<!-- eyebrow: 3/3 — LIMIT REACHED — no eyebrow -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);">
  <!-- Glow top-right, stronger for bg-alt -->
  <div style="position:absolute;top:-60px;right:-60px;width:480px;height:480px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.32),transparent 65%);pointer-events:none;"></div>
  <!-- Arc bottom-left -->
  <div style="position:absolute;bottom:-60px;left:-60px;width:280px;height:280px;border:6px solid rgba(var(--accent-rgb),0.48);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:3fr 2fr;padding:44px 64px;gap:48px;align-items:center;">
  <!-- Left: text content -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <h1 style="font-size:2.4rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Автоматические отчёты<br>каждую пятницу</h1>
    <div style="display:grid;grid-template-rows:1fr 1fr 1fr;gap:12px;">
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;">
        <div class="icon-container">
          <Icon name="check" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);">Что сделано / в работе / заблокировано</span>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;">
        <div class="icon-rounded">
          <Icon name="slack" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);">Отправка в Slack-канал или на email</span>
      </div>
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;">
        <div class="icon-rounded">
          <Icon name="settings" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.25rem;color:var(--color-text);">Настраиваемый шаблон отчёта</span>
      </div>
    </div>
  </div>
  <!-- Right: visual element -->
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="width:160px;height:160px;border-radius:50%;background:linear-gradient(145deg,rgba(var(--accent-rgb),0.18),rgba(var(--accent-rgb),0.06));border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
      <Icon name="mail" :size="72" color="var(--color-accent)" />
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 14: icon-trio — bg-base | Поддержка и ресурсы -->
<!-- eyebrow: 3/3 — LIMIT REACHED — no eyebrow, heading speaks for itself -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);">
  <!-- Bottom-right glow -->
  <div style="position:absolute;bottom:-60px;right:-60px;width:440px;height:440px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.20),transparent 65%);pointer-events:none;"></div>
  <!-- Top-left arc -->
  <div style="position:absolute;top:-40px;left:-40px;width:240px;height:240px;border:5px solid rgba(var(--accent-rgb),0.30);border-radius:50%;pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <h1 style="font-size:2.1rem;font-weight:800;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">Поддержка — ответ за 5 минут, сообщество 8 000+ участников</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:44px;">
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="book" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Документация</span>
      <span style="font-size:1.15rem;color:var(--color-muted);line-height:1.4;">docs.taskflow.io</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="message" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Чат поддержки</span>
      <span style="font-size:1.15rem;color:var(--color-muted);line-height:1.4;">Ответ менее 5 минут</span>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:190px;">
      <div style="width:72px;height:72px;border-radius:50%;background:rgba(var(--text-rgb),0.06);border:1.5px solid rgba(var(--text-rgb),0.14);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
        <Icon name="users" :size="28" color="var(--color-muted)" />
      </div>
      <span style="font-size:1.3rem;font-weight:700;color:var(--color-text);margin-bottom:6px;font-family:var(--font-heading);">Community</span>
      <span style="font-size:1.15rem;color:var(--color-muted);line-height:1.4;">Discord 8 000+ участников</span>
    </div>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>

---
layout: none
---

<!-- Slide 15: cta-warm — bg-accent | Pro-план -->
<!-- eyebrow: 3/3 — CTA slide exempt -->
<div style="position:absolute;inset:0;z-index:0;background:linear-gradient(145deg, var(--bg-accent, #0D9488) 0%, #0a6e65 100%);">
  <!-- Decorative dot grid overlay -->
  <div style="position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,0.14) 1.5px,transparent 1.5px);background-size:26px 26px;pointer-events:none;"></div>
  <!-- Large circle top-right -->
  <div style="position:absolute;top:-80px;right:-80px;width:380px;height:380px;border-radius:50%;border:2.5px solid rgba(255,255,255,0.16);pointer-events:none;"></div>
  <div style="position:absolute;top:-20px;right:-20px;width:220px;height:220px;border-radius:50%;border:1.5px solid rgba(255,255,255,0.10);pointer-events:none;"></div>
  <!-- Warm amber glow bottom-left for warmth -->
  <div style="position:absolute;bottom:-40px;left:-40px;width:400px;height:400px;background:radial-gradient(circle,rgba(217,119,6,0.18),transparent 65%);pointer-events:none;"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:20px;">Специальное предложение</span>
  <h1 style="font-size:2.9rem;font-weight:800;color:#ffffff;margin:0 0 32px;font-family:var(--font-heading);line-height:1.1;">Активируйте Pro-план —<br>14 дней бесплатно</h1>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:580px;width:100%;margin-bottom:36px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.28);border-radius:12px;padding:14px 20px;">
      <div style="width:28px;height:28px;border-radius:50%;background:rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="check" :size="16" color="#ffffff" />
      </div>
      <span style="font-size:1.25rem;color:#ffffff;text-align:left;">Все интеграции без ограничений</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.28);border-radius:12px;padding:14px 20px;">
      <div style="width:28px;height:28px;border-radius:50%;background:rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="check" :size="16" color="#ffffff" />
      </div>
      <span style="font-size:1.25rem;color:#ffffff;text-align:left;">Неограниченные проекты и участники</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.25);border:2px solid rgba(255,255,255,0.55);border-radius:12px;padding:14px 20px;">
      <div style="width:28px;height:28px;border-radius:50%;background:rgba(217,119,6,0.80);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="star" :size="16" color="#ffffff" />
      </div>
      <span style="font-size:1.25rem;color:#ffffff;font-weight:700;text-align:left;">Промокод: WELCOME2026</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.85);font-size:1.3rem;font-family:var(--font-heading);font-weight:700;">
    <span style="color:#ffffff;">taskflow.io/start</span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; overflow: hidden; }
</style>
