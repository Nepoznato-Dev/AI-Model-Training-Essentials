---
# Metadata
title: "Fortran"
description: "Comprehensive reference for the Fortran programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [fortran, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "32 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# फोरट्रान
फोरट्रान (फॉर्मूला ट्रांसलेशन) सबसे पुरानी उच्च स्तरीय प्रोग्रामिंग भाषा है जो अभी भी व्यापक रूप से उपयोग में है, इसे पहली बार वैज्ञानिक और इंजीनियरिंग गणना के लिए 1957 में आईबीएम द्वारा विकसित किया गया था। अपनी उम्र के बावजूद, आधुनिक फोरट्रान (फोरट्रान 2008/2018/2023) एक सक्षम, उच्च-प्रदर्शन वाली भाषा है जिसका उपयोग संख्यात्मक मौसम भविष्यवाणी, कम्प्यूटेशनल तरल गतिशीलता, भौतिकी सिमुलेशन, वित्तीय मॉडलिंग और उच्च-प्रदर्शन कंप्यूटिंग (एचपीसी) में बड़े पैमाने पर किया जाता है। दुनिया के कई सबसे तेज़ सुपर कंप्यूटर फोरट्रान कोड चलाते हैं।
भाषा अपने शुरुआती दिनों से ही काफी विकसित हुई है। आधुनिक फोरट्रान में मॉड्यूल, व्युत्पन्न प्रकार, सामान्य प्रक्रियाएं, कोएरेज़ (समानांतर प्रोग्रामिंग), और सी के साथ इंटरऑपरेबिलिटी है। यह कई वैज्ञानिक कंप्यूटिंग अनुप्रयोगों के लिए पसंद की भाषा बनी हुई है जहां प्रदर्शन सर्वोपरि है।
---

## फोरट्रान क्यों मायने रखता है
- **एचपीसी प्रदर्शन**: फोरट्रान कंपाइलर उपलब्ध कुछ सबसे तेज़ संख्यात्मक कोड का उत्पादन करते हैं - अक्सर सरणी संचालन के लिए सी/सी++ से मेल खाते हैं या उससे अधिक होते हैं।
- **विरासत कोडबेस**: दशकों के वैज्ञानिक कोड (जलवायु मॉडल, भौतिकी सिमुलेशन) फोरट्रान में लिखे गए हैं।
- **सरणी संचालन**: गणितीय गणना के लिए डिज़ाइन किए गए सिंटैक्स के साथ मूल बहु-आयामी सरणी समर्थन।
- **संख्यात्मक स्थिरता**: भाषा और कंपाइलर फ़्लोटिंग-पॉइंट गणना के लिए अनुकूलित हैं।
- **Coarrays**: अंतर्निहित समानांतर प्रोग्रामिंग समर्थन (फोरट्रान 2008+)।
- **अभी भी विकसित हो रहा है**: फोरट्रान 2023 बैकवर्ड अनुकूलता बनाए रखते हुए आधुनिक सुविधाएँ जोड़ता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **आला समुदाय** | छोटे और विशिष्ट - अधिकतर वैज्ञानिक/एचपीसी | कम्प्यूटेशनल विज्ञान में सक्रिय समुदाय |
| **सीमित पारिस्थितिकी तंत्र** | पायथन, जावा, या C++ की तुलना में कम लाइब्रेरी | संख्यात्मक कार्य के लिए BLAS/LAPACK का उपयोग करें; सी अन्य जरूरतों के लिए अंतरसंचालनीयता |
| **सामान्य प्रयोजन नहीं** | वेब, मोबाइल, जीयूआई, या सिस्टम प्रोग्रामिंग के लिए खराब | गणना के लिए फोरट्रान का उपयोग करें; अनुप्रयोगों के लिए पायथन/सी में लपेटें |
| **धारणा** | आधुनिक क्षमताओं के बावजूद अक्सर "अप्रचलित" के रूप में देखा जाता है | इसकी शक्तियों पर ध्यान दें: संख्यात्मक और एचपीसी |
| **नियुक्ति** | कुछ फोरट्रान डेवलपर्स बाजार में प्रवेश कर रहे हैं | शिक्षा जगत और राष्ट्रीय प्रयोगशालाओं में मौजूदा विशेषज्ञ |
---

