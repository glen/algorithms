require 'spec_helper'
require_relative File.join(App.root, 'lib', 'linear_search.rb')

describe 'LinearSearch' do
  let(:input_json_data) { {'input' => [1, 2, 3, 4]} }

  describe 'initialize' do
    before do
      allow_any_instance_of(LinearSearch).to receive(:read_input_file).and_return(input_json_data)
    end

    it 'sets the instance variable - input' do
      ls = LinearSearch.new('5')
      expect(ls.input).to eq([1, 2, 3, 4])
    end

    it 'sets the instance variable - no_to_search' do
      ls = LinearSearch.new('5')
      expect(ls.no_to_search).to eq(5)
    end
  end

  describe 'search' do

    before do
      allow_any_instance_of(LinearSearch).to receive(:read_input_file).and_return(input_json_data)
    end

    it 'returns the location of the number to search if present' do
      ls = LinearSearch.new('2')
      expect(ls.search).to eq(1)
    end

    it 'returns -1 if the number to search is not present' do
      ls = LinearSearch.new('5')
      expect(ls.search).to eq(-1)
    end
  end

  describe 'valid_number?' do
    ['0', '1', '5', '10', '345', '36126', '-5'].each do |number_as_string|
      it "returns true if input is a whole positive number - #{number_as_string}" do
        expect(LinearSearch.valid_number?(number_as_string)).to be true
      end
    end

    ['1.3', 'a_string', '1ten'].each do |number_as_string|
      it "returns false if input is a whole positive number - #{number_as_string}" do
        expect(LinearSearch.valid_number?(number_as_string)).to be false
      end
    end
  end
end