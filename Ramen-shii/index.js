document.addEventListener("DOMContentLoaded", () => {
    const ramens = [
        { id: 1, name: "Shoyu Ramen", restaurant: "Ichiran", image: "images/csm_1103-recipe-page-Spicy-Kimchi-Ramen-with-Pork_desktop_3daf5709fe.webp", rating: 5, comment: "Delicious!" },
        { id: 2, name: "Miso Ramen", restaurant: "Menya", image: "images/IMG_2535.jpg", rating: 4, comment: "Very flavorful!" },
        { id: 3, name: "Tonkotsu Ramen", restaurant: "Ramen-ya", image: "images/67.jpg", rating: 3, comment: "Rich broth!" }
    ];
    

    function displayRamens() {
        const ramenMenu = document.getElementById("ramen-menu");
        ramens.forEach(ramen => {
            const img = document.createElement("img");
            img.src = ramen.image;
            img.alt = ramen.name;
            img.addEventListener("click", () => displayRamenDetails(ramen));
            ramenMenu.appendChild(img);
        });
    }

    function displayRamenDetails(ramen) {
        document.getElementById("ramen-image").src = ramen.image;
        document.getElementById("ramen-name").textContent = ramen.name;
        document.getElementById("ramen-restaurant").textContent = ramen.restaurant;
        document.getElementById("ramen-rating").textContent = ramen.rating || "N/A";
        document.getElementById("ramen-comment").textContent = ramen.comment || "No comment.";
    }

    function addSubmitListener() {
        document.getElementById("new-ramen").addEventListener("submit", event => {
            event.preventDefault();
            const newRamen = {
                name: event.target.name.value,
                restaurant: event.target.restaurant.value,
                image: event.target.image.value,
                rating: event.target.rating.value,
                comment: event.target.comment.value
            };
            addNewRamen(newRamen);
            event.target.reset();
        });
    }

    function addNewRamen(ramen) {
        const ramenMenu = document.getElementById("ramen-menu");
        const img = document.createElement("img");
        img.src = ramen.image;
        img.alt = ramen.name;
        img.addEventListener("click", () => displayRamenDetails(ramen));
        ramenMenu.appendChild(img);
    }

    function main() {
        displayRamens();
        addSubmitListener();
    }

    main();
});