## सिंटेक्स फंडामेंटल (आधुनिक फोरट्रान)
```fortran
program hello
    implicit none

    ! Variables
    character(len=20) :: name = "Alice"
    integer :: age = 30
    real(8) :: score = 9.5d0
    logical :: active = .true.

    ! Arrays (Fortran's strength)
    real(8), dimension(3,3) :: matrix
    real(8), allocatable :: vector(:)

    ! Allocate dynamic array
    allocate(vector(100))
    vector = [(real(i, 8), i = 1, 100)]  ! Array constructor

    ! Array operations (no loops needed)
    matrix = reshape([1.0d0, 2.0d0, 3.0d0, &
                      4.0d0, 5.0d0, 6.0d0, &
                      7.0d0, 8.0d0, 9.0d0], [3,3])

    print '(A, I0)', "Hello, ", age

contains

    subroutine solve_linear(A, b, x, n)
        integer, intent(in) :: n
        real(8), intent(in) :: A(n,n), b(n)
        real(8), intent(out) :: x(n)
        x = matmul(inverse(A, n), b)
    end subroutine

end program hello
```

---

## उन्नत सिंटैक्स और पैटर्न
### व्युत्पन्न प्रकार और प्रकार-बद्ध प्रक्रियाएँ
```fortran
module particle_module
    implicit none
    private
    public :: particle, particle_system

    type :: particle
        real(8) :: position(3)
        real(8) :: velocity(3)
        real(8) :: mass
    contains
        procedure :: kinetic_energy
        procedure :: momentum
        procedure :: advance
    end type particle

    type :: particle_system
        type(particle), allocatable :: particles(:)
        real(8) :: time
    contains
        procedure :: total_energy
        procedure :: step
    end type particle_system

contains

    function kinetic_energy(self) result(ke)
        class(particle), intent(in) :: self
        real(8) :: ke
        ke = 0.5d0 * self.mass * dot_product(self.velocity, self.velocity)
    end function

    function momentum(self) result(p)
        class(particle), intent(in) :: self
        real(8) :: p(3)
        p = self.mass * self.velocity
    end function

    subroutine advance(self, dt)
        class(particle), intent(inout) :: self
        real(8), intent(in) :: dt
        self.position = self.position + self.velocity * dt
    end subroutine

    function total_energy(self) result(e)
        class(particle_system), intent(in) :: self
        real(8) :: e
        integer :: i
        e = 0.0d0
        do i = 1, size(self%particles)
            e = e + self%particles(i)%kinetic_energy()
        end do
    end function

    subroutine step(self, dt)
        class(particle_system), intent(inout) :: self
        real(8), intent(in) :: dt
        integer :: i
        do i = 1, size(self%particles)
            call self%particles(i)%advance(dt)
        end do
        self%time = self%time + dt
    end subroutine

end module particle_module
```

