<!--
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

-->
# ম্যাটল্যাব - সিনট্যাক্স রেফারেন্স
এই নথিটি MATLAB (R2024+) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, ম্যাট্রিক্স অপারেশন, প্লটিং, এবং বৈজ্ঞানিক কম্পিউটিং ইডিয়মগুলিতে ফোকাস করে মূল ম্যাটল্যাব রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``^`| পাটিগণিত | `A * B`| ম্যাট্রিক্স গুন |
| `.*``./``.^`| উপাদান-ভিত্তিক | `A .* B`| অ্যারে অপারেশন |
| `'`| স্থানান্তর | `A'`| কনজুগেট ট্রান্সপোজ |
| `.'`| নন-কনজুগেট ট্রান্সপোজ | `A.'`| |
| `\`| বাম বিভাজন | `A \ b`| Ax = b | সমাধান করুন
| `/`| ডান ভাগ | `b / A`| xA = b | সমাধান করুন
| `==``~=` | সমতা | `A == B`| উপাদান-ভিত্তিক |
| `<``>``<=``>=` | তুলনা | `A > 0`| উপাদান-ভিত্তিক |
| `&``\|``~`| যৌক্তিক (উপাদান-ভিত্তিক) | `A & B`| |
| `&&``\|\|` | শর্ট সার্কিট | `a && b`| শুধুমাত্র স্কেলার |
| `:`| কোলন/পরিসীমা | `1:10`| `start:step:stop`|
| `;`| সারি বিভাজক / দমন | `[1; 2; 3]`| |
| `,`| কলাম বিভাজক | `[1, 2, 3]`| |
---

## ম্যাট্রিক্স অপারেশন
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

## নিয়ন্ত্রণ প্রবাহ
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

## ফাংশন
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

## চক্রান্ত
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

## ডেটা I/O
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

## সারাংশ
MATLAB-এর সিনট্যাক্স হল ম্যাট্রিক্স-প্রথম — প্রতিটি ভেরিয়েবল একটি অ্যারে, এবং অপারেশনগুলি রৈখিক বীজগণিতের জন্য অপ্টিমাইজ করা হয়। কোলন অপারেটর, লজিক্যাল ইনডেক্সিং এবং ভেক্টরাইজড অপারেশনগুলি বেশিরভাগ সংখ্যাসূচক কাজের জন্য লুপগুলিকে সরিয়ে দেয়। প্লটিং সিস্টেম ন্যূনতম কোড সহ প্রকাশনা-মানের পরিসংখ্যান তৈরি করে। টুলবক্স প্রতিটি ইঞ্জিনিয়ারিং ডোমেনে MATLAB প্রসারিত করে। যদিও পাইথন কিছু অঞ্চল দখল করেছে, MATLAB ইঞ্জিনিয়ারিং কম্পিউটেশন, সিমুলিংক-ভিত্তিক মডেলিং এবং দ্রুত প্রোটোটাইপিংয়ের জন্য মান হিসাবে রয়ে গেছে।