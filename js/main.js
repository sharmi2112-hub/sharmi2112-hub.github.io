/**
 * Sharmi Thakor - Data & ML Portfolio Scripts
 * Distinct Design: Pill Navigation, Interactive Bento Filters, Modal Viewport
 */

document.addEventListener('DOMContentLoaded', () => {
  initCategoryFilters();
  initModalListeners();
});

/* Category Filter Tabs */
function initCategoryFilters() {
  const filterTabs = document.querySelectorAll('.filter-tab');
  const cards = document.querySelectorAll('.project-card');

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filter = tab.getAttribute('data-filter');

      cards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'grid';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* Switch Main Viewport Image on Thumbnail Click */
function switchMainImage(targetId, newSrc, newAlt) {
  const targetImg = document.getElementById(targetId);
  if (targetImg) {
    targetImg.src = newSrc;
    if (newAlt) targetImg.alt = newAlt;

    const parentStage = targetImg.closest('.display-stage');
    if (parentStage) {
      parentStage.setAttribute('onclick', `openLightbox('${newSrc}', '${newAlt}')`);
    }
  }
}

/* Lightbox Modal */
function openLightbox(src, title) {
  const backdrop = document.getElementById('lightbox-backdrop');
  const img = document.getElementById('lightbox-image');
  const titleEl = document.getElementById('lightbox-title');

  if (backdrop && img) {
    img.src = src;
    if (titleEl && title) titleEl.textContent = title;
    backdrop.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
}

function closeLightbox(e) {
  if (e && e.target && e.target.closest('.lightbox-box') && !e.target.classList.contains('lightbox-exit')) {
    return;
  }
  const backdrop = document.getElementById('lightbox-backdrop');
  const img = document.getElementById('lightbox-image');

  if (backdrop) {
    backdrop.classList.remove('open');
    if (img) img.src = '';
    document.body.style.overflow = '';
  }
}

function initModalListeners() {
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeLightbox();
    }
  });
}

// Expose globals for inline attributes
window.switchMainImage = switchMainImage;
window.openLightbox = openLightbox;
window.closeLightbox = closeLightbox;
