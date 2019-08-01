require 'spec_helper'
require_relative File.join(App.root, 'lib', 'binary_search.rb')

describe 'BinarySearch' do
  let(:input_array) { [5, 3, 6, 2, 7] }
  let(:json_data) { {'input' => input_array} }

  describe 'initialize' do
    before do
      allow_any_instance_of(BinarySearch).to receive(:read_input_file).and_return(json_data)
    end

    it 'sets the instance variable - input' do
      bs = BinarySearch.new('5')
      expect(bs.input).to eq(input_array.sort)
    end

    it 'sets the instance variable - no_to_search' do
      bs = BinarySearch.new('5')
      expect(bs.no_to_search).to eq(5)
    end
  end

  describe 'search' do

    before do
      allow_any_instance_of(BinarySearch).to receive(:read_input_file).and_return(json_data)
    end

    context 'number present' do
      it 'returns the location of the number to search if present' do
        bs = BinarySearch.new('2')
        expect(bs.search).to eq(0)
      end
    end

    context 'number not present' do
      it 'returns -1 if the number to search is not present' do
        bs = BinarySearch.new('8')
        allow(bs).to receive(:read_input_file).and_return( json_data )
        expect(bs.search).to eq(-1)
      end
    end

    it 'sets the iterations' do
      bs = BinarySearch.new('2')
      allow(bs).to receive(:read_input_file).and_return( json_data )
      bs.search
      expect(bs.iterations).to eq(3)
    end
  end

  describe 'valid_number?' do
    ['0', '1', '5', '10', '345', '36126'].each do |number_as_string|
      it "returns true if input is a whole positive number - #{number_as_string}" do
        expect(BinarySearch.valid_number?(number_as_string)).to be true
      end
    end

    ['-5', '1.3', 'a_string', '1ten'].each do |number_as_string|
      it "returns false if input is a whole positive number - #{number_as_string}" do
        expect(BinarySearch.valid_number?(number_as_string)).to be false
      end
    end
  end
end