### सामान्य प्रक्रियाएं और ऑपरेटर ओवरलोडिंग
```fortran
module vector_ops
    implicit none

    type :: Vec3
        real(8) :: x, y, z
    end type Vec3

    ! Generic interface for multiple specific procedures
    interface vec_create
        module procedure vec3_create, vec3_create_uniform
    end interface

    ! Operator overloading
    interface operator(+)
        module procedure vec3_add
    end interface

    interface operator(*)
        module procedure vec3_scale, vec3_dot
    end interface

    interface assignment(=)
        module procedure vec3_from_array
    end interface

contains

    function vec3_create(x, y, z) result(v)
        real(8), intent(in) :: x, y, z
        type(Vec3) :: v
        v = Vec3(x, y, z)
    end function

    function vec3_create_uniform(val) result(v)
        real(8), intent(in) :: val
        type(Vec3) :: v
        v = Vec3(val, val, val)
    end function

    function vec3_add(a, b) result(c)
        type(Vec3), intent(in) :: a, b
        type(Vec3) :: c
        c = Vec3(a%x + b%x, a%y + b%y, a%z + b%z)
    end function

    function vec3_scale(s, v) result(r)
        real(8), intent(in) :: s
        type(Vec3), intent(in) :: v
        type(Vec3) :: r
        r = Vec3(s * v%x, s * v%y, s * v%z)
    end function

    function vec3_dot(a, b) result(d)
        type(Vec3), intent(in) :: a, b
        real(8) :: d
        d = a%x*b%x + a%y*b%y + a%z*b%z
    end function

    subroutine vec3_from_array(lhs, rhs)
        type(Vec3), intent(out) :: lhs
        real(8), intent(in) :: rhs(3)
        lhs = Vec3(rhs(1), rhs(2), rhs(3))
    end subroutine

end module vector_ops
```

### मॉड्यूल और कार्यक्रम संगठन
```fortran
module constants
    implicit none
    integer, parameter :: dp = selected_real_kind(15, 307)
    real(dp), parameter :: PI = 3.14159265358979323846_dp
    real(dp), parameter :: GRAVITY = 9.81_dp
end module

module math_utils
    use constants
    implicit none
    private
    public :: integrate, differentiate, solve_ode

contains

    function integrate(f, a, b, n) result(val)
        interface
            function f(x) result(y)
                import :: dp
                real(dp), intent(in) :: x
                real(dp) :: y
            end function
        end interface
        real(dp), intent(in) :: a, b
        integer, intent(in) :: n
        real(dp) :: val, h
        integer :: i
        h = (b - a) / real(n, dp)
        val = 0.5_dp * (f(a) + f(b))
        do i = 1, n-1
            val = val + f(a + i * h)
        end do
        val = val * h
    end function

end module math_utils
```

---

## समवर्ती एवं समांतरता
### कॉरेरेस (फोरट्रान 2008 बिल्ट-इन पैरेललिज्म)
```fortran
program coarray_example
    implicit none
    integer :: i, me, np
    real(8) :: local_data(100)[*]
    real(8) :: global_sum

    me = this_image()   ! Current process ID
    np = num_images()   ! Total number of processes

    ! Each image computes its portion
    do i = 1, 100
        local_data(i) = real(me * 100 + i, 8)
    end do

    ! Synchronise all images
    sync all

    ! Image 1 collects results
    if (me == 1) then
        global_sum = sum(local_data)
        do i = 2, np
            global_sum = global_sum + sum(local_data[i])
        end do
        print *, "Total sum: ", global_sum
    end if

end program coarray_example
! Compile: gfortran -fcoarray=single program.f90
! Run:     cafrun -np 4 ./program
```

### ओपनएमपी (साझा-स्मृति समानांतरवाद)
```fortran
program openmp_example
    use omp_lib
    implicit none
    integer :: n, i
    real(8), allocatable :: a(:), b(:), c(:)

    n = 10000000
    allocate(a(n), b(n), c(n))
    a = 1.0d0; b = 2.0d0

    ! Parallel do with OpenMP directives
    !$omp parallel do shared(a, b, c) private(i)
    do i = 1, n
        c(i) = a(i) * b(i) + sin(real(i, 8))
    end do
    !$omp end parallel do

    ! Parallel reduction
    !$omp parallel do reduction(+:total)
    total = sum(c)

    print *, "Number of threads: ", omp_get_max_threads()
    print *, "Sum: ", total

end program openmp_example
! Compile: gfortran -fopenmp program.f90
```

