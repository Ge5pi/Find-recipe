
function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i].trim();
        if (c.indexOf(nameEQ) === 0) {
            return decodeURIComponent(c.substring(nameEQ.length, c.length));
        }
    }
    return null;
}

let savedDishes = getCookie('dishes');
console.log('Saved dishes:', savedDishes);

if (savedDishes) {
    try {
        savedDishes = JSON.parse(savedDishes);
        console.log('Parsed dishes:', savedDishes);
        // Находим контейнер для контента
        const contentDiv = document.getElementById('cookieContent');
        console.log('Content div:', contentDiv);

        if (contentDiv) {

            savedDishes.forEach(function(dish) {

                let link = document.createElement("a");
                link.href = `/recipe/${encodeURIComponent(dish)}`;
                link.className = 'card';


                let title = document.createElement("h3");
                title.textContent = dish;


                link.appendChild(title);


                contentDiv.appendChild(link);
            });
        } else {
            console.error("Element with id 'cookieContent' not found.");
        }
    } catch (e) {
        console.error('Error parsing saved dishes:', e);
    }
} else {
    console.log("No saved dishes found in cookies.");
}
