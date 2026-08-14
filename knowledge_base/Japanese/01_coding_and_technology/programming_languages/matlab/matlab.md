<!--
---
# Metadata
title: "MATLAB"
description: "Comprehensive reference for the MATLAB programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [matlab, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# MATLAB
MATLAB (Matrix Laboratory) は、数値計算、行列演算、工学/科学アプリケーション向けに設計された、高レベルの解釈型プログラミング言語および環境です。 MathWorks によって開発され、1984 年に初めてリリースされた MATLAB は、電気工学、制御システム、信号処理、画像処理、通信など、多くの工学分野における標準ツールです。
MATLAB は、強力な行列指向言語と、広範なツールボックス (アドオン パッケージ) および Simulink ビジュアル シミュレーション環境を組み合わせています。これは、実稼働コードに実装する前にアルゴリズムのプロトタイプを作成するために、学術界や産業界で広く使用されています。
---

## MATLAB が重要な理由
- **行列演算**: 基本的なデータ型は行列です。線形代数は自然で効率的です。
- **ツールボックス エコシステム**: 信号処理、制御システム、機械学習、通信などに特化した何百ものツールボックス。
- **Simulink**: 動的システムのモデリングとシミュレーションのための視覚的なブロック図環境。
- **業界標準**: 航空宇宙、自動車、電気通信、防衛など、多くのエンジニアリングの役割で必要なスキル。
- **迅速なプロトタイピング**: C/C++ または組み込みシステムに展開する前にアルゴリズムを迅速に開発およびテストします。
- **教育**: 数値的手法、線形代数、および工学コースのための標準的な教育ツール。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **商用ライセンス** |高価 (1 座席あたり数千ドル) |基本的な作業には GNU Octave (MATLAB と互換性のある無料の代替品) を使用してください。
| **汎用言語ではありません** | Web 開発、システム プログラミング、またはアプリケーションが苦手 |数値以外のタスクには Python、Go、またはその他の言語を使用する |
| **パフォーマンス** |解釈済み。ループのコンパイル言語よりも遅い |操作をベクトル化します。ホット コードには MEX (C/Fortran 拡張機能) を使用します。
| **展開** | MATLAB アプリケーションを配置するには、MATLAB Runtime が必要です。 MATLAB Compiler を使用するか、実稼働用に C/C++ で書き直す |
| **バージョン管理** | `.m`ファイルはテキストですが、Simulink`.mdl`/`.slx`はバイナリです。 MATLAB の組み込み比較ツールを使用する |
---

## 構文の基礎
```matlab
% Variables (no type declarations needed)
name = 'Alice';
age = 30;
scores = [9.5, 8.0, 7.5, 9.0];

% Matrices (the core data type)
A = [1, 2, 3; 4, 5, 6; 7, 8, 9];   % 3x3 matrix
B = magic(3);                        % 3x3 magic square
C = rand(4, 4);                      % 4x4 random matrix

% Matrix operations
D = A * B';          % Matrix multiplication
eigenvalues = eig(A); % Eigenvalues
inv_A = inv(A);       % Matrix inverse

% Plotting
x = linspace(0, 2*pi, 100);
y = sin(x);
plot(x, y, 'b-', 'LineWidth', 2);
xlabel('x'); ylabel('sin(x)');
title('Sine Wave');
grid on;

% Functions
function result = fibonacci(n)
    if n <= 1
        result = n;
    else
        result = fibonacci(n-1) + fibonacci(n-2);
    end
end

% Loops and conditionals
for i = 1:10
    if mod(i, 2) == 0
        fprintf('%d is even\n', i);
    end
end

% Vectorised operations (preferred — much faster than loops)
x = 1:1000;
y = x.^2 + 2.*x + 1;   % Element-wise operations
mean_y = mean(y);
```

---

