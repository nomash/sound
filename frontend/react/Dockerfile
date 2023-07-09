# Base image
FROM node:latest

WORKDIR /react

COPY package*.json ./

RUN npm install

# Copy the entire application code
COPY . .

RUN npm run build


EXPOSE 3000

# Command to start the application
CMD ["npm", "start"]
