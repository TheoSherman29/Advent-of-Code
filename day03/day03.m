input_matrix = readmatrix('input.txt');
input = arrayfun(@(x) uint16(str2num(sprintf("0b%d", x))), input_matrix); % Format input data

disp("Part 1: " + part1(input))
disp("Part 2: " + part2(input))


function answer = part1(data) % Function to solve part 1
    data_len = 12;
    g = uint16(0);
    for i = 1:data_len % Loops through the length of a line
        value = median(bitget(data, i)); % Median gives the most common of 2 values
        g = bitset(g, i, value); % Assigns most common bit in each place
    end
    e = bitand(bitcmp(g), 0b0000111111111111); % Flips g so each bit is the least common
    answer = single(g) * single(e);
end


function answer = part2(data) % Function to solve part 2
    o2 = data;
    co2 = data;
    data_len = 12;

    for i = data_len:-1:1 % Loops through length of a line
        value = ceil(median(bitget(o2, i))); % Gets most common bit
        o2(bitget(o2, i) ~= value) = []; % Removes numbers without most common bit in that place
        if numel(o2) == 1, break, end % Breaks if only 1 num left
    end
    for i = data_len:-1:1 % Same as above, but least common bit for each step
        value = ceil(median(bitget(co2, i)));
        co2(bitget(co2, i) == value) = [];
        if numel(co2) == 1, break, end
    end
    answer = single(o2)*single(co2);
end

