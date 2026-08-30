const cart = document.getElementById("cart");
const cart_checkout = document.getElementById("cart-checkout");
const cart_clear = document.getElementById("cart-clear");
const cart_list = document.getElementById("receipt");
const prod = document.getElementById("product-list");

	// Create the receipt list + add quants to components
// Quantitys are kept in here
let quants = [];


// Remove all index quantitys
cart_clear.addEventListener("click", () => {
	quants.forEach(q => q["quant"] = 0);
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
	quants.forEach((q, i) =>{
		
		// Update component quantitys
		q["element"].getElementsByClassName("total")[0]
			.innerText = q["quant"];

		// Create rows in receipt
		if (q["quant"] != 0){
			const item = document.createElement("p");
			const btn_dec = document.createElement("button");
			const btn_inc = document.createElement("button");
			const rest = document.createElement("span");

			btn_dec.innerText = "-1";
			btn_inc.innerText = "+1";
			rest.innerHTML = `<span class="sep"></span>x${q["quant"]} ${q["title"]} <i>(${format_price(q["quant"] *  q["price"])})</i>`

			item.appendChild(btn_inc);
			item.appendChild(btn_dec);
			item.appendChild(rest);

			btn_dec.addEventListener("click", () => {
				quants[i]["quant"]--;
				update_cart();
			});

			btn_inc.addEventListener("click", () => {
				quants[i]["quant"]++;
				update_cart();
			});

			cart_list.appendChild(item);
		}
	})
}


// Provide styles for individual product components
prod.querySelectorAll("article").forEach((el, i) => {
	const quant_max = Number(el.getAttribute("data-max-amount"));
	const btn_inc = el.getElementsByClassName("increase")[0];
	const btn_dec = el.getElementsByClassName("decrease")[0];

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
		update_cart();
	});

	// Decriment quantity if its above 0
	btn_dec.addEventListener("click", () => {
		if (quants[i]["quant"] > 0){
			quants[i]["quant"]--;
			update_cart();
		}
	});
})
