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
<!-- Rule 1: bg-accent hex fallback inline; Rule 6: cover-circle-accent -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="cover-variant-b">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:28px;">TechVentures Group · Q4 2025</span>
  <h1 style="font-size:3.4rem;font-weight:800;color:#ffffff;margin:0 0 16px;font-family:var(--font-heading);line-height:1.08;">Выручка превысила план<br>на 18%</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.82);margin:0 0 32px;font-family:var(--font-body);">Квартальный отчёт · Q4 2025</p>
  <div style="display:flex;align-items:center;gap:16px;color:rgba(255,255,255,0.65);font-size:1rem;">
    <span>TechVentures Group</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>Финансовые результаты</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <span>2025</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 2 — STAT-HERO centered (bg-base): 1,42 млрд ₽ -->
<!-- Rule 8: bottom anchor; Rule 11: stat-hero variation (full centered) -->
<!-- Eyebrow label used here — count: 1 of 10 slides = 10% ≤ 30% OK -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px 100px;">
  <span class="label-pill" style="margin-bottom:20px;">Выручка Q4 2025</span>
  <div class="stat-hero" style="font-size:6.2rem;">1,42 млрд ₽</div>
  <p style="font-size:1.4rem;color:var(--color-text);margin:14px 0 8px;font-family:var(--font-body);font-weight:500;">+18% к плану — рекордный квартал в истории компании</p>
  <p style="font-size:1.05rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);max-width:600px;line-height:1.5;">EBITDA: 380 млн ₽ (маржа 26,8%) · Чистая прибыль: 210 млн ₽</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
    <span class="label-pill">+2 400 клиентов</span>
    <span class="label-pill">маржа 26,8%</span>
    <span class="label-pill">210 млн ₽ прибыли</span>
  </div>
</div>
<div class="stat-footer-band">
  <span style="font-size:0.85rem;color:var(--color-muted);">Источник: внутренняя финансовая отчётность TechVentures Group, декабрь 2025</span>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 3 — BENTO-GRID (bg-base): Выручка по сегментам -->
<!-- Rule 8: visual dedup — prev was centered stat-hero, now grid layout -->
<!-- Rule 9: adjacent fingerprint differs (center→left-column grid) -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-dots"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Структура выручки</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Три сегмента — три истории роста</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <!-- Featured: Enterprise — largest, accent border -->
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(13,148,136,0.12),rgba(255,255,255,0.8));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:28px;display:flex;flex-direction:column;justify-content:center;">
      <div class="icon-circle" style="width:60px;height:60px;margin-bottom:18px;">
        <Icon name="briefcase" :size="26" color="var(--color-accent)" />
      </div>
      <span style="font-size:0.65rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--color-accent);font-weight:700;margin-bottom:8px;">Enterprise · 58%</span>
      <span style="font-size:2.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;margin-bottom:8px;">820 млн ₽</span>
      <span style="font-size:1rem;color:var(--color-text);font-weight:600;margin-bottom:6px;">+32% к аналогичному периоду</span>
      <span style="font-size:0.95rem;color:var(--color-muted);line-height:1.4;">Крупный бизнес — основной драйвер роста. Средний чек вырос на 28%.</span>
    </div>
    <!-- SMB -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:16px;">
      <div class="icon-rounded" style="width:48px;height:48px;flex-shrink:0;">
        <Icon name="users" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">SMB · 29%</span>
        <span style="display:block;font-size:1.4rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;margin-bottom:4px;">410 млн ₽</span>
        <span style="font-size:0.9rem;color:var(--color-muted);">+8% — стабильный органический рост</span>
      </div>
    </div>
    <!-- Госсектор -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:16px;">
      <div class="icon-ghost" style="width:48px;height:48px;flex-shrink:0;">
        <Icon name="globe" :size="22" color="var(--color-accent)" />
      </div>
      <div>
        <span style="display:block;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-accent);font-weight:700;margin-bottom:4px;">Госсектор · 13%</span>
        <span style="display:block;font-size:1.4rem;font-weight:800;color:var(--color-text);font-family:var(--font-heading);line-height:1;margin-bottom:4px;">190 млн ₽</span>
        <span style="font-size:0.9rem;color:var(--color-muted);">+45% — быстрейший сегмент квартала</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 4 — STAT-HERO asymmetric (bg-alt): Enterprise in 2.5x faster -->
