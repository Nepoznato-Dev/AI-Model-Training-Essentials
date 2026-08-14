<!--
---
# Metadata
title: "Fortran — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Fortran ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [fortran, ecosystem, tooling, compilers, hpc, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Fortran — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, thư viện và cơ sở hạ tầng thiết yếu trong hệ sinh thái Fortran.
---

## Trình biên dịch và tiêu chuẩn Fortran
| Trình biên dịch | Nền tảng | Ghi chú |
|----------|----------|-------|
| **gfortran** | Đa nền tảng | GNU Fortran (GCC), được sử dụng rộng rãi nhất |
| **ifx / ifort** | Đa nền tảng | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **bích** | Đa nền tảng | Dựa trên LLVM (mới) |
| **NAG** | Đa nền tảng | Thương mại, tuân thủ nghiêm ngặt |
| **Cray** | HPC | Siêu máy tính Cray |
| **IBM XL** | HPC | hệ thống IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Xây dựng hệ thống
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **CMake** | Đa nền tảng | Tiêu chuẩn ngành |
| **fpm** | Người gốc Fortran | Trình quản lý gói Fortran hiện đại |
| **Meson** | Hiện đại | Cú pháp nhanh, rõ ràng |
| **Thực hiện** | Cổ điển | Dự án đơn giản |
| **SCon** | Dựa trên Python | Bản dựng phức tạp |
```toml
# fpm.toml (Fortran Package Manager)
name = "myapp"
version = "0.1.0"
license = "MIT"
author = "Developer"

[build]
auto-executables = true
auto-tests = true

[dependencies]
stdlib = { git = "https://github.com/fortran-lang/stdlib.git" }

[[test]]
name = "test_main"
source-dir = "test"
main = "test_main.f90"
```

```bash
fpm build                 # build
fpm test                  # run tests
fpm run                   # run executable
fpm new myproject         # new project
```

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(myapp LANGUAGES Fortran)

add_executable(myapp src/main.f90 src/module1.f90)
set_target_properties(myapp PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)
target_include_directories(myapp PRIVATE ${CMAKE_BINARY_DIR}/modules)
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **fpm** | Trình quản lý gói Fortran (hiện đại) |
| **Fortran stdlib** | Nỗ lực thư viện chuẩn |
| **Conan** | Gói C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Thư viện khoa học
| Thư viện | Mục đích |
|----------|----------|
| **BLAS / LAPACK** | đại số tuyến tính |
| **OpenBLAS** | BLAS được tối ưu hóa |
| **Intel MKL** | Thư viện hạt nhân toán học Intel |
| **FFTW** | Biến đổi Fourier nhanh |
| **ARPACK** | Vấn đề về giá trị riêng |
| **ScaLAPACK** | Đại số tuyến tính song song |
| **PETSc** | Tính toán khoa học song song |
| **Trilinos** | Khoa học quy mô lớn |
| **HDF5** | Định dạng dữ liệu phân cấp |
| **NetCDF** | Dữ liệu khoa học/khí hậu |
| **stdlib** | Thư viện chuẩn Fortran |
| **fortran-os** | Giao diện hệ điều hành |
| **forlab** | Máy tính khoa học |
| **M_mảng** | Tiện ích mảng |
```fortran
! LAPACK example (solve linear system Ax = b)
program solve_linear
    use lapack95
    implicit none
    integer, parameter :: n = 3
    real(8) :: A(n,n), b(n)
    integer :: ipiv(n), info
    
    A = reshape([2.0, 1.0, 1.0, 1.0, 3.0, 2.0, 1.0, 2.0, 4.0], [n,n])
    b = [1.0, 2.0, 3.0]
    
    call gesv(A, b, ipiv, info)
    
    print *, "Solution:", b
end program
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **pFUnit** | Thử nghiệm đơn vị (NASA) |
| **Kiểm tra Fortran** | Kiểm tra đơn giản |
| **lái thử** | Thử nghiệm hiện đại |
| **kiểm tra fpm** | Người chạy thử tích hợp |
```fortran
! test-drive example
module test_math
    use testdrive, only : new_unittest, unittest_type, error_type, check
    implicit none
