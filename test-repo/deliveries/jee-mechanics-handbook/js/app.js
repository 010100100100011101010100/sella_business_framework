/**
 * JEE Main & Advanced Classical Mechanics Master Handbook
 * Publication-Grade Interactive Reader Application Engine
 *
 * Features:
 *   1. Dual Reading Modes: Chapter Focus Mode (single chapter with smooth transitions)
 *      vs Full Volume Continuous Scroll Mode.
 *   2. Theme Switcher: Warm Ivory (signature soft paper), Pure White, Dark Midnight OLED.
 *   3. Dynamic Typography Scaler: Responsive A- / 100% / A+ controls.
 *   4. Scrollspy Navigation: Real-time sidebar active highlighting with smooth auto-scroll.
 *   5. Chapter Pagination & Smooth Sliding Transitions between chapters.
 *   6. Dynamic Top Reading Progress Bar.
 *   7. Interactive Challenge Solution Disclosures (Expand All / Collapse All).
 *   8. Sidebar Live Search Filtering.
 */

document.addEventListener('DOMContentLoaded', function () {
  'use strict';

  // =========================================================================
  // 1. STATE & STORAGE MANAGEMENT
  // =========================================================================
  const STORAGE_KEY_THEME = 'jee-handbook-theme';
  const STORAGE_KEY_MODE = 'jee-handbook-mode';
  const STORAGE_KEY_FONT = 'jee-handbook-font-size';

  let currentMode = localStorage.getItem(STORAGE_KEY_MODE) || 'focus'; // 'focus' or 'volume'
  let currentTheme = localStorage.getItem(STORAGE_KEY_THEME) || 'warm-paper';
  let currentFontSize = parseInt(localStorage.getItem(STORAGE_KEY_FONT), 10) || 16;
  let activeChapterId = 'cover';

  const docEl = document.documentElement;
  const body = document.body;
  const progressBar = document.getElementById('reading-progress-bar') || document.getElementById('progress-bar');
  const chapterPill = document.getElementById('current-chapter-pill');
  const modeToggleBtn = document.getElementById('mode-toggle-btn');
  const modeText = document.getElementById('mode-text');
  const sidebar = document.getElementById('sidebar') || document.querySelector('.sidebar-nav');
  const sidebarToggle = document.getElementById('sidebar-toggle');

  // Chapters & Articles inventory
  const chapters = Array.from(document.querySelectorAll('article.chapter, section.book-cover, section#toc, section#trap-analysis, section#trap-index, section#pyq-index, section#practice-index'));
  const navLinks = Array.from(document.querySelectorAll('.nav-link, .nav-sublink'));

  // =========================================================================
  // 2. THEME ENGINE
  // =========================================================================
  function applyTheme(themeName) {
    currentTheme = themeName;
    docEl.setAttribute('data-theme', themeName);
    try {
      localStorage.setItem(STORAGE_KEY_THEME, themeName);
    } catch (e) {}

    // Update active state on theme buttons
    document.querySelectorAll('.theme-btn').forEach(function (btn) {
      if (btn.getAttribute('data-theme-target') === themeName) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }

  document.querySelectorAll('.theme-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const target = this.getAttribute('data-theme-target');
      if (target) applyTheme(target);
    });
  });

  applyTheme(currentTheme);

  // =========================================================================
  // 3. FONT SIZE ENGINE
  // =========================================================================
  function applyFontSize(size) {
    currentFontSize = Math.min(20, Math.max(14, size));
    docEl.style.fontSize = currentFontSize + 'px';
    const resetBtn = document.getElementById('font-reset-btn');
    if (resetBtn) {
      const percent = Math.round((currentFontSize / 16) * 100);
      resetBtn.textContent = percent + '%';
    }
    try {
      localStorage.setItem(STORAGE_KEY_FONT, currentFontSize.toString());
    } catch (e) {}
  }

  const decBtn = document.getElementById('font-dec-btn');
  const resetBtn = document.getElementById('font-reset-btn');
  const incBtn = document.getElementById('font-inc-btn');

  if (decBtn) decBtn.addEventListener('click', () => applyFontSize(currentFontSize - 1));
  if (resetBtn) resetBtn.addEventListener('click', () => applyFontSize(16));
  if (incBtn) incBtn.addEventListener('click', () => applyFontSize(currentFontSize + 1));

  applyFontSize(currentFontSize);

  // =========================================================================
  // 4. DUAL READING MODE ENGINE (FOCUS MODE vs VOLUME MODE)
  // =========================================================================
  function setReadingMode(mode) {
    currentMode = mode;
    try {
      localStorage.setItem(STORAGE_KEY_MODE, mode);
    } catch (e) {}

    if (mode === 'focus') {
      body.classList.add('focus-mode');
      if (modeText) modeText.textContent = 'Focus Mode';
      if (modeToggleBtn) modeToggleBtn.classList.add('active-mode');
      showChapterInFocusMode(activeChapterId);
    } else {
      body.classList.remove('focus-mode');
      if (modeText) modeText.textContent = 'All Chapters';
      if (modeToggleBtn) modeToggleBtn.classList.remove('active-mode');
      // In Volume mode, ensure all chapters are visible
      chapters.forEach(ch => {
        ch.style.display = '';
        ch.classList.remove('active-focus');
      });
      // Scroll to current chapter
      const target = document.getElementById(activeChapterId) || document.getElementById(activeChapterId.replace('chapter-', 'ch'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    }
    updateProgressBar();
  }

  function getChapterTitle(el) {
    if (!el) return 'Overview';
    const titleEl = el.querySelector('.chapter-title, .book-title');
    if (titleEl) {
      const text = titleEl.textContent.trim();
      const numMatch = el.getAttribute('id') ? el.getAttribute('id').match(/(\d+)/) : null;
      if (numMatch) return 'Ch 0' + numMatch[1] + ': ' + text.split(':')[0];
      return text.length > 25 ? text.substring(0, 22) + '...' : text;
    }
    return 'Overview';
  }

  function showChapterInFocusMode(targetId) {
    // Normalize targetId
    let resolvedId = targetId;
    if (targetId.startsWith('ch') && !targetId.includes('-sec') && document.getElementById('chapter-' + targetId.replace('ch', ''))) {
      resolvedId = 'chapter-' + targetId.replace('ch', '');
    }

    let activeEl = document.getElementById(resolvedId);
    if (!activeEl && targetId.includes('-sec')) {
      // Sub-section anchor: find parent article
      const secEl = document.getElementById(targetId);
      if (secEl) {
        activeEl = secEl.closest('article.chapter, section');
        resolvedId = activeEl ? activeEl.getAttribute('id') : resolvedId;
      }
    }

    if (!activeEl) {
      activeEl = document.getElementById('cover') || chapters[0];
      resolvedId = activeEl ? activeEl.getAttribute('id') : 'cover';
    }

    activeChapterId = resolvedId;

    // Apply active-focus class
    chapters.forEach(ch => {
      if (ch.getAttribute('id') === resolvedId) {
        ch.classList.add('active-focus');
      } else {
        ch.classList.remove('active-focus');
      }
    });

    // Update topbar pill badge
    if (chapterPill) {
      chapterPill.textContent = getChapterTitle(activeEl);
    }

    // Update sidebar navigation active links
    updateActiveSidebarLink(resolvedId);

    // Smooth scroll reading container to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
    updateProgressBar();
  }

  function updateActiveSidebarLink(currentId) {
    navLinks.forEach(function (link) {
      const href = link.getAttribute('href') || '';
      const cleanHref = href.replace('#', '');
      if (cleanHref === currentId ||
          cleanHref === currentId.replace('chapter-', 'ch') ||
          (currentId.startsWith('chapter-') && cleanHref === 'chapter-' + currentId.split('-')[1])) {
        link.classList.add('active');
        // Scroll link into view inside sidebar if not visible
        if (sidebar && link.offsetTop > sidebar.clientHeight) {
          sidebar.scrollTo({ top: link.offsetTop - 120, behavior: 'smooth' });
        }
      } else {
        link.classList.remove('active');
      }
    });
  }

  if (modeToggleBtn) {
    modeToggleBtn.addEventListener('click', function () {
      setReadingMode(currentMode === 'focus' ? 'volume' : 'focus');
    });
  }

  // Initialize initial mode
  setReadingMode(currentMode);

  // =========================================================================
  // 5. READING PROGRESS BAR
  // =========================================================================
  function updateProgressBar() {
    if (!progressBar) return;

    if (currentMode === 'focus') {
      const activeEl = document.querySelector('.active-focus');
      if (activeEl) {
        const rect = activeEl.getBoundingClientRect();
        const totalHeight = activeEl.offsetHeight;
        const visibleHeight = window.innerHeight;
        const scrolled = Math.max(0, -rect.top);
        const maxScroll = Math.max(1, totalHeight - visibleHeight);
        const percent = Math.min(100, Math.max(0, (scrolled / maxScroll) * 100));
        progressBar.style.width = percent + '%';
        progressBar.setAttribute('aria-valuenow', Math.round(percent));
        return;
      }
    }

    // Continuous scroll mode calculation
    const scrollTop = window.pageYOffset || docEl.scrollTop || document.body.scrollTop || 0;
    const scrollHeight = docEl.scrollHeight - docEl.clientHeight;
    if (scrollHeight > 0) {
      const scrollPercent = Math.min(100, Math.max(0, (scrollTop / scrollHeight) * 100));
      progressBar.style.width = scrollPercent + '%';
      progressBar.setAttribute('aria-valuenow', Math.round(scrollPercent));
    }
  }

  window.addEventListener('scroll', updateProgressBar, { passive: true });
  window.addEventListener('resize', updateProgressBar, { passive: true });

  // =========================================================================
  // 6. SCROLLSPY (CONTINUOUS VOLUME MODE)
  // =========================================================================
  function onScrollVolumeMode() {
    if (currentMode === 'focus') return;

    const scrollPosition = window.pageYOffset || docEl.scrollTop;
    const triggerOffset = 160;
    let foundActive = null;

    chapters.forEach(function (section) {
      const top = section.offsetTop - triggerOffset;
      const height = section.offsetHeight;
      if (scrollPosition >= top && scrollPosition < top + height) {
        foundActive = section;
      }
    });

    if (!foundActive && scrollPosition < 300) {
      foundActive = document.getElementById('cover');
    }

    if (foundActive) {
      const activeId = foundActive.getAttribute('id');
      if (activeId && activeId !== activeChapterId) {
        activeChapterId = activeId;
        updateActiveSidebarLink(activeId);
        if (chapterPill) {
          chapterPill.textContent = getChapterTitle(foundActive);
        }
      }
    }
  }

  window.addEventListener('scroll', onScrollVolumeMode, { passive: true });

  // =========================================================================
  // 7. INTERNAL LINK ROUTING & SMOOTH TRANSITIONS
  // =========================================================================
  document.addEventListener('click', function (e) {
    const link = e.target.closest('a[href^="#"]');
    if (!link) return;

    const href = link.getAttribute('href');
    if (!href || href === '#') return;
    const targetId = href.substring(1);

    if (currentMode === 'focus') {
      e.preventDefault();
      // In focus mode, switch chapter view smoothly
      showChapterInFocusMode(targetId);
      history.pushState(null, '', href);

      // If linking to specific section within chapter
      if (targetId.includes('-sec')) {
        setTimeout(() => {
          const secEl = document.getElementById(targetId);
          if (secEl) secEl.scrollIntoView({ behavior: 'smooth' });
        }, 50);
      }
    } else {
      // In volume mode, smooth scroll to element
      const targetElement = document.getElementById(targetId) || document.getElementById(targetId.replace('chapter-', 'ch'));
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({ behavior: 'smooth' });
        history.pushState(null, '', href);
      }
    }

    // Close mobile drawer if open
    if (window.innerWidth <= 992 && sidebar && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  });

  // Handle browser back/forward buttons
  window.addEventListener('popstate', function () {
    const hash = window.location.hash.substring(1);
    if (hash) {
      if (currentMode === 'focus') {
        showChapterInFocusMode(hash);
      } else {
        const el = document.getElementById(hash);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });

  // Check URL hash on initial page load
  if (window.location.hash) {
    const initialHash = window.location.hash.substring(1);
    if (currentMode === 'focus') {
      showChapterInFocusMode(initialHash);
    }
  }

  // =========================================================================
  // 8. RESPONSIVE MOBILE DRAWER
  // =========================================================================
  let backdrop = document.querySelector('.sidebar-backdrop');
  if (!backdrop && sidebar) {
    backdrop = document.createElement('div');
    backdrop.className = 'sidebar-backdrop';
    document.body.appendChild(backdrop);
  }

  function openSidebar() {
    if (sidebar) sidebar.classList.add('open');
    if (backdrop) backdrop.classList.add('active');
    body.style.overflow = window.innerWidth <= 992 ? 'hidden' : '';
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (backdrop) backdrop.classList.remove('active');
    body.style.overflow = '';
  }

  function toggleSidebar() {
    if (sidebar && sidebar.classList.contains('open')) {
      closeSidebar();
    } else {
      openSidebar();
    }
  }

  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', function (e) {
      e.stopPropagation();
      toggleSidebar();
    });
  }

  if (backdrop) backdrop.addEventListener('click', closeSidebar);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && sidebar && sidebar.classList.contains('open')) {
      closeSidebar();
    }
  });

  // =========================================================================
  // 9. SIDEBAR TOPIC SEARCH FILTER
  // =========================================================================
  const searchInput = document.getElementById('topic-search');
  if (searchInput) {
    searchInput.addEventListener('input', function (e) {
      const query = e.target.value.toLowerCase().trim();
      const navItems = document.querySelectorAll('.nav-group, .chapter-nav-item');

      if (!query) {
        navItems.forEach(item => { item.style.display = ''; });
        return;
      }

      navItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        item.style.display = text.includes(query) ? '' : 'none';
      });
    });
  }

  // =========================================================================
  // 10. EXPAND / COLLAPSE ALL SOLUTIONS
  // =========================================================================
  const expandBtn = document.getElementById('expand-all-btn');
  const collapseBtn = document.getElementById('collapse-all-btn');

  if (expandBtn) {
    expandBtn.addEventListener('click', function () {
      document.querySelectorAll('details.challenge-details, details.solution-details')
        .forEach(el => el.setAttribute('open', 'true'));
    });
  }

  if (collapseBtn) {
    collapseBtn.addEventListener('click', function () {
      document.querySelectorAll('details.challenge-details, details.solution-details')
        .forEach(el => el.removeAttribute('open'));
    });
  }

  console.log('[OK] JEE Classical Mechanics Master Reader Engine initialized (Mode: ' + currentMode + ').');
});
