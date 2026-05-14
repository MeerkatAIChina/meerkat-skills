// ===== Mermaid Init =====
mermaid.initialize({ startOnLoad: true, theme: 'dark' });

// ===== Particle Canvas Animation =====
const canvas = document.getElementById('particle-canvas');
if (canvas) {
  const ctx = canvas.getContext('2d');
  let particles = [];
  let w, h;

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class Particle {
    constructor() { this.reset(); }
    reset() {
      this.x = Math.random() * w; this.y = Math.random() * h;
      this.size = Math.random() * 2 + 0.5;
      this.speedX = (Math.random() - 0.5) * 0.3;
      this.speedY = (Math.random() - 0.5) * 0.3;
      this.opacity = Math.random() * 0.5 + 0.2;
      this.color = Math.random() > 0.7 ? '#00aaff' : '#a855f7';
    }
    update() {
      this.x += this.speedX; this.y += this.speedY;
      if (this.x < 0 || this.x > w || this.y < 0 || this.y > h) this.reset();
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fillStyle = this.color; ctx.globalAlpha = this.opacity;
      ctx.fill(); ctx.globalAlpha = 1;
    }
  }

  for (let i = 0; i < 80; i++) particles.push(new Particle());

  function drawLines() {
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 150) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = '#00aaff'; ctx.globalAlpha = 0.08 * (1 - dist / 150);
          ctx.lineWidth = 0.5; ctx.stroke(); ctx.globalAlpha = 1;
        }
      }
    }
  }

  function animate() {
    ctx.clearRect(0, 0, w, h);
    particles.forEach(p => { p.update(); p.draw(); });
    drawLines();
    requestAnimationFrame(animate);
  }
  animate();
}

// ===== Count-up Animation for Stats =====
function animateCounter(el, target, suffix = '', duration = 1500) {
  const start = performance.now();
  const from = 0;
  function update(now) {
    const progress = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(from + (target - from) * ease);
    el.textContent = current + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

const statObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const numEl = entry.target.querySelector('.stat-number');
      if (numEl && !numEl.dataset.animated) {
        numEl.dataset.animated = 'true';
        const text = numEl.textContent;
        const num = parseInt(text);
        const suffix = text.replace(/[0-9]/g, '');
        if (!isNaN(num)) animateCounter(numEl, num, suffix);
      }
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('#hero .stat-item, .impact-metric').forEach(el => statObserver.observe(el));

// ===== Scroll Animations =====
const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.15 });

document.querySelectorAll('.opportunity-card, .framework-card, .comparison, .mermaid-container, .curve-container, .value-chain').forEach(el => {
  el.classList.add('fade-in'); fadeObserver.observe(el);
});
