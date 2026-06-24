/* =========================================
   HARIKARTHIK PORTFOLIO — main.js
   ========================================= */

/* 1. PRELOADER */
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        preloader.style.transition = 'opacity 0.5s ease';
        setTimeout(() => {
            preloader.style.display = 'none';
            document.body.classList.remove('loading');
        }, 500);
    }
    initScrollAnimations();
    initTheme();
});

/* 2. DARK MODE TOGGLE
   - Persists via localStorage
   - Applies [data-theme="dark"] on <html>
   - Toggle button must have id="themeToggle"
*/
function initTheme() {
    const saved = localStorage.getItem('theme') || 'light';
    applyTheme(saved);
}

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

window.toggleTheme = function () {
    const current = document.documentElement.getAttribute('data-theme');
    applyTheme(current === 'dark' ? 'light' : 'dark');
};

/* 3. SCROLL ANIMATIONS */
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
}

/* 4. EXPERIENCE PAGE: ROLE SWITCHER */
window.switchRole = function (index) {
    document.querySelectorAll('.role-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.role-panel').forEach(p => p.classList.remove('active'));

    const tab = document.querySelectorAll('.role-tab')[index];
    const panel = document.getElementById(`role-${index}`);

    if (tab) tab.classList.add('active');
    if (panel) {
        panel.classList.add('active');
        if (window.innerWidth <= 960) {
            setTimeout(() => panel.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
        }
    }
};

/* 5. PROJECTS PAGE: FILTER */
window.filterProjects = function (category, event) {
    if (event?.target) {
        document.querySelectorAll('.filter-list .pill').forEach(b => b.classList.remove('active'));
        event.target.classList.add('active');
    }

    document.querySelectorAll('.visual-card').forEach(card => {
        const cats = card.getAttribute('data-categories') || '';
        const show = category === 'all' || cats.includes(category);
        card.style.display = show ? 'flex' : 'none';
        if (show) {
            card.classList.remove('visible');
            void card.offsetWidth;
            card.classList.add('visible');
        }
    });
};

/* 6. VIDEO MODAL */
window.openVideoModal = function () {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('demoVideo');
    if (modal) { modal.classList.add('show'); modal.style.display = 'flex'; }
    if (video) video.play();
};

window.closeModal = function () {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('demoVideo');
    if (modal) { modal.classList.remove('show'); modal.style.display = 'none'; }
    if (video) { video.pause(); video.currentTime = 0; }
};

document.addEventListener('keydown', e => { if (e.key === 'Escape') window.closeModal(); });
window.addEventListener('click', e => {
    const modal = document.getElementById('videoModal');
    if (e.target === modal) window.closeModal();
});

/* 2. SCROLL ANIMATIONS */
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
}

/* 3. EXPERIENCE PAGE: ROLE SWITCHER */
window.switchRole = function (index) {
    document.querySelectorAll('.role-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.role-panel').forEach(p => p.classList.remove('active'));

    const tab = document.querySelectorAll('.role-tab')[index];
    const panel = document.getElementById(`role-${index}`);

    if (tab) tab.classList.add('active');
    if (panel) {
        panel.classList.add('active');
        if (window.innerWidth <= 960) {
            setTimeout(() => panel.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
        }
    }
};

/* 4. PROJECTS PAGE: FILTER */
window.filterProjects = function (category, event) {
    if (event?.target) {
        document.querySelectorAll('.filter-list .pill').forEach(b => b.classList.remove('active'));
        event.target.classList.add('active');
    }

    document.querySelectorAll('.visual-card').forEach(card => {
        const cats = card.getAttribute('data-categories') || '';
        const show = category === 'all' || cats.includes(category);
        card.style.display = show ? 'flex' : 'none';
        if (show) {
            card.classList.remove('visible');
            void card.offsetWidth;
            card.classList.add('visible');
        }
    });
};

/* 5. VIDEO MODAL */
window.openVideoModal = function () {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('demoVideo');
    if (modal) { modal.classList.add('show'); modal.style.display = 'flex'; }
    if (video) video.play();
};

window.closeModal = function () {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('demoVideo');
    if (modal) { modal.classList.remove('show'); modal.style.display = 'none'; }
    if (video) { video.pause(); video.currentTime = 0; }
};

document.addEventListener('keydown', e => { if (e.key === 'Escape') window.closeModal(); });
window.addEventListener('click', e => {
    const modal = document.getElementById('videoModal');
    if (e.target === modal) window.closeModal();
});