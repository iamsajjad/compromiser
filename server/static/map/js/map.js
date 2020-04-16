
function compromiserMap(x, y, z) {

  let date = document.getElementById('date').innerHTML;
  var map = L.map('compromiserMap').setView([x, y], 8);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  L.marker([x, y]).addTo(map)
      .bindPopup('Last Signal From The Object <br> ' + date)
      .openPopup();
}

