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

# MATLAB — مرجع بناء الجملة
توفر هذه الوثيقة مرجعًا شاملاً ومنظمًا لصيغة MATLAB (R2024+). وهو يكمل مرجع MATLAB الرئيسي من خلال التركيز على أنماط بناء الجملة الشاملة وعمليات المصفوفة والتخطيط ومصطلحات الحوسبة العلمية.
---

## العوامل والتعبيرات
### المشغلين الأساسيين
| المشغل | الاسم | مثال | ملاحظات |
|----------|------|--------|-------|
| `+``-``*``/``^`| حسابية | `A * B`| ضرب المصفوفة |
| `.*``./``.^`| العنصر الحكيم | `A .* B`| عملية المصفوفة |
| `'`| تبديل | `A'`| النقل المقترن |
| `.'`| تبديل غير مترافق | `A.'`| |
| `\`| الانقسام الأيسر | `A \ b`| حل الفأس = ب |
| `/`| القسمة اليمنى | `b / A`| حل xA = b |
| `==``~=` | المساواة | `A == B`| العنصر الحكيم |
| `<``>``<=``>=` | مقارنة | `A > 0`| العنصر الحكيم |
| `&``\|``~`| منطقي (عنصري) | `A & B`| |
| `&&``\|\|` | ماس كهربائى | `a && b`| العددية فقط |
| `:`| القولون/النطاق | `1:10`| `start:step:stop`|
| `;`| فاصل الصف / قمع | `[1; 2; 3]`| |
| `,`| فاصل العمود | `[1, 2, 3]`| |
---

## عمليات المصفوفة
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

## التحكم في التدفق
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

## الوظائف
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

## التآمر
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

## إدخال/إخراج البيانات
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

## ملخص
بناء جملة MATLAB هو المصفوفة أولاً — كل متغير عبارة عن مصفوفة، ويتم تحسين العمليات للجبر الخطي. يقوم عامل النقطتين والفهرسة المنطقية والعمليات الموجهة بإزالة الحلقات لمعظم المهام الرقمية. ينتج نظام الرسم أرقامًا بجودة النشر مع الحد الأدنى من التعليمات البرمجية. تعمل صناديق الأدوات على توسيع MATLAB إلى كل مجال هندسي. في حين أن بايثون تعدت على بعض المناطق، يظل MATLAB هو المعيار للحسابات الهندسية والنمذجة المستندة إلى Simulink والنماذج الأولية السريعة.