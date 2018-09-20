import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
# Raspberry Pi pin configuration:
RST = 17
# Note the following are only used with SPI:
DC = 22
SPI_PORT = 0
SPI_DEVICE = 0
# 128x32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
image = Image.open('qrcode.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
# Display image.
disp.image(image)
disp.display()
