FROM node:20-alpine

WORKDIR /app

# Copy dependency manifests
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application source code
COPY . .

# Expose API Gateway port
EXPOSE 5000

# Start the application
CMD ["npm", "start"]