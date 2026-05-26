document.addEventListener('DOMContentLoaded', function() {
    // Basic micro-animations or interactivity can be added here
    // Chart.js initialization is handled directly in the expense_summary.html template
    // to easily pass Django template variables.
    
    // Add subtle entrance animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 * index);
    });
});
