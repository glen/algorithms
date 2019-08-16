require 'rubygems'
require 'bundler/setup'
require 'byebug'

Bundler.require(:default)

Dir.glob(File.join('./config/initializer', '**.rb')).sort.each do |initializer|
  require initializer
end
