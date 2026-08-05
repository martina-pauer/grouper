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

function decToHex(number)
{
    // Turn Decimal number to hexadecimal number
    return number;
}

async function saveContent(id)
{
    // Save In Cookies the bytes for server cookie getter
		let files = document.getElementById(id).files;
		let buffer
			
		let bytes;
		let content = "";
				
		for (let file in files)
		{
		    buffer = await files[file].arrayBuffer();
		    bytes = new Uint8Array(buffer)
				    
		    for (let byte in bytes)
		    {
		        if (byte <= 4095)
				{
                    // Only Accept Files of 4 KB as Maximum
				    content = content.concat(decToHex(bytes[byte]));
				}   
			}
				    
			document.cookie = "grouper=" + content;
		}
}