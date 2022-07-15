    data = readtable('input.txt', 'Delimiter', 'space');
    dir = string(table2array(data(:,1)));
    mag = table2array(data(:,2));
    
    disp("Part 1: " + part1(dir, mag));
    disp("Part 2: " + part2(dir, mag));

    % Function to solve p1
    function answer = part1(dir, mag)
        xpos = 0;
        depth = 0;

        for i = 1:length(dir)
            if dir(i) == "forward"
                xpos = xpos + mag(i);
            elseif dir(i) == "up"
                depth = depth - mag(i);
            elseif dir(i) == "down"
                depth = depth + mag(i);
            end
        end
        answer = xpos * depth;
    end

    % Function to solve p2
    function answer = part2(dir, mag)
        xpos = 0;
        depth = 0;
        aim = 0;    
        
        for i = 1:length(dir)
            if dir(i) == "forward"
                xpos = xpos + mag(i);
                depth = depth + aim * mag(i);
            elseif dir(i) == "up"
                aim = aim - mag(i);
            elseif dir(i) == "down"
                aim = aim + mag(i);
            end
        end
        answer = xpos * depth;
    end
