FROM mhart/alpine-node:12 as build

# install dependencies
WORKDIR /app
COPY package.json ./
# Copy all local files into the image.
COPY . .
RUN npm install
RUN npm run build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM mhart/alpine-node:slim-12 as public

WORKDIR /app
COPY --from=build /app .
COPY . .
CMD ls
EXPOSE 3000
CMD ["node", "./build"]