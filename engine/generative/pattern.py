# PNG
# https://www.adobe.com/creativecloud/file-types/image/raster/png-file.html
# https://en.wikipedia.org/wiki/PNG

# BMP
# https://docs.krita.org/en/general_concepts/file_formats/file_bmp.html#


# pip install pillow

from PIL import Image, ImageDraw


class Pattern:
    @staticmethod
    def create(pattern: list[list], size=50, path="example.png"):
        # Define Sizes
        w, h = size, size
        c_count = len(pattern[0])
        r_count = len(pattern)
        cc = w / c_count
        rr = h / r_count

        # Create empty image
        image = Image.new("RGB", (w, h), color="white")

        # Get a drawing object
        draw = ImageDraw.Draw(image)

        # Draw a rectangle
        for r in range(0, r_count):
            for c in range(0, c_count):
                if pattern[r][c] == 1:
                    draw.rectangle(
                        (c * cc, r * rr, (c + 1) * cc, (r + 1) * rr), fill="black"
                    )

        # Save the image
        image.save(path)

    @staticmethod
    def tile(img_path, new_path, cols, rows):
        tile = Image.open(img_path)

        sw = tile.width
        sh = tile.height

        w = sw * cols
        h = sh * rows

        pattern = Image.new("RGB", (w, h), color="white")

        for row in range(rows):
            for col in range(cols):
                x = col * sw
                y = row * sh
                pattern.paste(tile, (x, y))

        pattern.save(new_path)


if __name__ == "__main__":
    sample = [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
    ]

    Pattern.create(sample)
