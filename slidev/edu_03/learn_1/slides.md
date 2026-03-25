---
theme: default
layout: none
colorSchema: light
fonts:
  sans: Sora
  body: IBM Plex Sans
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
title: CyberShield — Кибербезопасность для среднего бизнеса
---

<!-- ============================================================ -->
<!-- SLIDE 1: Cover Hero — bg-accent (teal) -->
<!-- Archetype: cover-hero -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-accent);overflow:hidden;">
  <!-- Radial glow decoration -->
  <div style="position:absolute;top:-120px;right:-120px;width:560px;height:560px;background:radial-gradient(circle,rgba(255,255,255,0.14) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>
  <!-- Dot grid decoration -->
  <div style="position:absolute;bottom:20px;left:40px;width:280px;height:200px;background-image:radial-gradient(circle,rgba(255,255,255,0.32) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>
  <!-- Arc decoration -->
  <div style="position:absolute;bottom:-80px;right:80px;width:340px;height:340px;border:2px solid rgba(255,255,255,0.18);border-radius:50%;pointer-events:none;"></div>

  <!-- Content -->
  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <div style="display:inline-flex;align-items:center;justify-content:center;line-height:1;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;margin-bottom:28px;">
      <span style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:#FFFFFF;font-weight:600;font-family:var(--font-heading);">Раунд А · Март 2026</span>
    </div>
    <h1 style="font-size:4rem;font-weight:800;color:#FFFFFF;margin:0 0 14px;font-family:var(--font-heading);line-height:1.06;letter-spacing:-0.02em;">CyberShield</h1>
    <p style="font-size:1.4rem;color:rgba(255,255,255,0.88);margin:0 0 32px;font-family:var(--font-body);font-weight:300;max-width:640px;">Защита, которая работает, пока вы спите</p>
    <div style="display:flex;align-items:center;gap:20px;color:rgba(255,255,255,0.72);font-size:0.95rem;font-family:var(--font-body);">
      <span>Кибербезопасность для среднего бизнеса</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);display:inline-block;"></span>
      <span>100–1000 сотрудников</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);display:inline-block;"></span>
      <span>Россия</span>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 2: Stat Hero — left-number-right-text — bg-base -->
<!-- Archetype: stat-hero (left-number-right-text variant) -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-base);overflow:hidden;">
  <!-- Glow decoration top-right -->
  <div style="position:absolute;top:-80px;right:-60px;width:440px;height:440px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>
  <!-- Dot grid bottom-left -->
  <div style="position:absolute;bottom:30px;left:50px;width:240px;height:180px;background-image:radial-gradient(circle,rgba(13,148,136,0.42) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:1fr 1fr;padding:48px 64px;gap:48px;align-items:center;">
    <!-- Left: hero number -->
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
        <Icon name="alert" :size="30" color="var(--color-accent)" />
      </div>
      <div style="font-size:6rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">74%</div>
      <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:8px;letter-spacing:0.04em;text-transform:uppercase;font-size:0.72rem;font-weight:600;">компаний среднего бизнеса</div>
    </div>

    <!-- Right: context text -->
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:10px;font-family:var(--font-heading);">Масштаб угрозы</span>
      <h1 style="font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.15;">Атакованы за последние 12 месяцев</h1>

      <div style="display:flex;flex-direction:column;gap:14px;">
        <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;">
          <div style="width:40px;height:40px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="dollar" :size="18" color="var(--color-accent)" />
          </div>
          <div>
            <div style="font-size:1.6rem;font-weight:800;color:#D97706;line-height:1;font-family:var(--font-heading);">4,2 млн ₽</div>
            <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">средний ущерб одной атаки</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;">
          <div style="width:40px;height:40px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <Icon name="briefcase" :size="18" color="var(--color-accent)" />
          </div>
          <div>
            <div style="font-size:1.6rem;font-weight:800;color:var(--color-text);line-height:1;font-family:var(--font-heading);">60%</div>
            <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">закрываются в течение 6 месяцев после инцидента</div>
          </div>
        </div>
      </div>
      <p style="font-size:0.72rem;color:var(--color-muted);margin-top:16px;font-family:var(--font-body);">Источник: Positive Technologies, 2025</p>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 3: Asymmetric Split — hero metric + context — bg-alt -->
