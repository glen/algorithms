require_relative File.join(App.root, 'lib', 'read_json_file.rb')

INPUT_JSON = File.join(App.root, 'data', 'input.json')

class LinearSearch
  attr_reader :input, :no_to_search, :iterations
  include ReadJsonFile


  def initialize(number_to_search)
    @input = read_input_file(INPUT_JSON)['input']
    @no_to_search = number_to_search.to_i
    @iterations = 0
  end

  def search
    0.upto(@input.length - 1) do |i|
      @iterations += 1
      if @input[i] == @no_to_search
        return i
      end
    end
    return -1
  end

  def self.valid_number?(number)
    number.match?(/^-?\d+$/)
  end
end
