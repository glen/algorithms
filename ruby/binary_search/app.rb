require File.expand_path('../boot', __FILE__)

["binary_search.rb"].each do |lib_file|
  require_relative(File.join(App.root, 'lib', lib_file))
end
require_relative(File.join(App.root, 'helpers', 'formatted_output.rb'))

include FormattedOutput

print_value(value: "#{'#'*25} Binary Search Implementation #{'#'*25}", color: :black, background: :white)
begin
  if BinarySearch.valid_number?(ARGV[0])
    bs = BinarySearch.new(ARGV[0])
    print_label(label: "Input", color: :blue, column_width: 20)
    print_value(value: "[#{bs.input.join(', ')}]", color: :yellow)
    print_label(label: "Number to Search", color: :blue, column_width: 20)
    print_value(value: ARGV[0], color: :yellow)
    print_label(label: "Located ?", color: :blue)
    if bs.search == -1
      print_value(value: "No", color: :red)
    else
      print_value(value: "Yes", color: :green)
    end
    print_label(label: "Iterations", color: :blue)
    print_value(value: bs.iterations, color: :yellow)
  else
  	puts "Invalid input. Use only numbers."
  	puts
  	exit 1
  end
rescue Exception => e
  raise e
end
puts
