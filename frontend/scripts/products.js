async function loadProducts()
{
    const response = await fetch("http://localhost:8000/products");
    const products = await response.json()

    const container = document.querySelector(".Products");
    container.innerHTML = "";

    products.forEach(p => {
        const item = document.createElement("div");
        item.className = "Product-Card";
        item.innerHTML = `<h3>${p.Name}</h3>
        <h4>Category: ${p.Category}</h4>
        <p>Price: ${p.Price}</p>
        <p>Stock: ${p.Stock}</p>
        <button id = "Edit" type= "button" onclick="showForm('${p.Product_ID}', '${p.Name}', '${p.Category_ID}', ${p.Price}, ${p.Stock})">Edit</button>`;

        // separate the form from the product
        // one form only
        // const form = document.createElement("form");
        // form.id = `Product-Form-${p.Product_ID}`;
        // form.style.display = "none";
        // form.innerHTML = 
        // `<form>
        //     <input type = "text" name="name" autocomplete="name" value = "${p.Name}">
        //     <input type = "number" name="price" value = "${p.Price}">
        //     <input type = "number" name="stock" value = "${p.Stock}">
        // </form>`;

        // item.appendChild(form)
        container.appendChild(item);
    });
}
function showForm(product_ID, name, category_ID, price, stock)
{
    const ProductForm = document.querySelector(".Modal");
    document.getElementById("product_ID").value = product_ID;
    document.getElementById("pName").value = name;
    document.getElementById("pCategory").value = category_ID;
    document.getElementById("pPrice").value = price;
    document.getElementById("pStock").value = stock;
    ProductForm.style.display = "flex";
    console.log(category_ID);

}

function closeForm()
{
    const ProductForm = document.querySelector(".Modal");
    ProductForm.style.display = "none";
}
async function submitForm()
{
    const formData = new FormData();


    const product_Image = document.getElementById("product_Image").files[0];
    const product_ID = document.getElementById("product_ID").value;
    const name = document.getElementById("pName").value;
    const category = document.getElementById("pCategory").value;
    const price = document.getElementById("pPrice").value;
    const stock = document.getElementById("pStock").value;


    if(product_Image)
    {
        formData.append("image", product_Image);
    }
    else{

    }
    formData.append("product_id", Number(product_ID));
    formData.append("name", name);
    formData.append("category_id", category);
    formData.append("price", Number(price));
    formData.append("stock", Number(stock));

    const response = await fetch(`http://localhost:8000/products/${product_ID}`,{
        method: "PUT",
        body: formData
    });

    const data = await response.json();
    console.log(data);
    loadProducts();
    closeForm();
}

window.onload = loadProducts;