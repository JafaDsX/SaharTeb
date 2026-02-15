(function () {
                // AOS init
                AOS.init({
                    duration: 800,
                    once: true,
                    easing: "ease-out-cubic",
                    offset: 80
                });

                // Bootstrap tooltips
                const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
                tooltipTriggerList.map(el => new bootstrap.Tooltip(el));

                // Year
                document.getElementById("year").textContent = new Date().getFullYear();

                // Scroll progress + toTop
                const $toTop = $("#toTop");
                $(window).on("scroll", function () {
                    const st = window.scrollY || document.documentElement.scrollTop;
                    const dh = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                    const p = dh > 0 ? (st / dh) * 100 : 0;
                    $("#scrollProgress").css("width", p + "%");

                    if (st > 500) $toTop.addClass("show");
                    else $toTop.removeClass("show");
                });

                $toTop.on("click", function () {
                    window.scrollTo({ top: 0, behavior: "smooth" });
                });

                // Smooth close navbar on mobile click
                $("#nav .nav-link").on("click", function () {
                    const nav = document.getElementById("nav");
                    if (nav.classList.contains("show")) {
                        bootstrap.Collapse.getOrCreateInstance(nav).hide();
                    }
                });

                // Theme toggle (persist)
                const themeKey = "esra_theme";
                const $body = $("body");
                const $themeBtn = $("#themeToggle i");

                function applyTheme(t) {
                    if (t === "light") {
                        $body.addClass("light");
                        $themeBtn.removeClass("fa-moon").addClass("fa-sun");
                    } else {
                        $body.removeClass("light");
                        $themeBtn.removeClass("fa-sun").addClass("fa-moon");
                    }
                }
                applyTheme(localStorage.getItem(themeKey) || "dark");

                $("#themeToggle").on("click", function () {
                    const next = $body.hasClass("light") ? "dark" : "light";
                    localStorage.setItem(themeKey, next);
                    applyTheme(next);
                });

                // Animated counters (when visible)
                function animateCounter(el) {
                    const target = parseInt(el.dataset.target, 10) || 0;
                    const duration = 1100;
                    const start = 0;
                    const t0 = performance.now();

                    function tick(now) {
                        const p = Math.min((now - t0) / duration, 1);
                        const eased = 1 - Math.pow(1 - p, 3);
                        el.textContent = Math.floor(start + (target - start) * eased);
                        if (p < 1) requestAnimationFrame(tick);
                    }
                    requestAnimationFrame(tick);
                }

                const counters = document.querySelectorAll(".counter");
                const seen = new WeakSet();
                const io = new IntersectionObserver((entries) => {
                    entries.forEach(e => {
                        if (e.isIntersecting && !seen.has(e.target)) {
                            seen.add(e.target);
                            animateCounter(e.target);
                        }
                    });
                }, { threshold: 0.35 });

                counters.forEach(c => io.observe(c));

                // Appointment form (demo)
                // $("#appointmentForm").on("submit", function (e) {
                //     e.preventDefault();
                //     const data = Object.fromEntries(new FormData(this).entries());

                //     // You can send data to backend here (AJAX)
                //     // $.post('/api/appointment', data)...

                //     const msg = `تم استلام طلبك ✅ سنقوم بالتواصل قريباً.
                //     الاسم: ${data.name} — الخدمة: ${data.service}`;

                //     $("#formToast")
                //         .removeClass("d-none")
                //         .text(msg);

                //     this.reset();
                // });

                // Subtle parallax blobs (GSAP)
                const blobs = [".b1", ".b2", ".b3"];
                window.addEventListener("mousemove", (e) => {
                    const x = (e.clientX / window.innerWidth) - 0.5;
                    const y = (e.clientY / window.innerHeight) - 0.5;

                    gsap.to(blobs[0], { x: x * 30, y: y * 18, duration: 0.8, ease: "power2.out" });
                    gsap.to(blobs[1], { x: x * -26, y: y * 16, duration: 0.9, ease: "power2.out" });
                    gsap.to(blobs[2], { x: x * 22, y: y * -18, duration: 1.0, ease: "power2.out" });
                });

                // Particles canvas (lightweight)
                const canvas = document.getElementById("particles");
                const ctx = canvas.getContext("2d");
                let w, h, particles;

                function resize() {
                    w = canvas.width = window.innerWidth;
                    h = canvas.height = Math.max(window.innerHeight, 700);
                    particles = Array.from({ length: Math.min(120, Math.floor(w / 12)) }).map(() => ({
                        x: Math.random() * w,
                        y: Math.random() * h,
                        r: 0.8 + Math.random() * 2.2,
                        vx: (-0.2 + Math.random() * 0.4),
                        vy: (0.05 + Math.random() * 0.35),
                        a: 0.18 + Math.random() * 0.25
                    }));
                }

                function draw() {
                    ctx.clearRect(0, 0, w, h);
                    // glow dots
                    for (const p of particles) {
                        p.x += p.vx;
                        p.y += p.vy;
                        if (p.x < -20) p.x = w + 20;
                        if (p.x > w + 20) p.x = -20;
                        if (p.y > h + 30) {
                            p.y = -30;
                            p.x = Math.random() * w;
                        }

                        ctx.beginPath();
                        ctx.fillStyle = `rgba(255,255,255,${p.a})`;
                        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                        ctx.fill();
                    }

                    requestAnimationFrame(draw);
                }

                window.addEventListener("resize", resize);
                resize();
                draw();
            })();
