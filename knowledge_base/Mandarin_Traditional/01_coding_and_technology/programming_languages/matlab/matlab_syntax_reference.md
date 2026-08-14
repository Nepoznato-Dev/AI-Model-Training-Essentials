---
# Metadata
title: "MATLAB — Syntax Reference"
description: "Detailed syntax reference for MATLAB covering matrix operations, plotting, Simulink, toolboxes, and scientific computing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [matlab, syntax-reference, matrices, plotting, scientific-computing, simulink, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# MATLAB — 語法參考
本文檔提供了 MATLAB (R2024+) 的全面、結構化語法參考。它透過關注詳盡的語法模式、矩陣運算、繪圖和科學計算慣用語來補充主要的 MATLAB 參考。
---

## 運算子和表達式
### 核心運營商
|操作員|名稱 |範例|筆記|
|----------|------|---------|--------|
|`+``-``*``/``^`|算術|`A * B`|矩陣乘法 |
|`.*``./``.^`|元素方面 |`A .* B`|陣列運算 |
|`'`|轉置 |`A'`|共軛轉置|
|`.'`|非共軛轉置 |`A.'`| |
|`\`|左除法 |`A \ b`|求解 Ax = b |
|`/`|右除 |`b / A`|求解 xA = b |
|`==``~=` |平等|`A == B`|元素方面 |
|`<``>``<=``>=` |比較|`A > 0`|元素方面 |
|`&``\|``~`|邏輯（按元素）|`A & B`| |
|`&&``\|\|` |短路|`a && b`|僅標量 |
|`:`|冒號/範圍 |`1:10`|`start:step:stop`|
|`;`|行分隔符號/抑制|`[1; 2; 3]`| |
|`,`|列分隔符號 |`[1, 2, 3]`| |
---

## 矩陣運算
```matlab
% Create matrices
A = [1 2 3; 4 5 6; 7 8 9];    % 3x3 matrix
v = [1; 2; 3];                  % column vector
row = [1, 2, 3];                % row vector
I = eye(3);                     % identity matrix
Z = zeros(3, 4);               % 3x4 zeros
O = ones(3, 3);                % 3x3 ones
R = rand(3, 3);                % uniform random
N = randn(3, 3);               % normal random
D = diag([1 2 3]);             % diagonal matrix
L = linspace(0, 1, 100);       % 100 points from 0 to 1

% Matrix operations
B = A';                         % transpose
C = A * B;                      % matrix multiply
D = A .* B;                     % element-wise multiply
E = A^2;                        % matrix power
F = inv(A);                     % inverse
g = det(A);                     % determinant
r = rank(A);                    % rank
[V, D] = eig(A);               % eigenvalues/eigenvectors
[U, S, V] = svd(A);            % singular value decomposition

% Solving systems
x = A \ b;                      % solve Ax = b (preferred)
x = inv(A) * b;                 % same but slower/less stable

% Indexing (1-based!)
A(2, 3)                         % row 2, col 3
A(:, 1)                         % first column
A(1, :)                         % first row
A(1:2, 2:3)                     % submatrix
A(A > 5)                        % logical indexing
A(A > 5) = 0                    % set elements > 5 to 0

% Reshaping
B = reshape(A, 9, 1);          % reshape to 9x1
C = A(:);                       % flatten to column vector
D = repmat(A, 2, 3);           % tile 2x3 times
```

---

## 控制流程
```matlab
% if / elseif / else
if x > 0
    disp('positive');
elseif x < 0
    disp('negative');
else
    disp('zero');
end

% for loop
for i = 1:10
    fprintf('i = %d\n', i);
end

% Nested loops
for i = 1:3
    for j = 1:3
        fprintf('(%d,%d) ', i, j);
    end
    fprintf('\n');
end

% while loop
while err > tol
    x = update(x);
    err = compute_error(x);
end

% switch
switch status
    case 'active'
        disp('Active');
    case 'pending'
        disp('Pending');
    otherwise
        disp('Unknown');
end

% Break and continue
for i = 1:100
    if mod(i, 2) == 0; continue; end
    if i > 50; break; end
    disp(i);
end
```

---

## 函數
```matlab
% Function definition (in file myFunc.m)
function result = myFunc(x, y)
    % MYFUNC Computes x + y
    result = x + y;
end

% Multiple outputs
function [mag, phase] = complex_analysis(z)
    mag = abs(z);
    phase = angle(z);
end

% Anonymous function
square = @(x) x.^2;
add = @(x, y) x + y;

% Function handles
f = @sin;
f(pi/2)                          % 1

% Apply function to array
result = arrayfun(@(x) x^2, 1:10);

% Cell array of function handles
funcs = {@sin, @cos, @tan};
for i = 1:length(funcs)
    fprintf('f(pi/4) = %f\n', funcs{i}(pi/4));
end
```

---

## 繪圖
```matlab
% Basic plot
x = linspace(0, 2*pi, 100);
figure;
plot(x, sin(x), 'b-', 'LineWidth', 2);
hold on;
plot(x, cos(x), 'r--', 'LineWidth', 2);
xlabel('x (radians)');
ylabel('y');
title('Trigonometric Functions');
legend('sin(x)', 'cos(x)', 'Location', 'best');
grid on;

% Subplots
figure;
subplot(2, 2, 1); plot(x, sin(x)); title('Sine');
subplot(2, 2, 2); plot(x, cos(x)); title('Cosine');
subplot(2, 2, 3); plot(x, tan(x)); title('Tangent');
subplot(2, 2, 4); polarplot(x, sin(2*x)); title('Polar');

% 3D plot
[X, Y] = meshgrid(-5:0.5:5, -5:0.5:5);
Z = sin(sqrt(X.^2 + Y.^2));
figure;
surf(X, Y, Z);
colormap('jet');
colorbar;

% Histogram
figure;
histogram(randn(10000, 1), 50);
title('Normal Distribution');

% Save figure
saveas(gcf, 'plot.png');
print(gcf, '-dpdf', 'plot.pdf');
```

---

## 資料輸入/輸出
```matlab
% Read CSV
data = readmatrix('data.csv');
T = readtable('data.csv');

% Write CSV
writetable(T, 'output.csv');
writematrix(A, 'output.csv');

% MAT files (native binary)
save('results.mat', 'x', 'y', 'model');
load('results.mat');

% Excel
T = readtable('data.xlsx', 'Sheet', 'Sheet1');
writetable(T, 'output.xlsx');

% Text files
fid = fopen('output.txt', 'w');
fprintf(fid, '%.4f\t%s\n', value, label);
fclose(fid);

% JSON (R2016b+)
json_str = jsonencode(struct('name', 'Alice', 'age', 30));
S = jsondecode(json_str);
```

---

＃＃ 概括
MATLAB 的語法是矩陣優先 — 每個變數都是數組，並且運算針對線性代數進行了最佳化。冒號運算子、邏輯索引和向量化運算消除了大多數數值任務的循環。繪圖系統以最少的程式碼產生出版品質的圖形。工具箱將 MATLAB 擴展到每個工程領域。儘管 Python 已經侵入了某些領域，但 MATLAB 仍然是工程計算、基於 Simulink 的建模和快速原型設計的標準。