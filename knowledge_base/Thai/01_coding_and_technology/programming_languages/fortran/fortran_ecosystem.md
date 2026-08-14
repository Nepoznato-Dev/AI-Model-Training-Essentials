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
# Fortran - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ ไลบรารี และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศของ Fortran
---

## มาตรฐาน Fortran และคอมไพเลอร์
| คอมไพเลอร์ | แพลตฟอร์ม | หมายเหตุ |
|----------|----------|-------|
| **กฟอร์ทราน** | ข้ามแพลตฟอร์ม | GNU Fortran (GCC) ที่ใช้กันอย่างแพร่หลาย |
| **ifx / ifort** | ข้ามแพลตฟอร์ม | Intel Fortran (oneAPI) |
| **nvfortran** | จีพียู | NVIDIA Fortran (CUDA) |
| **หน้าแปลน** | ข้ามแพลตฟอร์ม | อิง LLVM (ใหม่) |
| ** NAG ** | ข้ามแพลตฟอร์ม | เชิงพาณิชย์ การปฏิบัติตามอย่างเข้มงวด |
| **เครย์** | HPC | เครย์ซูเปอร์คอมพิวเตอร์ |
| **ไอบีเอ็ม XL** | HPC | ระบบไอบีเอ็ม |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## สร้างระบบ
| เครื่องมือ | พิมพ์ | ดีที่สุดสำหรับ |
|------|-|---------|
| **ซีเมค** | ข้ามแพลตฟอร์ม | มาตรฐานอุตสาหกรรม |
| **เอฟพีเอ็ม** | ชาว Fortran | ตัวจัดการแพ็คเกจ Fortran สมัยใหม่ |
| **มีซอน** | ทันสมัย ​​| ไวยากรณ์ที่รวดเร็วและสะอาดตา |
| **ทำ** | คลาสสิค | โครงการง่ายๆ |
| **สคอน** | ที่ใช้ Python | งานสร้างที่ซับซ้อน |
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

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **เอฟพีเอ็ม** | Fortran Package Manager (ทันสมัย) |
| **Fortran stdlib** | ความพยายามของห้องสมุดมาตรฐาน |
| **โคนัน** | แพ็คเกจ C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## ห้องสมุดวิทยาศาสตร์
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **บลาส / ลาแพ็ค** | พีชคณิตเชิงเส้น |
| **OpenBLAS** | เพิ่มประสิทธิภาพ BLAS |
| **อินเทลเอ็มเคแอล** | ไลบรารี Intel Math Kernel |
| **FFTW** | การแปลงฟูเรียร์เร็ว |
| **อาแพ็ค** | ปัญหาค่าลักษณะเฉพาะ |
| **สกาลาแพค** | พีชคณิตเชิงเส้นแบบขนาน |
| **PETSc** | การคำนวณทางวิทยาศาสตร์แบบขนาน |
| **ทริลิโนส** | วิทยาศาสตร์ขนาดใหญ่ |
| **HDF5** | รูปแบบข้อมูลแบบลำดับชั้น |
| **NetCDF** | ข้อมูลภูมิอากาศ/วิทยาศาสตร์ |
| **stdlib** | ไลบรารีมาตรฐาน Fortran |
| **ฟอร์ทราน-ออส** | ส่วนต่อประสานระบบปฏิบัติการ |
| **สำหรับห้องปฏิบัติการ** | คอมพิวเตอร์ทางวิทยาศาสตร์ |
| **M_array** | ยูทิลิตี้อาร์เรย์ |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **pFUnit** | การทดสอบหน่วย (NASA) |
| **การทดสอบ Fortran** | การทดสอบอย่างง่าย |
| **ทดลองขับ** | การทดสอบสมัยใหม่ |
| **การทดสอบ fpm** | นักวิ่งทดสอบในตัว |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ทำให้สวยขึ้น** | การจัดรูปแบบโค้ด |
| **ค้นหา** | การเยื้องและการจัดรูปแบบ |
| **ฟอร์แทรน-ลินเตอร์** | สำลี |
| **แคมฟอร์ต** | การรีแฟคเตอร์ |
| **โคโคนัท** | ความครอบคลุมของโค้ด |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## คอมพิวเตอร์แบบขนาน
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **OpenMP** | ความขนานของหน่วยความจำแบบแบ่งใช้ |
| **เอ็มพีไอ** | หน่วยความจำแบบกระจาย (ข้อความผ่าน) |
| **ปลาคาร์เรย์** | ความเท่าเทียมโดยกำเนิดของ Fortran |
| **CUDA ฟอร์ทราน** | การประมวลผล GPU |
| **OpenACC** | GPU ตามคำสั่ง |
| **ทำพร้อมกัน** | Fortran 2008 ลูปขนาน |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **stdlib** | ไลบรารีมาตรฐาน |
| **json-fortran** | การแยกวิเคราะห์ JSON |
| **เพื่อประโยชน์** | ฟังก์ชั่นยูทิลิตี้ |
| **พนัง** | การแยกวิเคราะห์อาร์กิวเมนต์บรรทัดคำสั่ง |
| **for_time** | การจัดการวันที่/เวลา |
| **FiNeR** | การจัดการไฟล์ |
| **forxml** | การแยกวิเคราะห์ XML |
| **ฟอร์ปี้** | Python ทำงานร่วมกัน |
| **ISO_C_BINDING** | การทำงานร่วมกันของ C |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **VS Code + Modern Fortran** | สุดยอด Fortran LSP |
| **IntelliJ + ปลั๊กอิน fortran** | การสนับสนุน JetBrains |
| **นีโอวิม + ป้อมปราการ** | บนเทอร์มินัล |
| **คราส + โพทราน** | คราสฟอร์แทรน |
| **รหัส::บล็อก** | IDE น้ำหนักเบา |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ไบนารีแบบคงที่** | `gfortran -static`|
| **ไลบรารีที่ใช้ร่วมกัน** | `gfortran -shared`|
| **การทำงานร่วมกัน** | โทรจาก C/C++ ผ่าน`ISO_C_BINDING`|
| **การทำงานร่วมกันของ Python** | f2py, forpy |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **คลัสเตอร์ HPC** | MPI + สเลิร์ม |
---

## สรุป
ระบบนิเวศของ Fortran สร้างขึ้นโดยมีจุดประสงค์เพื่อการประมวลผลทางวิทยาศาสตร์ที่มีประสิทธิภาพสูง Toolchain มาตรฐานคือ **gfortran** หรือ **ifx** สำหรับการคอมไพล์ **fpm** สำหรับการจัดการแพ็คเกจ **CMake** สำหรับบิลด์ **BLAS/LAPACK** สำหรับพีชคณิตเชิงเส้น **OpenMP** และ **MPI** สำหรับความขนาน **pFUnit** สำหรับการทดสอบ และ **fprettify** สำหรับการจัดรูปแบบ Fortran เป็นเลิศในด้านการคำนวณเชิงตัวเลข การจำลองสภาพอากาศ พลศาสตร์ของไหลเชิงคำนวณ และการจำลองทางวิทยาศาสตร์ขนาดใหญ่ Modern Fortran (2018/2023) พร้อม coarrays, DO CONCURRENT และ OOP ที่ปรับปรุงแล้วเป็นภาษาสมัยใหม่ที่มีความสามารถ ระบบนิเวศมีความสำคัญใน HPC การสร้างแบบจำลองสภาพภูมิอากาศ และฟิสิกส์เชิงคำนวณ