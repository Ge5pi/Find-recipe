document.addEventListener('DOMContentLoaded', function() {
    let submit = document.getElementById("submit");

    submit.addEventListener("click", function(event) {
        event.preventDefault();
        sendData();
    });

    function sendData() {
    var value = document.querySelector(".prompt").value;
    $.ajax({
        url: "/generate",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ value: value }),
        success: function(response) {
            if (response.dishes) {
                let dishList = document.getElementById("dishList");
                dishList.innerHTML = '';


                setCookie('dishes', JSON.stringify(response.dishes), 7);

                response.dishes.forEach(function(dish) {
                    let listItem = document.createElement("li");
                    let gif = document.querySelector('#loading');
                    let wrapper = document.querySelector('.wrapper');
                    let footer = document.querySelector('.footer');
                    listItem.textContent = dish;
                    listItem.addEventListener("click", function() {
                        window.location.href = `/recipe/${encodeURIComponent(dish)}`;
                        gif.style.display = 'block';
                        wrapper.style.display='none';
                        footer.style.display='none';
                    });

                    dishList.appendChild(listItem);
                });
            } else {
                document.getElementById("output").innerHTML = "Error: " + response.error;
            }
        },
        error: function(error) {
            console.log("AJAX Error:", error);
        },
    });
}

});

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + encodeURIComponent(value || "") + expires + "; path=/";
    console.log(document.cookie = name + "=" + encodeURIComponent(value || "") + expires + "; path=/");
}

