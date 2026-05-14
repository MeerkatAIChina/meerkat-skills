# Template Guide

## 模板系统概述

Templates are stored in `assets/templates/`. The rendering engine reads JSON data + HTML templates → produces a single-file `index.html` with zero external dependencies.

## File Structure

```
assets/templates/
├── base.html              # HTML skeleton with {{styles}} and {{scripts}} placeholders
├── styles.css            # Dark-industrial theme (customizable via CSS vars)
├── scripts.js            # Particle canvas + scroll animations + count-up
├── sections/
│   ├── hero.html         # Product showcase with stats
│   ├── framework.html    # Analysis framework steps (9 cards)
│   ├── painpoint.html    # Before/after comparison + metrics
│   ├── opportunities.html # Opportunity cards with 8 fields each
│   ├── flowchart.html    # Mermaid diagram container
│   ├── valuechain.html   # Value chain nodes
│   ├── emotion.html      # SVG emotion curve
│   └── brand.html        # Brand closing section
└── themes/               # (Future: CSS theme files)
    ├── dark-industrial.css
    ├── light-minimal.css
    └── dark-cyber.css
```

## How Rendering Works

1. **Load base.html** skeleton
2. **Inject sections** in order specified by `output_sections` config
3. **Replace variables** — all `{{variable}}` get replaced with JSON data
4. **Inline CSS/JS** into `<style>` and `<script>` tags
5. **Output** single `index.html`

## Variable Syntax

### Simple variables
```html
<h1>{{product.name}}</h1>
<div>{{hero.tagline}}</div>
```

### Nested objects (dot notation)
```html
<span>{{product.core_specs.weight}}</span>
```

### Conditionals
```html
{{#if hero_image}}
  <img src="{{hero_image}}" />
{{/if}}
```

### Loops
```html
{{#each opportunities}}
  <div class="card">
    <h3>{{title}}</h3>
    <p>{{business_goal}}</p>
  </div>
{{/each}}
```

Inside a loop, you can access:
- Loop item properties directly: `{{title}}`, `{{priority}}`
- Parent context via full path: `{{product.name}}`

## Adding a New Section

1. Create `sections/my-section.html`
2. Add `my-section` to `output_sections` config
3. Provide data in the build context (modify render.py or pass via JSON)

## Customizing Themes

Current theme is controlled by CSS custom properties in `styles.css`:

```css
:root {
  --bg-dark: #0a0a0a;
  --accent-blue: #00aaff;
  --accent-gold: #FFD700;
  --accent-green: #00ff88;
  /* ... */
}
```

To create a new theme:
1. Copy `styles.css` to `themes/your-theme.css`
2. Change color values
3. In build config, set `theme: "your-theme"`
4. Rendering engine will swap the CSS file

## Responsive Breakpoints

Current breakpoints:
- Mobile: `max-width: 768px`
- Tablet: `768px - 1024px`
- Desktop: `> 1024px`

## Performance Notes

- Particle canvas: 80 particles, renders with `requestAnimationFrame`
- Scroll animations: IntersectionObserver-based (only visible elements animate)
- Images: `object-fit: cover` with max-height limits
- CSS: No external font loading (system fonts only)

## Extending the Renderer

The Python renderer (`scripts/render.py`) supports:
- `{{#each array}}` loops
- `{{#if condition}}` conditionals
- `{{dot.nested.keys}}` object traversal
- Nested loops with merged context

To add new syntax, extend `render_simple()` in `render.py`.