<!-- Archetype: asymmetric-split -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-alt);overflow:hidden;">
  <!-- Glow left -->
  <div style="position:absolute;top:50%;left:-100px;transform:translateY(-50%);width:480px;height:480px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>
  <!-- Arc right -->
  <div style="position:absolute;bottom:-60px;right:-60px;width:300px;height:300px;border:2px solid rgba(13,148,136,0.25);border-radius:50%;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
    <!-- Left: big visual metric -->
    <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
      <div style="font-size:5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">350K</div>
      <div style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;text-align:center;">₽ / месяц</div>
      <div style="margin-top:24px;width:64px;height:64px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;">
        <Icon name="clock" :size="28" color="var(--color-accent)" />
      </div>
    </div>

    <!-- Right: text content -->
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:8px;font-family:var(--font-heading);">Стоимость бездействия</span>
      <h1 style="font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 22px;font-family:var(--font-heading);line-height:1.15;">Каждый месяц без защиты — потенциальные потери</h1>

      <div style="display:flex;flex-direction:column;gap:12px;">
        <div style="display:flex;align-items:flex-start;gap:12px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:7px;flex-shrink:0;"></div>
          <span style="font-size:1.15rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Ransomware-атаки выросли на <strong style="color:var(--color-accent);">130%</strong> за год</span>
        </div>
        <div style="display:flex;align-items:flex-start;gap:12px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:7px;flex-shrink:0;"></div>
          <span style="font-size:1.15rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Средний простой после атаки — <strong style="color:var(--color-accent);">21 день</strong></span>
        </div>
        <div style="display:flex;align-items:flex-start;gap:12px;">
          <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:7px;flex-shrink:0;"></div>
          <span style="font-size:1.15rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Репутационные потери невосполнимы</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 4: Icon Trio — 3 protection vectors — bg-base -->
<!-- Archetype: icon-trio -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-base);overflow:hidden;">
  <!-- Glow top-left -->
  <div style="position:absolute;top:-100px;left:-80px;width:400px;height:400px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>
  <!-- Dot grid bottom-right -->
  <div style="position:absolute;bottom:20px;right:40px;width:260px;height:200px;background-image:radial-gradient(circle,rgba(13,148,136,0.42) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Решение</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">CyberShield закрывает 95% векторов атак за 48 часов</h1>

    <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:40px;">
      <!-- Item 1: AI monitoring -->
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="brain" :size="30" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);margin-bottom:8px;font-family:var(--font-heading);">AI-мониторинг 24/7</span>
        <span style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.45;">Автоматическое реагирование на инциденты без участия человека</span>
      </div>

      <!-- Vertical divider -->
      <div style="width:1px;height:140px;background:var(--color-surface-border);flex-shrink:0;"></div>

      <!-- Item 2: Multi-vector protection -->
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="layers" :size="30" color="var(--color-accent)" />
        </div>
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);margin-bottom:8px;font-family:var(--font-heading);">Почта, эндпоинты, облако</span>
        <span style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.45;">Комплексная защита всех векторов в одном решении</span>
      </div>

      <!-- Vertical divider -->
      <div style="width:1px;height:140px;background:var(--color-surface-border);flex-shrink:0;"></div>

      <!-- Item 3: Fast integration -->
      <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:210px;">
        <div style="width:72px;height:72px;border-radius:12px;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.35);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="zap" :size="30" color="#D97706" />
        </div>
        <span style="font-size:1.2rem;font-weight:700;color:var(--color-text);margin-bottom:8px;font-family:var(--font-heading);">Интеграция за 48 часов</span>
        <span style="font-size:1rem;color:var(--color-muted);font-family:var(--font-body);line-height:1.45;">Без остановки бизнес-процессов и простоев</span>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 5: Comparison Table — 3 pricing tiers — bg-alt -->
