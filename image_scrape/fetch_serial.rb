require "serialport"
require "sqlite3"
require_relative 'radar_fetch'

port_str = "/dev/ttyACM0"

baud_rate = 9600
data_bits = 8
stop_bits = 1
parity = SerialPort::NONE



def main(serial, db)
	while true do
		value = get_serial_value(serial)
		unless value.nil?
			insert_data(db, value.to_i)
			download_images(value.to_i)
		end
		sleep 0.2
	end
end

def create_schema(db)
	db.execute "CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT, t TIMESTAMP DEFAULT CURRENT_TIMESTAMP, value INT)"
end

def insert_data(db, value)
	puts "#{DateTime.now} - #{value}"
	db.execute "INSERT INTO data(value) VALUES(#{value})"
end


def get_serial_value(serial, value="")
	begin
		serial.readline("|")
	rescue
	end
end




#	value = ""
#	begin
#		value = serial.gets(sep="|")
#	rescue
#	end

#	unless value.nil? or value.empty?
#		value.to_i
#		p "value is #{value} ... #{value.to_i}"
#	else
#		nil
#	end
#end

def download_images(value)
	if value.to_i > 200 and RadarFetch.minutes_since_last_image > 120
		RadarFetch.get_all
	end
end

serial = SerialPort.new(port_str, baud_rate, data_bits, stop_bits, parity)
db = SQLite3::Database.open "data.db"
create_schema db

main(serial, db)
