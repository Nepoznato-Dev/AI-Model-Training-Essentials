---
# Metadatos
título: "MATLAB"
descripción: "Referencia completa para el lenguaje de programación MATLAB que cubre descripción general, compensaciones, fundamentos de sintaxis, ecosistema y cuándo usarlo".
categoría: "Codificación y tecnología"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [matlab, lenguaje-de-programación, sintaxis, ecosistema, codificación-y-tecnología]
nivel_dificultad: "avanzado"
requisitos previos: []
estimado_reading_time: "31 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
#MATLAB
MATLAB (Matrix Laboratory) es un entorno y lenguaje de programación interpretado de alto nivel diseñado para computación numérica, operaciones matriciales y aplicaciones científicas/de ingeniería. Desarrollado por MathWorks y lanzado por primera vez en 1984, MATLAB es la herramienta estándar en muchas disciplinas de ingeniería: ingeniería eléctrica, sistemas de control, procesamiento de señales, procesamiento de imágenes y comunicaciones.
MATLAB combina un potente lenguaje orientado a matrices con amplias cajas de herramientas (paquetes complementarios) y el entorno de simulación visual Simulink. Se utiliza ampliamente en el mundo académico y la industria para crear prototipos de algoritmos antes de implementarlos en el código de producción.
---

## Por qué es importante MATLAB
- **Operaciones matriciales**: El tipo de dato fundamental es la matriz. El álgebra lineal es natural y eficiente.
- **Ecosistema de caja de herramientas**: Cientos de cajas de herramientas especializadas para procesamiento de señales, sistemas de control, aprendizaje automático, comunicaciones y más.
- **Simulink**: Entorno visual de diagramas de bloques para modelar y simular sistemas dinámicos.
- **Estándar de la industria**: habilidad requerida en muchos roles de ingeniería: aeroespacial, automotriz, telecomunicaciones y defensa.
- **Creación rápida de prototipos**: desarrollo y prueba rápidos de algoritmos antes de implementarlos en C/C++ o sistemas integrados.
- **Educación**: la herramienta de enseñanza estándar para métodos numéricos, álgebra lineal y cursos de ingeniería.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Licencia comercial** | Caro (miles de dólares por asiento) | Utilice GNU Octave (alternativa gratuita compatible con MATLAB) para trabajos básicos |
| **No es un lenguaje de propósito general** | Pobre para desarrollo web, programación de sistemas o aplicaciones | Utilice Python, Go u otros lenguajes para tareas no numéricas |
| **Rendimiento** | Interpretado; más lento que los lenguajes compilados para bucles | Operaciones de vectorización; use MEX (extensiones C/Fortran) para código activo |
| **Implementación** | La implementación de aplicaciones MATLAB requiere MATLAB Runtime | Utilice MATLAB Compiler o reescriba en C/C++ para producción |
| **Control de versiones** |  Los archivos`.m`son de texto pero Simulink`.mdl`/`.slx`son binarios | Utilice las herramientas de comparación integradas de MATLAB |
---

## Fundamentos de sintaxis
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

## Sintaxis y patrones avanzados
### Manejar clases y programación orientada a objetos
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

### Sobrecarga del operador
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

### Funciones dinámicas y controladores de funciones
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

### Metaprogramación con inputname y varargin
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

## Concurrencia y paralelismo
### parfor (bucles For paralelos)
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

### spmd (programa único, datos múltiples)
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

### gpuArray (Computación GPU)
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto MATLAB
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

### Archivo de proyecto MATLAB (.prj)
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

### Gestión de dependencias
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

### CI/CD con MATLAB CI/CD
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

## Pruebas
### Marco de pruebas unitarias de MATLAB
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

## Interoperabilidad
### Integración C/C++ (MEX)
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

## Patrones de diseño
### Patrón 1: Vectorización sobre bucles
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

### Patrón 2: Preasignación
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

### Patrón 3: Patrón de estructura de configuración
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Generación de código y JIT
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

### Evaluación comparativa
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

## Implementación
### Compilador MATLAB
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

### Servidor de producción MATLAB
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

### Implementación de contenedores
```dockerfile
FROM mathworks/matlab-runtime:R2024a
COPY myapp.ctf /app/
COPY run_app.sh /app/
RUN chmod +x /app/run_app.sh
ENTRYPOINT ["/app/run_app.sh"]
```

---

## Cuándo utilizar MATLAB
| Escenario | Por qué MATLAB | Mejor alternativa |
|----------|-----------|-------------------|
| Prototipos de ingeniería | Estándar de la industria; Integración con Simulink | Python (NumPy/SciPy) para contextos que no son de ingeniería |
| Procesamiento de señales/imágenes | Amplias cajas de herramientas | Python (scipy.signal, OpenCV) |
| Diseño de sistemas de control | Simulink es inigualable | — |
| Álgebra lineal | Sintaxis de matriz natural | Python (NumPy), Julia |
| Investigación académica | Estándar en muchos campos de la ingeniería | Pitón, R |
| Sistemas de producción | No diseñado para implementación | C++, Python, Ir |
| Desarrollo web | No adecuado | JavaScript, Pitón |
| Ciencia de datos (general) | Posible pero Python es más versátil | Pitón, R |
---

## Resumen
MATLAB es la herramienta estándar para computación de ingeniería y creación de prototipos científicos. Su lenguaje orientado a matrices, sus amplias cajas de herramientas y su entorno Simulink lo hacen indispensable en muchas disciplinas de ingeniería. Si bien Python ha invadido parte del territorio de MATLAB (especialmente en ciencia de datos), MATLAB sigue siendo la herramienta preferida para sistemas de control, procesamiento de señales y educación en ingeniería. Para la implementación en producción, el código normalmente se traduce de MATLAB a C/C++ o Python.
---

## Computación matricial y numérica avanzada
### Matrices dispersas
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

### Integración numérica y EDO
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

### Procesamiento de señales
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

### Procesamiento de imágenes
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