## 高度な構文とパターン
### ハンドルクラスとオブジェクト指向プログラミング
```matlab
% classdef file: Point.m
classdef Point < handle
    properties
        X (1,1) double
        Y (1,1) double
    end
    methods
        function obj = Point(x, y)
            obj.X = x;
            obj.Y = y;
        end
        function d = distanceTo(obj, other)
            d = sqrt((obj.X - other.X)^2 + (obj.Y - other.Y)^2);
        end
    end
end

% Value class (immutable semantics)
classdef Color
    properties (SetAccess = immutable)
        R, G, B
    end
    methods
        function obj = Color(r, g, b)
            obj.R = r; obj.G = g; obj.B = b;
        end
    end
end

% Abstract classes and interfaces
classdef Shape
    methods (Abstract)
        a = area(obj);
        p = perimeter(obj);
    end
end

classdef Circle < Shape
    properties
        Radius
    end
    methods
        function obj = Circle(r)
            obj.Radius = r;
        end
        function a = area(obj)
            a = pi * obj.Radius^2;
        end
        function p = perimeter(obj)
            p = 2 * pi * obj.Radius;
        end
    end
end
```

### 演算子のオーバーロード
```matlab
classdef Vector2D
    properties
        x, y
    end
    methods
        function obj = Vector2D(x, y)
            obj.x = x; obj.y = y;
        end
        function result = plus(a, b)
            result = Vector2D(a.x + b.x, a.y + b.y);
        end
        function result = mtimes(a, b)
            if isa(a, 'numeric')
                result = Vector2D(a * b.x, a * b.y);
            else
                result = a.x * b.x + a.y * b.y; % dot product
            end
        end
        function disp(obj)
            fprintf('Vector2D(%.2f, %.2f)\n', obj.x, obj.y);
        end
    end
end

v1 = Vector2D(1, 2); v2 = Vector2D(3, 4);
v3 = v1 + v2;       % Vector2D(4, 6)
d = v1 * v2;        % 11 (dot product)
```

### 動的関数と関数ハンドル
```matlab
% Anonymous functions
square = @(x) x.^2;
result = square(5);  % 25

% Function handles for callbacks
f = @sin;
x = f(pi/2);  % 1

% Cell array of function handles
funcs = {@sin, @cos, @tan};
for i = 1:length(funcs)
    fprintf('f(%d) = %f\n', i, funcs{i}(pi/4));
end

% Dynamic field access
s = struct('name', 'Alice', 'age', 30);
field_name = 'name';
value = s.(field_name);  % 'Alice'

% eval and feval (use sparingly)
result = feval(@mean, [1, 2, 3, 4, 5]);
```

### inputname と varargin を使用したメタプログラミング
```matlab
function printvar(var)
    % Prints variable name and value
    name = inputname(1);
    fprintf('%s = %s\n', name, mat2str(var));
end

x = 42;
printvar(x)  % x = 42

% Variable-length arguments
function result = compute(op, varargin)
    switch op
        case 'sum'
            result = sum([varargin{:}]);
        case 'max'
            result = max([varargin{:}]);
    end
end
```

---

## 同時実行性と並列処理
### parfor (並列 For ループ)
```matlab
% Parallel for-loop (requires Parallel Computing Toolbox)
parfor i = 1:1000
    result(i) = sqrt(i) * sin(i);
end

% parfor with sliced variables
data = rand(1000, 100);
means = zeros(1000, 1);
parfor i = 1:1000
    means(i) = mean(data(i, :));
end

% Nested parfor (use sparingly)
parfor i = 1:100
    for j = 1:1000  % inner loop is sequential
        A(i,j) = i + j;
    end
end
```

### spmd (単一プログラム、複数データ)
```matlab
% Open parallel pool
pool = parpool('local', 4);

spmd
    % Each worker has its own labindex
    local_data = rand(100, 1) + labindex;

    % Communication between workers
    % Send data from worker 1 to worker 2
    if labindex == 1
        dataToSend = rand(10, 1);
        labSend(dataToSend, 2);
    elseif labindex == 2
        received = labReceive(1);
    end

    % Gather all results to client
    all_data = gcat(local_data);
end

delete(pool)
```

