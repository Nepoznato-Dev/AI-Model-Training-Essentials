---
# Metadata
title: "Fortran"
description: "Comprehensive reference for the Fortran programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
#ফরট্রান
Fortran (ফর্মুলা ট্রান্সলেশন) হল প্রাচীনতম উচ্চ-স্তরের প্রোগ্রামিং ভাষা যা এখনও ব্যাপকভাবে ব্যবহৃত হয়, যা প্রথম IBM দ্বারা 1957 সালে বৈজ্ঞানিক ও প্রকৌশল গণনার জন্য তৈরি করা হয়েছিল। বয়স হওয়া সত্ত্বেও, আধুনিক ফোরট্রান (Fortran 2008/2018/2023) হল একটি সক্ষম, উচ্চ-কর্মক্ষমতার ভাষা যা সংখ্যাসূচক আবহাওয়ার পূর্বাভাস, গণনামূলক তরল গতিবিদ্যা, পদার্থবিজ্ঞানের সিমুলেশন, আর্থিক মডেলিং এবং উচ্চ-পারফরম্যান্স কম্পিউটিং (HPC) এ ব্যাপকভাবে ব্যবহৃত হয়। বিশ্বের দ্রুততম সুপারকম্পিউটারগুলির মধ্যে অনেকগুলি ফোর্টরান কোড চালায়।
ভাষা তার প্রথম দিন থেকে উল্লেখযোগ্যভাবে বিকশিত হয়েছে। আধুনিক ফোর্টরানের মডিউল, প্রাপ্ত প্রকার, জেনেরিক পদ্ধতি, কোয়ারে (সমান্তরাল প্রোগ্রামিং) এবং সি-এর সাথে আন্তঃকার্যযোগ্যতা রয়েছে। এটি অনেক বৈজ্ঞানিক কম্পিউটিং অ্যাপ্লিকেশনের জন্য পছন্দের ভাষা হিসাবে রয়ে গেছে যেখানে কর্মক্ষমতা সর্বাধিক।
---

## কেন ফরট্রান ব্যাপার
- **HPC পারফরম্যান্স**: Fortran কম্পাইলারগুলি উপলব্ধ কিছু দ্রুততম সংখ্যাসূচক কোড তৈরি করে — প্রায়শই অ্যারে অপারেশনের জন্য C/C++ মেলে বা অতিক্রম করে।
- **লিগেসি কোডবেস**: কয়েক দশকের বৈজ্ঞানিক কোড (জলবায়ু মডেল, পদার্থবিদ্যার সিমুলেশন) ফোর্টরানে লেখা হয়েছে।
- **অ্যারে অপারেশন**: গাণিতিক গণনার জন্য ডিজাইন করা সিনট্যাক্স সহ স্থানীয় বহু-মাত্রিক অ্যারে সমর্থন।
- **সংখ্যাসূচক স্থায়িত্ব**: ভাষা এবং কম্পাইলারগুলি ফ্লোটিং-পয়েন্ট গণনার জন্য অপ্টিমাইজ করা হয়েছে।
- **Coarrays**: অন্তর্নির্মিত সমান্তরাল প্রোগ্রামিং সমর্থন (Fortran 2008+)।
- **এখনও বিকশিত হচ্ছে**: Fortran 2023 পিছনের সামঞ্জস্য বজায় রেখে আধুনিক বৈশিষ্ট্য যোগ করে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **কুলুঙ্গি সম্প্রদায়** | ছোট এবং বিশেষায়িত — বেশিরভাগই বৈজ্ঞানিক/HPC | কম্পিউটেশনাল সায়েন্সে সক্রিয় সম্প্রদায় |
| **সীমিত ইকোসিস্টেম** | Python, Java, বা C++ | এর চেয়ে কম লাইব্রেরি সংখ্যাসূচক কাজের জন্য BLAS/LAPACK ব্যবহার করুন; C অন্যান্য প্রয়োজনের জন্য আন্তঃকার্যক্ষমতা |
| **সাধারণ উদ্দেশ্য নয়** | ওয়েব, মোবাইল, GUI, বা সিস্টেম প্রোগ্রামিং এর জন্য খারাপ | গণনার জন্য Fortran ব্যবহার করুন; অ্যাপ্লিকেশনের জন্য পাইথন/সি-তে মোড়ানো |
| ** উপলব্ধি** | আধুনিক ক্ষমতা থাকা সত্ত্বেও প্রায়শই "অপ্রচলিত" হিসাবে দেখা হয় | এর শক্তির উপর ফোকাস করুন: সংখ্যাসূচক এবং HPC |
| **নিয়োগ** | কিছু ফোর্টরান ডেভেলপার বাজারে প্রবেশ করছে | একাডেমিয়া এবং জাতীয় ল্যাবে বিদ্যমান বিশেষজ্ঞরা |
---

