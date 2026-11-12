/* AgroRota – Map & Draw logic (Leaflet + Leaflet.draw + OSM) */

let map, drawnItems, drawControl, currentLayer = "map";

function initMap(lat, lng, zoom) {
  lat = lat || -5.0945;   // Default: Chulucanas, Piura, Perú
  lng = lng || -80.1663;
  zoom = zoom || 15;

  map = L.map("map", { zoomControl: false }).setView([lat, lng], zoom);

  // Zoom control – top right
  L.control.zoom({ position: "topright" }).addTo(map);

  // Tile layers
  window.tileStreet = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    { attribution: "© OpenStreetMap contributors", maxZoom: 19 }
  ).addTo(map);

  window.tileSatellite = L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    { attribution: "© Esri Satellite", maxZoom: 19 }
  );

  // Layer for drawn shapes
  drawnItems = new L.FeatureGroup().addTo(map);

  // Draw control (hidden – triggered manually)
  drawControl = new L.Control.Draw({
    edit: { featureGroup: drawnItems },
    draw: {
      polygon: {
        allowIntersection: false,
        showArea: true,
        shapeOptions: { color: "#1C3A2B", fillOpacity: 0.25, weight: 2 },
      },
      rectangle: {
        shapeOptions: { color: "#1C3A2B", fillOpacity: 0.25, weight: 2 },
      },
      circle: false,
      circlemarker: false,
      polyline: false,
      marker: false,
    },
  });

  // After shape drawn – compute area and update UI
  map.on(L.Draw.Event.CREATED, function (e) {
    drawnItems.clearLayers();
    drawnItems.addLayer(e.layer);

    const geojson = JSON.stringify(e.layer.toGeoJSON());
    document.getElementById("geojson-input").value = geojson;

    const areaM2 = L.GeometryUtil.geodesicArea(e.layer.getLatLngs()[0] || e.layer.getLatLngs()[0][0]);
    const areaHa = (areaM2 / 10000).toFixed(2);
    updateAreaDisplay(areaHa);

    // Add area label popup
    e.layer.bindPopup(`<strong>${areaHa} ha</strong>`).openPopup();
  });

  map.on(L.Draw.Event.EDITED, function (e) {
    e.layers.eachLayer(function (layer) {
      const geojson = JSON.stringify(layer.toGeoJSON());
      document.getElementById("geojson-input").value = geojson;
      const latLngs = layer.getLatLngs()[0] || layer.getLatLngs()[0][0];
      const areaM2 = L.GeometryUtil.geodesicArea(latLngs);
      const areaHa = (areaM2 / 10000).toFixed(2);
      updateAreaDisplay(areaHa);
    });
  });
}

function updateAreaDisplay(ha) {
  const el = document.getElementById("area-display");
  if (el) el.textContent = ha;
  const hiddenArea = document.getElementById("area-ha-input");
  if (hiddenArea) hiddenArea.value = ha;
}

function startDraw() {
  if (!drawControl) return;
  new L.Draw.Polygon(map, drawControl.options.draw.polygon).enable();
}

function clearDraw() {
  drawnItems.clearLayers();
  document.getElementById("geojson-input").value = "";
  updateAreaDisplay("0.00");
}

function toggleLayer(type) {
  if (type === "satellite") {
    map.removeLayer(window.tileStreet);
    window.tileSatellite.addTo(map);
  } else {
    map.removeLayer(window.tileSatellite);
    window.tileStreet.addTo(map);
  }
  currentLayer = type;
  document.querySelectorAll(".map-toggle button").forEach(b => {
    b.classList.toggle("active", b.dataset.layer === type);
  });
}

function useCurrentLocation() {
  if (!navigator.geolocation) return;
  navigator.geolocation.getCurrentPosition(
    function (pos) {
      const { latitude, longitude } = pos.coords;
      map.setView([latitude, longitude], 17);
      document.getElementById("lat-input").value = latitude;
      document.getElementById("lng-input").value = longitude;
    },
    function () {
      alert("No se pudo obtener tu ubicación.");
    }
  );
}

function geocodeSearch(query) {
  if (!query) return;
  const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json&limit=1`;
  fetch(url, { headers: { "Accept-Language": "es" } })
    .then(r => r.json())
    .then(data => {
      if (data.length) {
        const { lat, lon, display_name } = data[0];
        map.setView([+lat, +lon], 15);
        document.getElementById("lat-input").value = lat;
        document.getElementById("lng-input").value = lon;
        document.getElementById("ubicacion-texto-input").value = display_name;
      }
    });
}