### gpuArray (GPU コンピューティング)
```matlab
% Transfer data to GPU
A_gpu = gpuArray(A);
B_gpu = gpuArray(B);

% Computations happen on GPU automatically
C_gpu = A_gpu * B_gpu;
D_gpu = sin(A_gpu) + cos(B_gpu);

% Bring result back to CPU
C = gather(C_gpu);

% GPU-specific functions
[~, ~, V] = svd(gpuArray(rand(1000)));
result = pagefun('mtimes', gpuArray(A), gpuArray(B));

% Check GPU info
gpuDevice(1)  % Select and display GPU
```

---

## プロジェクトの構成とシステムの構築
### MATLAB プロジェクトの構造
```
MyProject/
+-- MyProject.prj          # Project file
+-- src/
|   +-- main.m
|   +-- +myPackage/        # Package namespace
|   |   +-- utils.m
|   |   +-- solver.m
|   +-- classes/
|   |   +-- Point.m
|   |   +-- Shape.m
+-- tests/
|   +-- test_solver.m
|   +-- test_utils.m
+-- docs/
|   +-- html/
+-- resources/
|   +-- config.mat
+-- .gitignore
```

### MATLAB プロジェクト ファイル (.prj)
```matlab
% Create project programmatically
proj = matlab.project.createProject('MyProject');
addFolder(proj, 'src');
addFolder(proj, 'tests');

% Set project path
addPath(proj, 'src');

% Define project shortcuts
addShortcut(proj, 'docs', 'docs/html');

% Add file labels (classification)
file = addFile(proj, 'src/main.m');
addLabel(file, 'Classification', 'Design');
```

### 依存関係の管理
```matlab
% Check toolbox availability
ver                          % List all installed toolboxes
license('test', 'optim_tool') % Check specific toolbox

% Add-ons (MATLAB File Exchange)
% Install from Add-On Explorer or:
matlab.addons.install('PackageName')

% Path management
addpath('src/utils');
addpath(genpath('src'));  % Add all subdirectories
savepath;                  % Save for future sessions
```

### MATLAB CI/CD を使用した CI/CD
```yaml
# .github/workflows/matlab.yml
name: MATLAB Build
on:
  push: {branches: [main]}
  pull_request: {branches: [main]}
jobs:
  matlab:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: matlab-actions/setup-matlab@v2
      - uses: matlab-actions/run-command@v2
        with: {command: runtests}
      - uses: matlab-actions/run-build@v2
```

---

## テスト
### MATLAB 単体テスト フレームワーク
```matlab
% File: test_solver.m
classdef test_solver < matlab.unittest.TestCase
    properties
        solver
    end

    methods (TestMethodSetup)
        function setupOnce(tc)
            tc.solver = MySolver();
        end
    end

    methods (Test)
        function test_basic_solve(tc)
            result = tc.solver.solve([1 2; 3 4], [5; 6]);
            tc.verifyEqual(size(result), [2, 1]);
            tc.verifyFalse(any(isnan(result)));
        end

        function test_identity_matrix(tc)
            I = eye(3);
            b = [1; 2; 3];
            x = tc.solver.solve(I, b);
            tc.verifyEqual(x, b, 'AbsTol', 1e-10);
        end

        function test_singular_matrix_errors(tc)
            A = [1 2; 2 4];  % Singular
            b = [1; 2];
            tc.verifyError(@() tc.solver.solve(A, b), ...
                'MATLAB:singularMatrix');
        end
    end
end

% Run tests
results = runtests('tests/');
disp(results);
% Or from command line:
% matlab -batch "results = runtests; assertSuccess(results)"
```

---

