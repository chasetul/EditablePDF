import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import textwrap
import logging


def wrap_text(text, max_width):
    return textwrap.wrap(text, width=max_width)

def submitMulti(text):
    file_name = 'output_jpg_page_1.jpg'
    output_file = 'output_jpg_page_1_modified.jpg'  # Save to a new file

    #logging.basicConfig(level=logging.DEBUG)

    try:
        img = Image.open(file_name)  # Open existing JPG
        draw = ImageDraw.Draw(img)

        # Load a default font (or specify a .ttf file)
        try:
            font = ImageFont.truetype("Arial.ttf", 30)  # Ensure font exists
        except IOError:
            #exit(0)
            font = ImageFont.load_default()
        
        # wrap text ---------------------------------------------->
        max_chars_per_line = 20  # Adjust width as needed
        wrapped_lines = wrap_text(text, max_chars_per_line)

        # # Draw text line by line with vertical spacing
        x, y = 60, 80  # Starting position
        #line_spacing = font.getsize("A")[1] + 10  # THIS LINE BREAKS IT ALL !!

        for line in wrapped_lines:
            draw.text((x, y), line, fill="black", font=font)
            y += 25  # Move down for next line
        # -------------------------------------------------------->

        #draw.text((100, 200), "TESTING", fill="black", font=font)  # Draw input text

        img.save(output_file)  # Save modified image
        return output_file  # Return updated image path for preview
    except Exception as e:
        return f"Error: {e}"

def submit1(text):
    file_name = 'output_jpg_page_1.jpg'
    output_file = 'output_jpg_page_1_modified.jpg'  # Save to a new file

    #logging.basicConfig(level=logging.DEBUG)

    try:
        img = Image.open(file_name)  # Open existing JPG
        draw = ImageDraw.Draw(img)

        # Load a default font (or specify a .ttf file)
        try:
            font = ImageFont.truetype("Arial.ttf", 30)  # Ensure font exists
        except IOError:
            #exit(0)
            font = ImageFont.load_default()
        
        # wrap text ---------------------------------------------->
        # max_chars_per_line = 20  # Adjust width as needed
        # wrapped_lines = wrap_text(text, max_chars_per_line)

        # # Draw text line by line with vertical spacing
        # x, y = 100, 200  # Starting position
        # line_spacing = font.getsize("A")[1] + 10  # Get line height

        # for line in wrapped_lines:
        #     draw.text((x, y), line, fill="black", font=font)
        #     y += line_spacing  # Move down for next line
        # -------------------------------------------------------->

        draw.text((100, 200), text, fill="black", font=font)  # Draw input text
        draw.text((100, 180), 'Example Text!', fill="black", font=font)  # Draw input text

        img.save(output_file)  # Save modified image
        return output_file  # Return updated image path for preview
    except Exception as e:
        return f"Error: {e}"

with gr.Blocks() as demo:
    gr.Markdown("# Text Input with Live Preview")
    with gr.Row():
        with gr.Column():
            text1 = gr.Textbox(label="Input Text 1")
            btn1 = gr.Button(value='Submit')
        
        preview = gr.Image(value='output_jpg_page_1.jpg', label='Preview Document')

    btn1.click(submitMulti, inputs=[text1], outputs=[preview])  # Ensure correct function call

demo.launch()
