# Gunakan image resmi PHP dengan Apache
FROM php:8.1-apache

# Copy semua file dari folder proyek ke dalam container
COPY . /var/www/html/

# Set permission agar folder bisa diakses oleh Apache
RUN chown -R www-data:www-data /var/www/html

# Expose port 80 untuk akses HTTP
EXPOSE 80
