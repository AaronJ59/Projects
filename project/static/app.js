const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('hidden-text')) {
                entry.target.classList.add('show-text');
            }
            if (entry.target.classList.contains('hidden-adam')) {
                entry.target.classList.add('show-adam');
            }
            if (entry.target.classList.contains('hidden-god')) {
                entry.target.classList.add('show-god');
            }
            if (entry.target.classList.contains('hidden-author')) {
                entry.target.classList.add('show-author');
            }
            if (entry.target.classList.contains('hidden-verse')) {
                entry.target.classList.add('show-verse');
            }
            if (entry.target.classList.contains('hidden-reference')) {
                entry.target.classList.add('show-reference');
            }
        } else {
            if (entry.target.classList.contains('hidden-text')) {
                entry.target.classList.remove('show-text');
            }
            if (entry.target.classList.contains('hidden-adam')) {
                entry.target.classList.remove('show-adam');
            }
            if (entry.target.classList.contains('hidden-god')) {
                entry.target.classList.remove('show-god');
            }
            if (entry.target.classList.contains('hidden-author')) {
                entry.target.classList.remove('show-author');
            }
            if (entry.target.classList.contains('hidden-verse')) {
                entry.target.classList.remove('show-verse');
            }
            if (entry.target.classList.contains('hidden-reference')) {
                entry.target.classList.remove('show-reference');
            }
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden-text, .hidden-adam, .hidden-god, .hidden-author, .hidden-verse, .hidden-reference');
hiddenElements.forEach((el) => observer.observe(el));
