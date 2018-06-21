#!/bin/bash
# Pins on the NEO2: http://nanopi.io/nanopi-neo2.html
# GPIO Pin Spec

# Pin#	Name	Linux gpio	Pin#	Name	Linux gpio
# 1	SYS_3.3V		2	VDD_5V	
# 3	I2C0_SDA		4	VDD_5V	
# 5	I2C0_SCL		6	GND	
# 7	GPIOG11	203	8	UART1_TX/GPIOG6	198
# 9	GND		10	UART1_RX/GPIOG7	199
# 11	UART2_TX/GPIOA0	0	12	PWM1/GPIOA6	6
# 13	UART2_RTS/GPIOA2	2	14	GND	
# 15	UART2_CTS/GPIOA3	3	16	UART1_RTS/GPIOG8	200
# 17	SYS_3.3V		18	UART1_CTS/GPIOG9	201
# 19	SPI0_MOSI/GPIOC0	64	20	GND	
# 21	SPI0_MISO/GPIOC1	65	22	UART2_RX/GPIOA1	1
# 23	SPI0_CLK/GPIOC2	66	24	SPI0_CS/GPIOC3	67

###
### Set GPIO pins if they are missing
###
for i in 198 199 200 201; do
  echo "Exporting GPIO#$i"
  ! [ -e /sys/class/gpio/gpio$i ] && echo $i > /sys/class/gpio/export
  echo " * Setting active_low"
  echo 1 > /sys/class/gpio/gpio$i/active_low
  echo " * Setting direction to high to aviod glitches"
  echo high > /sys/class/gpio/gpio$i/direction
done
