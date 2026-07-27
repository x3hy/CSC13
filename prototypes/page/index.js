// Use coc-tsserver for ale

// Page settings
const website_name = "Rebbit"
const website_slogan = "Frog-friendly forum"

// Navbar component (fuck react)
document.addEventListener("DOMContentLoaded", () => {
	const nav = document.getElementById("navbar");
	if (nav){
		nav.innerHTML = /*html*/`
			<header class="nav-header">
				<a href="index.html">
					<img src="logo_small.svg" id="nav-logo">
				</a>
			</header>
			<div class="nav-buttons">
				<button>Posts (Public)</button>
				<button class="alt">Sign Up</button>
			</div>
		`
	}
})

// Animation library:
document.addEventListener("DOMContentLoaded", () => {
	document.querySelectorAll(".animate-in").forEach(element => {
		element.classList.add("hidden");
		const intersect_options = {
			root: document.body,
			threshold: 1.0
		}

		// Wait for the element to come into screen
		const observer = new IntersectionObserver((e) => {
			if (e[0].isIntersecting){
				console.log("test123");
			}
		},intersect_options);
		observer.observe(element);
	})
})
