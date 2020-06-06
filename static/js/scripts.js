
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

        var product = document.querySelector('#product-id').value

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

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.progress-button').forEach(function (button) {
        button.onclick = () => {
            // Initialize new request
            const request = new XMLHttpRequest();

            var order_number = button.dataset.id

            request.open('POST', 'rec/');

            // Callback function for when request completes
            request.onload = () => {

                // Extract JSON data from request
                const response = JSON.parse(request.responseText);
                var id = response.order_id

                var id_concat = `#progress-${id}`
                console.log(id_concat)
                // Get element
                var elem = document.querySelector(id_concat);

                // Set inner HTML text
                elem.innerHTML = "Delivered";

                // Set the width to 100%
                elem.style.width = "100%";

                // Hide button
                button.style.visibility = 'hidden';
            }

            // Add data to send with request
            const data = new FormData();
            data.append('id', order_number);

            // Set request header
            request.setRequestHeader("X-CSRFToken", csrftoken);

            // Send request
            request.send(data);
            return false;
        }
    })
})
