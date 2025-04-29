document.addEventListener(function() {
    const target = document.getElementById("target");

    const items = ["first item", "second item", "third item"];

    items.forEach(text => {
        const li = document.createElement("li");
        li.textContent = text;
        target.appendChild(li);
    });
});