## সিনট্যাক্স ফান্ডামেন্টালস (আধুনিক ফোর্টরান)
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### প্রাপ্ত প্রকার এবং টাইপ-বাউন্ড পদ্ধতি
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

### জেনেরিক পদ্ধতি এবং অপারেটর ওভারলোডিং
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

### মডিউল এবং প্রোগ্রাম অর্গানাইজেশন
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

## সামঞ্জস্য এবং সমান্তরালতা
### Coarrays (Fortran 2008 অন্তর্নির্মিত সমান্তরালতা)
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

### OpenMP (শেয়ারড-মেমরি প্যারালেলিজম)
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

### MPI (ডিস্ট্রিবিউটেড-মেমরি প্যারালেলিজম)
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### ফোরট্রান প্যাকেজ ম্যানেজার (fpm)
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

### সিমেক বিল্ড সিস্টেম
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

### প্রকল্পের কাঠামো
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

## পরীক্ষা
### টেস্ট ফ্রেমওয়ার্ক (ফরট্রান-টেস্ট বা পিএফইউনিট)
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

## ইন্টারঅপারেবিলিটি
### সি ইন্টারঅপারেবিলিটি (ISO_C_BINDING)
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

### পাইথন ইন্টিগ্রেশন (f2py বা শেয়ার্ড লাইব্রেরির মাধ্যমে)
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: অ্যারে প্রোগ্রামিং (লুপ এড়িয়ে চলুন)
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

### প্যাটার্ন 2: প্যারামিটারাইজড ডিরাইভড টাইপ
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

### প্যাটার্ন 3: পদ্ধতি পয়েন্টার সহ কলব্যাক প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### কম্পাইলার অপ্টিমাইজেশান ফ্ল্যাগ
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

### ভেক্টরাইজেশন এবং মেমরি
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

## স্থাপনা
### HPC এর জন্য বিল্ডিং
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

### কন্টেইনার স্থাপনা
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

### পাইথন ডিস্ট্রিবিউশন (f2py)
```bash
# Build Python extension module
f2py -c -m mymodule --f90flags="-O3" mymodule.f90

# Distribute via pip (with meson build system)
# Users: pip install my-fortran-module
```

---

## কখন Fortran ব্যবহার করবেন
| দৃশ্যকল্প | কেন ফরট্রান | ভাল বিকল্প |
|------------|------------|---------|
| এইচপিসি / সুপারকম্পিউটিং | সংখ্যাগত কর্মক্ষমতা জন্য অপ্টিমাইজ করা | C++ (যত্ন সহ), জুলিয়া |
| বৈজ্ঞানিক সিমুলেশন | বৈধ কোডের দশক | পাইথন (প্রোটোটাইপিংয়ের জন্য), C++ |
| জলবায়ু/আবহাওয়া মডেল | উত্তরাধিকার কোডবেস; কর্মক্ষমতা | — |
| কম্পিউটেশনাল পদার্থবিদ্যা | নেটিভ অ্যারে অপারেশন | পাইথন (NumPy), জুলিয়া |
| আর্থিক মডেলিং (HPC) | বড় আকারের গণনার জন্য কর্মক্ষমতা | C++, পাইথন |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | উপযুক্ত নয় | Python, Java, Go |
| ওয়েব ডেভেলপমেন্ট | উপযুক্ত নয় | জাভাস্ক্রিপ্ট, পাইথন |
| ডেটা সায়েন্স (ইন্টারেক্টিভ) | কর্মপ্রবাহ নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: Fortran 90 এবং আধুনিক Fortran (2008+) এর মধ্যে পার্থক্য কী?
**A:** আধুনিক ফোরট্রান অনেক বৈশিষ্ট্য যুক্ত করেছে যা এটিকে আরও অভিব্যক্তিপূর্ণ করে তোলে:
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

