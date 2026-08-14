---
# Metadata
title: "MATLAB — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic MATLAB code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [matlab, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# MATLAB — 慣用模式與最佳實踐
本指南涵蓋了編寫簡潔、慣用的 MATLAB 程式碼的慣用模式和最佳實務。
---

## 向量化
```matlab
% ✅ Vectorized operations (avoid loops)
squares = x.^2;
total = sum(values);
mean_val = mean(values, 'omitnan');

% ✅ Logical indexing
adults = data(data.age >= 18, :);
valid = data(~isnan(data.value), :);

% ✅ Vectorized conditionals
categories = discretize(scores, [0 60 70 80 90 100], {'F','D','C','B','A'});

% ✅ Pre-allocate arrays
result = zeros(1, n);
for i = 1:n
    result(i) = compute(i);
end
```

---

## 函數
```matlab
% ✅ Function with input validation
function result = process(input)
    arguments
        input (1,:) double {mustBePositive}
    end
    
    result = input.^2 + 1;
end

% ✅ Multiple outputs
function [mean_val, std_val] = stats(data)
    mean_val = mean(data);
    std_val = std(data);
end

% ✅ Name-value arguments
function plot_data(data, options)
    arguments
        data (:,:) double
        options.Color (1,3) double = [0 0 1]
        options.LineWidth double = 1.5
        options.Title string = "Plot"
    end
    plot(data, 'Color', options.Color, 'LineWidth', options.LineWidth);
    title(options.Title);
end
```

---

## 課程
```matlab
% ✅ value class for data
classdef User
    properties
        Name  (1,1) string
        Email (1,1) string
        Age   (1,1) double {mustBePositive}
    end
    
    methods
        function obj = User(name, email, age)
            obj.Name = string(name);
            obj.Email = string(email);
            obj.Age = age;
        end
        
        function disp(obj)
            fprintf("User: %s (%s)\n", obj.Name, obj.Email);
        end
    end
end
```

---

## 錯誤處理
```matlab
% ✅ error with identifier
if isempty(data)
    error('MyApp:EmptyInput', 'Data must not be empty');
end

% ✅ try/catch
try
    result = risky_operation();
catch ME
    if strcmp(ME.identifier, 'MyApp:EmptyInput')
        result = default_value;
    else
        rethrow(ME);
    end
end

% ✅ warning
if any(isnan(values))
    warning('MyApp:NaNValues', 'NaN values detected');
end
```

---

＃＃ 概括
MATLAB 慣用語強調：向量化（避免迴圈）、邏輯索引、預先分配、函數參數驗證和句柄/值類別。遵循 MATLAB 的程式碼分析器（橘色/綠色標記），使用 checkcode 進行 linting，並使用 timeit 進行基準測試。 MATLAB 重視矩陣運算和科學計算的可讀性。