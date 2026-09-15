function plotMap(id, longitude, latitude)
{
    // Make a map using a canvas element
    let canvas = document.getElementById(id);
    // Set correlation width to latitude and height to longitude
    let width = canvas.width / Math.abs(longitude);
    let height = canvas.height / Math.abs(latitude);
    canvas = canvas.getContext("2d");
	// Clear Full Map
	canvas.reset();
    // Draw map
	const img = new Image();
	
	if ((longitude == -38.68) && (latitude == -62.24))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_0.png";
	}	
	else if ((longitude == -38.69) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_1.png";
	}
	else if ((longitude == -38.70) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_2.png";
	}
	else if ((longitude == -38.71) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_3.png";
	}
	else if ((longitude == -38.72) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_4.png";
	}
	else if ((longitude == -38.73) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_5.png";
	}
	else if ((longitude == -38.74) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_6.png";
	}
	else if ((longitude == -38.75) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_7.png";
	}
	else if ((longitude == -38.76) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_8.png";
	}
	else if ((longitude == -38.77) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_9.png";
	}
	else if ((longitude == -38.78) && (latitude == -62.27))
	{
		img.src = "https://raw.githubusercontent.com/martina-pauer/grouper/refs/heads/main/3Delivery/cities/city_0/BBA_10.png";
	}
	canvas.drawImage(img, 0, 0);
    // Add Mark
    canvas.strokeRect(width, height, 10, 10)
}

function getClick(axis)
{
	// Get click position from width or height
		document.addEventListener (	"click",	(event) => {
					if (axis = "x")
					{
						return event.clientX;
					}
					else
					{
						return event.clientY;
					}
		});
}

function getLongitude(click_X)
{
	// Turn landscape click position into longitude in the map
	let minor_comparing = click_X - 38.68;
	let minor_value = -38.68
	for (let value = -38.68; value >= -38.78; value = value - 0.01)
	{
		value = value.toFixed(2);
	  // Use Last Nearest Value To Longitude In The Map Values
		if ((click_X + value) < minor_comparing)
		{
			minor_comparing = (click_X + value);
			minor_value = value;
		}
	}
	return minor_value;
}

function getLatitude(click_Y)
{
  // Turn  portrait click position into latitude in the map
	if (click_Y <= 42)
	{
		return -62.24
	}
	else
	{
		return -62.27;
	}
}
function decToHex(number)
{
    // Turn Decimal number to hexadecimal number
	let digits = ["F", "E", "D", "C", "B", "A", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"];
	// Use digits in right order to give rights results
	digits = digits.reverse();
	// Use Nested Loops Decimal Convertion Comparing Until Found the number
	for (leftDigit in digits)
	{
		for (rightDigit in digits)
		{
			let compared = digits[leftDigit].concat(digits[rightDigit])

			if (parseInt(compared, 16) == number)
			{
				number = compared;
				break;
			}	
		}
	}

	// Delete left zeros

	if (number[0] == "0")
	{
		number = number[1];
	}
	
    return number;
}

function bytes_translate(character)
{
	// Turn Hexadecimal numbers into 1 character
	let state = (parseInt(character, 16) + 100);
	// Turn From code To Unicode Character
	state = String.fromCodePoint("0x" + state);					
	// Give The One Digit Character Compressing For Cookie Size
	return state;
}

async function saveContent(id)
{
    // Save In Cookies the bytes for server cookie getter
		let files = document.getElementById(id).files;
		let buffer
			
		let bytes;
		let content = "";
		// The Cookies Only Could Storage Until 4096 Bytes
		const maxCookieSize = 4096;
		// Each character Has 4 Bytes The Most Of Times
		let storedSize = (document.cookie.length() * 4);

		for (let file in files)
		{
		  // filter only list index instead of list properties
			if ((file.charCodeAt(0) > 47) && (file.charCodeAt(0) < 58))
			{
		    	buffer = await files[file].arrayBuffer();
		    	bytes = new Uint8Array(buffer)
				    
		    	for (let byte in bytes)
		    	{
		        	if (storedSize <= (maxCookieSize - 32))
					{
                    	// Compress To don't pass The 4kb Cookie Maximum Size
				    	content = content.concat(bytes_translate(decToHex(bytes[byte])));
						storedSize = (storedSize + 1);
					}   
				}
				    
				document.cookie = "grouper=" + content;
			}	
		}
}