<!-- Rule 11: stat-hero variation — asymmetric layout differs from slide 2 centered -->
<!-- Rule 5: bg-alt decorative 1.5x extra opacity -->
<!-- Rule 9: adjacent fingerprint — prev was bento-grid, now asymmetric-split -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-dots-alt"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <!-- Left: hero metric -->
  <div style="display:flex;flex-direction:column;justify-content:center;align-items:flex-start;">
    <span class="label-pill" style="margin-bottom:16px;">Enterprise · IDC Russia 2025</span>
    <div class="stat-hero" style="font-size:5.5rem;margin-bottom:6px;">2,5×</div>
    <span class="stat-caption" style="margin-bottom:20px;">быстрее рынка</span>
    <div style="padding:16px 20px;background:var(--color-surface);border:1.5px solid var(--color-accent-dim);border-radius:12px;">
      <span style="font-size:0.9rem;color:var(--color-muted);">Средний чек Enterprise</span>
      <span style="display:block;font-size:1.5rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">4,2 млн ₽</span>
    </div>
  </div>
  <!-- Right: KPI cards -->
  <div style="display:flex;flex-direction:column;gap:12px;justify-content:center;">
    <h2 style="font-size:1.6rem;font-weight:700;color:var(--color-text);margin:0 0 8px;font-family:var(--font-heading);line-height:1.2;">Ключевые метрики сегмента</h2>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(13,148,136,0.10);border:1.5px solid rgba(13,148,136,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="shield" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">Retention</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">94% клиентов остаются на второй год</span>
      </div>
      <span style="margin-left:auto;font-size:1.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">94%</span>
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:14px;background:rgba(13,148,136,0.10);border:1.5px solid rgba(13,148,136,0.40);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="trending-up" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">Upsell</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">38% существующих клиентов расширяют подписку</span>
      </div>
      <span style="margin-left:auto;font-size:1.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);">38%</span>
    </div>
    <div style="background:linear-gradient(135deg,rgba(13,148,136,0.08),rgba(13,148,136,0.02));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:16px;">
      <div style="width:44px;height:44px;border-radius:50%;background:rgba(13,148,136,0.15);border:1.5px solid rgba(13,148,136,0.45);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="activity" :size="20" color="var(--color-accent)" />
      </div>
      <div>
        <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);">Рост рынка</span>
        <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Enterprise-сегмент вырос в 2,5× быстрее IDC-бенчмарка</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 5 — SECTION DIVIDER left-aligned (bg-accent) -->
<!-- Rule 2: bg-accent + prominent decorative "05" element -->
<!-- Rule 10: section dividers differentiated — this one left-aligned + decorative number -->
<!-- Rule 9: adjacent — prev was stat/split, now section divider -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);" class="section-stripe"></div>
<div style="position:absolute;top:-30px;right:60px;z-index:0;font-size:14rem;font-weight:900;color:rgba(255,255,255,0.06);font-family:var(--font-heading);line-height:1;pointer-events:none;user-select:none;">05</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.65);font-weight:600;margin-bottom:20px;">Раздел 1 из 2</span>
  <h1 style="font-size:3.6rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.08;">Операционная<br>эффективность</h1>
  <div style="width:64px;height:3px;background:rgba(255,255,255,0.45);border-radius:2px;margin-bottom:20px;"></div>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.78);max-width:560px;line-height:1.6;font-family:var(--font-body);">Unit-экономика достигла целевых показателей. CAC снижен на 22%, LTV/CAC вырос до 11,7x.</p>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 6 — CARD-MOSAIC 2×2 (bg-base): Unit-экономика -->
