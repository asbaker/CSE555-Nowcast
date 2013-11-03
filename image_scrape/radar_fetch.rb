require 'nokogiri'
require 'open-uri'

class RadarFetch
  def self.get_product(type, product)
    base_url = "http://radar.weather.gov/ridge/#{type}/#{product}/DTX/"

    doc = Nokogiri::HTML(open(base_url))
    files = doc.css('a').map { |el| el.attributes['href'].value }
    gif_files = files.select { |file| file.end_with?(".gif")}

    gif_files.each do |file| 
      unless File.exists?("#{type}/#{product}/#{file}")
        `wget #{base_url}#{file} -P #{type}/#{product}`
      end
    end
  end

  def self.get_all()
    self.get_product("RadarImg", "N0R")
    self.get_product("RadarImg", "N0S")
    self.get_product("RadarImg", "N0V")
    self.get_product("RadarImg", "N0Z")
    self.get_product("RadarImg", "N1P")
    self.get_product("RadarImg", "NCR")
    self.get_product("RadarImg", "NTP")


    self.get_product("Legend", "N0R")
    self.get_product("Legend", "N0S")
    self.get_product("Legend", "N0V")
    self.get_product("Legend", "N0Z")
    self.get_product("Legend", "N1P")
    self.get_product("Legend", "NCR")
    self.get_product("Legend", "NTP")
  end
end
