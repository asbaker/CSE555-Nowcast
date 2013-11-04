
desc "Fetch latest radar data from NOAA"
task :fetch do
		system("cd image_scrape; ruby fetch_now.rb")
end

desc "Open arduino solution on the mac"
task :arduino do
  system("open arduino_rain_sensor/arduino_rain_sensor.ino -a arduino")
end


desc "Open sqlite3 database"
task :db do
	system("sqlite3 image_scrape/data.db")
end

desc "Find all elements of rain"
task :find_rain do
	system("sqlite3 image_scrape/data.db 'SELECT * FROM data WHERE value > 0'")
end