<!-- Rule 8: dedup check — only 1 bento-grid so far (slide 3), mosaic differs -->
<!-- Rule 9: adjacent — prev section divider, now dense mosaic -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-arc"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Unit-экономика</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Все ключевые показатели — в зелёной зоне</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    <!-- CAC — card-solid -->
    <div class="card-solid" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
        <div class="icon-circle" style="width:44px;height:44px;">
          <Icon name="target" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-muted);font-weight:600;">CAC</span>
      </div>
      <span style="font-size:2.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;margin-bottom:6px;">180 тыс.</span>
      <span style="font-size:1rem;color:var(--color-text);font-weight:600;margin-bottom:4px;">−22% к Q3 2025</span>
      <span style="font-size:0.9rem;color:var(--color-muted);">Стоимость привлечения клиента</span>
    </div>
    <!-- LTV — card-ghost -->
    <div class="card-ghost" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
        <div class="icon-rounded" style="width:44px;height:44px;">
          <Icon name="trending-up" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-muted);font-weight:600;">LTV</span>
      </div>
      <span style="font-size:2.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;margin-bottom:6px;">2,1 млн ₽</span>
      <span style="font-size:1rem;color:var(--color-text);font-weight:600;margin-bottom:4px;">Пожизненная ценность клиента</span>
      <span style="font-size:0.9rem;color:var(--color-muted);">+18% к предыдущему кварталу</span>
    </div>
    <!-- LTV/CAC ratio — card-accent (highlighted) -->
    <div class="card-accent" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
        <div class="icon-ghost" style="width:44px;height:44px;">
          <Icon name="chart-bar" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-accent);font-weight:700;">LTV/CAC</span>
      </div>
      <span style="font-size:2.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;margin-bottom:6px;">11,7×</span>
      <span style="font-size:1rem;color:var(--color-text);font-weight:600;margin-bottom:4px;">Цель: ≥8× — перевыполнено</span>
      <span style="font-size:0.9rem;color:var(--color-muted);">Отраслевой бенчмарк: 7–9×</span>
    </div>
    <!-- Payback period — card-solid -->
    <div class="card-solid" style="display:flex;flex-direction:column;justify-content:center;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
        <div class="icon-circle" style="width:44px;height:44px;">
          <Icon name="clock" :size="20" color="var(--color-accent)" />
        </div>
        <span style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.10em;color:var(--color-muted);font-weight:600;">Payback</span>
      </div>
      <span style="font-size:2.4rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;margin-bottom:6px;">4,2 мес.</span>
      <span style="font-size:1rem;color:var(--color-text);font-weight:600;margin-bottom:4px;">Срок окупаемости</span>
      <span style="font-size:0.9rem;color:var(--color-muted);">Цель: 6 мес. — перевыполнено на 30%</span>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 7 — ASYMMETRIC-SPLIT (bg-base): Команда -->
