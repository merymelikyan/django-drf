const fetch = require('node-fetch');

async function getData(url) {
    const res = await fetch(url);
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
  
    return await res.json();
  }
  
  getData("http://127.0.0.1:8000/api/v1/categories/")
    .then(data => {
      data.forEach(item => console.log(item.title_hy));
    })
  
  getData("http://127.0.0.1:8000/api/v1/products/")
    .then(data => console.log(data))