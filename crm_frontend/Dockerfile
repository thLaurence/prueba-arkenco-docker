FROM node:14

WORKDIR /app

COPY crm_cliente/package*.json ./

RUN npm install

COPY crm_cliente .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
