from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    file = request.files['image']

    input_image = Image.open(file.stream)

    # High quality remove
    output_image = remove(input_image)

    img_io = io.BytesIO()
    output_image.save(img_io, format='PNG')  # PNG = transparent
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
