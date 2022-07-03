var updateBtns=document.getElementsByClassName('option-btn')
var showBtns=document.getElementsByClassName('show-btn')
for(var i = 0; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var orderId = this.dataset.product
        var action=this.dataset.action
        console.log('orderId:', orderId, 'action:', action)
        console.log("press")
         deliver_product(orderId, action)
         
    })

}

for(var i = 0; i < showBtns.length;i++){
    showBtns[i].addEventListener('click', function(){
        var itemsid = this.dataset.product
        var action=this.dataset.action
        console.log('itemsid:', itemsid, 'action:', action)
        console.log("press")
        
        show_product(itemsid, action)
    })

}

function deliver_product(orderId, action){
    console.log('user is logged in')

    var url = '/delivery_update/'

    fetch(url, { 
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'orderId': orderId,'action':action,})

        
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
       console.log('data:',data)
       location.reload()
    })
}

function show_product(itemsid, action){
    console.log('user is logged in')

    var url = '/show_products/'

    fetch(url, { 
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'itemsid': itemsid,'action':action,})

        
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
       console.log('data:',data)
       location.reload()
    })
}