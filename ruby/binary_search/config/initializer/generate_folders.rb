%w[data log].each do |folder|
  Dir.mkdir(folder) unless File.exists?(File.join(App.root, folder))
end

FileUtils.touch File.join(App.root, 'log', 'app.log')
