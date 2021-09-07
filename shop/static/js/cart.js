var updateButton = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButton.length; i++) {


	updateButton[i].addEventListener('click', function(){
	    var amountInput = document.getElementsByClassName('amount-input-js')
		var productId = this.dataset.product
		var action = this.dataset.action

        this.dataset.amount = amountInput[0].value
		var amount = this.dataset.amount

		console.log('productId:', productId, 'Action:', action, 'Amount:', amount)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
		    console.log('anon')
		}else{
			updateUserOrder(productId, action, amount)
		}
	})

}



function updateUserOrder(productId, action, amount){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId': productId, 'action': action, 'amount': amount})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

