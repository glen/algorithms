require_relative File.join(App.root, 'lib', 'read_json_file.rb')

INPUT_JSON = File.join(App.root, 'data', 'input.json')

class BinarySearch
  attr_reader :input, :no_to_search, :iterations
  include ReadJsonFile


  def initialize(number_to_search)
    @input = read_input_file(INPUT_JSON)['input'].sort
    @no_to_search = number_to_search.to_i
  end

  def search(low_index=0, high_index=@input.length - 1, iterations=0, input=@input)
    @iterations = iterations + 1
    if high_index >= low_index
      mid_index = low_index + ((high_index - low_index)/2.0).ceil
      # puts "#{@iterations} - #{low_index}, #{mid_index} and #{high_index} of #{@input}"
      # puts "Comparing #{input[mid_index]} with #{no_to_search}"
      if input[mid_index] == no_to_search
        return mid_index
      elsif input[mid_index] < no_to_search
        search(mid_index + 1, high_index, @iterations)
      else input[mid_index] > no_to_search
        search(low_index, mid_index - 1, @iterations)
      end
    else
      return -1
    end
  end

  def self.valid_number?(number)
    number.match?(/^\d+$/)
  end
end
