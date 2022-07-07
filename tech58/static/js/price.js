class priceCal{
	constructor (unitPrice, quantity, taxPercentage){
		this.unitPrice = unitPrice;
		this.quantity = quantity;
		this.taxPercentage = taxPercentage
	}

	getTax(over_head){
		console.log(this.getPriceWithoutTax(), parseFloat(this.taxPercentage))
		var totalTaxAmount = this.getPriceWithoutTax() * parseFloat(this.taxPercentage)/100;
		return totalTaxAmount.toFixed(2);
	}

	getPriceWithoutTax(){
		var totalAmount = parseFloat(this.unitPrice) * parseFloat(this.quantity);
		return totalAmount.toFixed(2);
	}
	 
}