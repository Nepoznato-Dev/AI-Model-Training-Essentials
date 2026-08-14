---
# Metadata
title: "MATLAB — Syntax Reference"
description: "Detailed syntax reference for MATLAB covering matrix operations, plotting, Simulink, toolboxes, and scientific computing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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
# MATLAB — 構文リファレンス
このドキュメントは、MATLAB (R2024+) の包括的で構造化された構文リファレンスを提供します。網羅的な構文パターン、行列演算、プロット、科学技術計算のイディオムに焦点を当て、主要な MATLAB リファレンスを補完します。
---

## 演算子と式
### コアオペレーター
|オペレーター |名前 |例 |メモ |
|----------|------|----------|----------|
| `+``-``*``/``^`|算数 | `A * B`|行列の乗算 |
| `.*``./``.^`|要素ごと | `A .* B`|配列演算 |
| `'`|移調 | `A'`|共役転置 |
| `.'`|非共役転置 | `A.'`| |
| `\`|左除算 | `A \ b`| Ax = b | を解く
| `/`|右除算 | `b / A`| xA = b | を解きます。
| `==`|`~=`|平等 | `A == B`|要素ごと |
| `<``>``<=``>=` |比較 | `A > 0`|要素ごと |
| `&``\|``~`|論理 (要素ごと) | `A & B`| |
| `&&`|`\|\|`|短絡 | `a && b`|スカラーのみ |
| `:`|コロン/範囲 | `1:10`| `start:step:stop`|
| `;`|行区切り文字 / 抑制 | `[1; 2; 3]`| |
| `,`|列区切り文字 | `[1, 2, 3]`| |
---

## 行列演算
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

## 制御フロー
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

## 関数
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

## プロット
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

## データ入出力
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

＃＃ まとめ
MATLAB の構文は行列優先です。すべての変数は配列であり、演算は線形代数用に最適化されています。コロン演算子、論理インデックス付け、およびベクトル化された演算により、ほとんどの数値タスクのループが排除されます。プロット システムは、最小限のコードで出版品質の図を生成します。ツールボックスは、MATLAB をあらゆるエンジニアリング ドメインに拡張します。 Python がある程度の領域に侵入している一方で、MATLAB は依然としてエンジニアリング計算、Simulink ベースのモデリング、およびラピッド プロトタイピングの標準です。