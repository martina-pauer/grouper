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
	let state = character;
	// From A to FF turn into respective character
	if (character == "A")
	{
		state = "x";
	}
	else if (character == "B")
	{
		state =	"g";
	}
	else if (character == "C")
	{
		state = "h";
	}
	else if (character == "D")
	{
		state = "i";
	}
	else if (character == "E")
	{
		state = "j";
	}
	else if (character == "F")
	{
		state = "k";
	}
	else if (character == "10")
	{
		state = "l";
	}
	else if (character == "11")
	{
		state = "m";
	}
	else if (character == "12")
	{
		state = "n";
	}
	else if (character == "13")
	{
		state = "o";
	}
	else if (character == "14")
	{
		state = "p";
	}
	else if (character == "15")
	{									
		state = "q";
	}
	else if (character == "16")
	{
		state = "r";
	}
	else if (character == "17")
	{
		state = "s";
	}
	else if (character == "18")
	{
		state = "t";
	}
	else if (character == "19")
	{
		state = "u";
	}
	else if (character == "1A")
	{
		state = "v";
	
	}
	else if (character == "1B")
	{
		state = "w";
	}
	else if (character == "1C")
	{
		state = "y";
	}
	else if (character == "1D")
	{
		state = "z";
	}
	else if (character == "1E")
	{
		state = "+";
	}
	else if (character == "1F")
	{
		state = "*";
	}
	else if (character == "20")
	{
		state = "-";
	}				
	else if (character == "21")
	{
		state = "/";
	}
	else if (character == "22")
	{
		state = ".";
	}
	else if (character == "23")
	{
		state = ",";
	}
	else if (character == "24")
	{
		state = ";";
	}
	else if (character == "25")
	{
		state = "{";
	}	
	else if (character == "26")
	{
		state = "}";
	}
	else if (character == "27")
	{
		state = "(";
	}
	else if (character == "28")
	{
		state = ")";
	}
	else if (character == "29")
	{
		state = ":";
	}
	else if (character == "2A")
	{
		state = "@";
	}
	else if (character == "2B")
	{
		state = "%";
	}
	else if (character == "2C")
	{
		state = "=";
	}
	else if (character == "2D")
	{
		state = "?";
	}
	else if (character == "2E")
	{
		state = "¿";
	}
	else if (character == "2F")
	{
		state = "$";
	}
	else if (character == "30")
	{
		state = "#";
	}
	else if (character == "31")
	{
		state = "&";
	}
	else if (character == "32")
	{
		state = "\\";
	}
	else if (character == "33")
	{
		state = "~";
	}	
	else if (character == "34")
	{
		state = "<";
	}
	else if (character == "35")
	{
		state = ">";
	}
	else if (character == "36")
	{
		state = "!";
	}
	else if (character == "37")
	{
		state = "_";
	}
	else if (character == "38")
	{
		state = "°";
	}	
	else if (character == "39")
	{
		state = "|";
	}
	else if (character == "3A")
	{
		state = "¬";
	}
	else if (character == "3B")
	{
		state = "^";
	}
	else if (character == "3C")
	{
		state = "`";
	}
	else if (character == "3D")
	{
		state = "¨";
	}
	else if (character == "3E")
	{
		state = "'";
	}
	else if (character == "3F")
	{
		state = "Ø";
	}
	else if (character == "40")
	{
		state = "«";
	}
	else if (character == "41")
	{
		state = "»";
	}
	else if (character == "42")
	{
		state = "¦";
	}
	else if (character == "43")
	{
		state = "©";
	}
	else if (character == "44")
	{
		state = "¢";
	}
	else if (character == "45")
	{
		state = "Ł";
	}
	else if (character == "46")
	{
		state = "Ω";
	}
	else if (character == "47")
	{
		state = "ß";
	}
	else if (character == "48")
	{
		state = "æ";
	}
	else if (character == "49")
	{
		state = "Ð";
	}	
	else if (character == "4A")
	{
		state = 'ŋ';
	}	
	else if (character == "4B")
	{
		state =  "þ";
	}
	else if (character == "4C")
	{
		state = " ";
	}
	else if (character == "4D")
	{
		state = "€";
	}	
	else if (character == "4E")
	{
		state = "¥";
	}
	else if (character == "4F")
	{
		state = '·';
	}
	else if (character == "50")
	{
		state = "Σ";
	}		
	else if (character == "51")
	{
		state = "φ";
	}
	else if (character == "52")
	{
		state = "ψ";
	}	
	else if (character == "53")
	{
		state = "ᴨ";
	}	
	else if (character == "54")
	{
		state = "Δ";
	}
	else if (character == "55")
	{
		state = "¶";
	}	
	else if (character == "56")
	{
		state = "®";
	}
	else if (character == "57")
	{
		state = "¼";
	}
	else if (character == "58")
	{
		state = "½";
	}
	else if (character == "59")
	{
		state = "♦";
	}	
	else if (character == "5A")
	{
		state = "♣";
	}
	else if (character == "5B")
	{
		state = "♠";
	}	
	else if (character == "5C")
	{
		state = "♥";
	}
	else if (character == "5D")
	{
		state = "♩";
	}	
	else if (character == "5E")
	{
		state = "♫";
	}
	else if (character == "5F")
	{
		state = "♪";
	}
	else if (character == "60")
	{
		state = "♬";
	}
	else if (character == "61")
	{
		state = "◘";
	}
	else if (character == "62")
	{
		state = "◙";
	}
	else if (character == "63")
	{
		state = "◖";
	}
	else if (character == "64")
	{
		state = "◗";
	}
	else if (character == "65")
	{
		state = "▌";
	}
	else if (character == "66")
	{
		state = "∞";
	}	
	else if (character == "67")
	{
		state = "◕";
	}
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
				
		for (let file in files)
		{
		  // filter only list index instead of list properties
			if ((file.charCodeAt(0) > 47) && (file.charCodeAt(0) < 58))
			{
		    	buffer = await files[file].arrayBuffer();
		    	bytes = new Uint8Array(buffer)
				    
		    	for (let byte in bytes)
		    	{
		        	if (byte <= 4095)
					{
                    	// Compress To don't pass The 4kb Cookie Maximum Size
				    	content = content.concat(bytes_translate(decToHex(bytes[byte])));
					}   
				}
				    
				document.cookie = "grouper=" + content;
			}	
		}
}