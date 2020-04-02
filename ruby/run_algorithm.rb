require File.expand_path('../boot', __FILE__)

AVAILABLE_ALGORITHMS = %w[linear_search]
require_relative(File.join(App.root, 'helpers', 'formatted_output.rb'))

class RunAlgorithm
  include FormattedOutput
  def initialize
    parse_args
    load_algorithm
    @number_to_search
    @algorithm =  eval("#{algorithm_class_name}.new")
  end

  def locate
    @algorithm.search(@number_to_search)
  end

  def print_result
    if @algorithm_to_run.match?(/_search$/)
      print_search_result
    else
      print_sort_result
    end
  end

  private
  def print_search_result
    print_value(value: "#{'#'*25} #{formatted_algorithm_name} Implementation #{'#'*25}", color: :black, background: :white)
    print_label(label: "Input", color: :blue, column_width: 20)
    print_value(value: "[#{@algorithm.input.join(', ')}]", color: :yellow)
    print_label(label: "Number to Search", color: :blue, column_width: 20)
    print_value(value: @number_to_search, color: :yellow)
    print_label(label: "Located", color: :blue)
    if @algorithm.located.eql?(false)
      print_value(value: "No", color: :red)
    else
      print_value(value: "Yes", color: :green)
    end
    print_label(label: "Iterations", color: :blue)
    print_value(value: @algorithm.iterations, color: :yellow)
  end

  def print_sort_result
    puts "Update method to print sort result!"
  end

  def parse_args
    if ARGV.length < 1
      puts("Invalid input!\nRun code like this 'ruby run_algorithm.rb [algorithm_name]'")
      exit
    end

    @algorithm_to_run = ARGV[0]
    if @algorithm_to_run.match?(/_search$/) && ARGV.length < 2
      puts("Invalid input!\nRun code like this 'ruby run_algorithm.rb [algorithm_name] [number_to_search]'")
      exit
    end

    unless AVAILABLE_ALGORITHMS.include?(@algorithm_to_run)
      puts("Invalid algorithm!\nAvailable algorithms are #{AVAILABLE_ALGORITHMS.join(',')}")
      exit
    end

    if @algorithm_to_run.match?(/_search$/) && valid_number?(ARGV[1])
      @number_to_search = ARGV[1].to_i
    else
      puts("Invalid input!\nGive a number to search.")
      exit
    end
  end

  def load_algorithm
    require_relative(File.join(App.root, 'lib', "#{@algorithm_to_run}.rb"))
  end

  def algorithm_class_name
    @algorithm_to_run.split('_').collect(&:capitalize).join
  end

  def formatted_algorithm_name
    @algorithm_to_run.split('_').map(&:capitalize).join(' ')
  end

  def valid_number?(number)
    number.match?(/^-?\d+$/)
  end
end

algo = RunAlgorithm.new
algo.locate
algo.print_result