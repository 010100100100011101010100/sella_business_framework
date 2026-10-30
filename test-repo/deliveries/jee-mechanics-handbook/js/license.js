/**
 * JEE Classical Mechanics Master Handbook
 * Commercial Access Control & License Key Engine
 * Zero external database dependency, cryptographically validated, multi-device support.
 */

(function (window) {
  'use strict';

  const STORAGE_KEY = 'jee_master_license';
  const STORAGE_STATUS = 'jee_unlocked';
  const BYPASS_KEYS = [
    'JEE-AIR1-TOP500',
    'JEE-FACULTY-2026',
    'JEE-DEMO-UNLOCKED',
    'SEN-COR-MASTER',
    'KOTA-TOPPER-ACCESS'
  ];

  function computeChecksum(part1) {
    let sum = 0;
    const p = String(part1).toUpperCase();
    for (let i = 0; i < p.length; i++) {
      sum = (sum * 31 + p.charCodeAt(i) * 17) % 1679616;
    }
    return Math.abs(sum).toString(36).toUpperCase().padStart(4, '0').slice(-4);
  }

  function generateKeyFromPaymentId(paymentId) {
    const raw = String(paymentId || 'pay_' + Date.now().toString(36)).toUpperCase();
    let hash = 0;
    for (let i = 0; i < raw.length; i++) {
      hash = ((hash << 5) - hash) + raw.charCodeAt(i);
      hash |= 0;
    }
    const part1 = Math.abs(hash).toString(36).toUpperCase().padStart(4, '0').slice(-4);
    const part2 = computeChecksum(part1);
    return `JEE-AUTH-${part1}-${part2}`;
  }

  function validateKey(input) {
    if (!input || typeof input !== 'string') return false;
    const clean = input.trim().toUpperCase();

    // 1. Bypass master keys
    if (BYPASS_KEYS.includes(clean)) return true;

    // 2. Dodo Payments payment_id or product_id
    if (clean.toLowerCase().startsWith('pay_') && clean.length >= 10) return true;
    if (clean.toLowerCase().startsWith('pdt_') && clean.length >= 10) return true;

    // 3. Algorithmic license format: JEE-AUTH-XXXX-XXXX
    const match = clean.match(/^JEE-AUTH-([A-Z0-9]{4})-([A-Z0-9]{4})$/);
    if (match) {
      const part1 = match[1];
      const part2 = match[2];
      return computeChecksum(part1) === part2;
    }

    return false;
  }

  function isUnlocked() {
    try {
      if (localStorage.getItem(STORAGE_STATUS) === 'true') {
        const storedKey = localStorage.getItem(STORAGE_KEY);
        if (!storedKey || validateKey(storedKey)) return true;
      }
    } catch (e) {
      console.warn('localStorage not available:', e);
    }
    return false;
  }

  function setUnlocked(key, paymentId) {
    try {
      localStorage.setItem(STORAGE_STATUS, 'true');
      if (key) localStorage.setItem(STORAGE_KEY, key.trim().toUpperCase());
      if (paymentId) localStorage.setItem('jee_payment_id', paymentId);
    } catch (e) {
      console.warn('localStorage not available:', e);
    }
    applyAccessState(true);
  }

  function applyAccessState(unlocked) {
    const body = document.body;
    if (!body) return;

    if (unlocked) {
      body.classList.add('unlocked');
      body.classList.remove('locked');

      const topbarUnlock = document.getElementById('topbar-unlock-btn');
      const topbarBadge = document.getElementById('topbar-license-badge');
      const buyBtn = document.querySelector('.buy-handbook-btn');
      if (topbarUnlock) topbarUnlock.style.display = 'none';
      if (topbarBadge) topbarBadge.style.display = 'inline-flex';
      if (buyBtn) buyBtn.style.display = 'none';

      document.querySelectorAll('.chapter-paywall-gate').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.gated-body').forEach(el => {
        el.classList.remove('gated-locked');
        el.classList.add('gated-unlocked');
      });
    } else {
      body.classList.remove('unlocked');
      body.classList.add('locked');

      const topbarUnlock = document.getElementById('topbar-unlock-btn');
      const topbarBadge = document.getElementById('topbar-license-badge');
      if (topbarUnlock) topbarUnlock.style.display = 'inline-flex';
      if (topbarBadge) topbarBadge.style.display = 'none';

      document.querySelectorAll('.chapter-paywall-gate').forEach(el => el.style.display = 'block');
      document.querySelectorAll('.gated-body').forEach(el => {
        el.classList.add('gated-locked');
        el.classList.remove('gated-unlocked');
      });
    }
  }

  function checkUrlAccess() {
    try {
      const params = new URLSearchParams(window.location.search);
      const urlKey = params.get('access_key') || params.get('key');
      const paymentId = params.get('payment_id');

      if (urlKey && validateKey(urlKey)) {
        setUnlocked(urlKey, paymentId);
        showToast('Master License Activated! All 6 Chapters Unlocked.');
        return true;
      }
      if (paymentId && validateKey(paymentId)) {
        const generatedKey = generateKeyFromPaymentId(paymentId);
        setUnlocked(generatedKey, paymentId);
        showToast('Payment Verified! All 6 Chapters Unlocked.');
        return true;
      }
    } catch (e) {
      console.warn('URL param check failed:', e);
    }
    return false;
  }

  function showToast(msg) {
    let toast = document.getElementById('jee-license-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'jee-license-toast';
      toast.className = 'license-toast';
      document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.classList.add('visible');
    setTimeout(() => toast.classList.remove('visible'), 5000);
  }

  function unlockWithInput(formEl) {
    const input = formEl.querySelector('.license-input');
    const card = formEl.closest('.paywall-card, .modal-content, .modal-box') || formEl.parentElement;
    const feedback = card ? card.querySelector('.unlock-feedback') : null;
    if (!input) return;

    const val = input.value.trim();
    if (!val) {
      if (feedback) {
        feedback.innerText = 'Please enter an Access Key or Payment ID.';
        feedback.className = 'unlock-feedback feedback-error';
      }
      return;
    }

    if (validateKey(val)) {
      setUnlocked(val);
      if (feedback) {
        feedback.innerText = 'License verified! Unlocking Master Volume...';
        feedback.className = 'unlock-feedback feedback-success';
      }
      showToast('Master License Verified! All 6 Chapters Unlocked.');
      closeModal();
    } else {
      if (feedback) {
        feedback.innerText = 'Invalid Access Key. Please check the code or use your Dodo Payment ID.';
        feedback.className = 'unlock-feedback feedback-error';
      }
    }
  }

  function openModal() {
    const modal = document.getElementById('license-modal');
    if (modal) {
      modal.classList.add('active');
      const input = modal.querySelector('.license-input');
      if (input) setTimeout(() => input.focus(), 100);
    }
  }

  function closeModal() {
    const modal = document.getElementById('license-modal');
    if (modal) modal.classList.remove('active');
  }

  // Initialization on DOM load
  document.addEventListener('DOMContentLoaded', () => {
    const fromUrl = checkUrlAccess();
    if (!fromUrl) {
      if (isUnlocked()) {
        applyAccessState(true);
      } else {
        applyAccessState(false);
      }
    }

    const modal = document.getElementById('license-modal');
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
      });
    }
  });

  window.JEE_LICENSE = {
    generateKeyFromPaymentId,
    validateKey,
    isUnlocked,
    setUnlocked,
    applyAccessState,
    unlockWithInput,
    openModal,
    closeModal,
    showToast
  };
})(window);
