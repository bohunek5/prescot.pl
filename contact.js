const revealItems = document.querySelectorAll(".reveal");

if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  revealItems.forEach((item) => item.classList.add("is-visible"));
} else {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12 },
  );
  revealItems.forEach((item) => revealObserver.observe(item));
}

const contactForm = document.querySelector("#contact-form");
const topicSelect = document.querySelector("#contact-topic");
const formStatus = document.querySelector("#form-status");

document.querySelectorAll("[data-topic]").forEach((button) => {
  button.addEventListener("click", () => {
    if (topicSelect) {
      topicSelect.value = button.dataset.topic;
    }
    const b2bModal = document.getElementById('b2b-register-modal');
    if (b2bModal && typeof b2bModal.showModal === 'function') {
      b2bModal.showModal();
      b2bModal.setAttribute("open", "");
    }
  });
});

if (contactForm) {
  contactForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!contactForm.checkValidity()) {
    contactForm.reportValidity();
    return;
  }

  formStatus.textContent = "Formularz działa obecnie wyłącznie lokalnie. Wiadomość nie została wysłana — obsługę skrzynki podłączymy przed publikacją strony.";
  formStatus.classList.add("is-visible");
  });
}
