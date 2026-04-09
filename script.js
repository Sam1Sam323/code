function toRadians(deg) {
  return (deg * Math.PI) / 180;
}

function haversineDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // Earth radius in kilometers
  const dLat = toRadians(lat2 - lat1);
  const dLon = toRadians(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRadians(lat1)) * Math.cos(toRadians(lat2)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

function euclideanDistance(x1, y1, x2, y2) {
  return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
}

const geoBtn = document.getElementById("geoBtn");
const planeBtn = document.getElementById("planeBtn");

geoBtn.addEventListener("click", () => {
  const lat1 = parseFloat(document.getElementById("lat1").value);
  const lon1 = parseFloat(document.getElementById("lon1").value);
  const lat2 = parseFloat(document.getElementById("lat2").value);
  const lon2 = parseFloat(document.getElementById("lon2").value);
  const distance = haversineDistance(lat1, lon1, lat2, lon2);
  document.getElementById("geoResult").textContent =
    `ระยะทางประมาณ ${distance.toFixed(3)} กิโลเมตร`;
});

planeBtn.addEventListener("click", () => {
  const x1 = parseFloat(document.getElementById("x1").value);
  const y1 = parseFloat(document.getElementById("y1").value);
  const x2 = parseFloat(document.getElementById("x2").value);
  const y2 = parseFloat(document.getElementById("y2").value);
  const distance = euclideanDistance(x1, y1, x2, y2);
  document.getElementById("planeResult").textContent =
    `ระยะทางระหว่างจุด = ${distance.toFixed(3)}`;
});
