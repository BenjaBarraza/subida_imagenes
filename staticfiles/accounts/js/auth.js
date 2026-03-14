document.addEventListener('DOMContentLoaded', () => {
    // Buscar todos los inputs de contraseña
    const passwordInputs = document.querySelectorAll('.auth-form input[type="password"]');

    passwordInputs.forEach(input => {
        // Crear el contenedor para el ícono del ojo
        const wrapper = document.createElement('div');
        wrapper.style.position = 'relative';
        
        // Envolver el input
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(input);

        // Crear el botón de "Ver"
        const toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.innerHTML = '👁️';
        toggleBtn.style.position = 'absolute';
        toggleBtn.style.right = '12px';
        toggleBtn.style.top = '50%';
        toggleBtn.style.transform = 'translateY(-50%)';
        toggleBtn.style.background = 'none';
        toggleBtn.style.border = 'none';
        toggleBtn.style.cursor = 'pointer';
        toggleBtn.style.opacity = '0.5';
        toggleBtn.style.padding = '0';
        toggleBtn.style.fontSize = '1.1rem';

        // Agregar evento para mostrar/ocultar
        toggleBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (input.type === 'password') {
                input.type = 'text';
                toggleBtn.style.opacity = '1';
            } else {
                input.type = 'password';
                toggleBtn.style.opacity = '0.5';
            }
        });

        // Solo agregar el botón si el input no tiene errores (para evitar cruces visuales)
        if (!input.nextElementSibling || !input.nextElementSibling.classList.contains('errorlist')) {
            wrapper.appendChild(toggleBtn);
        }
    });
});