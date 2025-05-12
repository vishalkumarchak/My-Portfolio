document.addEventListener('DOMContentLoaded', () => {
  // Smooth scroll to top
  document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      if (btn.getAttribute('href') === '#') {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  });
});



const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  menuBtn.addEventListener('click', () => {
    const isHidden = mobileMenu.classList.contains('hidden');

    if (isHidden) {
      mobileMenu.classList.remove('hidden');
      // Trigger animation
      setTimeout(() => {
        mobileMenu.classList.remove('scale-y-0');
        mobileMenu.classList.add('scale-y-100');
      }, 10);
    } else {
      // Start scale animation
      mobileMenu.classList.remove('scale-y-100');
      mobileMenu.classList.add('scale-y-0');
      // Hide after animation ends
      setTimeout(() => {
        mobileMenu.classList.add('hidden');
      }, 300); // match duration-300
    }
  });
