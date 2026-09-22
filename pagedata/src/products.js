/*
 * This file controls all systems relating to the cart.
 */
const cart = document.getElementById("cart");
const cart_checkout = document.getElementById("cart-checkout");
const cart_clear = document.getElementById("cart-clear");
const cart_list = document.getElementById("receipt");
const prod = document.getElementById("product-list");


// Quantitys are kept in here
let quants = [];


// Remove all index quantitys
cart_clear.addEventListener("click", () => {
	quants.forEach(q => q["quant"] = 0);
	prod.querySelectorAll(`input[type="radio"]`).forEach(el => {
		el.checked = false;
	});

	update_cart();
	return;
});


// Send quants to the server
cart_checkout.addEventListener("click", async () => {
	// Clean the json into a nice format:
	// We only too send the amounts and
	// the uuids of the products.
	let out_json = [];
	quants.forEach(q => {
		if (q["quant"] != 0){
			out_json.push({
				"quant": q["quant"],
				"uuid": q["uuid"]
			})
		}
	});

	try {
		const resp = await fetch("http://127.0.0.1:8072/checkout", {
			method: "POST",
			headers: {
				"Content-Type" : "application/json"
			},
		body: JSON.stringify(out_json)});

		pywebview.api.change_page('checkout_page');
		//document.body.innerHTML = pywebview.api.port();

		if (!resp.ok)
			throw new Error("HTTP error, " + response.status);

		// Request was successful
		//
		// Move over to checkout page
		localStorage.setItem("test", "123");

	} catch (err){
		console.error(err);
	}

});


const clamp = (val, min, max) => Math.min(Math.max(val, min), max);

// Updates the receipt section
function update_receipt(){
	cart_list.innerHTML = "";
	quants.forEach((q, i) => {
		if (q["radio"]) return;

		// Update component quantitys
		q["element"].getElementsByClassName("total")[0].innerText = q["quant"];
		if (q["quant"] == 0) return;

		// Create rows in receipt
		const item = document.createElement("p");
		const buttons = document.createElement("div");
		const btn_dec = document.createElement("button");
		const btn_inc = document.createElement("button");
		const btn_val = document.createElement("span");
		const rest = document.createElement("span");
		const hr = document.createElement("hr");

		/*
		item:
			hr
			buttons:
				btn_dec
				btn_val
				btn_inc
			rest:
				...
		*/

		btn_val.classList.add("total");
		buttons.classList.add("buttons");
		btn_val.innerText = q["quant"];
		btn_dec.innerText = "-";
		btn_inc.innerText = "+";

		const ele_title = q["element"].getAttribute("data-title");
		rest.innerHTML = `<span class="sep"></span>${ele_title} <i>(${format_price(q["quant"] *  q["price"])})</i>	`

		btn_dec.addEventListener("click", () => update_cart(i, -1));
		btn_inc.addEventListener("click", () => update_cart(i, +1));

		buttons.appendChild(btn_inc);
		buttons.appendChild(btn_val);
		buttons.appendChild(btn_dec);

		item.appendChild(hr);
		item.appendChild(buttons);
		item.appendChild(rest);

		cart_list.appendChild(item);
	})

	// Radio components
	quants.forEach((q, i) => {
		if (!q["radio"] || q["quant"] == 0) return;

		// Construct the receipt row
		const item = document.createElement("div");
		const hr = document.createElement("hr");
		const remove = document.createElement("button");
		const rest = document.createElement("span");
		remove.innerText = "Remove";

		// Uses the content from the selected row in the radio
		rest.innerHTML = `<span class="sep"></span>` + q["element"]
			.getElementsByClassName("title")[0].innerHTML;

		// Append to the receipt
		item.appendChild(hr);
		item.appendChild(remove);
		item.appendChild(rest);
		cart_list.appendChild(item);

		// Remove item from cart
		remove.addEventListener("click", ()=>{
			q["price"] = q["quant"] = 0;
			q["element"].querySelectorAll(`input[type="radio"]`)
				.forEach(el => el.checked = false)

			update_cart();
		});
	});

	if (cart_list.innerHTML == "")
		cart_list.innerHTML = "<hr>No Items Selected";
}


// Updates the total items and total price in the cart
function update_cart(idx = 0, change = 0){
	quants[idx]["quant"] = clamp(quants[idx]["quant"] + change, 0, quants[idx]["max"]);

	// Sum prices*quantitys accross all elements
	const cost = cart.getElementsByClassName("price")[0];
	cost.innerText = format_price(quants.reduce((sum, item) =>
			sum + (item.quant*item.price), 0));

	// Sum the quantitys
	cart.getElementsByClassName("item-count")[0]
		.innerText = quants.reduce((sum, item) =>
			sum + item.quant , 0);

	// Update the item list (receipt)
	update_receipt();
}


// Gives function to the product components on the page
prod.querySelectorAll("article:not(:has(form))").forEach((el, i) => {
	const quant_max = Number(el.getAttribute("data-max-amount"));
	const btn_inc = el.getElementsByClassName("increase")[0];
	const btn_dec = el.getElementsByClassName("decrease")[0];

	// Create a new indice in the array
	quants.push({
		"quant": 0,
		"price": parseFloat(el.getAttribute("data-price")),
		"element": el,
		"max": quant_max,
		"radio": false,
		"uuid": el.getAttribute("data-uuid")
	});

	// Hook events
	btn_inc.addEventListener("click", () => update_cart(i, +1));
	btn_dec.addEventListener("click", () => update_cart(i, -1));
})


// Provides functionality to the radio forms on the page
prod.querySelectorAll(".radio-form").forEach((el, i) => {
	const labels = el.querySelectorAll(`label`);
	const radios = el.querySelectorAll(`input[type="radio"]`);

	// Create a new index in the quants array
	quants.push({
		"title": "",
		"quant": 0,
		"price": 0,
		"element": el,
		"max": 1,
		"radio": true
	});

	// Add hooks for individual clicked items
	const quant_idx = (quants.length - 1);
	labels.forEach((item) => {
		item.addEventListener("click", (e)=>{

			// Update the price of the component and
			// update the cart.
			quants[quant_idx]["element"] = item;
			quants[quant_idx]["quant"] = 1;

			// Selected UUID
			quants[quant_idx]["uuid"] = item.getAttribute("data-uuid");
			quants[quant_idx]["price"] = parseFloat(item.getAttribute("data-price"));
			update_cart();
		});
	});

	// Behavior for "uncheck" button
	el.addEventListener("submit", (e) => {
		e.preventDefault()

		// Uncheck all buttons and update the cart
		radios.forEach(radio => radio.checked = false);
		quants[quant_idx]["element"] = el;
		quants[quant_idx]["uuid"] = "";
		quants[quant_idx]["quant"] = 0;
		update_cart();
	});
});
