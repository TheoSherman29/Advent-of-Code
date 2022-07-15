data = readtable('input.txt', Delimiter = {'comma'}); % Converts full input data to table

bingo_rolls = [str2double(data.Var1{1}) table2array(data(1, 2:end))]; % Takes list of rolls from top of input

data = readtable('input.txt', ... % Ignores rolls and takes boards
    Delimiter = {'space'}, ...
    LeadingDelimitersRule = 'ignore', ...
    ConsecutiveDelimitersRule = 'join');

for i = (height(data) - 4):-5:1 % Reformats card data
    bingo_cards((i + 4)/5) = {table2array(data(i:i+4, :))};
end

disp("Part 1: " + part1(bingo_rolls, bingo_cards));
disp("Part 2: " + part2(bingo_rolls, bingo_cards));


function score = part1(rolls, cards) % Function to solve part 1
    picked = -1; 
    winner = false;
    for roll = rolls
        for card = 1:numel(cards)
            % Marks -1 in the spot of the roll to indicate it's been picked 
            cards{card}(roll == cards{card}) = picked;
            % Check for vertical or horizontal bingo
            if any(sum(cards{card}, 1) == 5*picked) || any(sum(cards{card}, 2) == 5*picked)
                score = roll * sum(cards{card}(cards{card}(:) ~= picked));
                winner = true;
            end
        end
        if winner % Exits the loop if a card won
            break
        end
    end
end


function score = part2(rolls, cards) % Function to solve part 2
    picked = -1;
    won = -2;
    for roll = rolls
        for card = 1:numel(cards)
            % Marks -2 in top left square if board has won already
            if cards{card}(1, 1) == won, continue, end
            % Marks -1 in the spot of the roll to indicate it's been picked
            cards{card}(roll == cards{card}) = picked;
            % Check for vertical or horizontal bingo
            if any(sum(cards{card}, 1) == 5*picked) || any(sum(cards{card}, 2) == 5*picked)
                score = roll * sum(cards{card}(cards{card}(:) ~= picked));
                % Marks -2 in top left square of winning card
                cards{card}(1, 1) = won;
            end
        end
    end
end