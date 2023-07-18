# Video Project Web Application

## Development

### Backend

1. Create virtualenv in your local machine.
2. Install requirements.txt file using command `pip install -r requirements.txt`.
3. Setup Postgresql database
4. Install `imagemagick` from `https://imagemagick.org/script/download.php` to .used for editing and manipulating digital images and add features in a video.


### Running

1. Run `python manage.py migrate` to create the tables in the database.
2. Run `python manage.py runserver` to run the server.

### Functionality

1. User can post new videos with subtitle files in multiple language.
2. User can see subtitles of the language selected if the file exists in the database.
3. User can add filters to the video as an editing feature and download the video with the filter added. 

### Frontend

1. To install dependencies run `npm install`.
2. To check frontend run command `npm run` 
