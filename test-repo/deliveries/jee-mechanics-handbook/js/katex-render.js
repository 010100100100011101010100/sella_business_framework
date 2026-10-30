/**
 * JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook
 * KaTeX Mathematical Typesetting Engine & Offline Resilience Pipeline
 */

(function () {
  'use strict';

  // Master KaTeX Configuration with JEE Physics & Rotational Dynamics Macros
  const KATEX_CONFIG = {
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '\\[', right: '\\]', display: true },
      { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false }
    ],
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    throwOnError: false,
    errorColor: '#ef4444',
    strict: false,
    trust: true,
    macros: {
      // Vector and Tensor Typography
      '\\bm': '\\boldsymbol{#1}',
      '\\mathbf': '\\boldsymbol{#1}',
      '\\va': '\\vec{#1}',
      '\\vb': '\\mathbf{#1}',
      '\\vu': '\\hat{#1}',

      // Vector Calculus Operators
      '\\grad': '\\boldsymbol{\\nabla}',
      '\\div': '\\boldsymbol{\\nabla} \\cdot',
      '\\curl': '\\boldsymbol{\\nabla} \\times',
      '\\laplacian': '\\nabla^2',

      // Differential and Derivative Calculus Notation
      '\\dd': '\\mathrm{d}#1',
      '\\dv': '\\frac{\\mathrm{d}#1}{\\mathrm{d}#2}',
      '\\pdv': '\\frac{\\partial #1}{\\partial #2}',

      // Rotational Mechanics & Rigid Body Shorthands
      '\\Icm': 'I_{\\text{cm}}',
      '\\rcm': '\\mathbf{r}_{\\text{cm}}',
      '\\vcm': '\\mathbf{v}_{\\text{cm}}',
      '\\acm': '\\mathbf{a}_{\\text{cm}}',
      '\\Lcm': '\\mathbf{L}_{\\text{cm}}',
      '\\IAOR': '\\text{IAOR}'
    }
  };

  /**
   * Renders KaTeX math in the target DOM element or whole document
   * @param {HTMLElement} [rootElement]
   */
  function renderAllMath(rootElement) {
    const target = rootElement || document.getElementById('book-content') || document.body;
    if (typeof window.renderMathInElement === 'function') {
      try {
        window.renderMathInElement(target, KATEX_CONFIG);
      } catch (err) {
        console.error('KaTeX rendering error:', err);
      }
    } else {
      loadOfflineFallback(target);
    }
  }

  /**
   * Robust Offline Fallback Mechanism for Standalone HTML distribution.
   * Dynamically attaches local asset scripts and CSS if not already present.
   */
  function loadOfflineFallback(target) {
    console.warn('KaTeX auto-render not yet initialized. Attaching local offline fallback from assets/katex/...');

    // 1. Ensure KaTeX CSS is present
    if (!document.getElementById('katex-css-local')) {
      const link = document.createElement('link');
      link.id = 'katex-css-local';
      link.rel = 'stylesheet';
      link.href = 'assets/katex/katex.min.css';
      document.head.appendChild(link);
    }

    // 2. Ensure KaTeX JS is loaded
    function injectAutoRender() {
      if (typeof window.renderMathInElement === 'function') {
        window.renderMathInElement(target, KATEX_CONFIG);
        return;
      }
      const autoRenderScript = document.createElement('script');
      autoRenderScript.src = 'assets/katex/contrib/auto-render.min.js';
      autoRenderScript.onload = function () {
        if (typeof window.renderMathInElement === 'function') {
          window.renderMathInElement(target, KATEX_CONFIG);
          console.log('[OK] KaTeX successfully rendered via local offline assets.');
        }
      };
      document.body.appendChild(autoRenderScript);
    }

    if (typeof window.katex === 'undefined') {
      const katexScript = document.createElement('script');
      katexScript.src = 'assets/katex/katex.min.js';
      katexScript.onload = injectAutoRender;
      katexScript.onerror = function () {
        console.error('Failed to load local KaTeX JS from assets/katex/katex.min.js');
      };
      document.body.appendChild(katexScript);
    } else {
      injectAutoRender();
    }
  }

  // Expose API for external invocation or re-render
  window.katexEngine = {
    config: KATEX_CONFIG,
    render: renderAllMath,
    fallback: loadOfflineFallback
  };

  // Run automatically when DOM is interactive
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      renderAllMath();
    });
  } else {
    renderAllMath();
  }
})();
