
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Set the Cross-Site Request Forgery (CSRF) token
var csrftoken = getCookie('csrftoken');


addEventListener('DOMContentLoaded', () => {
    document.querySelector('#add-to-cart').onclick = () => {

        // Clear current url
        window.history.replaceState({}, document.title, "/");

        // Initialize new request
        const request = new XMLHttpRequest();

        var product = document.querySelector('#product-id').innerHTML

        var sizes = document.querySelector('#sizes');
        
        if (sizes != null) {
            var size = sizes.options[sizes.selectedIndex].value;
        }
        else {
            var size = null
        }

        var colors = document.querySelector('#colors');
        var color = colors.options[colors.selectedIndex].value;

        var quantity = document.querySelector('#quantity').value;

        request.open('POST', 'carts/add/');

        // Callback function for when request completes
        request.onload = () => {

            // Extract JSON data from request
            const response = JSON.parse(request.responseText);

        }

        // Add data to send with request
        const data = new FormData();
        data.append('product', product);
        data.append('size', size);
        data.append('color', color);
        data.append('quantity', quantity);

        // Set request header
        request.setRequestHeader("X-CSRFToken", csrftoken);

        // Send request
        request.send(data);
        return false;
    }
})