<!-- Rule 9: adjacent — prev card-mosaic (grid), now asymmetric-split -->
<!-- Rule 6: icon diversity — different semantic icons per item -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-base, #FAF9F6);" class="slide-decor-glow"></div>
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <!-- Left: hero visual -->
  <div style="display:flex;justify-content:center;align-items:center;">
    <div style="text-align:center;">
      <div style="width:140px;height:140px;border-radius:50%;background:linear-gradient(135deg,rgba(13,148,136,0.14),rgba(13,148,136,0.04));border:2px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;">
        <span style="font-size:3.8rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);line-height:1;">420</span>
      </div>
      <span class="stat-caption" style="display:block;font-size:1.15rem;">сотрудников</span>
      <span style="display:block;font-size:1rem;color:var(--color-accent);font-weight:600;margin-top:6px;">+110 за квартал (+35%)</span>
    </div>
  </div>
  <!-- Right: team KPIs -->
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <h1 style="font-size:1.9rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);line-height:1.2;">Команда растёт без потери качества найма</h1>
    <div style="display:flex;flex-direction:column;gap:10px;">
      <!-- eNPS — users icon (people focus) -->
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div class="icon-circle" style="width:44px;height:44px;flex-shrink:0;">
          <Icon name="award" :size="20" color="var(--color-accent)" />
        </div>
        <div style="flex:1;">
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">eNPS сотрудников</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Высокая вовлечённость — выше отраслевого медиана</span>
        </div>
        <span style="font-size:1.3rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">72</span>
      </div>
      <!-- Time-to-hire — calendar (time/scheduling) -->
      <div style="display:flex;align-items:center;gap:14px;background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:10px;padding:14px 18px;">
        <div class="icon-rounded" style="width:44px;height:44px;flex-shrink:0;">
          <Icon name="calendar" :size="20" color="var(--color-accent)" />
        </div>
        <div style="flex:1;">
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">Time-to-hire</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">Цель была 21 день — перевыполнено на 14%</span>
        </div>
        <span style="font-size:1.3rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">18 дн.</span>
      </div>
      <!-- Текучесть — activity (flow/churn) -->
      <div style="display:flex;align-items:center;gap:14px;background:linear-gradient(135deg,rgba(13,148,136,0.07),rgba(13,148,136,0.02));border:1.5px solid var(--color-accent-dim);border-radius:10px;padding:14px 18px;">
        <div class="icon-ghost" style="width:44px;height:44px;flex-shrink:0;">
          <Icon name="check" :size="20" color="var(--color-accent)" />
        </div>
        <div style="flex:1;">
          <span style="font-size:1rem;font-weight:600;color:var(--color-text);">Текучесть персонала</span>
          <span style="display:block;font-size:0.9rem;color:var(--color-muted);">В 2× ниже отраслевого норматива (15%)</span>
        </div>
        <span style="font-size:1.3rem;font-weight:800;color:var(--color-accent);font-family:var(--font-heading);flex-shrink:0;">8%</span>
      </div>
    </div>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 8 — SECTION DIVIDER centered+circle (bg-accent) -->
<!-- Rule 2 & 10: SECOND section divider — MUST differ from slide 5 -->
<!-- Slide 5 was left-aligned + decorative "05" number -->
<!-- This one: centered + large circle visual element -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);"></div>
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:480px;height:480px;border-radius:50%;border:1.5px solid rgba(255,255,255,0.12);z-index:0;pointer-events:none;"></div>
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:320px;height:320px;border-radius:50%;border:1px solid rgba(255,255,255,0.08);z-index:0;pointer-events:none;"></div>
<div style="position:absolute;bottom:40px;right:60px;z-index:0;font-size:10rem;font-weight:900;color:rgba(255,255,255,0.05);font-family:var(--font-heading);line-height:1;pointer-events:none;user-select:none;">08</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:rgba(255,255,255,0.65);font-weight:600;margin-bottom:20px;">Раздел 2 из 2</span>
  <h1 style="font-size:3.5rem;font-weight:800;color:#ffffff;margin:0 0 20px;font-family:var(--font-heading);line-height:1.1;">Прогноз<br>и стратегия</h1>
  <p style="font-size:1.25rem;color:rgba(255,255,255,0.78);max-width:640px;line-height:1.6;font-family:var(--font-body);">2026 — год масштабирования. Выручка 7,2 млрд ₽, новые рынки, запуск AI-модуля.</p>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 9 — TIMELINE-HORIZONTAL (bg-alt): План 2026 -->
