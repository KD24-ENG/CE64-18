# Start from base image
FROM mysql:latest

# Set the current working directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY package.json ./

# Download all dependencies
RUN npm install

# Copy source from current directory to working directory
COPY . .

# Expose necessary port
EXPOSE 3000

# Run the created binary executable after wait for mysql container to be up
CMD ["./wait-for.sh" , "mysql:3306" , "--timeout=300" , "--" , "./main"]