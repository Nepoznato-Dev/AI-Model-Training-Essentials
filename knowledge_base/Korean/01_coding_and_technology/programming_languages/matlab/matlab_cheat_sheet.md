---
# Metadata
title: "MATLAB — Cheat Sheet"
description: "Quick-reference cheat sheet for MATLAB syntax, matrices, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [matlab, scientific, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# MATLAB — 치트 시트
## 기본
```matlab
% Variables (no declaration needed)
name = 'Alice';
age = 30;
pi_val = 3.14159;
active = true;

% Types
class(name)       % 'char'
class(42)         % 'double'
class(int8(42))   % 'int8'
class(true)       % 'logical'

% String operations (char arrays)
length(name)
upper(name)
lower(name)
strtrim(name)
contains(name, 'lic')
strrep(name, 'Alice', 'Bob')
name(1:3)         % 'Ali'
strsplit('a,b,c', ',')
sprintf('Hello, %s!', name)
str2double('42')
num2str(42)

% String type (R2016b+)
s = "Hello, World";
s = "Hello, " + name;
```

## 행렬 및 배열
```matlab
% Create matrices
A = [1 2 3; 4 5 6; 7 8 9];
v = [1, 2, 3, 4, 5];      % row vector
v = (1:5)';                % column vector
Z = zeros(3, 4);           % 3x4 zeros
O = ones(3, 4);            % 3x4 ones
I = eye(3);                % 3x3 identity
R = rand(3, 4);            % random 3x4
L = linspace(0, 1, 100);  % 100 points from 0 to 1

% Indexing (1-based!)
A(1, 2)          % row 1, col 2: 2
A(:, 1)          % first column
A(1, :)          % first row
A(1:2, 1:2)      % submatrix
A(end, :)        % last row
A(A > 5)         % logical indexing
v(1:2:end)       % every other element

% Matrix operations
A'               % transpose
A * B            % matrix multiply
A .* B           % element-wise multiply
A .^ 2           % element-wise power
inv(A)           % inverse
det(A)           % determinant
eig(A)           % eigenvalues
rank(A)          % rank
norm(A)          % norm

% Array manipulation
size(A)          % [3, 3]
length(v)        % 5
reshape(A, 9, 1)
cat(1, A, B)     % vertical concat
cat(2, A, B)     % horizontal concat
[A; B]           % vertical
[A, B]           % horizontal
sort(v)
unique(v)
flip(v)
```

## 제어 흐름
```matlab
if condition
    % ...
elseif other
    % ...
else
    % ...
end

% Ternary (no native ternary)
result = condition * value_true + (~condition) * value_false;

% Switch
switch day
    case 'Monday'
        disp('early week');
    case {'Saturday', 'Sunday'}
        disp('weekend');
    otherwise
        disp('later');
end

% Loops
for i = 1:10
    disp(i);
end

for item = array
    disp(item);
end

while condition
    % ...
end

% Vectorized (preferred!)
result = sin(x) .^ 2 + cos(x) .^ 2;  % instead of loop
```

## 기능
```matlab
% Function (in file: myfunc.m)
function result = myfunc(a, b)
    result = a + b;
end

% Multiple outputs
function [sum, diff] = addsub(a, b)
    sum = a + b;
    diff = a - b;
end
[s, d] = addsub(5, 3);

% Anonymous function
square = @(x) x.^2;
add = @(a, b) a + b;
f = @(x) x.^2 + 2*x + 1;

% Function handles
result = arrayfun(@sin, 1:10);
result = cellfun(@sum, C);

% Local functions (in same file)
function helper(x)
    disp(x);
end
```

## 플로팅
```matlab
% Basic plot
x = linspace(0, 2*pi, 100);
y = sin(x);
plot(x, y);
title('Sine Wave');
xlabel('x'); ylabel('sin(x)');
grid on;

% Multiple plots
subplot(2, 1, 1);
plot(x, sin(x));
subplot(2, 1, 2);
plot(x, cos(x));

% Scatter
scatter(x, y, 50, 'r', 'filled');

% Histogram
histogram(data, 20);

% 3D plot
[X, Y] = meshgrid(-5:0.5:5, -5:0.5:5);
Z = sin(sqrt(X.^2 + Y.^2));
surf(X, Y, Z);
colorbar;

% Save figure
saveas(gcf, 'plot.png');
print(gcf, '-dpdf', 'plot.pdf');
```

## 데이터 분석
```matlab
% Statistics
mean(data)
median(data)
std(data)
var(data)
min(data)
max(data)
corrcoef(x, y)

% Curve fitting
p = polyfit(x, y, 2);    % polynomial fit
yfit = polyval(p, x);

% Signal processing
fft(data)
ifft(data)
filter(b, a, signal)

% Interpolation
yi = interp1(x, y, xi, 'linear');
yi = interp1(x, y, xi, 'spline');

% Optimization
x_opt = fminsearch(@(x) sum((x - data).^2), x0);
```

## 파일 I/O
```matlab
% Read CSV
data = readtable('data.csv');
data = readmatrix('data.csv');

% Write CSV
writetable(data, 'output.csv');
writematrix(M, 'output.csv');

% Read/write MAT files
save('data.mat', 'var1', 'var2');
load('data.mat');

% Read Excel
data = readtable('data.xlsx', 'Sheet', 'Sheet1');

% Text files
fid = fopen('file.txt', 'r');
content = fread(fid);
fclose(fid);

% Import data interactively
data = importdata('file.dat');
```

## 오류 처리
```matlab
try
    result = risky_operation();
catch ME
    fprintf('Error: %s\n', ME.message);
    fprintf('Identifier: %s\n', ME.identifier);
    rethrow(ME);
end

% Custom error
error('MyApp:InvalidInput', 'Value must be positive');
warning('MyApp:Slow', 'Operation is slow');

% assert
assert(x > 0, 'x must be positive');
```
