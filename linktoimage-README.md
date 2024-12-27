# HTML Giveaway Generator 🎁

This Python script generates an HTML file that formats a list of giveaway links into sections with images, dividing the list into groups of 10 links per section. Each section is titled with "Paragraph" followed by a counter, and the links are displayed with a giveaway image.

## Features 🚀

- Reads a text file containing giveaway links 📄.
- Generates HTML with the links formatted in groups of 10 🔟.
- Adds a giveaway image next to each link 🖼️.
- Divides the links into sections with titles formatted as "Paragraph 1", "Paragraph 2", etc. 📝.
- Supports custom image URLs to display next to each link 🌐.

## Requirements ⚙️

- Python 3.x 🐍.
- A text file containing links (one per line) 📋.
- Internet connection to use the default image URL or you can specify your own 🌍.

## How to Use 🛠️

1. Clone or download the repository to your local machine 💻.

2. Place the script in a folder on your computer 📂.

3. Prepare a text file (`.txt`) with the list of links you want to format. Each link should be on its own line 🔗.

4. Run the script:

```bash
python script_name.py
```

5. When prompted, input the path to the text file with the links and the desired output file path (for example, `C:/path/to/output.html`) 📍.

6. The script will generate an HTML file with all the links and images, and it will split the links into sections of 10 links each 📑.

### Example of usage:

```bash
Please enter the location of the input file (e.g., C:/path/to/file.txt): C:/path/to/input.txt
Please enter the location of the output file (e.g., C:/path/to/output.txt): C:/path/to/output.html
```

## Output 📊

The generated HTML file will look like this:

```html
<p id="giveaways" align="left">
    <a class="giveaway" href="https://example.com" target="_blank" rel="noreferrer">
        <img src="https://gaming-cdn.com/images/avatars/16693760-1689603180.jpg" alt="Giveaway Image" width="76" height="76" />
    </a>
    <!-- More links here -->
    <br><h1>Paragraph 1</h1>
    <br>
    <a class="giveaway" href="https://anotherlink.com" target="_blank" rel="noreferrer">
        <img src="https://gaming-cdn.com/images/avatars/16693760-1689603180.jpg" alt="Giveaway Image" width="76" height="76" />
    </a>
    <!-- More links here -->
</p>
```

## Customization 🛠️

- **Image URL**: You can customize the image URL by modifying the `image_url` variable in the script 🌟.
- **File paths**: The script asks for the file paths to the input file (with links) and the output file (where the generated HTML will be saved). Make sure to provide full file paths 🗂️.

## License 📝
Creative Common, feel free to use dawg
