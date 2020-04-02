require_relative File.join(App.root, 'lib', 'read_json_file.rb')

INPUT_JSON = File.join(App.root, 'data', 'input.json')

class LinearSearch
  attr_reader :input, :located, :iterations
  include ReadJsonFile


  def initialize
    @input = read_input_file(INPUT_JSON)['input']
    @located = false
    @iterations = 0
  end

  def search(number_to_search)
    input.each_with_index do |number, index|
      @iterations = index + 1
      if number == number_to_search
        @located = true
        return @iterations
      end
    end
    return -1
  end

end
