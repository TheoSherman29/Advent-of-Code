
% Save data from input text file to an array
A = table2array(readtable("input.txt"));

% Print answers to both parts 1 and 2
disp("Part 1: " + part1(A));
disp("Part 2: " + part2(A));


% Function to solve part 1
function [answer] = part1(list)
    answer = 0;
    
    % Iterate through list, and increment answer if value is greater than
    % the previous value
    for i = 2:length(list)
        if list(i) > list(i-1)
            answer = answer + 1;
        end
    end
end


% Function to solve part 2
function [answer] = part2(list)
    answer = 0;
    
    % Iterate through list, and increment answer if the sum of 3 values is
    % greater than the sum of the previous three values.
    for i = 2:length(list) - 2
        window1 = list(i-1) + list(i) + list(i+1);
        window2 = list(i) + list(i+1) + list(i+2);
        if window2 > window1
            answer = answer + 1;
        end
    end
end