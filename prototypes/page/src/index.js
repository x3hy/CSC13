// Use coc-tsserver for ale


// Navbar component (fuck react)
document.addEventListener("DOMContentLoaded", () => {
	const nav = document.getElementById("navbar");
	if (nav){
		nav.innerHTML = /*html*/`
			<header class="nav-header">
				<a href="index.html">
					<img src="logos/logo_textonly.svg" id="nav-logo">
				</a>
			</header>
			<div class="nav-buttons">
				<!-- Hamburger icon is ez to do in css -->
				
				<div class="hamburger" tabindex="0">
					<svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M4 7L7 7M20 7L11 7" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>
						<path d="M20 17H17M4 17L13 17" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>
						<path d="M4 12H7L20 12" stroke="#1C274C" stroke-width="1.5" stroke-linecap="round"/>
					</svg>
				</div>
				<div class="dropdown-buttons">
					<a href="" title="View Posts"><button>Posts <i>(Public)</i></button></a>
					<a href="" title="Log in"><button>Login</button></a>
					<a href="" title="Sign up"><button class="alt">Sign Up</button></a>
					<a href="" title="Create Post"><button class="alt">+</button></a>
				</div>
			</div>
		`
	}
})


// Animation library:
document.addEventListener("DOMContentLoaded", () => {
	document.querySelectorAll("[data-anim]").forEach(element => {
		element.classList.add ("anim");

		// Run this when element is on screen
		function callback(){
			const duration = element.dataset.duration;
			const animation = element.dataset.anim;
			const timing = element.dataset.trans;
			const delay = element.dataset.delay;

			if (animation)  element.style.animationName = animation
			if (timing) element.style.animationTimingFunction = timing;
			if (delay) element.style.animationDelay = delay;
			if (duration) element.style.animationDuration = duration;
		}

		if (element.dataset.anim_instant){
			callback();
			return;
		}

		// Listen for the element to come onscreen
		const observer = new IntersectionObserver((e) => {
			if (!e[0].isIntersecting) return
			
			// Unobserve or animations will play EVERY time
			// the element comes on screen.
			observer.unobserve(element);

			// Run the primary function above
			callback();
		}, {threshold: 0.1});

		// Start listener
		observer.observe(element);
	})
})
