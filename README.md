# Django Bookstore Backend

### Overview

This is a **Django Bookstore backend project** built mainly for learning and portfolio purposes. The focus of this project is on writing clean backend code, understanding Django fundamentals, and practicing real-world patterns such as CRUD operations, form validation, permissions, and relational data modeling.

The frontend is intentionally kept simple so the main attention stays on **backend logic and structure** rather than UI design.

### Features

* Book management (create, list, detail)
* Author management and relationships with books
* Django ModelForms with custom validation
* Staff-only permissions for sensitive actions
* Clean and readable URL & view structure
* Persian (Farsi) localization support

### Tech Stack

* Python
* Django
* SQLite (for development)

### Project Structure

* `models.py` – Database models (Book, Author)
* `forms.py` – Forms and validation logic
* `views.py` – Application views
* `urls.py` – URL routing
* `templates/` – Simple templates for testing workflows

### Permissions

* Only **staff users** can create or manage books and authors
* Public users can browse books and view book details

### Why this project?

This project exists to:

* Improve Django backend skills
* Practice clean and maintainable code
* Serve as a solid backend portfolio project

### Notes
AI-assisted tools were used during development for learning, brainstorming, and code review purposes.  
All architectural decisions and implementations were reviewed, understood, and adapted by the developer.

### معرفی پروژه

این پروژه یک **فروشگاه کتاب با Django** است که با هدف یادگیری، تمرین مفاهیم بک‌اند و ساخت نمونه‌کار ایجاد شده است. تمرکز اصلی پروژه روی کدنویسی تمیز، درک ساختار Django و پیاده‌سازی الگوهای رایج در پروژه‌های واقعی است.

فرانت‌اند عمداً ساده نگه داشته شده تا تمرکز اصلی روی **منطق بک‌اند** باشد، نه ظاهر.

### امکانات

* مدیریت کتاب‌ها (افزودن، لیست، نمایش جزئیات)
* مدیریت نویسندگان و ارتباط آن‌ها با کتاب‌ها
* استفاده از ModelForm و اعتبارسنجی داده‌ها
* محدودیت دسترسی برای عملیات حساس (فقط staff)
* ساختار تمیز و قابل توسعه برای View و URL
* پشتیبانی از زبان فارسی در کل پروژه

### تکنولوژی‌ها

* Python
* Django
* SQLite (برای محیط توسعه)

### ساختار کلی پروژه

* `models.py` : مدل‌های دیتابیس (کتاب، نویسنده)
* `forms.py` : فرم‌ها و منطق validation
* `views.py` : ویوهای پروژه
* `urls.py` : مسیردهی
* `templates/` : قالب‌های ساده برای تست جریان‌ها

### سطح دسترسی

* فقط کاربران staff امکان افزودن و مدیریت کتاب و نویسنده را دارند
* کاربران عادی فقط امکان مشاهده اطلاعات را دارند

### هدف پروژه

این پروژه برای این ساخته شده که:

* مهارت‌های بک‌اند Django تقویت شوند
* مفاهیم ارتباط بین مدل‌ها بهتر درک شود
* یک پروژه مناسب برای GitHub و رزومه داشته باشم

### توضیح
در فرآیند توسعه این پروژه از ابزارهای هوش مصنوعی به‌عنوان کمک آموزشی، ایده‌پردازی و بازبینی کد استفاده شده است.  
تمام تصمیم‌های معماری و پیاده‌سازی‌ها با درک کامل و توسط توسعه‌دهنده انجام شده‌اند.



### Status

This project is under active development and will be extended with additional backend features.
