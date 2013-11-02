require 'nokogiri'
require 'open-uri'


def get_product(type, product)
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


get_product("RadarImg", "N0R")
get_product("RadarImg", "N0S")
get_product("RadarImg", "N0V")
get_product("RadarImg", "N0Z")
get_product("RadarImg", "N1P")
get_product("RadarImg", "NCR")
get_product("RadarImg", "NTP")


get_product("Legend", "N0R")
get_product("Legend", "N0S")
get_product("Legend", "N0V")
get_product("Legend", "N0Z")
get_product("Legend", "N1P")
get_product("Legend", "NCR")
get_product("Legend", "NTP")

