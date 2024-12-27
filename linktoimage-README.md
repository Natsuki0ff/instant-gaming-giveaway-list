# HTML Generator for Giveaway Links

This script generates an HTML file containing links to giveaways, each with an associated image. The links are read from an input file, and the output HTML is written to a specified output file. The image URL can be customized.

## Features
- Reads links from a specified text file.
- Generates HTML with `<a>` tags for each link.
- Each link is displayed with a small image.
- Customizable image URL.

## Requirements
- Python 3.x
- Basic text file containing the giveaway links (one link per line).

## Usage

1. **Clone or download the repository**:
   - Clone this repository using Git or download it as a ZIP file.

2. **Run the script**:
   - Open a terminal and run the script by typing:
   
     ```bash
     python generate_html.py
     ```

3. **Enter the file paths**:
   - The script will prompt you to enter the file paths for:
     - The input file (text file containing the giveaway links).
     - The output file (where the HTML will be saved).

4. **Customize the image URL**:
   - The script uses a default image URL, but you can modify it directly in the script if needed.

5. **Output**:
   - The generated HTML will be saved to the specified output file.

## Example

- Input file (`input_links.txt`):
  ```
  http://example.com/giveaway1
  http://example.com/giveaway2
  http://example.com/giveaway3
  ```

- Output HTML:
  ```html
  <p id="giveaways" align="left">
      <a class="giveaway" href="http://example.com/giveaway1" target="_blank" rel="noreferrer">
          <img src="https://gaming-cdn.com/images/avatars/default-avatar.jpg" alt="Giveaway Image" width="76" height="76" />
      </a>
      <a class="giveaway" href="http://example.com/giveaway2" target="_blank" rel="noreferrer">
          <img src="https://gaming-cdn.com/images/avatars/default-avatar.jpg" alt="Giveaway Image" width="76" height="76" />
      </a>
      <a class="giveaway" href="http://example.com/giveaway3" target="_blank" rel="noreferrer">
          <img src="https://gaming-cdn.com/images/avatars/default-avatar.jpg" alt="Giveaway Image" width="76" height="76" />
      </a>
  </p>

