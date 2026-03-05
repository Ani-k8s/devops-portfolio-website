/**
 * Portfolio — Annappa M
 * main.js — Scroll animations, typed effect, nav, and UI logic
 */

"use strict";

/* ── Config ─────────────────────────────────────────────────── */
const CONFIG = {
  navScrollThreshold: 30,
  observerThreshold: 0.12,
  observerRootMargin: "0px 0px -60px 0px",
};

/* ── DOM Ready ───────────────────────────────────────────────── */
document.addEventListener("DOMContentLoaded", () => {
  initNav();
  initTyped();
  initScrollReveal();
  initFooterYear();
  initSkillCardGlow();
  initSmoothScroll();
});

/* ════════════════════════════════════════════════════════════
   NAVIGATION
   ════════════════════════════════════════════════════════════ */
function initNav() {
  const navbar    = document.getElementById("navbar");
  const hamburger = document.getElementById("hamburger");
  const navLinks  = document.getElementById("navLinks");
  const links     = navLinks?.querySelectorAll("a");

  // Scroll: add .scrolled class
  const onScroll = () => {
    if (window.scrollY > CONFIG.navScrollThreshold) {
      navbar?.classList.add("scrolled");
    } else {
      navbar?.classList.remove("scrolled");
    }
    updateActiveLink();
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile hamburger toggle
  hamburger?.addEventListener("click", () => {
    const isOpen = navLinks?.classList.toggle("open");
    hamburger.classList.toggle("open", isOpen);
    hamburger.setAttribute("aria-expanded", String(isOpen));
    document.body.style.overflow = isOpen ? "hidden" : "";
  });

  // Close menu on link click
  links?.forEach((link) => {
    link.addEventListener("click", () => {
      navLinks?.classList.remove("open");
      hamburger?.classList.remove("open");
      hamburger?.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    });
  });

  // Close on outside click
  document.addEventListener("click", (e) => {
    if (
      navLinks?.classList.contains("open") &&
      !navLinks.contains(e.target) &&
      !hamburger?.contains(e.target)
    ) {
      navLinks.classList.remove("open");
      hamburger?.classList.remove("open");
      hamburger?.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    }
  });
}

/* ── Active nav link based on scroll position ──────────────── */
function updateActiveLink() {
  const sections = ["hero", "about", "skills", "experience", "projects", "contact"];
  const navLinks = document.querySelectorAll(".nav__link");

  let current = "";
  sections.forEach((id) => {
    const section = document.getElementById(id);
    if (section) {
      const rect = section.getBoundingClientRect();
      if (rect.top <= 120) current = id;
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove("active");
    const href = link.getAttribute("href")?.replace("#", "");
    if (href === current) link.classList.add("active");
  });
}


/* ════════════════════════════════════════════════════════════
   TYPED.JS EFFECT
   ════════════════════════════════════════════════════════════ */
function initTyped() {
  const el = document.getElementById("typedTarget");
  if (!el || typeof Typed === "undefined") return;

  const strings = window.TYPED_STRINGS || [
    "DevOps Engineer",
    "Cloud Architect",
    "Pipeline Builder",
    "Automation Specialist",
  ];

  new Typed(el, {
    strings,
    typeSpeed: 55,
    backSpeed: 30,
    backDelay: 2000,
    startDelay: 600,
    loop: true,
    smartBackspace: true,
    cursorChar: "▌",
    onStringTyped: (arrayPos) => {
      el.closest(".hero__typed-wrapper")?.classList.add("typed-complete");
    },
  });
}


/* ════════════════════════════════════════════════════════════
   SCROLL REVEAL ANIMATIONS
   ════════════════════════════════════════════════════════════ */
function initScrollReveal() {
  const revealEls = document.querySelectorAll(
    ".reveal-up, .reveal-left, .reveal-right"
  );

  if (!revealEls.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Honour CSS transition-delay set via inline style
          const el = entry.target;
          const delay = el.style.getPropertyValue("--delay") || "0s";
          const delayMs = parseFloat(delay) * 1000;

          setTimeout(() => {
            el.classList.add("revealed");
          }, delayMs);

          observer.unobserve(el);
        }
      });
    },
    {
      threshold: CONFIG.observerThreshold,
      rootMargin: CONFIG.observerRootMargin,
    }
  );

  revealEls.forEach((el) => observer.observe(el));
}


/* ════════════════════════════════════════════════════════════
   SKILL CARD INTERACTIVE GLOW
   ════════════════════════════════════════════════════════════ */
function initSkillCardGlow() {
  const cards = document.querySelectorAll(".skill-card, .project-card");

  cards.forEach((card) => {
    card.addEventListener("mousemove", (e) => {
      const rect  = card.getBoundingClientRect();
      const x     = ((e.clientX - rect.left) / rect.width)  * 100;
      const y     = ((e.clientY - rect.top)  / rect.height) * 100;
      const glow  = card.querySelector(".skill-card__glow, .project-card__glow");

      if (glow) {
        glow.style.background = `radial-gradient(circle at ${x}% ${y}%, var(--accent, #00d4ff) 0%, transparent 65%)`;
      }
    });
  });
}


/* ════════════════════════════════════════════════════════════
   SMOOTH SCROLL (offset for fixed nav)
   ════════════════════════════════════════════════════════════ */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const targetId = anchor.getAttribute("href").slice(1);
      const target   = document.getElementById(targetId);
      if (!target) return;

      e.preventDefault();
      const navH   = document.getElementById("navbar")?.offsetHeight || 80;
      const top    = target.getBoundingClientRect().top + window.scrollY - navH;

      window.scrollTo({ top, behavior: "smooth" });
    });
  });
}


/* ════════════════════════════════════════════════════════════
   FOOTER YEAR
   ════════════════════════════════════════════════════════════ */
function initFooterYear() {
  const el = document.getElementById("footerYear");
  if (el) el.textContent = new Date().getFullYear();
}


/* ════════════════════════════════════════════════════════════
   TERMINAL TYPEWRITER (optional enhancement)
   ════════════════════════════════════════════════════════════ */
(function initTerminalAnimation() {
  const terminal = document.querySelector(".terminal__body");
  if (!terminal) return;

  // Stagger-animate terminal lines on load
  const lines = terminal.querySelectorAll(".terminal__line, .terminal__output");
  lines.forEach((line, i) => {
    line.style.opacity = "0";
    line.style.transform = "translateX(-8px)";
    line.style.transition = `opacity 0.4s ease, transform 0.4s ease`;
    setTimeout(() => {
      line.style.opacity = "1";
      line.style.transform = "none";
    }, 800 + i * 350);
  });
})();
