//1
const target1 = document.getElementById("target");
target1.innerHTML = `
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
`;
target1.classList.add("my-list");

//2
const target2 = document.getElementById("target");

const items = ["First item", "Second item", "Third item"];
items.forEach((text, index) => {
  const li = document.createElement("li");
  li.textContent = text;
  if (index === 1) {
    li.classList.add("my-item");
  }
  target2.appendChild(li);
});

//3
const target3 = document.getElementById("target");
const names = ["John", "Paul", "Jones"];

let htmlContent = "";
for (let name of names) {
  htmlContent += `<li>${name}</li>`;
}
target3.innerHTML = htmlContent;

//4
const target4 = document.getElementById("target");
const students = [
  { value: "2345678", name: "John" },
  { value: "2134657", name: "Paul" },
  { value: "5423679", name: "Jones" }
];

students.forEach(student => {
  const option = document.createElement("option");
  option.value = student.value;
  option.textContent = student.name;
  target4.appendChild(option);
});

//5
const section = document.querySelector("section");
const picArray = [
  {
    title: "Sunset",
    medium_image: "sunset.jpg",
    caption: "Beautiful sunset",
    description: "A view of the sunset by the sea."
  },
  {
    title: "Mountains",
    medium_image: "mountains.jpg",
    caption: "Snowy peaks",
    description: "Snow-covered mountains under a clear sky."
  }
  // Add more objects as needed
];

picArray.forEach(pic => {
  const article = document.createElement("article");
  article.className = "card";

  article.innerHTML = `
    <h2>${pic.title}</h2>
    <figure>
      <img src="${pic.medium_image}" alt="${pic.title}">
      <figcaption>${pic.caption}</figcaption>
    </figure>
    <p>${pic.description}</p>
  `;

  section.appendChild(article);
});