### প্রশ্ন 2: ফোরট্রান অ্যারে কীভাবে সি অ্যারে থেকে আলাদা?
**A:** ফোরট্রান অ্যারেগুলি বিল্ট-ইন অপারেশন সহ প্রথম শ্রেণীর বস্তু:
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

### প্রশ্ন 3: আমি কীভাবে ফোরট্রানে সর্বোচ্চ কার্যক্ষমতা অর্জন করব?
**A:** মূল অনুশীলন:
- সমস্ত ডামি আর্গুমেন্টের জন্য স্পষ্ট`intent`ব্যবহার করুন
- সব জায়গায়`implicit none`ব্যবহার করুন
- লুপের উপর অ্যারে অপারেশন পছন্দ করুন
- সংলগ্ন মেমরি অ্যাক্সেস প্যাটার্ন ব্যবহার করুন
- কম্পাইলার অপ্টিমাইজেশান ফ্ল্যাগ ব্যবহার করুন:`-O3 -march=native -ffast-math`
-`gprof`বা কম্পাইলার-নির্দিষ্ট টুল সহ প্রোফাইল
- কম্পাইলার অপ্টিমাইজ করতে পারে এমন ফাংশনগুলির জন্য`pure`এবং`elemental`ব্যবহার করুন
### প্রশ্ন 4: আমি কিভাবে C এর সাথে Fortran ইন্টারফেস করব?
**A:**`iso_c_binding`মডিউল ব্যবহার করুন:
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

### প্রশ্ন 5: ফরট্রান প্রকল্পের জন্য আমার কোন বিল্ড সিস্টেম ব্যবহার করা উচিত?
**A:** CMake এর চমৎকার Fortran সমর্থন রয়েছে। এফপিএম (ফরট্রান প্যাকেজ ম্যানেজার) হল আধুনিক নেটিভ বিকল্প:
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: সীমাবদ্ধ পার্থক্য সহ একটি PDE সমাধান করা
**ধাপ 1: সমস্যাটি বুঝুন**
1D তাপ সমীকরণটি সমাধান করুন: du/dt = alpha * d²u/dx²
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
সসীম পার্থক্য ব্যবহার করে স্থান এবং সময়কে আলাদা করুন। একটি সুস্পষ্ট স্কিম ব্যবহার করুন.
**ধাপ 3: প্রয়োগ করুন**```fortran
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

**পদক্ষেপ 4: যাচাই করুন**
সংরক্ষণ পরীক্ষা করুন, গ্রিড পরিমার্জনের সাথে একত্রীকরণ, এবং বিশ্লেষণাত্মক সমাধানের সাথে তুলনা করুন।
### সমস্যা 2: ম্যাট্রিক্স ডায়াগোনালাইজেশন
**ধাপ 1: সমস্যাটি বুঝুন**
একটি প্রতিসম ম্যাট্রিক্সের eigenvalues এবং eigenvectors খুঁজুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
Fortran এর ইন্টারফেসের মাধ্যমে LAPACK এর`dsyev`রুটিন ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```fortran
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

**পদক্ষেপ 4: যাচাই করুন**
প্রতিটি eigenpair এর জন্য A*v = lambda*v চেক করুন।
---

## সারাংশ
Fortran হল মূল বৈজ্ঞানিক প্রোগ্রামিং ভাষা এবং উচ্চ-কার্যক্ষমতা সম্পন্ন কম্পিউটিং এর একটি পাওয়ার হাউস হিসেবে রয়ে গেছে। আধুনিক ফোর্টরান একটি সক্ষম, বিবর্তিত ভাষা যার সাথে নেটিভ অ্যারে অপারেশন, সমান্তরাল প্রোগ্রামিং সমর্থন এবং সি ইন্টারঅপারেবিলিটি। যদিও এর সম্প্রদায়টি ছোট এবং বিশেষায়িত, ফোর্টরান বিশ্বের সবচেয়ে চাহিদাপূর্ণ গণনামূলক কাজের চাপগুলি চালিয়ে যাচ্ছে। স্কেলে সংখ্যাসূচক কম্পিউটিংয়ের জন্য, ফোরট্রান প্রাসঙ্গিক রয়ে গেছে।