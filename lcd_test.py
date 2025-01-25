import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# **Define LCD Columns and Rows**
lcd_columns = 16
lcd_rows = 2

# **Define GPIO Pins for LCD**
lcd_rs = digitalio.DigitalInOut(board.D26)  # Register select pin
lcd_en = digitalio.DigitalInOut(board.D19)  # Enable pin
lcd_d4 = digitalio.DigitalInOut(board.D13)  # Data pin D4
lcd_d5 = digitalio.DigitalInOut(board.D6)  # Data pin D5
lcd_d6 = digitalio.DigitalInOut(board.D5)  # Data pin D6
lcd_d7 = digitalio.DigitalInOut(board.D11)  # Data pin D7

# **Initialize the LCD**
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

# **Example Message**
lcd.message = "Hello, Plant!"
