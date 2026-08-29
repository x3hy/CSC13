document.querySelectorAll(".price").forEach(e => {
	const raw = parseFloat(e.textContent);
	e.textContent = new Intl.NumberFormat("en-US", {
		minimumFractionDigits: 2,
		maximumFractionDigits: 2
	}).format(raw);
	e.textContent = '$' + e.textContent;
});