## 相互運用性
### C/C++ 統合 (MEX)
```matlab
% MEX file: dot_product.c
% Compile: mex dot_product.c

% C source (dot_product.c):
% #include "mex.h"
% void mexFunction(int nlhs, mxArray *plhs[],
%                  int nrhs, const mxArray *prhs[]) {
%     double *a = mxGetPr(prhs[0]);
%     double *b = mxGetPr(prhs[1]);
%     int n = mxGetNumberOfElements(prhs[0]);
%     plhs[0] = mxCreateDoubleScalar(0.0);
%     double *result = mxGetPr(plhs[0]);
%     for (int i = 0; i < n; i++)
%         *result += a[i] * b[i];
% }

% Call from MATLAB (same as any function after mex compile):
result = dot_product([1,2,3], [4,5,6]);  % 32

% Calling Python from MATLAB
pyenv  % Configure Python interpreter
np = py.importlib.import_module('numpy');
arr = np.array({1, 2, 3, 4, 5});
result = double(py.numpy.mean(arr));

% Call .NET assemblies (Windows)
NET.addAssembly('System.Windows.Forms');
msgbox = System.Windows.Forms.MessageBox;
msgbox.Show('Hello from .NET!');
```

---

## デザインパターン
### パターン 1: ループ上のベクトル化
```matlab
% BAD — loop-based
n = 1000000;
result = zeros(n, 1);
for i = 1:n
    result(i) = sin(i) * cos(i) + i^2;
end

% GOOD — vectorised (100x faster)
i = (1:1000000)';
result = sin(i) .* cos(i) + i.^2;
```

### パターン 2: 事前割り当て
```matlab
% BAD — growing array in loop
result = [];
for i = 1:10000
    result = [result, i^2];  % Copies entire array each iteration!
end

% GOOD — preallocate
result = zeros(1, 10000);
for i = 1:10000
    result(i) = i^2;
end
```

### パターン 3: 構成構造体パターン
```matlab
function result = simulate(data, options)
    % Set defaults
    defaults = struct('maxIter', 100, 'tol', 1e-6, ...
                      'verbose', false, 'method', 'newton');
    options = fillmissing(options, defaults);

    for iter = 1:options.maxIter
        residual = compute_residual(data);
        if options.verbose
            fprintf('Iter %d: residual = %e\n', iter, residual);
        end
        if residual < options.tol, break; end
    end
end

function opts = fillmissing(opts, defaults)
    fields = fieldnames(defaults);
    for i = 1:length(fields)
        if ~isfield(opts, fields{i})
            opts.(fields{i}) = defaults.(fields{i});
        end
    end
end
```

---

## パフォーマンスと最適化
### プロファイリングツール
```matlab
% Profile entire session
profile on
my_computation();
profile off
profile viewer  % Opens interactive profile report

% Profile specific code section
profile clear
profile on
A = rand(1000);
B = inv(A);
C = A * B;
profile off
stats = profile('info');
for i = 1:length(stats.Functions)
    fprintf('%s: %.3f s\n', stats.Functions(i).Name, ...
        stats.Functions(i).TotalTime);
end

% Line-by-line profiling
profile -memory on
my_function();
profile off
```

### コード生成と JIT
```matlab
% MATLAB's JIT accelerator (automatic since R2013a)
% Tips for JIT-friendly code:
% 1. Preallocate arrays
% 2. Use functions (not scripts) for JIT optimisation
% 3. Avoid changing variable types within a function
% 4. Use typed arguments in functions

% MATLAB Coder — generate C/C++ from MATLAB
% codegen my_function -args {zeros(3,3)}
% Generates standalone C code

% GPU acceleration
A = gpuArray(rand(5000));
tic; B = A * A; toc  % Runs on GPU
B_cpu = gather(B);   % Transfer back
```

### ベンチマーク
```matlab
% timeit (accurate timing)
f = @() my_algorithm(data);
t = timeit(f);  % Runs multiple times, reports median
fprintf('Elapsed: %.4f seconds\n', t);

% Compare approaches
t1 = timeit(@() loop_approach(n));
t2 = timeit(@() vectorized_approach(n));
fprintf('Speedup: %.1fx\n', t1/t2);
```

