# Use a specific Node.js version compatible with Next.js
FROM node:latest

# Set the working directory to the app directory
WORKDIR /app

# Copy the package.json and package-lock.json first
COPY package*.json ./

RUN npm ci

# Now copy the entire app source code
COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "start"]