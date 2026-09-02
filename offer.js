document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".controller-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const model = button.closest(".controller-model");
      const willOpen = !model.classList.contains("is-open");
      model.classList.toggle("is-open", willOpen);
      button.setAttribute("aria-expanded", String(willOpen));
    });
  });

  document.querySelectorAll(".controller-thumb").forEach((button) => {
    button.addEventListener("click", () => {
      const gallery = button.closest(".controller-gallery");
      const main = gallery?.querySelector(".controller-main-image");
      const source = button.dataset.image;
      if (!main || !source) return;
      main.src = source;
      main.alt = button.dataset.alt || main.alt;
      gallery.querySelectorAll(".controller-thumb").forEach((thumb) => thumb.classList.remove("is-active"));
      button.classList.add("is-active");
    });
  });

  const reveal = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-visible");
      reveal.unobserve(entry.target);
    });
  }, { threshold: .1 });
  document.querySelectorAll(".offer-reveal").forEach((element) => reveal.observe(element));
});