---

## デプロイメント
### MATLAB コンパイラ
```matlab
% Compile to standalone executable
% mcc -m main.m -a src/

% Compile to shared library
% mcc -W lib:mylib -T link:lib mylib_functions.m

% Compile to CTF (Component Technology File)
% mcc -W main:myapp -d deploy/ main.m

% Deploy with MATLAB Runtime (free, no license needed)
% Distribute: myapp + MATLAB Runtime installer
```

### MATLAB 実稼働サーバー
```matlab
% Deploy as REST API
% 1. Create CTF archive
% 2. Deploy to MATLAB Production Server
% 3. Access via HTTP

% Client-side HTTP call
import matlab.net.*
import matlab.net.http.*
client = HTTPClient;
req = RequestMessage('set', 'Body', ...
    structuredarray(input_data));
resp = client.send('http://server:9910/myapp', req);
```

### コンテナのデプロイメント
```dockerfile
FROM mathworks/matlab-runtime:R2024a
COPY myapp.ctf /app/
COPY run_app.sh /app/
RUN chmod +x /app/run_app.sh
ENTRYPOINT ["/app/run_app.sh"]
```

---

## MATLAB を使用する場合
|シナリオ | MATLAB を選ぶ理由 |より良い代替案 |
|----------|-----------|--------|
|エンジニアリングプロトタイピング |業界標準。 Simulink の統合 |非エンジニアリングコンテキスト用の Python (NumPy/SciPy) |
|信号・画像処理 |豊富なツールボックス | Python (scipy.signal、OpenCV) |
|制御システム設計 | Simulink は比類のないものです。 — |
|線形代数 |自然行列構文 | Python (NumPy)、ジュリア |
|学術研究 |多くのエンジニアリング分野の標準 |パイソン、R |
|生産システム |導入用に設計されていません | C++、Python、Go |
|ウェブ開発 |適さない | JavaScript、Python |
|データサイエンス（一般） |可能ですが、Python の方が多用途です。パイソン、R |
---

## 総合的な Q&A
### Q1: ループを使用する代わりに演算をベクトル化するにはどうすればよいですか?
**A:** MATLAB は行列演算用に最適化されています。ループをベクトル化されたコードに置き換えます。
```matlab
% Slow — loop
result = zeros(1, n);
for i = 1:n
    result(i) = sin(i) * cos(i);
end

% Fast — vectorized
i = 1:n;
result = sin(i) .* cos(i);

% Element-wise operations use .
a = [1 2 3]; b = [4 5 6];
c = a .* b;   % [4 10 18]
c = a .^ 2;   % [1 4 9]
c = a ./ b;   % [0.25 0.4 0.5]
```

### Q2: 行列と配列の違いは何ですか?
**A:** MATLAB では、すべてが配列です。行列は 2D 配列です。
```matlab
% Matrix (2D array)
A = [1 2 3; 4 5 6; 7 8 9];  % 3x3 matrix

% Array operations
size(A)      % [3, 3]
A'           % transpose
inv(A)       % inverse
A * B        % matrix multiplication
A .* B       % element-wise multiplication

% Cell array — mixed types
c = {1, 'hello', [1 2 3]};

% Struct array
s.name = 'Alice';
s.age = 30;

% Table — labeled columns (modern approach)
T = table(['Alice'; 'Bob  '], [30; 25], 'VariableNames', {'Name','Age'});
```

### Q3: MATLAB で効果的なプロットを作成するにはどうすればよいですか?
**A:** 適切なラベルを付けてプロット関数を使用してください。
```matlab
x = linspace(0, 2*pi, 100);
y1 = sin(x); y2 = cos(x);

figure;
plot(x, y1, 'b-', 'LineWidth', 2); hold on;
plot(x, y2, 'r--', 'LineWidth', 2);
xlabel('x (radians)'); ylabel('y');
title('Trigonometric Functions');
legend('sin(x)', 'cos(x)');
grid on;

% Subplots
subplot(2, 1, 1); plot(x, y1); title('Sine');
subplot(2, 1, 2); plot(x, y2); title('Cosine');
```

