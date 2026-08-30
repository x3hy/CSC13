const cart = document.getElementById("cart");
const cart_checkout = document.getElementById("cart-checkout");
const cart_clear = document.getElementById("cart-clear");
const cart_list = document.getElementById("receipt");
const prod = document.getElementById("product-list");

// Quantitys are kept in here
let quants = [];

// Clear all of the quantitys in the array
cart_clear.addEventListener("click", () => {
	quants.forEach(q => {
		q["quant"] = 0;
		q["element"].getElementsByClassName("total")[0]
			.innerText = 0;
	});
	
	update_cart();
	return;
});

// Updates the total items and total price in the cart
function update_cart(){
	// Sum prices*quantitys accross all elements
	const cost = cart.getElementsByClassName("price")[0];
	cost.innerText = format_price(quants.reduce((sum, item) =>
			sum + (item.quant*item.price)
		, 0));

	// Sum the quantitys
	cart.getElementsByClassName("item-count")[0]
		.innerText = quants.reduce((sum, item) =>
			sum + item.quant
		, 0);

	cart_list.innerHTML = ""
	quants.forEach(q=>{
		if (q["quant"] != 0)
			cart_list.innerHTML +=
				`<p>x${q["quant"]} ${q["title"]} <i>(${format_price(q["quant"] *  q["price"])})</i></p>`
	})

	return;
}


// Provide styles for individual product components
prod.querySelectorAll("article").forEach((el, i) => {
	const quant_max = Number(el.getAttribute("data-max-amount"));
	const btn_inc = el.getElementsByClassName("increase")[0];
	const btn_dec = el.getElementsByClassName("decrease")[0];
	const quant_val = el.getElementsByClassName("total")[0];

	// Update the individual components amount
	function update_quant(){
		quant_val.innerText = quants[i]["quant"];
		update_cart();
	}

	// Create a new indice in the array
	quants.push({
		"quant": 0,
		"price": parseFloat(el.getAttribute("data-price")),
		"element": el,
		"title": el.getAttribute("data-title")
	});

	// Incriment total cost
	btn_inc.addEventListener("click", () => {
		if (quant_max != -1 && quant_max <= quants[i]["quant"])
			return;

		quants[i]["quant"]++;
		update_quant();
	});

	// Decriment quantity if its above 0
	btn_dec.addEventListener("click", () => {
		if (quants[i]["quant"] > 0){
			quants[i]["quant"]--;
			update_quant();
			return;
		}
	});
})
