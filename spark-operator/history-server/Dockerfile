# Use the official Apache Spark PySpark image as the base image
FROM apache/spark-py:latest

# Set the working directory
WORKDIR /opt/spark/work-dir/

# Copy the application files to the work directory
COPY app .

# Install Python dependencies and set permissions
USER root
RUN chown -R 185:0 /opt/spark/work-dir/ && \
    pip install --no-cache-dir -r requirements.txt && \
    chown -R 185:0 /opt/spark/work-dir/

# Install Tini
#ENV TINI_VERSION v0.19.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
#RUN chmod +x /tini

# Switch to a non-root user
CMD ["/bin/bash"]
# Set the default command to run Apache Spark History Server
#ENTRYPOINT ["/tini", "--"]
#CMD ["/opt/spark/bin/spark-class", "-Dspark.history.fs.logDirectory=/data/", "org.apache.spark.deploy.history.HistoryServer"]