<!-- Archetype: comparison-table -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-alt);overflow:hidden;">
  <!-- Arc decoration top-right -->
  <div style="position:absolute;top:-60px;right:-60px;width:320px;height:320px;border:2px solid rgba(13,148,136,0.25);border-radius:50%;pointer-events:none;"></div>
  <!-- Dot grid left -->
  <div style="position:absolute;top:50px;left:20px;width:200px;height:280px;background-image:radial-gradient(circle,rgba(13,148,136,0.42) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Тарифы</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Три уровня защиты — от базового до enterprise</h1>

    <div style="flex:1;display:grid;grid-template-rows:1fr 1fr 1fr;gap:12px;align-items:stretch;">
      <!-- Basic -->
      <div style="display:flex;align-items:center;gap:16px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:0 24px;">
        <div style="width:44px;height:44px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="mail" :size="20" color="var(--color-accent)" />
        </div>
        <div style="flex:1;">
          <div style="display:flex;align-items:baseline;gap:8px;">
            <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Basic</span>
            <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">Почта + антифишинг</span>
          </div>
        </div>
        <div style="text-align:right;flex-shrink:0;">
          <span style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">25 000 ₽</span>
          <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);display:block;">/месяц</span>
        </div>
      </div>

      <!-- Pro -->
      <div style="display:flex;align-items:center;gap:16px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:0 24px;">
        <div style="width:44px;height:44px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="shield" :size="20" color="var(--color-accent)" />
        </div>
        <div style="flex:1;">
          <div style="display:flex;align-items:baseline;gap:8px;">
            <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Pro</span>
            <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">+ эндпоинты + SIEM-мониторинг</span>
          </div>
        </div>
        <div style="text-align:right;flex-shrink:0;">
          <span style="font-size:1.6rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">75 000 ₽</span>
          <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);display:block;">/месяц</span>
        </div>
      </div>

      <!-- Enterprise -->
      <div style="display:flex;align-items:center;gap:16px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:0 24px;">
        <div style="width:44px;height:44px;border-radius:12px;background:var(--color-accent);border:1.5px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="star" :size="20" color="#FFFFFF" />
        </div>
        <div style="flex:1;">
          <div style="display:flex;align-items:baseline;gap:8px;">
            <span style="font-size:1.15rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Enterprise</span>
            <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">+ SOC 24/7 + пентесты</span>
          </div>
        </div>
        <div style="text-align:right;flex-shrink:0;">
          <span style="font-size:1.6rem;font-weight:800;color:#D97706;font-family:var(--font-heading);">180 000 ₽</span>
          <span style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);display:block;">/месяц</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 6: Bento Grid — market size + key stats — bg-base -->
<!-- Archetype: bento-grid -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-base);overflow:hidden;">
  <!-- Glow top-right -->
  <div style="position:absolute;top:-100px;right:-80px;width:480px;height:480px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Рынок</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);line-height:1.1;">Рынок кибербезопасности РФ удвоится к 2028</h1>

    <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
      <!-- Featured card: market size -->
      <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(13,148,136,0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
        <div style="width:52px;height:52px;border-radius:50%;background:rgba(13,148,136,0.12);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
          <Icon name="globe" :size="22" color="var(--color-accent)" />
        </div>
        <div style="font-size:4.2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">350</div>
        <div style="font-size:1.1rem;color:var(--color-muted);font-family:var(--font-body);margin-top:4px;margin-bottom:20px;">млрд ₽ к 2028 году</div>

        <div style="display:flex;gap:10px;">
          <div style="display:inline-flex;align-items:center;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 14px;line-height:1;">
            <span style="font-size:0.7rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.12em;font-family:var(--font-heading);">CAGR 24%</span>
          </div>
          <div style="display:inline-flex;align-items:center;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.35);border-radius:20px;padding:6px 14px;line-height:1;">
            <span style="font-size:0.7rem;color:#D97706;font-weight:700;text-transform:uppercase;letter-spacing:0.12em;font-family:var(--font-heading);">+3 года роста</span>
          </div>
        </div>
      </div>

      <!-- Side card 1: underserved segment -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="target" :size="20" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);line-height:1.2;">Средний бизнес</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:3px;line-height:1.4;">100–1000 сотрудников — самый недозащищённый сегмент</div>
        </div>
      </div>

      <!-- Side card 2: regulatory pressure -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
        <div style="width:44px;height:44px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="flag" :size="20" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);line-height:1.2;">Регуляторное давление</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:3px;line-height:1.4;">152-ФЗ, ФСТЭК, ЦБ ужесточают требования</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 7: Timeline Horizontal — 12 months to 200 clients — bg-alt -->
