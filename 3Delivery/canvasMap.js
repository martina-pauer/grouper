function plotMap(id, longitude, latitude)
{
    // Make a map using a canvas element
    let canvas = document.getElementById(id);
    // Set correlation width to latitude and height to longitude
    let width = canvas.width / Math.abs(longitude);
    let height = canvas.height / Math.abs(latitude);
    canvas = canvas.getContext("2d");
    // Draw map From 0 to longitud and from 0 to latitude
    // Add Mark
    canvas.strokeRect(width, height, 10, 10)
}