### एमपीआई (वितरित-स्मृति समानांतरवाद)
```fortran
program mpi_example
    use mpi
    implicit none
    integer :: ierr, rank, nprocs, tag
    integer :: status(MPI_STATUS_SIZE)
    real(8), allocatable :: local_data(:)
    real(8), allocatable :: all_data(:)

    call MPI_Init(ierr)
    call MPI_Comm_rank(MPI_COMM_WORLD, rank, ierr)
    call MPI_Comm_size(MPI_COMM_WORLD, nprocs, ierr)

    ! Each process works on its chunk
    allocate(local_data(1000))
    local_data = real(rank, 8)

    ! Gather all data to rank 0
    if (rank == 0) allocate(all_data(1000 * nprocs))
    call MPI_Gather(local_data, 1000, MPI_DOUBLE_PRECISION, &
                    all_data, 1000, MPI_DOUBLE_PRECISION, &
                    0, MPI_COMM_WORLD, ierr)

    if (rank == 0) then
        print *, "Global sum: ", sum(all_data)
    end if

    call MPI_Finalize(ierr)
end program mpi_example
! Compile: mpif90 program.f90
! Run:     mpirun -np 4 ./program
```

---

## परियोजना विन्यास एवं निर्माण प्रणाली
### फोरट्रान पैकेज मैनेजर (एफपीएम)
```toml
# fpm.toml
name = "my-scientific-lib"
version = "0.1.0"
license = "MIT"
author = "Jane Doe"

[build]
auto-executables = true
auto-tests = true

[dependencies]
fortranstdlib = { git = "https://github.com/fortran-lang/stdlib" }

[[test]]
name = "test_solver"
source-dir = "test"
main = "test_solver.f90"
```

### सीएमके बिल्ड सिस्टम
```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(MyScientificApp
    VERSION 1.0.0
    LANGUAGES Fortran)

# Set Fortran standards
set(CMAKE_Fortran_STANDARD 2008)
set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -O2 -Wall")

# Find dependencies
find_package(LAPACK REQUIRED)
find_package(BLAS REQUIRED)
find_package(MPI)

# Library
add_library(mylib STATIC
    src/constants.f90
    src/math_utils.f90
    src/solver.f90
)
target_link_libraries(mylib LAPACK::LAPACK BLAS::BLAS)

# Executable
add_executable(myapp src/main.f90)
target_link_libraries(myapp mylib)

# Tests
enable_testing()
add_executable(test_solver test/test_solver.f90)
target_link_libraries(test_solver mylib)
add_test(NAME solver_tests COMMAND test_solver)

# MPI support
if(MPI_Fortran_FOUND)
    target_link_libraries(myapp MPI::MPI_Fortran)
endif()
```

### परियोजना संरचना
```
my-scientific-app/
+-- fpm.toml              # fpm package manifest
+-- CMakeLists.txt         # CMake build file
+-- src/
|   +-- main.f90
|   +-- constants.f90
|   +-- math_utils.f90
|   +-- solver.f90
|   +-- particle_module.f90
+-- test/
|   +-- test_solver.f90
|   +-- test_math.f90
+-- doc/
|   +-- Doxyfile
+-- .github/
|   +-- workflows/
|       +-- ci.yml
```

---

