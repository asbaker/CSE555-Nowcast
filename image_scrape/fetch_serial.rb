require "serialport"

port_str = "/dev/ttyUSB0"

baud_rate = 9600
data_bits = 8
stop_bits = 1
parity = SerialPort::NONE

serial = SerialPort.new(port_str, baud_rate, data_bits, stop_bits, parity)

while true do
  while (i = serial.gets.chomp) do
    puts i
  end
end

serial.close
