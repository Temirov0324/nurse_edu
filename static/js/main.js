// Enhanced JavaScript for Course Center Website - Modern & Responsive

class CourseCenter {
    constructor() {
        this.init();
    }

    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initializeApp());
        } else {
            this.initializeApp();
        }
    }

    initializeApp() {
        console.log('🚀 CourseCenter App Initialized');
        
        // Initialize all components
        this.initNavigation();
        this.initScrollEffects();
        this.initAnimations();
        this.initImageLoading();
        this.initFormEnhancements();
        this.initSmoothScrolling();
        this.initParallaxEffects();
        this.initCounters();
        this.initTooltips();
        this.initFAQ();
        this.initVideoTriggers();
        this.initAOS();
        this.initPerformanceOptimizations();
        
        // Hide loading screen
        this.hideLoadingScreen();
    }

    hideLoadingScreen() {
        const loadingScreen = document.getElementById('loading-screen');
        if (loadingScreen) {
            setTimeout(() => {
                loadingScreen.style.opacity = '0';
                setTimeout(() => {
                    loadingScreen.style.display = 'none';
                }, 500);
            }, 1000);
        }
    }

    // Enhanced Navigation with modern features
    initNavigation() {
        const navToggle = document.getElementById('nav-toggle');
        const navMenu = document.getElementById('nav-menu');
        const navbar = document.querySelector('.navbar');
        const body = document.body;

        // Create overlay for mobile menu
        const overlay = document.createElement('div');
        overlay.className = 'nav-overlay';
        body.appendChild(overlay);

        // Mobile menu toggle with enhanced functionality
        if (navToggle && navMenu) {
            navToggle.addEventListener('click', (e) => {
                e.stopPropagation();
                const isActive = navMenu.classList.contains('active');
                
                if (isActive) {
                    this.closeMenu(navMenu, navToggle, overlay);
                } else {
                    this.openMenu(navMenu, navToggle, overlay);
                }
            });

            // Close mobile menu when clicking on a link
            document.querySelectorAll('a.nav-link, .dropdown-item').forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        this.closeMenu(navMenu, navToggle, overlay);
                    }
                });
            });

            // Close mobile menu when clicking overlay
            overlay.addEventListener('click', () => {
                this.closeMenu(navMenu, navToggle, overlay);
            });

            // Close menu on Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                    this.closeMenu(navMenu, navToggle, overlay);
                }
            });
        }

        // Enhanced navbar scroll effect with progress indicator
        if (navbar) {
            let ticking = false;
            const updateNavbar = () => {
                const scrolled = window.scrollY > 100;
                navbar.classList.toggle('scrolled', scrolled);
                
                // Update scroll progress indicator
                const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
                const scrollProgress = (window.scrollY / scrollHeight) * 100;
                navbar.style.setProperty('--scroll-width', `${Math.min(scrollProgress, 100)}%`);
                
                ticking = false;
            };

            window.addEventListener('scroll', () => {
                if (!ticking) {
                    requestAnimationFrame(updateNavbar);
                    ticking = true;
                }
            });
        }

        // Dropdown functionality for mobile
        const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
        dropdownToggles.forEach(toggle => {
            toggle.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    const dropdown = toggle.closest('.nav-dropdown');
                    dropdown.classList.toggle('active');
                }
            });
        });

        // Enhanced active link highlighting
        this.updateActiveLink();
    }

    openMenu(navMenu, navToggle, overlay) {
        navMenu.classList.add('active');
        navToggle.classList.add('active');
        overlay.classList.add('active');
        navToggle.setAttribute('aria-expanded', 'true');
        document.body.style.overflow = 'hidden';
    }

    closeMenu(navMenu, navToggle, overlay) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
        overlay.classList.remove('active');
        navToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
    }

    updateActiveLink() {
        const currentPath = window.location.pathname;
        const links = document.querySelectorAll('a.nav-link, .dropdown-item');

        links.forEach(link => {
            if (link.href) {
                const linkPath = new URL(link.href).pathname;
                if (linkPath === currentPath) {
                    link.style.color = '#4299e1';
                    link.style.background = 'rgba(66, 153, 225, 0.1)';
                    link.setAttribute('aria-current', 'page');

                    // If it's a dropdown item, highlight the parent dropdown toggle as well
                    const dropdown = link.closest('.nav-dropdown');
                    if (dropdown) {
                        const toggle = dropdown.querySelector('.dropdown-toggle');
                        if (toggle) {
                            toggle.style.color = '#4299e1';
                            toggle.style.background = 'rgba(66, 153, 225, 0.1)';
                        }
                    }
                }
            }
        });
    }

    // Scroll Effects
    initScrollEffects() {
        // Parallax effect for hero section
        const hero = document.querySelector('.hero');
        if (hero) {
            window.addEventListener('scroll', function() {
                const scrolled = window.pageYOffset;
                const rate = scrolled * -0.5;
                hero.style.transform = `translateY(${rate}px)`;
            });
        }

        // Fade in elements on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';

                    // Add staggered animation for grid items
                    if (entry.target.classList.contains('stagger-animation')) {
                        const children = entry.target.children;
                        Array.from(children).forEach((child, index) => {
                            setTimeout(() => {
                                child.style.opacity = '1';
                                child.style.transform = 'translateY(0)';
                            }, index * 100);
                        });
                    }
                }
            });
        }, observerOptions);

        // Observe elements for scroll animations
        const elementsToAnimate = document.querySelectorAll(`
            .section-header,
            .department-card,
            .news-card,
            .specialist-card,
            .course-card,
            .vacancy-card,
            .certificate-card,
            .direction-card,
            .module-item,
            .contact-item
        `);

        elementsToAnimate.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });

        // Add stagger animation class to grids
        const grids = document.querySelectorAll(`
            .departments-grid,
            .news-grid,
            .specialists-grid,
            .courses-grid,
            .certificates-grid,
            .directions-grid
        `);

        grids.forEach(grid => {
            grid.classList.add('stagger-animation');
            observer.observe(grid);
        });
    }

    // Enhanced Animations
    initAnimations() {
        // Hover effects for cards
        const cards = document.querySelectorAll(`
            .department-card,
            .news-card,
            .specialist-card,
            .course-card,
            .vacancy-card,
            .certificate-card,
            .direction-card
        `);

        cards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.02)';
            });

            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });

        // Button hover effects
        const buttons = document.querySelectorAll('.btn');
        buttons.forEach(btn => {
            btn.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-3px)';
            });

            btn.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
    }

    // Enhanced Image Loading
    initImageLoading() {
        const images = document.querySelectorAll('img');

        images.forEach(img => {
            // Add loading placeholder
            img.style.backgroundColor = '#f7fafc';
            img.style.transition = 'opacity 0.3s ease';

            if (!img.complete) {
                img.style.opacity = '0';

                img.addEventListener('load', function() {
                    this.style.opacity = '1';
                    this.classList.add('loaded');
                });

                img.addEventListener('error', function() {
                    this.style.opacity = '0.5';
                    this.alt = 'Rasm yuklanmadi';
                });
            } else {
                img.style.opacity = '1';
                img.classList.add('loaded');
            }
        });

        // Lazy loading for images
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        if (img.dataset.src) {
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                            observer.unobserve(img);
                        }
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }

    // Form Enhancements
    initFormEnhancements() {
        const forms = document.querySelectorAll('form');

        forms.forEach(form => {
            // Add loading state to form submissions
            form.addEventListener('submit', function() {
                const submitBtn = this.querySelector('button[type="submit"]');
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Yuborilmoqda...';
                    submitBtn.style.opacity = '0.7';
                }
            });

            // Enhanced form validation
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                // Real-time validation
                input.addEventListener('blur', () => {
                    this.validateField(input);
                });

                input.addEventListener('input', function() {
                    if (this.classList.contains('error')) {
                        this.validateField(this);
                    }
                });

                // Enhanced focus effects
                input.addEventListener('focus', function() {
                    this.parentElement.classList.add('focused');
                });

                input.addEventListener('blur', function() {
                    this.parentElement.classList.remove('focused');
                });
            });
        });

        // File upload enhancements
        const fileInputs = document.querySelectorAll('input[type="file"]');
        fileInputs.forEach(input => {
            input.addEventListener('change', function() {
                const fileName = this.files[0]?.name;
                const label = this.nextElementSibling || this.previousElementSibling;
                if (label && fileName) {
                    label.textContent = `Tanlangan: ${fileName}`;
                    label.style.color = '#38a169';
                }
            });
        });
    }

    // Field validation function
    validateField(field) {
        const value = field.value.trim();
        let isValid = true;
        let errorMessage = '';

        // Remove existing error styles
        field.classList.remove('error');
        const existingError = field.parentElement.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }

        // Required field validation
        if (field.hasAttribute('required') && !value) {
            isValid = false;
            errorMessage = 'Bu maydon to\'ldirilishi shart';
        }

        // Email validation
        if (field.type === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Email manzil noto\'g\'ri formatda';
            }
        }

        // Phone validation
        if (field.type === 'tel' && value) {
            const phoneRegex = /^[\+]?[0-9\s\-\(\)]{10,}$/;
            if (!phoneRegex.test(value)) {
                isValid = false;
                errorMessage = 'Telefon raqam noto\'g\'ri formatda';
            }
        }

        // Show error if validation failed
        if (!isValid) {
            field.classList.add('error');
            field.style.borderColor = '#e53e3e';

            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.style.color = '#e53e3e';
            errorDiv.style.fontSize = '0.875rem';
            errorDiv.style.marginTop = '0.25rem';
            errorDiv.textContent = errorMessage;

            field.parentElement.appendChild(errorDiv);
        } else {
            field.style.borderColor = '#38a169';
        }

        return isValid;
    }

    // Smooth Scrolling
    initSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const offsetTop = target.offsetTop - 100; // Account for fixed navbar
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Back to top button
        const backToTop = document.createElement('button');
        backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
        backToTop.className = 'back-to-top';
        backToTop.style.cssText = `
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #4299e1, #3182ce);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 4px 20px rgba(66, 153, 225, 0.4);
        `;

        document.body.appendChild(backToTop);

        window.addEventListener('scroll', function() {
            if (window.scrollY > 500) {
                backToTop.style.opacity = '1';
                backToTop.style.visibility = 'visible';
            } else {
                backToTop.style.opacity = '0';
                backToTop.style.visibility = 'hidden';
            }
        });

        backToTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Parallax Effects
    initParallaxEffects() {
        const parallaxElements = document.querySelectorAll('.parallax');

        if (parallaxElements.length > 0) {
            window.addEventListener('scroll', function() {
                const scrolled = window.pageYOffset;

                parallaxElements.forEach(element => {
                    const rate = scrolled * -0.3;
                    element.style.transform = `translateY(${rate}px)`;
                });
            });
        }
    }

    // Enhanced Counter Animation with easing
    initCounters() {
        const counters = document.querySelectorAll('.counter');
        if (!counters.length) return;

        const easeOutQuart = (t) => 1 - (--t) * t * t * t;

        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.dataset.target);
                    const duration = 2500;
                    const startTime = performance.now();

                    const updateCounter = (currentTime) => {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const easedProgress = easeOutQuart(progress);
                        const current = Math.floor(easedProgress * target);

                        counter.textContent = current.toLocaleString();

                        if (progress < 1) {
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target.toLocaleString();
                        }
                    };

                    requestAnimationFrame(updateCounter);
                    counterObserver.unobserve(counter);
                }
            });
        }, {
            threshold: 0.5,
            rootMargin: '0px 0px -50px 0px'
        });

        counters.forEach(counter => {
            counterObserver.observe(counter);
        });
    }

    // Tooltips
    initTooltips() {
        const tooltipElements = document.querySelectorAll('[data-tooltip]');

        tooltipElements.forEach(element => {
            element.addEventListener('mouseenter', function() {
                const tooltip = document.createElement('div');
                tooltip.className = 'tooltip';
                tooltip.textContent = this.dataset.tooltip;
                tooltip.style.cssText = `
                    position: absolute;
                    background: #2d3748;
                    color: white;
                    padding: 8px 12px;
                    border-radius: 6px;
                    font-size: 0.875rem;
                    white-space: nowrap;
                    z-index: 1000;
                    opacity: 0;
                    transition: opacity 0.3s ease;
                    pointer-events: none;
                `;

                document.body.appendChild(tooltip);

                const rect = this.getBoundingClientRect();
                tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
                tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';

                setTimeout(() => {
                    tooltip.style.opacity = '1';
                }, 10);

                this.addEventListener('mouseleave', function() {
                    tooltip.remove();
                }, { once: true });
            });
        });
    }

    // FAQ Functionality
    initFAQ() {
        const faqQuestions = document.querySelectorAll('[data-faq-toggle]');
        
        faqQuestions.forEach(question => {
            question.addEventListener('click', () => {
                const faqItem = question.closest('.faq-item');
                const answer = faqItem.querySelector('.faq-answer');
                const isActive = faqItem.classList.contains('active');
                
                // Close all other FAQs
                document.querySelectorAll('.faq-item.active').forEach(item => {
                    if (item !== faqItem) {
                        item.classList.remove('active');
                        const otherAnswer = item.querySelector('.faq-answer');
                        const otherQuestion = item.querySelector('[data-faq-toggle]');
                        otherAnswer.style.maxHeight = '0';
                        otherQuestion.setAttribute('aria-expanded', 'false');
                    }
                });
                
                // Toggle current FAQ
                if (isActive) {
                    faqItem.classList.remove('active');
                    answer.style.maxHeight = '0';
                    question.setAttribute('aria-expanded', 'false');
                } else {
                    faqItem.classList.add('active');
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                    question.setAttribute('aria-expanded', 'true');
                }
            });
        });
    }

    // Video Triggers
    initVideoTriggers() {
        const videoTriggers = document.querySelectorAll('[data-video-trigger]');
        
        videoTriggers.forEach(trigger => {
            trigger.addEventListener('click', () => {
                // This would open a modal with video content
                console.log('Video trigger clicked');
                // Implementation for video modal would go here
            });
        });
    }

    // AOS (Animate On Scroll) Integration
    initAOS() {
        // Simple AOS-like functionality
        const animatedElements = document.querySelectorAll('[data-aos]');
        
        const aosObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const element = entry.target;
                    const delay = element.dataset.aosDelay || 0;
                    
                    setTimeout(() => {
                        element.style.opacity = '1';
                        element.style.transform = 'translateY(0)';
                    }, delay);
                    
                    aosObserver.unobserve(element);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        animatedElements.forEach(element => {
            element.style.opacity = '0';
            element.style.transform = 'translateY(30px)';
            element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            aosObserver.observe(element);
        });
    }

    // Performance Optimizations
    initPerformanceOptimizations() {
        // Preload critical images
        this.preloadCriticalImages();
        
        // Defer non-critical resources
        this.deferNonCriticalResources();
        
        // Initialize service worker if available
        this.initServiceWorker();
    }

    preloadCriticalImages() {
        const criticalImages = document.querySelectorAll('img[data-critical]');
        criticalImages.forEach(img => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = img.src;
            document.head.appendChild(link);
        });
    }

    deferNonCriticalResources() {
        // Defer loading of non-critical CSS
        const nonCriticalCSS = document.querySelectorAll('link[data-defer]');
        nonCriticalCSS.forEach(link => {
            link.media = 'print';
            link.onload = () => { link.media = 'all'; };
        });
    }

    initServiceWorker() {
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/static/sw.js')
                    .then(registration => {
                        console.log('SW registered: ', registration);
                    })
                    .catch(registrationError => {
                        console.log('SW registration failed: ', registrationError);
                    });
            });
        }
    }
}

// Initialize the application
const app = new CourseCenter();

// Enhanced Error Handling
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Send to error reporting service in production
});

window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled promise rejection:', e.reason);
    // Send to error reporting service in production
});

// Legacy function support for backward compatibility
function initNavigation() {
    if (window.app) {
        window.app.initNavigation();
    }
}

function initCounters() {
    if (window.app) {
        window.app.initCounters();
    }
}

// Export for external access
window.CourseCenter = CourseCenter;