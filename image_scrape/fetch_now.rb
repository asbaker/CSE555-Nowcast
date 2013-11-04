require_relative 'radar_fetch'

p "Last Image Fetched: #{RadarFetch.minutes_since_last_image} minutes ago"
RadarFetch.get_all
