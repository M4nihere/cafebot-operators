# Use the official Apache Spark PySpark image as the base image
FROM apache/spark-py:latest

# Copy the application files to the work directory
COPY app /opt/spark/work-dir/
COPY jars /opt/spark/jars

# Switch to a non-root user
USER 185:0

# Switch to root to download Microsoft JDBC Driver for SQL Server
USER root
#RUN wget -O /opt/spark/jars/mssql-jdbc-9.2.1.jre8.jar https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/9.2.1.jre8/mssql-jdbc-9.2.1.jre8.jar

# Switch back to the non-root user


# Install Python dependencies with --user flag
#RUN pip install --no-cache-dir -r /opt/spark/work-dir/requirements.txt

# Change ownership of the installed packages directory
RUN chown -R 185:0 /opt/spark/work-dir
RUN chown -R 185:0 /opt/spark/jars
USER 185:0