### Q4: MATLAB コードを効果的にデバッグするにはどうすればよいですか?
**A:** 組み込みのデバッガーと診断ツールを使用します。
```matlab
% Set breakpoints
dbstop in myFunction at 42   % line 42
dbstop if error              % break on any error

% During debugging
dbstep        % step one line
dbcont        % continue
dbquit        % exit debug mode
whos          % list workspace variables
disp(x)       % display variable value

% Performance profiling
profile on
myFunction()
profile viewer

% Check code quality
checkcode('myFunction.m')  % lint-like suggestions
```

### Q5: データ ファイルを読み書きするにはどうすればよいですか?
**A:** MATLAB は多くのファイル形式をサポートしています。
```matlab
% CSV
data = readmatrix('data.csv');
T = readtable('data.csv');
writetable(T, 'output.csv');

% Excel
T = readtable('data.xlsx', 'Sheet', 'Sheet1');

% MAT files (native binary)
save('results.mat', 'variable1', 'variable2');
load('results.mat');

% Text with format control
fid = fopen('output.txt', 'w');
fprintf(fid, '%.4f\t%s\n', value, label);
fclose(fid);
```

---

## 思考連鎖による問題解決
### 問題 1: 連立一次方程式を解く
**ステップ 1: 問題を理解する**
Ax = b を解きます。ここで、A は行列、b はベクトルです。
**ステップ 2: アプローチを特定する**
最適なアルゴリズムを自動的に選択する MATLAB のバックスラッシュ演算子`\`を使用します。
**ステップ 3: 実装**```matlab
A = [3 2 -1; 2 -2 4; -1 0.5 -1];
b = [1; -2; 0];

% Best approach — backslash
x = A \ b;

% Verify
residual = norm(A * x - b);  % should be ~0
fprintf('Solution: x = [%.4f, %.4f, %.4f]\n', x);
fprintf('Residual: %.2e\n', residual);
```

**ステップ 4: 延長**
過剰決定システムの場合、`\` は最小二乗解を与えます。スパース システムの場合は、`sparse` 行列を使用します。
### 問題 2: 信号処理 — FFT 解析
**ステップ 1: 問題を理解する**
ノイズを含む信号の周波数成分を分析します。
**ステップ 2: アプローチを特定する**
テスト信号を生成し、FFT を適用して、周波数スペクトルをプロットします。
**ステップ 3: 実装**```matlab
% Generate signal: 50 Hz + 120 Hz + noise
fs = 1000;                    % sampling frequency
t = 0:1/fs:1-1/fs;            % time vector
signal = sin(2*pi*50*t) + 0.5*sin(2*pi*120*t) + 0.3*randn(size(t));

