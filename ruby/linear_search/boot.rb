require 'rubygems'
require 'bundler/setup'
require 'byebug'
require 'colorize'

Bundler.require(:default)

Dir.glob(File.join('./config/initializer', '**.rb')).each do |initializer|
  require initializer
end
