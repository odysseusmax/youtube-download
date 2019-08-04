# [YouTube Download](http://odysseusmax.tk/youtube-download/)

> A simple web app to download youtube videos/audios.

# Technology Used

This app is made with [Vue JS](https://github.com/vuejs/vue) for front end and [Sanic](https://github.com/huge-success/sanic) web server
for back end.

**Additional info**
<br>
This app uses [Axios](https://github.com/axios/axios) to do API requests to the back end. In back end, youtube-dl is used to fetch required data. Detailed list is given below.

## Dependency Table

Name  | Usage
------------- | -------------
VueJS  | Main base framework with which app's front end is built on
Sanic  | Back end framework
Axios  | Used to do API requests to back end from client side
sanic-cors  | to handle CORS
youtube-dl  | To generate resourses for download
pafy  | To interface youtube-dl
tailwindcss  | For styling

### Hosting

Currently the app's front end is hosted on github pages and back end at heroku.