## परीक्षण
### टेस्ट फ्रेमवर्क (फोरट्रान-टेस्ट या पीएफयूनिट)
```fortran
! Simple test framework using assertions
module test_helpers
    implicit none
    integer :: tests_run = 0, tests_passed = 0
contains
    subroutine assert_equal_real(actual, expected, msg)
        real(8), intent(in) :: actual, expected
        character(*), intent(in) :: msg
        tests_run = tests_run + 1
        if (abs(actual - expected) < 1.0d-10) then
            tests_passed = tests_passed + 1
        else
            print '(A,A,A,ES12.5,A,ES12.5)', "FAIL: ", msg, &
                " got=", actual, " expected=", expected
        end if
    end subroutine

    subroutine assert_equal_int(actual, expected, msg)
        integer, intent(in) :: actual, expected
        character(*), intent(in) :: msg
        tests_run = tests_run + 1
        if (actual == expected) then
            tests_passed = tests_passed + 1
        else
            print '(A,A,A,I0,A,I0)', "FAIL: ", msg, &
                " got=", actual, " expected=", expected
        end if
    end subroutine

    subroutine print_summary()
        print '(A,I0,A,I0,A)', "Tests: ", tests_passed, " / ", &
            tests_run, " passed"
    end subroutine
end module

program test_solver
    use test_helpers
    use math_utils
    implicit none

    call test_trapezoid()
    call test_array_ops()
    call print_summary()

contains

    subroutine test_trapezoid()
        real(8) :: result
        result = integrate(my_func, 0.0d0, 1.0d0, 10000)
        call assert_equal_real(result, 0.5d0, "integral of x from 0 to 1")
    end subroutine

    subroutine test_array_ops()
        real(8) :: a(3), b(3), c(3)
        a = [1.0d0, 2.0d0, 3.0d0]
        b = [4.0d0, 5.0d0, 6.0d0]
        c = a + b
        call assert_equal_real(c(1), 5.0d0, "array add element 1")
        call assert_equal_real(c(3), 9.0d0, "array add element 3")
    end subroutine

    function my_func(x) result(y)
        real(8), intent(in) :: x
        real(8) :: y
        y = x
    end function

end program test_solver
```

---

## अंतरसंचालनीयता
### सी इंटरऑपरेबिलिटी (आईएसओ_सी_बाइंडिंग)
```fortran
module c_interface
    use, intrinsic :: iso_c_binding
    implicit none

    ! Call C function from Fortran
    interface
        function c_sqrt(x) bind(C, name="sqrt") result(r)
            import :: c_double
            real(c_double), value :: x
            real(c_double) :: r
        end function

        subroutine c_sort(array, n) bind(C, name="sort_array")
            import :: c_double, c_int
            real(c_double), intent(inout) :: array(*)
            integer(c_int), value :: n
        end subroutine
    end interface

    ! Export Fortran function to C
contains
    function fortran_compute(n) bind(C, name="compute") result(r)
        real(c_double), value :: n
        real(c_double) :: r
        r = n * n + 1.0d0
    end function
end module

! Usage
program use_c
    use c_interface
    implicit none
    print *, "sqrt(2) = ", c_sqrt(2.0d0)
end program
```

### पायथन एकीकरण (f2py या साझा लाइब्रेरी के माध्यम से)
```fortran
! Fortran subroutine callable from Python via f2py
subroutine compute_statistics(data, n, mean_val, std_val)
    implicit none
    integer, intent(in) :: n
    real(8), intent(in) :: data(n)
    real(8), intent(out) :: mean_val, std_val

    mean_val = sum(data) / real(n, 8)
    std_val = sqrt(sum((data - mean_val)**2) / real(n, 8))
end subroutine
! Build: f2py -c -m fortran_stats stats.f90
! Python: import fortran_stats; fortran_stats.compute_statistics(data)
```

---

## डिज़ाइन पैटर्न
### पैटर्न 1: ऐरे प्रोग्रामिंग (लूप्स से बचें)
```fortran
! BAD — element-by-element loop
do i = 1, n
    do j = 1, m
        c(i,j) = a(i,j) * b(i,j) + sin(a(i,j))
    end do
end do

! GOOD — whole-array operations
c = a * b + sin(a)

! WHERE construct for conditional array operations
where (a > 0.0d0)
    result = log(a)
elsewhere
    result = 0.0d0
end where
```

### पैटर्न 2: पैरामीटरयुक्त व्युत्पन्न प्रकार
```fortran
module precision_types
    implicit none
    integer, parameter :: sp = selected_real_kind(6, 37)
    integer, parameter :: dp = selected_real_kind(15, 307)
    integer, parameter :: qp = selected_real_kind(33, 4931)
end module

! Use parameterised types for portable precision
module simulation
    use precision_types
    implicit none
    real(dp), parameter :: tol = 1.0e-12_dp
    real(dp), parameter :: pi = 3.14159265358979323846_dp
end module
```