<!-- Archetype: timeline-horizontal -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-alt);overflow:hidden;">
  <!-- Glow center -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:520px;height:300px;background:radial-gradient(ellipse,rgba(13,148,136,0.14) 0%,transparent 70%);pointer-events:none;"></div>
  <!-- Dot grid top-right -->
  <div style="position:absolute;top:20px;right:30px;width:240px;height:160px;background-image:radial-gradient(circle,rgba(13,148,136,0.42) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Трекшн</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);line-height:1.1;">12 месяцев — от MVP до 200 клиентов</h1>

    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
      <!-- Q1 2025 -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Q1 2025</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);line-height:1.3;font-family:var(--font-heading);">Запуск MVP</span>
        <span style="font-size:0.9rem;color:var(--color-muted);margin-top:4px;font-family:var(--font-body);">15 пилотных клиентов</span>
      </div>
      <!-- Q3 2025 -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Q3 2025</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);line-height:1.3;font-family:var(--font-heading);">80 клиентов</span>
        <span style="font-size:0.9rem;color:var(--color-muted);margin-top:4px;font-family:var(--font-body);">MRR 6 млн ₽</span>
      </div>
      <!-- Q1 2026 -->
      <div style="background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;">
        <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;font-family:var(--font-heading);">Q1 2026 — Сейчас</span>
        <span style="font-size:1.35rem;font-weight:700;color:var(--color-text);line-height:1.3;font-family:var(--font-heading);">200 клиентов</span>
        <span style="font-size:0.9rem;color:var(--color-muted);margin-top:4px;font-family:var(--font-body);">MRR 15 млн ₽</span>
      </div>
      <!-- Growth metric -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="trend-up" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1.5rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">×13</div>
          <div style="font-size:0.82rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">рост клиентской базы за год</div>
        </div>
      </div>
      <!-- Unit economics -->
      <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;border-radius:12px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="chart" :size="18" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);line-height:1.2;font-family:var(--font-heading);">Unit-экономика</div>
          <div style="font-size:0.82rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">положительная с Q1 2026</div>
        </div>
      </div>
      <!-- Next milestone -->
      <div style="background:rgba(217,119,6,0.07);border:1.5px solid rgba(217,119,6,0.25);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:12px;">
        <div style="width:40px;height:40px;border-radius:12px;background:rgba(217,119,6,0.12);border:1.5px solid rgba(217,119,6,0.35);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="target" :size="18" color="#D97706" />
        </div>
        <div>
          <div style="font-size:1.5rem;font-weight:800;color:#D97706;line-height:1;font-family:var(--font-heading);">500</div>
          <div style="font-size:0.82rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">клиентов — цель Q1 2027</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 8: Profile Grid — team — bg-base -->
