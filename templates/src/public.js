function format_price(text){
	return "$" + new Intl.NumberFormat("en-US", {
		minimumFractionDigits: 2,
		maximumFractionDigits: 2
	}).format(text);
}

document.querySelectorAll(".price").forEach(e => {
	e.textContent = format_price(parseFloat(e.textContent))
});