### पैटर्न 3: प्रक्रिया संकेतकों के साथ कॉलबैक पैटर्न
```fortran
module integrator
    implicit none
    abstract interface
        function integrand_func(x) result(fx)
            real(8), intent(in) :: x
            real(8) :: fx
        end function
    end interface
contains
    function integrate_adaptive(f, a, b, tol) result(val)
        procedure(integrand_func) :: f
        real(8), intent(in) :: a, b, tol
        real(8) :: val
        ! Adaptive quadrature implementation...
        val = (b - a) / 6.0d0 * (f(a) + 4.0d0 * f((a+b)/2.0d0) + f(b))
    end function
end module
```

---

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
```bash
# gprof profiling
gfortran -pg -O2 program.f90 -o program
./program
gprof program gmon.out > analysis.txt

# perf (Linux)
perf record ./program
perf report

# Valgrind for memory profiling
valgrind --tool=massif ./program
```

### कंपाइलर अनुकूलन फ़्लैग
```bash
# GNU Fortran (gfortran)
gfortran -O3 -march=native -ffast-math -funroll-loops program.f90

# Intel Fortran (ifx/ifort)
ifx -O3 -xHost -qopt-report=5 program.f90

# NAG Fortran
nagfor -O4 -ieee=full program.f90

# Key flags explained:
# -O3         : Maximum optimisation
# -march=native: Use CPU-specific instructions (AVX, SSE)
# -ffast-math : Relaxed IEEE compliance for speed
# -funroll-loops: Loop unrolling
# -flto       : Link-time optimisation
```

### सदिशीकरण और स्मृति
```fortran
! Contiguous memory access (column-major order in Fortran)
! GOOD — access along columns (fast)
do j = 1, n
    do i = 1, m
        a(i,j) = b(i,j) + c(i,j)
    end do
end do

! BAD — access along rows (cache-unfriendly in Fortran)
do i = 1, m
    do j = 1, n
        a(i,j) = b(i,j) + c(i,j)
    end do
end do

! Use contiguous arrays for better vectorisation
real(8), contiguous, pointer :: arr(:)

! Explicit vectorisation hints
!dir$ vector aligned
do i = 1, n
    c(i) = a(i) * b(i)
end do
```

---

## तैनाती
### एचपीसी के लिए भवन
```bash
# Static linking for portable binaries
gfortran -O3 -static program.f90 -o program_static

# Build with MPI for cluster deployment
mpif90 -O3 program.f90 -o program_mpi

# Submit SLURM job script
#!/bin/bash
#SBATCH --job-name=fortran_sim
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=32
#SBATCH --time=48:00:00
module load intel-mpi
srun -n 256 ./program_mpi
```

### कंटेनर परिनियोजन
```dockerfile
FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gfortran cmake
COPY . /app
WORKDIR /app
RUN cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build

FROM ubuntu:22.04
COPY --from=builder /app/build/myapp /usr/local/bin/
ENTRYPOINT ["myapp"]
```

### पायथन वितरण (f2py)
```bash
# Build Python extension module
f2py -c -m mymodule --f90flags="-O3" mymodule.f90

# Distribute via pip (with meson build system)
# Users: pip install my-fortran-module
```

---