<!-- Archetype: profile-grid -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-base);overflow:hidden;">
  <!-- Glow bottom-right -->
  <div style="position:absolute;bottom:-100px;right:-80px;width:440px;height:440px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>
  <!-- Arc top-left -->
  <div style="position:absolute;top:-60px;left:-60px;width:280px;height:280px;border:2px solid rgba(13,148,136,0.25);border-radius:50%;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Команда</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">40 лет совокупного опыта в информационной безопасности</h1>

    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:10px;align-items:stretch;">
      <!-- CEO -->
      <div style="display:flex;align-items:center;gap:14px;background:transparent;border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="user" :size="22" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-family:var(--font-heading);">CEO</div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Алексей Новиков</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">Экс-руководитель SOC Kaspersky</div>
        </div>
      </div>

      <!-- CTO -->
      <div style="display:flex;align-items:center;gap:14px;background:transparent;border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="lock" :size="22" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-family:var(--font-heading);">CTO</div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Дмитрий Ким</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">15 лет в penetration testing</div>
        </div>
      </div>

      <!-- VP Sales -->
      <div style="display:flex;align-items:center;gap:14px;background:transparent;border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="trend-up" :size="22" color="var(--color-accent)" />
        </div>
        <div>
          <div style="font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-accent);font-family:var(--font-heading);">VP Sales</div>
          <div style="font-size:1rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Марина Соколова</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);">Построила продажи в 3 ИБ-компаниях</div>
        </div>
      </div>

      <!-- Stat card: 40 years -->
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
        <div style="width:48px;height:48px;border-radius:50%;background:var(--color-accent);border:1.5px solid var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <Icon name="star" :size="22" color="#FFFFFF" />
        </div>
        <div>
          <div style="font-size:2rem;font-weight:800;color:var(--color-accent);line-height:1;font-family:var(--font-heading);">40 лет</div>
          <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">совокупный опыт</div>
        </div>
      </div>

      <!-- Advisory note -->
      <div style="grid-column:1/3;display:flex;align-items:center;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 20px;">
        <Icon name="shield-check" :size="20" color="var(--color-accent)" />
        <span style="font-size:0.95rem;color:var(--color-muted);font-family:var(--font-body);">Команда прошла путь от построения SOC в крупных корпорациях до создания продукта для рынка SMB</span>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 9: Two-Col Text — competitive landscape — bg-alt -->
<!-- Archetype: two-col-text -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;background:var(--bg-alt);overflow:hidden;">
  <!-- Dot grid bottom-left -->
  <div style="position:absolute;bottom:20px;left:30px;width:260px;height:200px;background-image:radial-gradient(circle,rgba(13,148,136,0.42) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>
  <!-- Glow top-right -->
  <div style="position:absolute;top:-80px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 68%);border-radius:50%;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;font-family:var(--font-heading);">Конкуренция</span>
    <h1 style="font-size:2.3rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Конкуренты защищают enterprise — мы тех, кого они игнорируют</h1>

    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-content:center;">
      <!-- Left column: market gap -->
      <div>
        <div style="display:inline-flex;align-items:center;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.35);border-radius:20px;padding:6px 14px;margin-bottom:16px;line-height:1;">
          <span style="font-size:0.7rem;color:#D97706;font-weight:700;text-transform:uppercase;letter-spacing:0.12em;font-family:var(--font-heading);">Конкуренты</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 16px;">
            <div style="width:36px;height:36px;border-radius:10px;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.30);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <Icon name="briefcase" :size="16" color="#D97706" />
            </div>
            <div>
              <div style="font-size:0.95rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">Positive Technologies</div>
              <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">Фокус на крупный бизнес и госсектор</div>
            </div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 16px;">
            <div style="width:36px;height:36px;border-radius:10px;background:rgba(217,119,6,0.10);border:1.5px solid rgba(217,119,6,0.30);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <Icon name="briefcase" :size="16" color="#D97706" />
            </div>
            <div>
              <div style="font-size:0.95rem;font-weight:700;color:var(--color-text);font-family:var(--font-heading);">BI.ZONE</div>
              <div style="font-size:0.85rem;color:var(--color-muted);font-family:var(--font-body);margin-top:2px;">Enterprise-решения, высокий порог входа</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right column: our advantage -->
      <div>
        <div style="display:inline-flex;align-items:center;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:20px;padding:6px 14px;margin-bottom:16px;line-height:1;">
          <span style="font-size:0.7rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.12em;font-family:var(--font-heading);">CyberShield</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:6px;flex-shrink:0;"></div>
            <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Единственное решение «всё в одном» для среднего сегмента</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:6px;flex-shrink:0;"></div>
            <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;">Цена в <strong style="color:var(--color-accent);">3–5×</strong> ниже enterprise-решений</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <div style="width:8px;height:8px;border-radius:50%;background:var(--color-accent);margin-top:6px;flex-shrink:0;"></div>
            <span style="font-size:1rem;color:var(--color-text);font-family:var(--font-body);line-height:1.45;"><strong style="color:var(--color-accent);">95%</strong> покрытия векторов атак при доступной цене</span>
          </div>
          <div style="margin-top:8px;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:12px 16px;">
            <span style="font-size:0.95rem;font-weight:600;color:var(--color-accent);font-family:var(--font-heading);">Наш TAM: ~80 000 компаний в РФ</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- SLIDE 10: CTA Warm — investment ask — bg-accent -->
