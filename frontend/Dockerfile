FROM node:14-buster-slim as build

# install dependencies
WORKDIR /app
COPY package.json ./
COPY src ./
COPY static ./
RUN npm install
# Svelte is useless piece of bleeding edge garbage
RUN npm install '@sveltejs/kit@1.0.0-next.110'
# Copy all local files into the image.
COPY . .
RUN npm run build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM node:14-buster-slim as public

WORKDIR /app
COPY --from=build /app .
COPY . .
CMD ls
EXPOSE 3000
CMD ["node", "./build"]
