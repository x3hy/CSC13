/*
{% if PRODUCTS is defined and PRODUCTS %}
	{% for p in PRODUCTS %}
		<article data-price="{{ p.price }}" data-max-amount="{{ p.maxamount }}">
			<header>
				<div class="other">
					<h3>{{ p.title }} <span class="price">{{ p.price }}</span></h3>
					<p>{{ p.description }}</p>
				</div>
				<div class="buttons">
					<button class="increase">+</button>
					<span class="total">0</span>
					<button class="decrease">-</button>
				</div>
			</header>
			<img src="{{ url_for('static', filename=p.image) }}", draggable="false", alt="{{ p.description }}">
		</article>
	{% endfor %}
*/

const cart = document.getElementById("cart");
const prod = document.getElementById("product-list");
prod.querySelectorAll("article")
