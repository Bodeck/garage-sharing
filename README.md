# :car: Garage Sharing
Idea behind application is that who owns parking place can share it during absence with other employees.

We plan to build it with [Django](https://www.djangoproject.com/) for server and back-end and [React.js](https://reactjs.org/) for client side.

## Client

Client has been built using create-react-app, so you can use default react-scripts (`start, build`).

#### Install

To install client run following scripts from project root folder
```sh
cd client
yarn install || npm install
```
#### Run development server

```sh
yarn start || npm start
```
#### Build production bundle

```sh
yarn build || npm build
```
## Server

Before run server you need Python(3.x.x) and Django(3.0.1) installed locally.

#### Install

```sh
cd client
yarn build || npm build #compile src to build folder
cd ../server
py manage.py runserver
```
## Issues

## Todos