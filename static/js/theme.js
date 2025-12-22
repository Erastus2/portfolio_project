const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("nav-links");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("show");
});



const toggleBtn = document.getElementById("themeToggle");
const icon = toggleBtn.querySelector("i");

toggleBtn.onclick = () => {
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    icon.className = "fa fa-sun";
  } else {
    icon.className = "fa fa-moon";
  }
};
