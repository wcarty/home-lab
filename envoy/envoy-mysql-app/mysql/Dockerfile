FROM mysql:8.0.32-debian

# Copy initialization SQL script
COPY db_init.sql /docker-entrypoint-initdb.d/

# Set environment variables (Optional: Can be overridden in Docker Compose)
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

CMD ["mysqld"]