contains
    subroutine collect_tests(testsuite)
        type(unittest_type), allocatable, intent(out) :: testsuite(:)
        testsuite = [ &
            new_unittest("addition", test_addition), &
            new_unittest("multiplication", test_multiplication) &
        ]
    end subroutine
    
    subroutine test_addition(error)
        type(error_type), allocatable, intent(out) :: error
        call check(2 + 3 == 5, error)
    end subroutine
end module
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **flàm đẹp** | Định dạng mã |
| **tìm thấy** | Thụt lề và định dạng |
| **fortran-linter** | Lining |
| **thoải mái** | Tái cấu trúc |
| **CoCoNuT** | Bảo hiểm mã |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Tính toán song song
| Công nghệ | Mục đích |
|----------||---------|
| **OpenMP** | Song song bộ nhớ dùng chung |
| **MPI** | Bộ nhớ phân tán (Truyền tin nhắn) |
| **Coarrays** | Sự song song bản địa của Fortran |
| **CUDA Fortran** | điện toán GPU |
| **OpenACC** | GPU dựa trên chỉ thị |
| **HÃY ĐỒNG HÀNH** | Vòng lặp song song Fortran 2008 |
```fortran
! OpenMP example
program parallel_sum
    implicit none
    integer, parameter :: n = 1000000
    real(8) :: a(n), b(n), c(n)
    integer :: i
    
    !$omp parallel do
    do i = 1, n
        c(i) = a(i) + b(i)
    end do
    !$omp end parallel do
end program
```

```fortran
! Coarray example
program coarray_example
    implicit none
    integer :: i
    real, codimension[:] :: shared_value
    
    shared_value[this_image()] = real(this_image())
    sync all
    
    if (this_image() == 1) then
        do i = 1, num_images()
            print *, "Image", i, "has value", shared_value[i]
        end do
    end if
end program
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **stdlib** | Thư viện chuẩn |
| **json-fortran** | Phân tích cú pháp JSON |
| **forutils** | Chức năng tiện ích |
| **BẬT** | Phân tích đối số dòng lệnh |
| **trong_thời gian** | Xử lý ngày/giờ |
| **FiNeR** | Xử lý tập tin |
| **forxml** | Phân tích cú pháp XML |
| **forpy** | Tương tác Python |
| **ISO_C_BINDING** | Khả năng tương tác C |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + Fortran hiện đại** | LSP Fortran tốt nhất |
| **IntelliJ + fortran-plugin** | Hỗ trợ JetBrains |
| **Nevim + pháo đài** | Dựa trên thiết bị đầu cuối |
| **Nhật thực + Photran** | Nhật thực Fortran |
| **Code::Khối** | IDE nhẹ |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Nhị phân tĩnh** | `gfortran -static`|
| **Thư viện chia sẻ** | `gfortran -shared`|
| **C tương tác** | Gọi từ C/C++ qua`ISO_C_BINDING`|
| **Tương tác Python** | f2py, forpy |
| **Docker** | Được đóng gói |
| **Cụm HPC** | MPI + SLURM |
---

## Bản tóm tắt
Hệ sinh thái của Fortran được xây dựng có mục đích dành cho điện toán khoa học hiệu suất cao. Chuỗi công cụ tiêu chuẩn là: **gfortran** hoặc **ifx** để biên dịch, **fpm** để quản lý gói, **CMake** cho các bản dựng, **BLAS/LAPACK** cho đại số tuyến tính, **OpenMP** và **MPI** cho tính song song, **pFUnit** cho thử nghiệm và **fprettify** cho định dạng. Fortran vượt trội về tính toán số, mô phỏng thời tiết, động lực học chất lỏng tính toán và mô phỏng khoa học quy mô lớn. Fortran hiện đại (2018/2023) với coarrays, DO CONCURRENT và OOP cải tiến là một ngôn ngữ hiện đại có khả năng. Hệ sinh thái rất cần thiết trong HPC, mô hình hóa khí hậu và vật lý tính toán.