## फोरट्रान का उपयोग कब करें
| परिदृश्य | फोरट्रान क्यों | बेहतर विकल्प |
|---|----|-----|
| एचपीसी/सुपरकंप्यूटिंग | संख्यात्मक प्रदर्शन के लिए अनुकूलित | सी++ (सावधानीपूर्वक), जूलिया |
| वैज्ञानिक अनुकरण | दशकों के मान्य कोड | पायथन (प्रोटोटाइपिंग के लिए), C++ |
| जलवायु/मौसम मॉडल | लीगेसी कोडबेस; प्रदर्शन | — |
| कम्प्यूटेशनल भौतिकी | मूल सरणी संचालन | पायथन (NumPy), जूलिया |
| वित्तीय मॉडलिंग (एचपीसी) | बड़े पैमाने पर गणना के लिए प्रदर्शन | सी++, पायथन |
| सामान्य अनुप्रयोग विकास | अनुकूल नहीं | पायथन, जावा, गो |
| वेब विकास | अनुकूल नहीं | जावास्क्रिप्ट, पायथन |
| डेटा विज्ञान (इंटरैक्टिव) | वर्कफ़्लो नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: फोरट्रान 90 और आधुनिक फोरट्रान (2008+) के बीच क्या अंतर है?
**ए:** आधुनिक फोरट्रान ने कई विशेषताएं जोड़ीं जो इसे और अधिक अभिव्यंजक बनाती हैं:
```fortran
! Fortran 90: free-form source, modules, derived types
! Fortran 2003: OOP (classes, inheritance, polymorphism)
! Fortran 2008: coarrays (parallel programming), submodules
! Fortran 2018: further coarray enhancements, IEEE arithmetic

! Modern OOP example
type :: Shape
    character(len=20) :: name
contains
    procedure :: area => shape_area
end type

type, extends(Shape) :: Circle
    real :: radius
contains
    procedure :: area => circle_area
end type
```

### Q2: फोरट्रान सरणियाँ C सरणियों से किस प्रकार भिन्न हैं?
**ए:** फोरट्रान सरणियाँ अंतर्निहित संचालन के साथ प्रथम श्रेणी की वस्तुएं हैं:
```fortran
! Declaration with bounds
real, dimension(100) :: x          ! 1 to 100
real, dimension(-50:50) :: y       ! -50 to 50
real, dimension(10, 20) :: matrix  ! 2D array

! Array operations (no loops needed)
a = b + c           ! element-wise addition
a = sin(b) * cos(c) ! element-wise functions
where (a > 0)
    a = sqrt(a)
end where

! Array slices
sub_array = a(10:50:2)   ! elements 10, 12, 14, ..., 50
matrix_col = matrix(:, 3) ! entire 3rd column
```

### Q3: मैं फोरट्रान में अधिकतम प्रदर्शन कैसे प्राप्त करूं?
**ए:** मुख्य अभ्यास:
- सभी डमी तर्कों के लिए स्पष्ट`intent`का उपयोग करें
- हर जगह`implicit none`का उपयोग करें
- लूप के बजाय ऐरे ऑपरेशंस को प्राथमिकता दें
- सन्निहित मेमोरी एक्सेस पैटर्न का उपयोग करें
- कंपाइलर ऑप्टिमाइज़ेशन फ़्लैग का उपयोग करें:`-O3 -march=native -ffast-math`
-`gprof`या कंपाइलर-विशिष्ट टूल के साथ प्रोफ़ाइल
- उन कार्यों के लिए`pure`और`elemental`का उपयोग करें जिन्हें कंपाइलर अनुकूलित कर सकता है
### Q4: मैं फोरट्रान को C के साथ कैसे इंटरफ़ेस करूं?
**ए:**`iso_c_binding`मॉड्यूल का उपयोग करें:
```fortran
use iso_c_binding

! Call a C function
interface
    function c_strlen(str) bind(C, name='strlen') result(len)
        import :: c_ptr, c_size_t
        type(c_ptr), intent(in), value :: str
        integer(c_size_t) :: len
    end function
end interface
```

### Q5: फोरट्रान परियोजनाओं के लिए मुझे किस बिल्ड सिस्टम का उपयोग करना चाहिए?
**ए:** सीएमके के पास उत्कृष्ट फोरट्रान समर्थन है। एफपीएम (फोरट्रान पैकेज मैनेजर) आधुनिक देशी विकल्प है:
```bash
# FPM — simple, Fortran-native
fpm new my_project
fpm build
fpm test
fpm run

# CMake — for larger projects
# add_executable(myapp src/main.f90 src/module1.f90)
# target_compile_options(myapp PRIVATE -O3)
```

