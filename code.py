from PIL import Image
import sys

# Daftar karakter ASCII berwarna yang akan digunakan
charset = "@%#*+=-:. "

# Fungsi untuk mengonversi gambar ke gambar ASCII berwarna
def image_to_ascii_color(image_path, columns, char_width):
    img = Image.open(image_path)
    width, height = img.size
    char_height = char_width * height // (2 * width)
    img = img.resize((columns, char_height * 2))
    img = img.convert('RGB')  # Konversi gambar ke mode RGB

    ascii_str = ''
    for y in range(char_height * 2):
        for x in range(columns):
            pixel_color = img.getpixel((x, y))
            r, g, b = pixel_color
            gray_value = 0.2989 * r + 0.5870 * g + 0.1140 * b
            char_index = int(gray_value / 256 * len(charset))
            ascii_str += f"\033[38;2;{r};{g};{b}m{charset[char_index]}\033[0m"  # Efek warna pada karakter ASCII
        ascii_str += '\n'

    return ascii_str

# Masukkan path gambar yang ingin Anda konversi menjadi gambar ASCII berwarna
image_path = "contoh.JPG"
# Tentukan lebar kolom dan karakter pengganti
columns = 400
char_width = 300

# Konversi gambar ke gambar ASCII berwarna
output = image_to_ascii_color(image_path, columns, char_width)
sys.stdout.write(output)