<!-- Archetype: cta-warm -->
<!-- ============================================================ -->
---
layout: none
---

<div style="position:absolute;inset:0;overflow:hidden;">
  <!-- CTA gradient background -->
  <div style="position:absolute;inset:0;background:linear-gradient(145deg,var(--bg-accent) 0%,color-mix(in srgb,var(--bg-accent) 70%,black) 100%);"></div>
  <!-- Radial glow -->
  <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:400px;background:radial-gradient(ellipse,rgba(255,255,255,0.12) 0%,transparent 65%);pointer-events:none;"></div>
  <!-- Dot grid bottom-left -->
  <div style="position:absolute;bottom:20px;left:40px;width:260px;height:180px;background-image:radial-gradient(circle,rgba(255,255,255,0.28) 1.5px,transparent 1.5px);background-size:22px 22px;pointer-events:none;"></div>
  <!-- Arc top-right -->
  <div style="position:absolute;top:-80px;right:-80px;width:360px;height:360px;border:2px solid rgba(255,255,255,0.18);border-radius:50%;pointer-events:none;"></div>

  <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
    <div style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.15);border:1.5px solid rgba(255,255,255,0.35);border-radius:20px;padding:6px 18px;margin-bottom:20px;line-height:1;">
      <span style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:#FFFFFF;font-weight:600;font-family:var(--font-heading);">Раунд А</span>
    </div>

    <h1 style="font-size:3rem;font-weight:800;color:#FFFFFF;margin:0 0 12px;font-family:var(--font-heading);line-height:1.1;letter-spacing:-0.01em;">Инвестируйте 120 млн ₽<br>в рынок, который удвоится за 3 года</h1>
    <p style="font-size:1.15rem;color:rgba(255,255,255,0.80);margin:0 0 32px;font-family:var(--font-body);max-width:560px;line-height:1.55;">Целевые показатели: 500 клиентов и MRR 40 млн ₽ к Q1 2027</p>

    <div style="display:flex;gap:16px;margin-bottom:36px;">
      <div style="background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.28);border-radius:14px;padding:16px 28px;text-align:center;">
        <div style="font-size:2rem;font-weight:800;color:#FFFFFF;font-family:var(--font-heading);line-height:1;">120 млн</div>
        <div style="font-size:0.8rem;color:rgba(255,255,255,0.70);font-family:var(--font-body);margin-top:4px;">объём раунда, ₽</div>
      </div>
      <div style="background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.28);border-radius:14px;padding:16px 28px;text-align:center;">
        <div style="font-size:2rem;font-weight:800;color:#FFFFFF;font-family:var(--font-heading);line-height:1;">×2,5</div>
        <div style="font-size:0.8rem;color:rgba(255,255,255,0.70);font-family:var(--font-body);margin-top:4px;">рост рынка за 3 года</div>
      </div>
      <div style="background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.28);border-radius:14px;padding:16px 28px;text-align:center;">
        <div style="font-size:2rem;font-weight:800;color:#FFFFFF;font-family:var(--font-heading);line-height:1;">40 млн</div>
        <div style="font-size:0.8rem;color:rgba(255,255,255,0.70);font-family:var(--font-body);margin-top:4px;">MRR цель, ₽/мес</div>
      </div>
    </div>

    <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.80);font-size:1rem;font-family:var(--font-body);">
      <span>founders@cybershield.ru</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);display:inline-block;"></span>
      <span>cybershield.ru</span>
      <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.55);display:inline-block;"></span>
      <span>Москва, 2026</span>
    </div>
  </div>
</div>