---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: सीमित अंतर के साथ पीडीई को हल करना
**चरण 1: समस्या को समझें**
1D ऊष्मा समीकरण को हल करें: du/dt = alpha * d²u/dx²
**चरण 2: दृष्टिकोण को पहचानें**
परिमित अंतरों का उपयोग करके स्थान और समय को अलग करें। एक स्पष्ट योजना का प्रयोग करें.
**चरण 3: कार्यान्वयन**```fortran
program heat_equation
    implicit none
    integer, parameter :: n = 100, nt = 1000
    real(8), parameter :: L = 1.0d0, alpha = 0.01d0
    real(8) :: dx, dt, x(n), u(n), u_new(n)
    integer :: i, t

    dx = L / (n - 1)
    dt = 0.4d0 * dx**2 / alpha  ! stability condition

    ! Initial condition
    x = [(real(i-1, 8) * dx, i = 1, n)]
    u = exp(-100.0d0 * (x - 0.5d0)**2)

    ! Time stepping
    do t = 1, nt
        u_new(1) = 0.0d0     ! boundary
        u_new(n) = 0.0d0     ! boundary
        do i = 2, n-1
            u_new(i) = u(i) + alpha * dt / dx**2 * &
                        (u(i+1) - 2.0d0*u(i) + u(i-1))
        end do
        u = u_new
    end do

    ! Output
    do i = 1, n
        print *, x(i), u(i)
    end do
end program
```

**चरण 4: सत्यापित करें**
संरक्षण की जाँच करें, ग्रिड शोधन के साथ अभिसरण, और विश्लेषणात्मक समाधान के साथ तुलना करें।
### समस्या 2: मैट्रिक्स विकर्णीकरण
**चरण 1: समस्या को समझें**
एक सममित मैट्रिक्स के eigenvalues ​​और eigenvectors खोजें।
**चरण 2: दृष्टिकोण को पहचानें**
फोरट्रान के इंटरफ़ेस के माध्यम से LAPACK के`dsyev`रूटीन का उपयोग करें।
**चरण 3: कार्यान्वयन**```fortran
program diagonalize
    use lapack95
    implicit none
    integer, parameter :: n = 3
    real(8) :: A(n,n), w(n), work(3*n-1)
    integer :: info

    A = reshape([2.0d0, -1.0d0, 0.0d0, &
                -1.0d0,  2.0d0, -1.0d0, &
                 0.0d0, -1.0d0,  2.0d0], [n,n])

    call dsyev('V', 'U', n, A, n, w, work, size(work), info)

    print *, 'Eigenvalues:'
    print '(3F12.6)', w
    print *, 'Eigenvectors (columns):'
    do i = 1, n
        print '(3F12.6)', A(i,:)
    end do
end program
```

**चरण 4: सत्यापित करें**
जाँचें कि प्रत्येक eigenpair के लिए A*v = Lambda*v।
---

## सारांश
फोरट्रान मूल वैज्ञानिक प्रोग्रामिंग भाषा है और उच्च-प्रदर्शन कंप्यूटिंग में एक पावरहाउस बनी हुई है। आधुनिक फोरट्रान देशी सरणी संचालन, समानांतर प्रोग्रामिंग समर्थन और सी इंटरऑपरेबिलिटी के साथ एक सक्षम, विकसित भाषा है। जबकि इसका समुदाय छोटा और विशिष्ट है, फोरट्रान दुनिया में सबसे अधिक मांग वाले कम्प्यूटेशनल वर्कलोड में से कुछ को चलाना जारी रखता है। पैमाने पर संख्यात्मक कंप्यूटिंग के लिए, फोरट्रान प्रासंगिक बना हुआ है।