FROM apache/nifi:1.23.2
USER 0

# Create the directory to house the JAR files in the specified path
RUN mkdir -p /opt/configuration_resources/custom_lib

# Copy all JAR files from the 'jars' directory into the created directory
COPY jars /opt/configuration_resources/custom_lib/

# Change ownership of the custom_lib directory to the 'nifi' user
RUN chown -R nifi:nifi /opt/configuration_resources/custom_lib

USER nifi
