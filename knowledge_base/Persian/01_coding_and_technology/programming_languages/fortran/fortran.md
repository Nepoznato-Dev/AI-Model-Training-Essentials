---
# فراداده
عنوان: "فرترن"
توضیحات: "مرجع جامع برای زبان برنامه نویسی فرترن شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم، و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [فرترن، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "پیشرفته"
پیش نیاز: []
تخمینی_زمان_خواندن: "32 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
#فرترن
Fortran (ترجمه فرمول) قدیمی ترین زبان برنامه نویسی سطح بالا است که هنوز در حال استفاده گسترده است، اولین بار توسط IBM در سال 1957 برای محاسبات علمی و مهندسی توسعه یافت. با وجود قدمت، فرترن مدرن (فرترن 2008/2018/2023) یک زبان توانا و با کارایی بالا است که به طور گسترده در پیش‌بینی عددی آب و هوا، دینامیک سیالات محاسباتی، شبیه‌سازی‌های فیزیک، مدل‌سازی مالی و محاسبات با عملکرد بالا (HPC) استفاده می‌شود. بسیاری از سریع ترین ابررایانه های جهان کد فرترن را اجرا می کنند.
این زبان از روزهای اولیه خود به طور قابل توجهی تکامل یافته است. فرترن مدرن دارای ماژول‌ها، انواع مشتق‌شده، رویه‌های عمومی، هم‌آهنگ‌ها (برنامه‌نویسی موازی) و قابلیت همکاری با C است. این زبان انتخابی برای بسیاری از برنامه‌های محاسباتی علمی است که در آن عملکرد در اولویت است.
---

## چرا فرترن مهم است
- **عملکرد HPC**: کامپایلرهای فرترن برخی از سریعترین کدهای عددی موجود را تولید می کنند - اغلب با C/C++ برای عملیات آرایه مطابقت دارند یا از آن فراتر می روند.
- **پایه های کدهای قدیمی**: چندین دهه کد علمی (مدل های آب و هوا، شبیه سازی های فیزیک) در فرترن نوشته شده است.
- **عملیات آرایه**: پشتیبانی از آرایه چند بعدی بومی با نحو طراحی شده برای محاسبات ریاضی.
- **پایداری عددی**: زبان و کامپایلرها برای محاسبات ممیز شناور بهینه شده اند.
- **Coarrays**: پشتیبانی از برنامه نویسی موازی داخلی (Fortran 2008+).
- **هنوز در حال تکامل**: Fortran 2023 ویژگی های مدرن را با حفظ سازگاری به عقب اضافه می کند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **جامعه طاقچه** | کوچک و تخصصی — عمدتاً علمی/HPC | جامعه فعال در علوم محاسباتی |
| **اکوسیستم محدود** | کتابخانه های کمتری نسبت به پایتون، جاوا یا C++ | از BLAS/LAPACK برای کار عددی استفاده کنید. قابلیت همکاری C برای سایر نیازها |
| **غیر منظوره** | ضعیف برای برنامه نویسی وب، موبایل، رابط کاربری گرافیکی یا سیستم ها | از Fortran برای محاسبات استفاده کنید. برای برنامه ها در Python/C قرار دهید |
| **ادراک** | با وجود قابلیت های مدرن اغلب به عنوان "منسوخ" دیده می شود | روی نقاط قوت آن تمرکز کنید: عددی و HPC |
| **استخدام** | تعداد کمی از توسعه دهندگان فرترن وارد بازار می شوند | کارشناسان موجود در دانشگاه ها و آزمایشگاه های ملی |
---

## اصول نحو (فرترن مدرن)
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

## نحو و الگوهای پیشرفته
### انواع مشتق شده و رویه های Type-Bound
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

### رویه های عمومی و بارگذاری بیش از حد اپراتور
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

### ماژول ها و سازمان برنامه
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

## همزمانی و موازی
### Coarrays (Fortran 2008 Built-in Parallelism)
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

### OpenMP (موازی حافظه مشترک)
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

### MPI (توازی حافظه توزیع شده)
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

## پیکربندی پروژه و سیستم ساخت
### مدیر بسته فرترن (fpm)
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

### CMake Build System
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

### ساختار پروژه
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

## تست
### چارچوب تست (تست فورتن یا pFUnit)
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

## قابلیت همکاری
### C قابلیت همکاری (ISO_C_BINDING)
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

### ادغام پایتون (از طریق f2py یا کتابخانه مشترک)
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

## الگوهای طراحی
### الگوی 1: برنامه نویسی آرایه (از حلقه ها اجتناب کنید)
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

### الگوی 2: انواع مشتق شده پارامتری شده
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

### الگوی 3: الگوی برگشت به تماس با اشاره گرهای رویه
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### پرچم های بهینه سازی کامپایلر
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

### برداری و حافظه
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

## استقرار
### ساختمان برای HPC
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

### استقرار کانتینر
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

### توزیع پایتون (f2py)
```bash
# Build Python extension module
f2py -c -m mymodule --f90flags="-O3" mymodule.f90

# Distribute via pip (with meson build system)
# Users: pip install my-fortran-module
```

---

## چه زمانی از Fortran استفاده کنیم
| سناریو | چرا فرترن | جایگزین بهتر |
|----------|----------|------------------|
| HPC / ابر رایانه | بهینه شده برای عملکرد عددی | C++ (با دقت)، جولیا |
| شبیه سازی علمی | چند دهه کد معتبر | پایتون (برای نمونه سازی)، C++ |
| مدل های آب و هوا/ آب و هوا | پایگاه های کد قدیمی؛ عملکرد | — |
| فیزیک محاسباتی | عملیات آرایه بومی | پایتون (NumPy)، جولیا |
| مدل سازی مالی (HPC) | عملکرد برای محاسبات در مقیاس بزرگ | سی پلاس پلاس، پایتون |
| توسعه برنامه عمومی | مناسب نیست | پایتون، جاوا، برو |
| توسعه وب | مناسب نیست | جاوا اسکریپت، پایتون |
| علم داده (تعاملی) | نه گردش کار | پایتون، R |
---

## خلاصه
فرترن زبان برنامه نویسی علمی اصلی است و همچنان یک نیروگاه در محاسبات با کارایی بالا است. فرترن مدرن یک زبان توانا و در حال تکامل با عملیات آرایه بومی، پشتیبانی از برنامه نویسی موازی و قابلیت همکاری C است. در حالی که انجمن آن کوچک و تخصصی است، فرترن همچنان به اجرای برخی از سخت ترین حجم کاری های محاسباتی در جهان ادامه می دهد. برای محاسبات عددی در مقیاس، فرترن همچنان مرتبط است.