% FFT
N = length(signal);
Y = fft(signal);
P2 = abs(Y/N);
P1 = P2(1:N/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = fs*(0:(N/2))/N;

% Plot
figure;
plot(f, P1, 'LineWidth', 1.5);
xlabel('Frequency (Hz)'); ylabel('Amplitude');
title('Single-Sided FFT');
xlim([0 200]);
```

**ステップ 4: 確認**
ピークは 50 Hz と 120 Hz に現れるはずです。ノイズフロアは低くなければなりません。
### 問題 3: カスタム モデルでの曲線フィッティング
**ステップ 1: 問題を理解する**
実験データをカスタム非線形モデルに適合させます。
**ステップ 2: アプローチを特定する**
`fit` をカスタム`fittype`または`lsqcurvefit`とともに使用します。
**ステップ 3: 実装**```matlab
% Data
x = (0:0.1:5)';
y = 3 * exp(-0.5 * x) + 0.2 * randn(size(x));

% Define model
ft = fittype('a * exp(-b * x)', 'independent', 'x');
opts = fitoptions('Method', 'NonlinearLeastSquares', ...
                  'StartPoint', [1, 1]);

% Fit
[fitted, gof] = fit(x, y, ft, opts);

% Display results
fprintf('a = %.4f, b = %.4f\n', fitted.a, fitted.b);
fprintf('R² = %.4f\n', gof.rsquare);

% Plot
figure;
plot(fitted, x, y);
xlabel('x'); ylabel('y');
legend('Data', 'Fit');
```

**ステップ 4: 検証**
パターンの残差を確認し、R² を検証し、異なる開始点でテストします。
---

＃＃ まとめ
MATLAB は、工学計算と科学プロトタイピングのための標準ツールです。行列指向言語、豊富なツールボックス、Simulink 環境により、多くのエンジニアリング分野で不可欠なものとなっています。 Python は MATLAB の領域 (特にデータ サイエンス) の一部に侵入していますが、MATLAB は依然として制御システム、信号処理、および工学教育において推奨されるツールです。運用環境での展開では、コードは通常、MATLAB から C/C++ または Python に変換されます。
---

## 高度な行列と数値計算
### スパース行列
```matlab
% Create sparse matrix
A = sparse([1,1,2,2,3,3], [1,2,2,3,1,3], [10,2,20,3,30,4], 3, 3);
full(A)  % Convert to full

% Sparse operations
B = speye(1000);  % Sparse identity
C = sprand(1000, 1000, 0.01);  % 1% density random

% Solve sparse system (much faster than full)
x = A \ b;  % Automatically detects sparsity

% Sparse matrix info
nnz(A)       % Number of non-zeros
spy(A)       % Visualize sparsity pattern
whos A       % Memory comparison
```

### 数値積分と ODE
```matlab
% Numerical integration
result = integral(@(x) sin(x).^2, 0, pi);

% Double integral
result2 = integral2(@(x,y) x.^2 + y.^2, 0, 1, 0, 1);

% ODE solving
% dy/dt = -2*y + sin(t), y(0) = 1
ode_fun = @(t, y) -2*y + sin(t);
[t, y] = ode45(ode_fun, [0 10], 1);
plot(t, y);

% System of ODEs (Lorenz attractor)
lorenz = @(t, y) [
    10*(y(2) - y(1));
    y(1)*(28 - y(3)) - y(2);
    y(1)*y(2) - (8/3)*y(3)
];
[t, y] = ode45(lorenz, [0 50], [1; 1; 1]);
plot3(y(:,1), y(:,2), y(:,3));

% Stiff ODE solver
[t, y] = ode15s(ode_fun, [0 100], 1);
```

### 信号処理
```matlab
% FFT analysis
fs = 1000;  % Sampling frequency
t = 0:1/fs:1-1/fs;
signal = sin(2*pi*50*t) + 0.5*sin(2*pi*120*t) + randn(size(t));

% Frequency domain
Y = fft(signal);
f = fs/2 * linspace(0, 1, length(Y)/2+1);
plot(f, abs(Y(1:length(Y)/2+1))/length(t));

% Filter design
[b, a] = butter(6, 100/(fs/2), 'low');  % 6th order lowpass at 100Hz
filtered = filter(b, a, signal);

% Spectrogram
spectrogram(signal, 256, 200, 256, fs, 'yaxis');
```

### 画像処理
```matlab
% Read and display image
img = imread('photo.jpg');
imshow(img);

% Convert to grayscale
gray = rgb2gray(img);

% Edge detection
edges = edge(gray, 'canny');

% Morphological operations
se = strel('disk', 5);
opened = imopen(edges, se);

% Histogram equalization
enhanced = histeq(gray);

% Fourier transform of image
F = fft2(double(gray));
F_shifted = fftshift(F);
magnitude = log(1 + abs(F_shifted));
imshow(magnitude, []);
```