<!-- Rule: 6 cells = density requirement met -->
<!-- Rule 5: bg-alt decorative 1.5x — use slide-decor-dots-alt -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-alt, #E8E6DF);" class="slide-decor-dots-alt"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">Стратегия 2026</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">Путь к 7,2 млрд ₽: четыре вектора роста</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    <!-- Q1 2026 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Q1 2026</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Масштабирование Enterprise</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Цель: 60 новых корпоративных клиентов, удвоение команды продаж</span>
    </div>
    <!-- Q2 2026 — accent card -->
    <div style="background:linear-gradient(135deg,rgba(13,148,136,0.12),rgba(13,148,136,0.04));border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Q2 2026 · Ключевое</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Запуск AI-модуля</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Авто-аналитика и предиктивные рекомендации для Enterprise-клиентов</span>
    </div>
    <!-- Q3 2026 -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Q3 2026</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Казахстан и Узбекистан</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">Выход на рынки СНГ: партнёрская сеть + локальные офисы продаж</span>
    </div>
    <!-- Целевой рост -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Рост выручки</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">+28% год к году</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">С 5,6 млрд ₽ в 2025 до 7,2 млрд ₽ в 2026</span>
    </div>
    <!-- EBITDA цель -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Маржа EBITDA</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">Целевые 30%</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">+3,2 п.п. к текущему уровню через операционный леверидж</span>
    </div>
    <!-- Команда план -->
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px;">Команда 2026</span>
      <span style="font-size:1.05rem;font-weight:600;color:var(--color-text);margin-bottom:4px;">650 сотрудников</span>
      <span style="font-size:0.9rem;color:var(--color-muted);line-height:1.35;">+230 к текущей численности, фокус на R&D и продажи</span>
    </div>
  </div>
  <div style="display:flex;justify-content:center;gap:24px;margin-top:12px;padding:10px 0;border-top:1px solid var(--color-surface-border);">
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">7,2 млрд ₽</strong> — цель выручки 2026</span>
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">+28%</strong> — рост год к году</span>
    <span style="font-size:0.85rem;color:var(--color-muted);">⬤ <strong style="color:var(--color-accent);">Q2</strong> — запуск AI-модуля</span>
  </div>
</div>

---

<!-- ============================================================ -->
<!-- SLIDE 10 — CTA-WARM (bg-accent): Investor call -->
<!-- Rule 1: bg-accent hex fallback; Rule 9: cover-circle-accent anchor -->
<!-- Rule 13: icon-container-cover on teal background -->
<!-- ============================================================ -->
<div style="position:absolute;inset:0;z-index:0;background:var(--bg-accent, #0D9488);background:linear-gradient(145deg, var(--bg-accent, #0D9488) 0%, #0a7a70 100%);" class="cover-variant-a">
  <div class="cover-circle-accent"></div>
</div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span class="label-pill-cover" style="margin-bottom:20px;">Инвесторам</span>
  <h1 style="font-size:2.8rem;font-weight:800;color:#ffffff;margin:0 0 12px;font-family:var(--font-heading);line-height:1.15;">Подключитесь к квартальному<br>звонку с инвесторами</h1>
  <p style="font-size:1.1rem;color:rgba(255,255,255,0.80);margin:0 0 32px;max-width:580px;line-height:1.5;">Обсудим результаты Q4 2025, стратегию на 2026 и ответим на ваши вопросы напрямую.</p>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:560px;width:100%;margin-bottom:32px;">
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:10px;padding:12px 20px;text-align:left;">
      <div class="icon-container-cover" style="width:40px;height:40px;flex-shrink:0;">
        <Icon name="calendar" :size="18" color="#ffffff" />
      </div>
      <span style="font-size:1rem;color:#ffffff;font-weight:500;">15 апреля 2026, 16:00 МСК — Zoom-ссылка в рассылке</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,0.14);border:1.5px solid rgba(255,255,255,0.30);border-radius:10px;padding:12px 20px;text-align:left;">
      <div class="icon-container-cover" style="width:40px;height:40px;flex-shrink:0;">
        <Icon name="mail" :size="18" color="#ffffff" />
      </div>
      <span style="font-size:1rem;color:#ffffff;font-weight:500;">Q&amp;A и запись: ir@techventures.ru</span>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:rgba(255,255,255,0.80);font-size:1rem;">
    <div style="display:flex;align-items:center;gap:8px;">
      <Icon name="globe" :size="16" color="rgba(255,255,255,0.80)" />
      <span>techventures.ru/ir</span>
    </div>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(255,255,255,0.45);display:inline-block;"></span>
    <div style="display:flex;align-items:center;gap:8px;">
      <Icon name="mail" :size="16" color="rgba(255,255,255,0.80)" />
      <span>ir@techventures.ru</span>
    </div>
  </div>
</div>
