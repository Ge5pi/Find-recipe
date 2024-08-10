document.addEventListener('DOMContentLoaded', function() {
    let submit = document.getElementById("submit");

    submit.addEventListener("click", function(event) {
        event.preventDefault();  // Prevent default form submission
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
                    // Get the dishList element
                    let dishList = document.getElementById("dishList");
                    dishList.innerHTML = ''; // Clear any previous dishes

                    // Append each dish as a list item
                    response.dishes.forEach(function(dish) {
                        let listItem = document.createElement("li");
                        listItem.textContent = dish;
                        listItem.addEventListener("click", function() {
                            window.location.href = `/recipe/${encodeURIComponent(dish)}`;
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
