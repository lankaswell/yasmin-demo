const { chromium } = require('C:/Users/alexp/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'msedge' });
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    for (const width of [1440, 390]) {
      await page.setViewportSize({ width, height: 900 });
      for (const file of ['index.html', 'chi-sono.html', 'musicoterapia.html', 'musicista.html', 'flauto.html', 'corsi.html', 'contatti.html', 'note-demo.html']) {
        await page.goto(`http://localhost:8000/${file}`);
        if (await page.locator('h1').count() !== 1) throw Error(`Heading issue: ${file}`);
        const links = await page.locator('a[href]').evaluateAll(anchors => anchors.map(a => a.getAttribute('href')));
        for (const href of links) {
          if (/^(#|https?:|mailto:|tel:)/.test(href)) continue;
          if (!fs.existsSync(`site/${href.split('#')[0]}`)) throw Error(`Broken link: ${file} → ${href}`);
        }
        if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error(`Overflow: ${file} at ${width}px`);
      }
    }
    await page.goto('http://localhost:8000/contatti.html');
    for (const name of ['phone', 'email', 'instagram', 'facebook']) {
      const image = page.locator(`img[src="assets/icon-${name}.svg"]`).first();
      if (!(await image.evaluate(img => img.complete && img.naturalWidth > 0))) throw Error(`Icon failed: ${name}`);
    }
    if (errors.length) throw Error(errors.join('\n'));
    console.log('PASS: 8 pages at desktop and mobile widths, internal links, contact icons, no overflow or JS errors');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exit(1); });
