// Previsualización
function previewImage(event) {
    const input = event.target;
    const container = document.getElementById('previewContainer');
    const previewImg = document.getElementById('instantPreview');

    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = e => {
            previewImg.src = e.target.result;
            container.classList.remove('hidden');
        };
        reader.readAsDataURL(input.files[0]);
    }
}

// Lógica de Galería
function openPop(url) {
    const popUp = document.getElementById('popUp');
    document.getElementById('popImage').src = url;
    document.getElementById('downloadBtn').href = url;
    popUp.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closePop() {
    document.getElementById('popUp').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// EFECTO DE PARTÍCULAS (Opcional pero genial)
const canvas = document.getElementById('uploadCanvas');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let particles = [];
    
    function resize() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    class Particle {
        constructor(x, y) {
            this.x = x; this.y = y;
            this.size = Math.random() * 2 + 1;
            this.speedX = Math.random() * 3 - 1.5;
            this.speedY = Math.random() * 3 - 1.5;
            this.color = 'rgba(99, 102, 241, 0.5)';
        }
        update() {
            this.x += this.speedX; this.y += this.speedY;
            if (this.size > 0.1) this.size -= 0.01;
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    document.getElementById('uploadForm').addEventListener('mousemove', e => {
        const rect = canvas.getBoundingClientRect();
        for (let i = 0; i < 2; i++) {
            particles.push(new Particle(e.clientX - rect.left, e.clientY - rect.top));
        }
    });

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particles.length; i++) {
            particles[i].update();
            particles[i].draw();
            if (particles[i].size <= 0.2) {
                particles.splice(i, 1); i--;
            }
        }
        requestAnimationFrame(animate);
    }
    animate();
}